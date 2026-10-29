# Haven — California Housing Price Prediction

An end-to-end machine learning application that estimates California housing values using **XGBoost**, a custom preprocessing pipeline, and a FastAPI backend with a dedicated web interface.

## Overview

Haven turns district-level housing and geographic information into an estimated property value. The application combines feature engineering, geographic cluster-similarity features, and a trained XGBoost regression model in a single saved pipeline.

This project builds on experimentation with the California Housing dataset and presents the final model through a web application.

## Features

- XGBoost regression for housing-value prediction
- Custom feature engineering, including `latlong_ratio` and `room_per_person`
- Geographic cluster-similarity features
- Integrated preprocessing and prediction pipeline
- FastAPI backend with input validation
- HTML, CSS, and JavaScript frontend
- JSON prediction responses
- Model health endpoint

## Tech Stack

- **Language:** Python
- **Machine learning:** XGBoost, scikit-learn
- **Data processing:** Pandas, NumPy
- **Backend:** FastAPI, Uvicorn
- **Frontend:** HTML, CSS, JavaScript
- **Model persistence:** Joblib

## Project Structure

```text
california-housing-2.0/
├── app/
│   ├── main.py
│   └── frontend/
│       ├── index.html
│       ├── style.css
│       └── app.js
├── models/
│   └── xgboost_california_housing_pipeline.joblib
├── src/
│   └── transformers.py
├── notebooks/
├── requirements.txt
├── README.md
└── .gitignore
```

## How It Works

1. The user enters district-level housing and geographic details.
2. FastAPI validates the submitted values.
3. The saved pipeline performs feature engineering, geographic transformations, imputation, and scaling.
4. XGBoost generates a housing-value estimate.
5. The API returns the prediction and its estimated dollar equivalent.

## Run Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd california-housing-2.0
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000` to use Haven.

API documentation is available at `http://127.0.0.1:8000/docs`, and the health endpoint is at `http://127.0.0.1:8000/health`.

## API

### `POST /predict`

Accepts the following input features:

- `MedInc`
- `HouseAge`
- `AveRooms`
- `AveBedrms`
- `Population`
- `AveOccup`
- `Latitude`
- `Longitude`

Returns a predicted housing value in units of $100,000 and an estimated dollar value.

### `GET /health`

Reports API health and the loaded regression model type.

## Model Evaluation

The trained XGBoost model achieved the following previously recorded held-out test results:

- **RMSE:** approximately `0.40057` target units, equivalent to approximately `$40,057`
- **R²:** approximately `0.8769`

These are evaluation results, not a guarantee of accuracy for every individual property. Predictions are estimates based on the dataset and its target definition.

## Limitations

- The model uses California Housing dataset features rather than a property's full address, condition, or current market listing.
- Predictions represent model estimates, not formal appraisals or financial advice.
- Actual property values can differ from predictions.

## License

No license has been selected yet. Add a license if you decide to distribute the project under specific reuse terms.