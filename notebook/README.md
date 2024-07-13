# Procesamiento dataset, modelado, entrenamiento y consumo del modelo

## Instalación de las librerías necesarias

Se instalan Keras y KerasNLP

```python
#Instalamos Keras 3.3.3
!pip install keras==3.3.3
#Instalamos Keras NLP
!pip install keras-nlp==0.12.0
```
Se monta Google Drive

```python
from google.colab import drive
drive.mount('/content/gdrive')
```

Se carga el dataset desde Google Drive

```python
from google.colab import drive
drive.mount('/content/gdrive')
```

Se procesa el dataset para crear una nueva columna target con la traducción de la frase

```python
import re
import json
print(df.dtypes)
df['metrics'] = df['metrics'].apply(lambda x: re.sub(';', ' ', x))
df['dimensions'] = df['dimensions'].fillna('none')
df['dimensions'] = df['dimensions'].apply(lambda x: re.sub(';', ' ', x))
df['dimensionFilter'] = df['dimensionFilter'].fillna('none')
df['dimensionFilter'] = df['dimensionFilter'].astype('str')
df['dimensionFilter'] = df['dimensionFilter'].apply(lambda x: re.sub(';', ' ', x))
df['dimensionFilter'] = df['dimensionFilter'].apply(lambda x: re.sub('_', '', x))
df['target'] = 'get ' + df['metrics'] + ' segmentedBy ' + df['dimensions']# + ' filteredBy ' + df['dimensionFilter']
```
## Limpieza y normalización

Este fragmento de código se encarga de limpiar y preparar textos dentro de un DataFrame en Python. A continuación, se detalla cada función y operación:

### Importaciones
```python
import re
from unicodedata import normalize
```
Se importan dos módulos:
- `re`: Módulo para trabajar con expresiones regulares en Python.
- `normalize` de `unicodedata`: Función para normalizar cadenas de texto en Unicode.

### Función `clean_text`
```python
def clean_text(text):
    text = normalize('NFD', text.lower())
    text = re.sub('[^A-Za-z0-9 ]+', '', text)
    return text
```
Esta función realiza la limpieza básica de un texto:
1. Normaliza el texto a la forma `NFD` y lo convierte a minúsculas.
2. Elimina todos los caracteres que no sean letras, números o espacios.
3. Devuelve el texto limpio.

### Función `clean_and_prepare_text`
```python
def clean_and_prepare_text(text):
    text = '[start] ' + text + ' [end]'
    return text
```
Esta función prepara un texto añadiendo etiquetas de inicio y fin:
1. Agrega la etiqueta `[start]` al comienzo del texto.
2. Agrega la etiqueta `[end]` al final del texto.
3. Devuelve el texto preparado.

### Aplicación a un DataFrame
```python
df['natural_language_query'] = df['natural_language_query'].apply(lambda row: clean_text(row))
df['target'] = df['target'].apply(lambda row: clean_and_prepare_text(row))
df.head()
```
Estas líneas aplican las funciones de limpieza y preparación a las columnas especificadas de un DataFrame `df`:
1. Limpia los textos en la columna `natural_language_query` utilizando la función `clean_text`.
2. Prepara los textos en la columna `target` utilizando la función `clean_and_prepare_text`.
3. Muestra las primeras filas del DataFrame para verificar los cambios.

### Uso
Para utilizar este código, asegúrate de tener un DataFrame `df` con las columnas `natural_language_query` y `target`. Luego, simplemente ejecuta el código para limpiar y preparar los textos en estas columnas.

## Cáculo de longitudes

Este fragmento de código se encarga de calcular la longitud máxima de las frases en dos columnas de un DataFrame y determinar la longitud de secuencia más larga entre ellas. A continuación, se detalla cada operación:

### Variables Iniciales
```python
nl = df['natural_language_query']
api = df['target']
```
Se extraen dos columnas del DataFrame `df`:
- `nl`: Contiene las consultas en lenguaje natural.
- `api`: Contiene los objetivos o resultados esperados.

### Cálculo de Longitudes Máximas
```python
nl_max_len = max(len(line.split()) for line in nl)
api_max_len = max(len(line.split()) for line in api)
sequence_len = max(nl_max_len, api_max_len)
```
Se calcula la longitud máxima de las frases en cada columna:
1. `nl_max_len`: Longitud máxima de las frases en la columna `nl`, medida en número de palabras.
2. `api_max_len`: Longitud máxima de las frases en la columna `api`, medida en número de palabras.
3. `sequence_len`: La mayor longitud entre `nl_max_len` y `api_max_len`.

