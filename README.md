# NL-to-GA4-Query

![TFM](https://github.com/user-attachments/assets/8d17ff97-fed0-433c-bfcf-05085900bff7)

## 📁 Contenidos
- **dataset-generator** : Scripts utilizados para generar el dataset de pares entre lenguaje natural y el listado de metricas, dimensiones, filtros y fechas compatibles con la API de Google Analytics 4.
- **google-cloud-platform** : Archivos a subir a la máquina virtual que actúa de endpoint con un servidor Flask en Google Cloud Platform con el servicio Compute Engine.
- **notebook** : Archivo compatible con Google Collab para entrenar el modelo Transformer Enconder-Decoder con KerasNLP
- **reflx-chat** : Interfaz gráfica para consultar el modelo entrenado anteriormente y alojado en Google Cloud.
- **resources** : Diferentes archivos usados en el proceso (listado de metricas, dimensiones, sinónimos, etc)

## 📈 Herramienta para eliminar la dependencia del equipo comercial del equipo de Analítica Digital

En muchas organizaciones, el equipo comercial depende del equipo de analítica digital para obtener datos y análisis sobre los clientes. Esto puede resultar en retrasos y cuellos de botella que afectan la eficiencia y la agilidad de las operaciones comerciales. Una herramienta que permita al equipo comercial acceder directamente a los datos de los clientes puede ser altamente beneficiosa.

### Beneficios de la Herramienta

1. **Eficiencia Operativa**:
    - **Reducción de Retrasos**: Los equipos comerciales pueden acceder a la información en tiempo real sin esperar a que el equipo de analítica digital procese y entregue los datos.
    - **Mayor Autonomía**: Los comerciales pueden realizar consultas específicas y personalizadas según sus necesidades inmediatas.

2. **Agilidad en la Toma de Decisiones**:
    - **Respuestas Rápidas**: La capacidad de obtener datos de manera instantánea permite tomar decisiones rápidas y oportunas, cruciales en un entorno competitivo.
    - **Adaptabilidad**: Los equipos comerciales pueden ajustar sus estrategias sobre la marcha basándose en datos actualizados.

3. **Mejora en la Relación con el Cliente**:
    - **Personalización**: Los comerciales pueden acceder a información detallada del cliente y ofrecer propuestas personalizadas que se alineen mejor con las necesidades y preferencias del cliente.
    - **Satisfacción del Cliente**: Una respuesta más rápida y precisa puede mejorar la experiencia del cliente, aumentando la satisfacción y fidelidad.

### Ejemplo Económico

Supongamos una empresa de software B2B con un equipo comercial de 10 personas y un equipo de analítica digital de 3 personas. El proceso actual implica que cada solicitud de datos del equipo comercial toma en promedio 2 días laborables para ser procesada por el equipo de analítica digital. 

#### Costos Actuales:
- **Salario promedio del equipo comercial**: 60,000€ anuales por persona.
- **Salario promedio del equipo de analítica digital**: 80,000€ anuales por persona.
- **Costo de oportunidad**: Si un comercial espera 2 días para obtener datos y cerrar una venta, se estima una pérdida de ingresos potenciales de 1,000€ por día.

### Impacto Económico de la Herramienta

1. **Reducción del Tiempo de Espera**:
    - Eliminando el tiempo de espera de 2 días, los comerciales pueden cerrar ventas más rápidamente.
    - Si cada comercial tiene una probabilidad del 10% de cerrar una venta adicional de 1,000€ por día debido a la reducción de tiempo de espera, esto resultaría en €1,000 adicionales por día para el equipo comercial completo, de 10 miembros.

2. **Aumento en la Eficiencia del Equipo de Analítica Digital**:
    - El equipo de analítica digital puede dedicar más tiempo a análisis complejos y estratégicos en lugar de responder consultas rutinarias.
    - Asumiendo que el equipo de analítica digital puede mejorar su productividad en un 30%, la empresa podría ahorrar o redirigir recursos equivalentes a 72,000€ anuales.

3. **Costo de Implementación de la Herramienta**:
    - Supongamos que el desarrollo e implementación de la herramienta cuesta 50,000€.
    - El mantenimiento anual y actualizaciones cuestan 10,000€.

### Análisis del Retorno de Inversión (ROI)

- **Ingresos Adicionales Anuales**: 1,000€ por día * 250 días laborables = 250,000€
- **Ahorros Anuales por Mejora en Productividad del Equipo de Analítica Digital**: 72,000€
- **Costo Total del Primer Año**: 50,000€ (implementación) + 10,000€ (mantenimiento) = 60,000€

**ROI del Primer Año**:
![image](https://github.com/user-attachments/assets/f2d53386-c7d8-436a-a7d9-e97695b415ab)

**ROI de años siguientes**
![image](https://github.com/user-attachments/assets/7dcc5ab7-454a-484f-a6dd-a685f70868e8)


### Conclusión

Una herramienta que elimine la dependencia del equipo comercial del equipo de analítica digital puede significar una mejora significativa en la eficiencia operativa, agilidad en la toma de decisiones y en la relación con el cliente. El análisis económico muestra que la inversión en dicha herramienta puede ofrecer un alto retorno de inversión, con ingresos adicionales y ahorros significativos.

