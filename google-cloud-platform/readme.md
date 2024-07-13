
# Guía para Crear y Activar una Máquina Virtual en Google Cloud Platform

Esta guía detalla los pasos para crear y activar una máquina virtual (VM) en Google Cloud Platform (GCP) usando Compute Engine.

## Prerrequisitos

1. Cuenta de Google Cloud Platform.
2. Proyecto configurado en Google Cloud.

## Pasos para Crear una Máquina Virtual

### 1. Iniciar Sesión en Google Cloud

Primero, asegúrate de estar autenticado en Google Cloud. Puedes hacerlo mediante la interfaz web de Google Cloud Console o utilizando la herramienta de línea de comandos `gcloud`.

```bash
gcloud auth login
```

### 2. Seleccionar el Proyecto

Asegúrate de que estás trabajando en el proyecto correcto. Puedes listar tus proyectos y seleccionar el adecuado con los siguientes comandos:

```bash
gcloud projects list
gcloud config set project [PROJECT_ID]
```

Reemplaza `[PROJECT_ID]` con el ID de tu proyecto.

### 3. Crear una Máquina Virtual

Para crear una nueva instancia de VM, usa el siguiente comando:

```bash
gcloud compute instances create [INSTANCE_NAME] \
    --zone=[ZONE] \
    --machine-type=[MACHINE_TYPE] \
    --subnet=default \
    --network-tier=PREMIUM \
    --maintenance-policy=MIGRATE \
    --image-family=debian-9 \
    --image-project=debian-cloud \
    --boot-disk-size=10GB \
    --boot-disk-type=pd-standard \
    --boot-disk-device-name=[INSTANCE_NAME]
```

Reemplaza `[INSTANCE_NAME]`, `[ZONE]` y `[MACHINE_TYPE]` con los valores específicos de tu configuración.

### 4. Verificar la Creación de la VM

Para verificar que la VM ha sido creada correctamente, usa el siguiente comando:

```bash
gcloud compute instances list
```

Busca el nombre de tu instancia en la lista para confirmar su creación.

## Pasos para Activar una Máquina Virtual

### 1. Iniciar la Máquina Virtual

Identifica el nombre de la instancia de VM que deseas iniciar y la zona en la que está ubicada. Luego, usa el siguiente comando para iniciar la VM:

```bash
gcloud compute instances start [INSTANCE_NAME] --zone=[ZONE]
```

Reemplaza `[INSTANCE_NAME]` con el nombre de tu instancia y `[ZONE]` con la zona en la que se encuentra.

### 2. Verificar el Estado de la VM

Para asegurarte de que la VM ha sido iniciada correctamente, puedes verificar su estado con:

```bash
gcloud compute instances describe [INSTANCE_NAME] --zone=[ZONE]
```

Busca la sección `status` en la salida del comando. Debería indicar `RUNNING` si la VM está activa.

### 3. Acceder a la Máquina Virtual

Puedes acceder a tu VM usando SSH. Google Cloud proporciona una forma sencilla de hacerlo con el siguiente comando:

```bash
gcloud compute ssh [INSTANCE_NAME] --zone=[ZONE]
```

Este comando abrirá una sesión SSH en tu VM.

## Instalación de Python y Bibliotecas Necesarias

Una vez que hayas accedido a tu VM, puedes instalar Python y las bibliotecas necesarias con los siguientes pasos:

### 1. Actualizar el Sistema e Instalar Python

```bash
sudo apt-get update
sudo apt-get install -y python3 python3-pip
```

### 2. Instalar TensorFlow, Keras y Flask

```bash
pip3 install tensorflow keras flask
```

## Subir Archivos a la Máquina Virtual

Para subir archivos como `deep.py`, `modelo.keras` y otros, puedes usar `gcloud compute scp`. Asegúrate de estar en el mismo directorio que tus archivos locales o proporciona la ruta completa.

### Ejemplo de Comando para Subir Archivos

```bash
gcloud compute scp deep.py modelo.keras [USER]@[INSTANCE_NAME]:~/ --zone=[ZONE]
```

Reemplaza `[USER]`, `[INSTANCE_NAME]` y `[ZONE]` con los valores específicos de tu configuración.

## Recursos Adicionales

- [Documentación de Google Cloud](https://cloud.google.com/docs)
- [gcloud compute instances](https://cloud.google.com/sdk/gcloud/reference/compute/instances)
