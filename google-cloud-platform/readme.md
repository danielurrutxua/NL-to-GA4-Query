
# API de Análisis de Datos de Google Analytics

Este proyecto proporciona una API basada en Flask que permite realizar consultas a Google Analytics utilizando un lenguaje natural. El script en Python maneja la interpretación de texto en lenguaje natural, la consulta a la API de Google Analytics y el retorno de resultados en formato JSON.

## Requisitos

Para ejecutar este proyecto, asegúrate de tener instalados los siguientes paquetes de Python:

- flask
- pandas
- tensorflow
- keras-nlp
- google-auth
- google-analytics-data

Puedes instalarlos utilizando pip:

```bash
pip install flask pandas tensorflow keras-nlp google-auth google-analytics-data
```

## Estructura del Proyecto

1. **Importaciones**
   - El script comienza importando los módulos necesarios, incluidos Flask, pandas, y varias herramientas de TensorFlow/Keras para procesamiento de texto y creación de modelos de machine learning.
   
2. **Funciones Principales**
   
   - `parseTranslate(text)`: Esta función toma una cadena de texto en lenguaje natural y la descompone en métricas, dimensiones y filtros para las consultas de Google Analytics. Separa las palabras clave basándose en identificadores como `segmentedby` y `filteredby`.

   - `camelCase(api_parameters, list, type)`: Convierte una lista de métricas o dimensiones en su formato de API correspondiente (camelCase). Esta función utiliza un DataFrame de pandas (`api_parameters`) que mapea los nombres en miniscula generados por el modelo a los nombres de la API en formato camelCase.

3. **Configuración de Flask**
   
   - Se configura una instancia de Flask para manejar las solicitudes HTTP.

4. **Autenticación con Google Analytics**
   
   - Utiliza las credenciales del servicio para autenticarse con la API de Google Analytics.

5. **Definición de Rutas**
   
   - El script define varias rutas en Flask para manejar diferentes tipos de solicitudes. La ruta principal procesa el texto de entrada, lo traduce a parámetros de API y realiza la consulta a Google Analytics.

## Uso

1. **Iniciar el Servidor**
   
   Para iniciar el servidor Flask, ejecuta el script `deep.py`:

   ```bash
   python deep.py
   ```

2. **Realizar Consultas**
   
   Una vez que el servidor esté en funcionamiento, puedes realizar consultas enviando una solicitud POST a la ruta definida con un JSON que contenga el texto en lenguaje natural que deseas interpretar.

## Ejemplo de Solicitud

```bash
curl -X POST -H "Content-Type: application/json" -d '{"query":"dime las sesiones segmentadas por tipo de dispositivo"}' http://localhost:5000/query
```

## Respuesta

El servidor responderá con un JSON que contiene los resultados de la consulta a Google Analytics basada en la interpretación del texto de entrada.

## Notas Adicionales

- Asegúrate de tener las credenciales adecuadas y acceso a la API de Google Analytics.
- La función `camelCase` depende de un DataFrame `api_parameters`, asegúrate de cargar este DataFrame correctamente en tu entorno a través de los CSVs alojados en la raíz del servidor.

Este proyecto es una herramienta para traducir consultas en lenguaje natural a consultas formales a la API de Google Analytics, facilitando así la extracción de datos y la generación de informes.
