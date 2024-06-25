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


def formatFilter(x):
  if x != 'none':
    res = json.loads(x)
    return 'filteredBy ' + res['filter']['fieldName'] + ' ' + res['filter']['fieldFilter']['match'] + ' ' + str(res['filter']['fieldFilter']['value'])
  else:
    return 'filteredBy none none none'
  
def clean_text(text):
    text = normalize('NFD', text.lower())
    text = re.sub('[^A-Za-z0-9- ]+', '', text)
    return text

def clean_and_prepare_text(text):
    text = '[start] ' + clean_text(text) + ' [end]'
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

df = pd.read_csv('output_subset.csv')

df['metrics'] = df['metrics'].apply(lambda x: re.sub(';', ' ', x))
df['dimensions'] = df['dimensions'].fillna('none')
df['dimensions'] = df['dimensions'].apply(lambda x: re.sub(';', ' ', x))
df['dimensionFilter'] = df['dimensionFilter'].fillna('none')
df['dimensionFilter'] = df['dimensionFilter'].astype('str')
df['dimensionFilter'] = df['dimensionFilter'].apply(formatFilter)
df['target'] = 'get ' + df['metrics'] + ' segmentedBy ' + df['dimensions'] + ' from ' + df['start_date'] + ' to ' + df['end_date'] + ' ' + df['dimensionFilter']
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
    # Aquí va tu función translate_text adaptada para recibir el input desde la request
    translated_text = translate_text(text, model, nl_tokenizer, api_tokenizer, api_index_lookup, sequence_len)    
    return jsonify({'translated_text': translated_text})

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)