# Generador de Datasets de Consultas a GA4

Este proyecto genera un dataset que relaciona consultas en lenguaje natural con sus equivalentes en la API de Google Analytics 4 (GA4). El objetivo es facilitar la creación de consultas para extraer datos de GA4 utilizando lenguaje natural, lo que puede ser útil para entrenar modelos de procesamiento de lenguaje natural (NLP).

## Descripción

La solución genera pares de consultas en lenguaje natural y sus equivalentes en formato de API de GA4. Utiliza un enfoque modular para seleccionar aleatoriamente métricas, dimensiones, filtros y rangos de fechas, garantizando una variedad significativa en el dataset generado.

## Instalación

### Requisitos Previos

- Python 3.7 o superior
- Pip (Gestor de paquetes de Python)

### Dependencias

Instalar las dependencias necesarias utilizando el siguiente comando:

```bash
pip install -r requirements.txt
```

### Configuración
Clonar el repositorio:

```bash
git clone https://github.com/danielurrutxua/NL-to-GA4-Query.git
cd NL-to-GA4-Query/dataset-generator
```

### Uso
Ejecutar el script principal para generar los pares de consultas:
```bash
python src/app.py
```

### Entrada del Usuario

La aplicación solicitará los siguientes inputs:

1. **Número de Pares**: Cantidad de pares de consultas a generar.
2. **Filtros**: Indicar si se desean incluir filtros (y/n).
3. **Fechas**: Indicar si se desean incluir rangos de fechas (y/n).

### Ejemplo de ejecución
```bash
Introduce la cantidad de pares: 100
¿Quieres que se generen filtros? y/n: y
¿Quieres que se generen fechas? y/n: y
```

### Ejemplo de Salida

#### Consulta en Lenguaje Natural

"Dame el número de sesiones por país en enero de 2023, filtrado por España."

#### Consulta Equivalente en la API de GA4 (JSON)

```json
{
  "natural_language_query": "Dame el número de sesiones por país en enero de 2023, filtrado por España.",
  "api_query": {
    "metrics": ["sessions"],
    "dimensions": ["country"],
    "dateRanges": [{"startDate": "2023-01-01", "endDate": "2023-01-31"}],
    "dimensionFilter": {
      "filter": {
        "fieldName": "country",
        "stringFilter": {
          "matchType": "EXACT",
          "value": "Spain"
        }
      }
    }
  }
}
```
## Estructura del Proyecto

### Generación de Consultas

1. **Inicio de la Frase**: Se selecciona aleatoriamente una frase inicial utilizando un diccionario de sinónimos.
2. **Selección de Métricas**: Se eligen una o dos métricas aleatoriamente de un archivo CSV.
3. **Selección de Dimensiones**: Se elige una dimensión aleatoriamente de un archivo CSV.
4. **Selección de Filtros**: Se aplican filtros a métricas o dimensiones según lo especificado por el usuario.
5. **Selección de Fechas**: Se generan rangos de fechas utilizando varios tipos de rangos predefinidos.

### Exportación de Resultados

Los pares de consultas generados se exportan a un archivo CSV para su uso posterior. El archivo generado se llama `output.csv`.


