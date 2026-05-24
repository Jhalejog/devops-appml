# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Goal

Train and deploy a machine learning app via Flask. This is an MLOps/DevOps project focused on the full lifecycle: model training, serving via API, and deployment.

## Environment

- Python 3.13.5 via miniconda3, with a local `.venv` virtual environment.
- Activate before running anything: `.venv\Scripts\Activate.ps1` (PowerShell) or `.venv\Scripts\activate.bat` (CMD).

## Running the App

```powershell
.venv\Scripts\Activate.ps1
python app.py
```

The Flask server starts on `http://0.0.0.0:8080`.

## Installing Dependencies

```powershell
pip install -r requirements.txt
```

## Architecture

- `app.py` — Flask application entry point. Defines HTTP routes that servirán predicciones del modelo.
- `src/data/` — Ingesta y preprocesamiento de datos.
- `src/features/` — Ingeniería de features.
- `src/models/` — Entrenamiento y evaluación de modelos.
- `src/utils/` — Utilidades compartidas.
- `data/raw/` — Datos originales sin modificar.
- `data/processed/` — Datos limpios listos para entrenar.
- `models/` — Artefactos serializados de modelos entrenados (.pkl, .onnx, etc.).
- `configs/` — Hiperparámetros y configuración en YAML/JSON.
- `notebooks/` — Exploración y experimentación.
- `tests/` — Pruebas unitarias e integración.
- `docker/` — Dockerfiles para containerización.
- `.github/workflows/` — Pipelines de CI/CD.