### Impresión de Resultados
```python
print(f'Max phrase length (NL): {nl_max_len}')
print(f'Max phrase length (API): {api_max_len}')
print(f'Sequence length: {sequence_len}')
```
Se imprimen las longitudes calculadas:
- Longitud máxima de frases en lenguaje natural (`nl`).
- Longitud máxima de frases en los objetivos (`api`).
- Longitud de secuencia más larga entre las dos columnas.

### Uso

Para utilizar este código, asegúrate de tener un DataFrame `df` con las columnas `natural_language_query` y `target`. Luego, simplemente ejecuta el código para calcular y visualizar las longitudes máximas de las frases y la longitud de secuencia más larga entre las dos columnas.

## Tokenizacion

Este fragmento de código se encarga de tokenizar y paddear secuencias de texto para dos columnas de un DataFrame usando TensorFlow. A continuación, se detalla cada operación:

### Importaciones
```python
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
```
Se importan dos módulos de `tensorflow.keras`:
- `Tokenizer`: Para convertir texto a secuencias de números.
- `pad_sequences`: Para paddear (rellenar) secuencias a una longitud fija.

### Tokenización y Padding para `nl`
```python
nl_tokenizer = Tokenizer()
nl_tokenizer.fit_on_texts(nl)
nl_sequences = nl_tokenizer.texts_to_sequences(nl)
nl_x = pad_sequences(nl_sequences, maxlen=sequence_len, padding='post')
```
1. Se crea una instancia de `Tokenizer` para la columna `nl`.
2. Se ajusta el tokenizador a los textos en `nl` usando `fit_on_texts`.
3. Se convierten los textos en `nl` a secuencias de números (`nl_sequences`).
4. Se paddean las secuencias a la longitud `sequence_len` con padding posterior (`padding='post'`).

