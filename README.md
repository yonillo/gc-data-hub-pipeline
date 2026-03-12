# ⛽ Gran Canaria Fuel Data Pipeline (ETL)

[![GC Fuel Data Pipeline](https://github.com/yonillo/gc-data-hub-pipeline/actions/workflows/main.yml/badge.svg)](https://github.com/yonillo/gc-data-hub-pipeline/actions/workflows/main.yml)

Este proyecto es un pipeline de ingeniería de datos (ETL) automatizado que monitoriza, procesa y almacena los precios de carburantes en la provincia de Las Palmas, con un enfoque específico en **Agaete, Gran Canaria**.

---

## 🏗️ Arquitectura del Pipeline

El sistema sigue una arquitectura de tres capas diseñada para ser robusta, escalable y eficiente:



1.  **Extract (Extracción):** Ingesta de datos en tiempo real desde la API oficial del Ministerio de Industria, Energía y Turismo. Manejo de excepciones y validación de respuesta de red.
2.  **Transform (Transformación):** Procesamiento con **Pandas**. Limpieza de tipos de datos, normalización de precios (comma-to-dot), filtrado geográfico por ID de provincia (35) y generación de métricas comparativas.
3.  **Load (Carga):** Persistencia en formato **Apache Parquet**. A diferencia del CSV, Parquet ofrece almacenamiento columnar y compresión de alta eficiencia, ideal para entornos de Big Data.

---

## 🛠️ Tech Stack & Herramientas

* **Lenguaje:** Python 3.10+
* **Procesamiento:** [Pandas](https://pandas.pydata.org/) & [PyArrow](https://arrow.apache.org/docs/python/index.html)
* **Automatización:** [GitHub Actions](https://github.com/features/actions) (Ejecución programada mediante Cron)
* **Formato de Datos:** Apache Parquet (Storage-efficient)
* **Infraestructura:** Entorno Linux (Ubuntu-latest) en GitHub Runners

---

## 🤖 Automatización y DevOps

El pipeline es un **organismo vivo**. Gracias a GitHub Actions, el proceso se dispara automáticamente cada mañana a las 08:00 AM UTC. 

* **CI/CD:** El flujo instala dependencias, ejecuta la lógica de ingeniería y realiza un *auto-commit* de los nuevos datos particionados en la carpeta `/data`.
* **Logging:** Sistema de logs profesional para monitorizar la salud del proceso y depurar errores de la fuente de datos.

---

## 📊 ¿Por qué Parquet?

En este proyecto he sustituido el uso tradicional de CSV por **Parquet** debido a:
* **Compresión:** Reducción de hasta un 80% en el peso del archivo.
* **Esquema:** Preservación estricta de los tipos de datos (float, int, datetime).
* **Rendimiento:** Optimizado para futuras consultas analíticas y dashboards.

---

## 📈 Análisis Local (Agaete Focus)
El pipeline calcula dinámicamente el diferencial de precios entre el municipio de **Agaete** y la media provincial, permitiendo identificar oportunidades de ahorro y tendencias de mercado local en tiempo real.

---

> Prototipo desarrollado por **Yone Suárez** | Estudiante de Ciencia e Ingeniería de Datos (ULPGC) & Administrador Linux (Red Hat Certified).
