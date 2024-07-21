# Reflex.dev

Reflex.dev es una plataforma de desarrollo web que permite a los programadores crear aplicaciones web interactivas y dinámicas con facilidad. Con Reflex.dev, puedes concentrarte en la lógica de tu aplicación sin preocuparte por los detalles complicados del front-end y el back-end.

## Características principales

- **Framework Unificado**: Reflex.dev proporciona un entorno de desarrollo unificado que simplifica la creación de aplicaciones web completas. No necesitas configurar múltiples herramientas y frameworks separados.
- **Desarrollo Rápido**: Ofrece una serie de herramientas y utilidades que aceleran el proceso de desarrollo, permitiéndote construir y desplegar aplicaciones más rápidamente.
- **Escalabilidad**: Diseñado para ser escalable, Reflex.dev soporta aplicaciones desde prototipos simples hasta grandes sistemas empresariales.
- **Interactividad**: Facilita la creación de interfaces de usuario interactivas con una mínima cantidad de código, gracias a su enfoque en la simplicidad y eficiencia.
- **Ecosistema Completo**: Incluye todo lo necesario para el desarrollo web, desde la gestión de bases de datos hasta la autenticación de usuarios y la gestión del estado de la aplicación.

## Funciones principales

No vamos a entrar en detalle a explicar todo el sistema, nos centraremos en el procesamiento del formulario y en la recepción por parte del servidor de la llamada.

### Procesamiento de la llamada

```bash
endpoint_url = "http://35.247.85.124:5000/translate"
        data = {
            "text": question,
            "propiedad": "properties/" + propiedad,
            "inicio": inicio,
            "fin": fin
        }
```

En la línea 130 de state.py se hace la llamada al endopoint con IP Fija y con el puerto 5000 abierto. En la petición se envía:
- El texto escrito en el chat.
- La propiedad de GA4 a la que hacer la consulta del input de tipo texto de la interfaz.
- Las fechas de inicio y fin del periodo sobre el que realizar la consulta a la API de GA4.

  
Del lado del servidor, en el archivo deep.py que se puede encontrar en la carpeta google-cloud-platform de este repositorio se recibe la llamada.

```bash
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
```
La función returnTranslation se encarga de llamar al modelo y hacer la consulta a la API de GA4 devolviendo tanto la traducción del modelo como los datos de la consulta a la API.

De nuevo en el lado de cliente se recibe la respuesta y se concatena en el texto de respuesta en el chat.