### Tokenización y Padding para `api`
```python
api_tokenizer = Tokenizer(filters='!"#$%&()*+,-./:;<=>?@\^_`{|}~	
')
api_tokenizer.fit_on_texts(api)
api_sequences = api_tokenizer.texts_to_sequences(api)
api_y = pad_sequences(api_sequences, maxlen=sequence_len + 1, padding='post')
```
1. Se crea una instancia de `Tokenizer` para la columna `api`, especificando un conjunto de filtros personalizados para excluir ciertos caracteres.
2. Se ajusta el tokenizador a los textos en `api` usando `fit_on_texts`.
3. Se convierten los textos en `api` a secuencias de números (`api_sequences`).
4. Se paddean las secuencias a la longitud `sequence_len + 1` con padding posterior (`padding='post'`).

### Uso

Para utilizar este código, asegúrate de tener un DataFrame `df` con las columnas `natural_language_query` y `target`, y haber calculado `sequence_len` como se muestra en ejemplos anteriores. Luego, simplemente ejecuta el código para tokenizar y paddear las secuencias de texto en estas columnas.

## Tamaño del vocabulario

Este fragmento de código calcula el tamaño del vocabulario para dos tokenizadores y los imprime. A continuación, se detalla cada operación:

### Cálculo del Tamaño del Vocabulario
```python
nl_vocab_size = len(nl_tokenizer.word_index) + 1
api_vocab_size = len(api_tokenizer.word_index) + 1
```
1. `nl_vocab_size`: Calcula el tamaño del vocabulario del tokenizador `nl_tokenizer`, sumando 1 al número de palabras únicas (`word_index`).
2. `api_vocab_size`: Calcula el tamaño del vocabulario del tokenizador `api_tokenizer`, sumando 1 al número de palabras únicas (`word_index`).

### Impresión de Resultados
```python
print(f'Vocabulary size (NL): {nl_vocab_size}')
print(f'Vocabulary size (API): {api_vocab_size}')
```
Se imprimen los tamaños de vocabulario calculados:
- Tamaño del vocabulario para el lenguaje natural (`nl_vocab_size`).
- Tamaño del vocabulario para los objetivos (`api_vocab_size`).

### Uso

Para utilizar este código, asegúrate de haber tokenizado los textos en `nl` y `api` utilizando instancias de `Tokenizer` como se muestra en ejemplos anteriores. Luego, simplemente ejecuta el código para calcular e imprimir los tamaños de vocabulario.

## Datos de entrada y salida

Este fragmento de código prepara los datos de entrada y salida para un modelo de aprendizaje automático, típicamente utilizado en tareas de secuencias como traducción o procesamiento de lenguaje natural. A continuación, se detalla cada operación:

### Preparación de Datos de Entrada y Salida
```python
inputs = { 'encoder_input': nl_x, 'decoder_input': api_y[:, :-1] }
outputs = api_y[:, 1:]
```
1. `inputs`: Un diccionario que contiene dos entradas:
   - `'encoder_input'`: Asignado a `nl_x`, que contiene las secuencias tokenizadas y paddeadas del lenguaje natural.
   - `'decoder_input'`: Asignado a `api_y[:, :-1]`, que contiene las secuencias tokenizadas y paddeadas del objetivo (`api`), excluyendo el último token de cada secuencia.
2. `outputs`: Asignado a `api_y[:, 1:]`, que contiene las secuencias del objetivo (`api`), excluyendo el primer token de cada secuencia. Esto se utiliza como las secuencias esperadas de salida en un modelo de secuencia a secuencia.

### Uso

Este fragmento de código es comúnmente utilizado en modelos de secuencia a secuencia (sequence-to-sequence), donde:
- `encoder_input` (entrada del codificador) es la secuencia de entrada original.
- `decoder_input` (entrada del decodificador) es la secuencia de salida desplazada por un token (excluyendo el último token).
- `outputs` (salidas esperadas) son las secuencias de salida desplazadas por un token (excluyendo el primer token).

Para utilizar este código, asegúrate de haber tokenizado y paddeado las secuencias de texto como se muestra en ejemplos anteriores. Luego, simplemente ejecuta el código para preparar las entradas y salidas para el modelo.

# Creación y entrenamiento del modelo

## Explicación del Código

Este fragmento de código construye y compila un modelo de Transformer para tareas de procesamiento de lenguaje natural usando TensorFlow y Keras. A continuación, se detalla cada operación:

### Importaciones
```python
import numpy as np
import tensorflow as tf
from tensorflow.keras import Model
from tensorflow.keras.layers import Input, Dense, Dropout
from keras_nlp.layers import TokenAndPositionEmbedding, TransformerEncoder, TransformerDecoder
```
Se importan los módulos necesarios:
- `numpy` y `tensorflow` para manipulación numérica y construcción de modelos.
- Componentes de `tensorflow.keras` para crear el modelo y capas.
- Componentes específicos de `keras_nlp` para embeddings y capas de Transformer.

### Configuración de Semillas Aleatorias
```python
np.random.seed(42)
tf.random.set_seed(42)
```
Se configuran las semillas aleatorias para reproducibilidad.

### Parámetros del Modelo
```python
num_heads = 8
embed_dim = 256
```
Se definen los parámetros del modelo:
- `num_heads`: Número de cabezas en las capas de atención del Transformer.
- `embed_dim`: Dimensión de los embeddings.

### Construcción del Codificador (Encoder)
```python
encoder_input = Input(shape=(None,), dtype='int64', name='encoder_input')
x = TokenAndPositionEmbedding(nl_vocab_size, sequence_len, embed_dim)(encoder_input)
encoder_output = TransformerEncoder(embed_dim, num_heads)(x)
```
1. `encoder_input`: Capa de entrada para el codificador.
2. `TokenAndPositionEmbedding`: Capa de embedding que combina embeddings de tokens y posiciones.
3. `TransformerEncoder`: Capa de codificador Transformer.

### Construcción del Decodificador (Decoder)
```python
encoded_seq_input = Input(shape=(None, embed_dim))

decoder_input = Input(shape=(None,), dtype='int64', name='decoder_input')
x = TokenAndPositionEmbedding(api_vocab_size, sequence_len, embed_dim, mask_zero=True)(decoder_input)
x = TransformerDecoder(embed_dim, num_heads)(x, encoded_seq_input)
x = Dropout(0.4)(x)

decoder_output = Dense(api_vocab_size, activation='softmax')(x)
```
1. `encoded_seq_input`: Entrada de secuencias codificadas para el decodificador.
2. `decoder_input`: Capa de entrada para el decodificador.
3. `TokenAndPositionEmbedding`: Capa de embedding para el decodificador con `mask_zero` activado.
4. `TransformerDecoder`: Capa de decodificador Transformer.
5. `Dropout`: Capa de regularización.
6. `Dense`: Capa densa con activación softmax para generar la salida final.

### Definición del Modelo
```python
decoder = Model([decoder_input, encoded_seq_input], decoder_output)
decoder_output = decoder([decoder_input, encoder_output])

