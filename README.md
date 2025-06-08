# pad_2025_1_2

## Proyecto ETL con Automatización CI/CD y Docker

## Objetivo

Aplicar la metodología GitHub Actions para automatizar procesos clave de desarrollo y despliegue de servicios, garantizando una puesta en producción eficiente y escalable.

## Descripción General

Este proyecto implementa un flujo ETL (Extracción, Transformación y Carga) para datos, orquestado con GitHub Actions y empaquetado con Docker para facilitar su despliegue.

## Flujo de Trabajo

### 1. Preparación del Entorno

- Configura dependencias y estructura del proyecto.
- Se ejecuta al hacer push al branch principal o manualmente.

### 2. Extracción de Datos

- Extrae datos desde fuentes externas (como Yahoo Finance).
- Guarda datos en archivos CSV.
- Corre automáticamente cada 12 horas o manualmente.

### 3. Carga de Datos

- Inserta los datos extraídos en la base de datos SQLite.
- Limpia archivos temporales luego de la carga.
- Se ejecuta tras la extracción exitosa.

### 4. Monitoreo

- Revisa la integridad y tendencias de los datos.
- Genera logs y envía alertas por correo si se detectan anomalías.
- Corre tras la carga o cada 6 horas.

## Estructura del Proyecto

```pad_2025_1_2/
├── .github/
│ └── workflows/
│ ├── 0-setup-environment.yml
│ ├── 1-data-extraction.yml
│ ├── 2-data-ingestion.yml
│ └── 3-data-monitoring.yml
├── src/
│ └── edu_pad/
│ ├── database.py
│ ├── dataweb.py
│ ├── main_extractor.py
│ ├── main_ingesta.py
│ ├── monitor.py
│ └── static/
│ ├── csv/
│ ├── db/
│ └── logs/
├── dockerFile
├── setup.py
└── README.md```

bash
Copy
Edit

## Cómo usar Docker

````markdown
1. Construye la imagen con:

```bash
docker build -t dajesa0937/pad_2025_1_2:latest .
Ejecuta el contenedor:
```

bash
Copy
Edit
docker run -it --rm dajesa0937/pad_2025_1_2:latest
Requisitos
Tener Docker instalado y corriendo.

Configurar secretos en GitHub para notificaciones por correo.

Personalización
Modifica dataweb.py para cambiar la fuente de datos.

Ajusta los workflows YAML para cambiar la frecuencia de ejecución.

Añade transformaciones o monitoreo en los scripts de Python.

Este proyecto sirve para aprendizaje y práctica en integración continua, despliegue con contenedores y automatización con GitHub Actions.

yaml
Copy
Edit

---



