# NL-toGA4-Query
Translate natural language queries into Google Analytics 4 (GA4) API query format. This project helps convert user-friendly questions into structured GA4 queries for efficient data retrieval.

Vamos a dividir las consultas a Google Analytics 4 en diferentes tipos para simplificar el proceso de desarrollo y garantizar una cobertura integral de las capacidades de la API.


## Tipo 1: Consultas de Métricas con Rango de Fechas

Las consultas de **Tipo 1** son las más básicas y comprenden únicamente una métrica y un rango de fechas.
No incluye: filtros dimensiones o segmentaciones

### Ejemplos

1. **Dame el número total de usuarios en marzo de 2022.**
   - Métrica: `users`
   - Rango de Fechas: `2022-03-01 a 2022-03-31`

2. **Quiero ver las sesiones totales del último trimestre.**
   - Métrica: `sessions`
   - Rango de Fechas: `2022-01-01 a 2022-03-31`

3. **Dame las páginas vistas durante diciembre de 2021.**
   - Métrica: `pageViews`
   - Rango de Fechas: `2021-12-01 a 2021-12-31`

4. **Quiero ver el total de eventos completados en febrero de 2022.**
   - Métrica: `eventCount`
   - Rango de Fechas: `2022-02-01 a 2022-02-28`

5. **Quiero ver el total de nuevas suscripciones durante el año pasado.**
   - Métrica: `newUsers`
   - Rango de Fechas: `2021-01-01 a 2021-12-31`

### Ejemplo de generación de pares

#### Consulta en lenguaje natural
```json
Necesito el costo por conversión en el 5 de mayo de 2014.
```
#### Consulta de tipo 1 traducida en formato JSON

```json
{
  "metrics": ["advertiserAdCostPerConversion"],
  "dateRanges": [{"startDate": "2014-05-05", "endDate": "2014-05-05"}]
}
```

#### Consulta en lenguaje natural
```json
Necesito el total de usuarios de la cohorte del último mes.
```
#### Consulta de tipo 1 traducida en formato JSON

```json
{
  "metrics": ["cohortTotalUsers"],
  "dateRanges": [{"startDate": "lastCalendarMonth", "endDate": "lastCalendarMonth"}]
}
```

## Tipo 2: Consultas de Métricas con Rango de Fechas y Dos Métricas

Las consultas de **Tipo 2** son un nivel más avanzado que las de **Tipo 1** y comprenden dos métricas y un rango de fechas.
No incluye: filtros dimensiones o segmentaciones.

### Ejemplos

1. **Dame el número total de usuarios y el número de sesiones en marzo de 2022.**
   - Métricas: `users`, `sessions`
   - Rango de Fechas: `2022-03-01 a 2022-03-31`

2. **Quiero ver las sesiones totales y las páginas vistas del último trimestre.**
   - Métricas: `sessions`, `pageViews`
   - Rango de Fechas: `2022-01-01 a 2022-03-31`

3. **Dame las páginas vistas y los eventos completados durante diciembre de 2021.**
   - Métricas: `pageViews`, `eventCount`
   - Rango de Fechas: `2021-12-01 a 2021-12-31`

4. **Quiero ver el total de eventos completados y el total de usuarios nuevos en febrero de 2022.**
   - Métricas: `eventCount`, `newUsers`
   - Rango de Fechas: `2022-02-01 a 2022-02-28`

5. **Quiero ver el total de nuevas suscripciones y el total de usuarios activos durante el año pasado.**
   - Métricas: `newUsers`, `activeUsers`
   - Rango de Fechas: `2021-01-01 a 2021-12-31`

### Ejemplo de generación de pares

#### Consulta en lenguaje natural
```json
Necesito el número total de usuarios y sesiones en el 5 de mayo de 2014.
```
#### Consulta de tipo 1 traducida en formato JSON

```json
{
  "metrics": ["users", "sessions"],
  "dateRanges": [{"startDate": "2014-05-05", "endDate": "2014-05-05"}]
}
```

#### Consulta en lenguaje natural
```json
Necesito el total de usuarios y páginas vistas del último mes.
```
#### Consulta de tipo 1 traducida en formato JSON

```json
{
  "metrics": ["users", "pageViews"],
  "dateRanges": [{"startDate": "lastCalendarMonth", "endDate": "lastCalendarMonth"}]
}
```

## Tipo 3: Consultas de Métricas con Rango de Fechas y Dimensiones

Las consultas de **Tipo 3** combinan una métrica con una dimensión junto con un rango de fechas.
No incluye: filtros o segmentaciones adicionales.

### Ejemplos

1. **Dame la tasa de conversión por campaña en enero de 2023.**
   - Métrica: `conversionRate`
   - Dimensión: `campaign`
   - Rango de Fechas: `2023-01-01 a 2023-01-31`

2. **Quiero ver las sesiones totales por navegador del último trimestre.**
   - Métrica: `sessions`
   - Dimensión: `browser`
   - Rango de Fechas: `2023-01-01 a 2023-03-31`

3. **Dame los ingresos por producto durante noviembre de 2022.**
   - Métrica: `itemRevenue`
   - Dimensión: `productName`
   - Rango de Fechas: `2022-11-01 a 2022-11-30`

4. **Quiero ver el total de eventos completados por tipo de evento en abril de 2023.**
   - Métrica: `eventCount`
   - Dimensión: `eventName`
   - Rango de Fechas: `2023-04-01 a 2023-04-30`

5. **Quiero ver el total de usuarios activos por ciudad durante el último mes.**
   - Métrica: `activeUsers`
   - Dimensión: `city`
   - Rango de Fechas: `2023-05-01 a 2023-05-31`

### Ejemplo de generación de pares

#### Consulta en lenguaje natural

```json
Necesito el número de conversiones por campaña el 15 de febrero de 2023.
```
##### Consulta de tipo 1 traducida en formato JSON

```json
{
  "metrics": ["conversionRate"],
  "dimensions": ["campaign"],
  "dateRanges": [{"startDate": "2023-02-15", "endDate": "2023-02-15"}]
}
```

#### Ejemplo de generación de pares con fechas relativas

##### Consulta en lenguaje natural
```json
Necesito el total de usuarios activos por ciudad del último mes.
```
##### Consulta de tipo 1 traducida en formato JSON

```json
{
  "metrics": ["activeUsers"],
  "dimensions": ["city"],
  "dateRanges": [{"startDate": "lastCalendarMonth", "endDate": "lastCalendarMonth"}]
}
```