model = Model([encoder_input, decoder_input], decoder_output)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary(line_length=120)
```
1. Se define un modelo intermedio `decoder` para el decodificador.
2. Se conecta la salida del codificador con el decodificador.
3. Se define el modelo completo que toma `encoder_input` y `decoder_input`.
4. Se compila el modelo con el optimizador `adam` y la función de pérdida `sparse_categorical_crossentropy`.
5. Se imprime un resumen del modelo.

### Uso

Este código construye y compila un modelo Transformer adecuado para tareas de secuencia a secuencia en procesamiento de lenguaje natural. Asegúrate de tener definidos `nl_vocab_size`, `api_vocab_size` y `sequence_len` antes de ejecutar este código.


## Entrenamiento

Este fragmento de código configura y entrena un modelo de aprendizaje automático, y luego guarda el modelo entrenado en un archivo. A continuación, se detalla cada operación:

### Importaciones
```python
from tensorflow.keras.callbacks import EarlyStopping
```
Se importa `EarlyStopping` de `tensorflow.keras.callbacks`, que es una técnica para detener el entrenamiento temprano si la métrica de validación no mejora.

### Configuración del Callback EarlyStopping
```python
callback = EarlyStopping(monitor='val_accuracy', patience=3, restore_best_weights=True)
```
1. `monitor='val_accuracy'`: Monitorea la métrica de precisión en el conjunto de validación.
2. `patience=3`: Detiene el entrenamiento si la métrica de validación no mejora después de 3 épocas consecutivas.
3. `restore_best_weights=True`: Restaura los pesos del modelo al estado de la mejor época.

### Entrenamiento del Modelo
```python
#hist = model.fit(inputs, outputs, epochs=30, validation_split=0.3, callbacks=[callback])
hist = model.fit(inputs, outputs, epochs=30, validation_split=0.2)
```
1. `inputs` y `outputs`: Datos de entrada y salida para el entrenamiento.
2. `epochs=30`: Número de épocas para entrenar el modelo.
3. `validation_split=0.2`: Porcentaje de datos utilizados para la validación (20% en este caso).

El comentario indica que se puede usar un `validation_split` del 30% y el callback `EarlyStopping`, pero la línea activa usa un `validation_split` del 20% sin el callback.

### Guardado del Modelo
```python
model.save('/content/gdrive/MyDrive/TFM - KSCHOOL - DataScience/Recursos/modeloBS64.keras')
```
Guarda el modelo entrenado en un archivo en el directorio especificado. El archivo tendrá la extensión `.keras`.

## Uso

Para utilizar este código, asegúrate de haber definido y compilado un modelo como se muestra en ejemplos anteriores. Luego, simplemente ejecuta el código para entrenar el modelo con los datos `inputs` y `outputs`, y guarda el modelo entrenado en la ubicación especificada.

# Comparativa accuracy

## Explicación del Código

Este fragmento de código visualiza la precisión del modelo durante el entrenamiento y la validación utilizando Seaborn y Matplotlib. A continuación, se detalla cada operación:

### Importaciones
```python
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
sns.set()
```
1. `seaborn` y `matplotlib.pyplot` se importan para crear gráficos.
2. `%matplotlib inline` se usa en Jupyter Notebooks para mostrar los gráficos en línea.
3. `sns.set()` configura el estilo estético de Seaborn para los gráficos.

### Extracción de Datos de Historial
```python
acc = hist.history['accuracy']
val = hist.history['val_accuracy']
epochs = range(1, len(acc) + 1)
```
1. `acc`: Lista de valores de precisión durante el entrenamiento.
2. `val`: Lista de valores de precisión durante la validación.
3. `epochs`: Rango de épocas utilizado para el eje x en el gráfico.

### Creación del Gráfico
```python
plt.plot(epochs, acc, '-', label='Training accuracy')
plt.plot(epochs, val, ':', label='Validation accuracy')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.plot()
```
1. `plt.plot(epochs, acc, '-', label='Training accuracy')`: Grafica la precisión del entrenamiento con una línea sólida.
2. `plt.plot(epochs, val, ':', label='Validation accuracy')`: Grafica la precisión de la validación con una línea punteada.
3. `plt.title('Training and Validation Accuracy')`: Establece el título del gráfico.
4. `plt.xlabel('Epoch')`: Etiqueta el eje x como "Epoch".
5. `plt.ylabel('Accuracy')`: Etiqueta el eje y como "Accuracy".
6. `plt.legend(loc='lower right')`: Muestra la leyenda en la parte inferior derecha del gráfico.

### Uso

Para utilizar este código, asegúrate de haber entrenado un modelo y tener disponible el historial (`hist`). Luego, simplemente ejecuta el código para visualizar la precisión del modelo durante el entrenamiento y la validación.


