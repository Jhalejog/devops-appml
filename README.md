# devops-appml

A machine learning web application deployed via Flask that predicts California housing prices based on property and location features. The model is trained on the **California Housing** dataset from `sklearn.datasets` and served through a REST API, following an MLOps lifecycle: data ingestion, feature engineering, model training, and deployment.

## What It Does

Given a set of housing characteristics, the API returns a predicted median house value for a block in California. The model is trained offline and loaded at startup — no retraining happens at request time.

## Dataset: California Housing

Source: `sklearn.datasets.fetch_california_housing` (derived from the 1990 U.S. Census).

**Target variable:** `MedHouseVal` — median house value for California districts, in units of $100,000.

**Features (8 numeric):**

| Feature | Description |
|---|---|
| `MedInc` | Median income in block group (in tens of thousands of USD) |
| `HouseAge` | Median house age in block group (years) |
| `AveRooms` | Average number of rooms per household |
| `AveBedrms` | Average number of bedrooms per household |
| `Population` | Block group population |
| `AveOccup` | Average number of household members |
| `Latitude` | Block group latitude |
| `Longitude` | Block group longitude |

**Size:** 20,640 samples, no missing values.

## Architecture

```
devops-appml/
├── app.py                          Flask entry point — exposes prediction endpoints
├── requirements.txt                Python dependencies
├── src/
│   └── data/
│       ├── ingest.py               Data ingestion from sklearn datasets
│       └── preprocess.py           Data cleaning and preprocessing
├── notebooks/
│   └── 01_eda_preliminar.ipynb     Exploratory data analysis
└── tests/                          Unit and integration tests
```

## Running the App

```powershell
# Activate virtual environment
.venv\Scripts\Activate.ps1

# Start the Flask server
python app.py
```

Server runs on `http://0.0.0.0:8080`.

## Installing Dependencies

```powershell
pip install -r requirements.txt
```

## API Usage

```bash
POST /predict
Content-Type: application/json

{
  "MedInc": 8.3252,
  "HouseAge": 41.0,
  "AveRooms": 6.984,
  "AveBedrms": 1.024,
  "Population": 322.0,
  "AveOccup": 2.555,
  "Latitude": 37.88,
  "Longitude": -122.23
}
```

Response:

```json
{
  "predicted_value": 4.526
}
```

## Deployment

The app is containerized via Docker and deployable through the CI/CD pipeline defined in `.github/workflows/`. The trained model artifact is packaged with the container at build time.
