from flask import Flask, request, jsonify
import pandas as pd
import json
import re
from unicodedata import normalize
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import tensorflow as tf
from tensorflow.keras import Model
from tensorflow.keras.layers import Input, Dense, Dropout
from keras_nlp.layers import TokenAndPositionEmbedding, TransformerEncoder
from keras_nlp.layers import TransformerDecoder
import keras as keras
from google.oauth2 import service_account
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)

def parseTranslate(text):

  metrics = []
  dimensions = []
  filters = []

  is_metric = True
  is_dimension = False
  is_filter = False

  for word in text.split():

    if (word == 'segmentedby'):
      is_metric = False
      is_dimension = True
      is_filter = False
    elif (word == 'filteredby'):
      is_metric = False
      is_dimension = False
      is_filter = True

    if (word != 'get' and word != 'segmentedby' and word != 'filteredby'):
      if is_metric:
        metrics.append(word)
      elif is_dimension:
        dimensions.append(word)
      elif is_filter:
        filters.append(word)

  return metrics, dimensions, filters

def camelCase(api_parameters, list, type):

  return_list = []

  if type == 'm':
    for word in list:
      if word == 'none':
        return 'none'
      else:
        filas_con_palabra = api_parameters[api_parameters['Nombre de la API'].str.lower().str.fullmatch(word, na=False)]
        return_list.append(filas_con_palabra['Nombre de la API'].unique()[0])
      
    return return_list

  if type == 'd':    
    for word in list:
      if word == 'none':
        return_list.append('date')
      else:
        filas_con_palabra = api_parameters[api_parameters['Nombre de la API'].str.lower().str.fullmatch(word, na=False)]
        return_list.append(filas_con_palabra['Nombre de la API'].unique()[0])
      
    return return_list

def returnTranslation(text, model, nl_tokenizer, api_tokenizer, api_index_lookup, sequence_len, propiedad, inicio, fin):
    
    translated_text = translate_text(text, model, nl_tokenizer, api_tokenizer, api_index_lookup, sequence_len)
    metric_lookup = pd.read_csv('metrics_lookuptable.csv')
    dimension_lookup = pd.read_csv('dimensions_lookuptable.csv')
    print(translated_text)
    m, d, f = parseTranslate(translated_text)
    
    
    m = camelCase(metric_lookup, m, 'm')
    d = camelCase(dimension_lookup, d, 'd')
    
    credentials = service_account.Credentials.from_service_account_file('analiticro-d937f7a1303a.json') 
    client_data = BetaAnalyticsDataClient(credentials = credentials)
    
    metrics_api = []
    dimensions_api = []
    for metric in m:
        metrics_api.append(Metric(name=metric))

    for dimension in d:
        dimensions_api.append(Dimension(name=dimension))
    
    request = RunReportRequest(
        property=propiedad, #Cambiar por algo dinamico
        dimensions=dimensions_api,
        metrics=metrics_api,
        date_ranges=[DateRange(start_date=inicio, end_date=fin)],
    )
    
    response = client_data.run_report(request)
    
    retorno = ''
    for row in response.rows:
        dim = 0
        for dimension in d:
            retorno += dimension + ' = ' + str(row.dimension_values[dim].value) + ' '
            dim += 1

        met = 0
        for metric in m:
            retorno += metric + ' = ' + str(row.metric_values[met].value) + ' '
            met += 1

        retorno += '\n'
    
    return translated_text, retorno


def formatFilter(x):
  if x != 'none':
    res = json.loads(x)
    return 'filteredBy ' + res['filter']['fieldName'] + ' ' + res['filter']['fieldFilter']['match'] + ' ' + str(res['filter']['fieldFilter']['value'])
  else:
    return 'filteredBy none none none'
  
def clean_text(text):
    text = normalize('NFD', text.lower())
    text = re.sub('[^A-Za-z0-9 ]+', '', text)
    return text

def clean_and_prepare_text(text):
    text = '[start] ' + text + ' [end]'
    return text


def translate_text(text, model, en_tokenizer, fr_tokenizer, fr_index_lookup, sequence_len):
    input_sequence = en_tokenizer.texts_to_sequences([text])
    padded_input_sequence = pad_sequences(input_sequence, maxlen=sequence_len, padding='post')
    decoded_text = '[start]'

    for i in range(sequence_len):
        target_sequence = fr_tokenizer.texts_to_sequences([decoded_text])
        padded_target_sequence = pad_sequences(target_sequence, maxlen=sequence_len, padding='post')[:, :-1]
        prediction = model([padded_input_sequence, padded_target_sequence])
        idx = np.argmax(prediction[0, i, :]) - 1
        token = fr_index_lookup[idx]
        decoded_text += ' ' + token

        if token == '[end]':
            break

    return decoded_text[8:-6] # Remove [start] and [end] tokens

app = Flask(__name__)

df = pd.read_csv('output.csv')

df['metrics'] = df['metrics'].apply(lambda x: re.sub(';', ' ', x))
df['dimensions'] = df['dimensions'].fillna('none')
df['dimensions'] = df['dimensions'].apply(lambda x: re.sub(';', ' ', x))
df['dimensionFilter'] = df['dimensionFilter'].fillna('none')
df['dimensionFilter'] = df['dimensionFilter'].astype('str')
df['dimensionFilter'] = df['dimensionFilter'].apply(lambda x: re.sub(';', ' ', x))
df['dimensionFilter'] = df['dimensionFilter'].apply(lambda x: re.sub('_', '', x))


df['target'] = 'get ' + df['metrics'] + ' segmentedBy ' + df['dimensions']# + ' filteredBy ' + df['dimensionFilter']

df['natural_language_query'] = df['natural_language_query'].apply(lambda row: clean_text(row))
df['target'] = df['target'].apply(lambda row: clean_and_prepare_text(row))


nl = df['natural_language_query']
api = df['target']

nl_max_len = max(len(line.split()) for line in nl)
api_max_len = max(len(line.split()) for line in api)

sequence_len = max(nl_max_len, api_max_len)

nl_tokenizer = Tokenizer()
nl_tokenizer.fit_on_texts(nl)
nl_sequences = nl_tokenizer.texts_to_sequences(nl)
nl_x = pad_sequences(nl_sequences, maxlen=sequence_len, padding='post')

api_tokenizer = Tokenizer(filters='!"#$%&()*+,-./:;<=>?@\\^_`{|}~\t\n')
api_tokenizer.fit_on_texts(api)
api_sequences = api_tokenizer.texts_to_sequences(api)
api_y = pad_sequences(api_sequences, maxlen=sequence_len + 1, padding='post')


nl_vocab_size = len(nl_tokenizer.word_index) + 1
api_vocab_size = len(api_tokenizer.word_index) + 1

inputs = { 'encoder_input': nl_x, 'decoder_input': api_y[:, :-1] }
outputs = api_y[:, 1:]

api_vocab = api_tokenizer.word_index
api_index_lookup = dict(zip(range(len(api_vocab)), api_vocab))

model = keras.models.load_model('modelo.keras')

# Ruta para crear un nuevo elemento
@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data['text']  
    propiedad = data['propiedad']
    inicio = data['inicio']
    fin = data['fin']  
    
    # Aquí va tu función translate_text adaptada para recibir el input desde la request
    traduccion, datos = returnTranslation(text, model, nl_tokenizer, api_tokenizer, api_index_lookup, sequence_len, propiedad, inicio, fin)    
    return jsonify({'translated_text': traduccion, 'respuesta': datos})

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)