
from pathlib import Path
import sys

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

# Locate project directories
PROJECT_ROOT = Path(__file__).resolve().parent.parent
FRONTEND_DIR = PROJECT_ROOT / "frontend"

# Make project root importable
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Import custom transformer classes before loading the pipeline
from src.transformers import (
    CombinedAttributesAdder,
    ClusterSimilarity,
)

# Load the trained XGBoost pipeline
MODEL_PATH = (
    PROJECT_ROOT
    / "models"
    / "xgboost_california_housing_pipeline.joblib"
)

if not MODEL_PATH.is_file():
    raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

model = joblib.load(MODEL_PATH)

app = FastAPI(
    title="California Housing Price Prediction API",
    description="Predict California housing values using a trained XGBoost pipeline.",
    version="2.0.0",
)

# Serve frontend files
app.mount(
    "/static",
    StaticFiles(directory=FRONTEND_DIR),
    name="static",
)


class HousingInput(BaseModel):
    MedInc: float = Field(
        gt=0,
        description="Median income in tens of thousands of dollars",
    )
    HouseAge: float = Field(ge=0, le=100)
    AveRooms: float = Field(gt=0)
    AveBedrms: float = Field(gt=0)
    Population: float = Field(gt=0)
    AveOccup: float = Field(gt=0)
    Latitude: float = Field(ge=-90, le=90)
    Longitude: float = Field(ge=-180, le=180)


@app.get("/")
def home():
    return FileResponse(FRONTEND_DIR / "index.html")


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "model_type": type(model.named_steps["regression"]).__name__,
    }


@app.post("/predict")
def predict(data: HousingInput):
    input_data = pd.DataFrame(
        [data.model_dump()],
        columns=[
            "MedInc",
            "HouseAge",
            "AveRooms",
            "AveBedrms",
            "Population",
            "AveOccup",
            "Latitude",
            "Longitude",
        ],
    )

    prediction = float(model.predict(input_data)[0])

    # California Housing target is measured in units of $100,000
    return {
        "predicted_value_100k": round(prediction, 4),
        "estimated_price_usd": round(prediction * 100_000, 2),
    }
