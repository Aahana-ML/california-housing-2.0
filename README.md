# 🌇 Haven — California Housing Price Prediction

**An end-to-end machine learning application that estimates California housing values using XGBoost, a custom preprocessing pipeline, and FastAPI.**

<p align="center">
  <a href="https://california-housing-2-0.onrender.com/">
    <img src="https://img.shields.io/badge/🌇_Live_Demo-Explore_Haven-2E8B57?style=for-the-badge" alt="Live Demo" />
  </a>
  <a href="https://california-housing-2-0.onrender.com/docs">
    <img src="https://img.shields.io/badge/API-Documentation-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="API Documentation" />
  </a>
  <a href="https://github.com/Aahana-ML/california-housing-2.0">
    <img src="https://img.shields.io/badge/GitHub-Source_Code-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Repository" />
  </a>
</p>

---

## 🌇 Overview

**Haven** turns district-level housing and geographic information into an estimated California housing value.

The application combines custom feature engineering, geographic cluster-similarity features, and a trained XGBoost regression model in a single saved preprocessing and prediction pipeline.

Built around experimentation with the California Housing dataset, Haven brings the final model into an interactive web application backed by a FastAPI API.

## ✨ Features

- 🌇 **Housing Value Prediction** — Generate estimated housing values using XGBoost regression.
- ⚙️ **Custom Feature Engineering** — Create features such as `latlong_ratio` and `room_per_person`.
- 📍 **Geographic Intelligence** — Incorporate geographic cluster-similarity features.
- 🔄 **Integrated ML Pipeline** — Keep preprocessing and prediction together in one saved pipeline.
- 🚀 **FastAPI Backend** — Validate inputs and serve predictions through REST endpoints.
- 🎨 **Interactive Frontend** — A dedicated interface built with HTML, CSS, and JavaScript.
- 📦 **JSON Responses** — Return structured prediction results.
- ❤️ **Health Monitoring** — Check application status and the loaded regression model.
- ☁️ **Live Deployment** — Access the application online through Render.

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Language | Python |
| Machine Learning | XGBoost, scikit-learn |
| Data Processing | Pandas, NumPy |
| Backend & API | FastAPI, Uvicorn |
| Frontend | HTML, CSS, JavaScript |
| Model Persistence | Joblib |
| Deployment | Render |
| AI Development Assistance | ChatGPT (GPT) |


## 🏗️ Project Structure

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

## 🧠 How It Works

```text
🌇 User enters housing & geographic details
                    ↓
          🛡️ FastAPI validates input
                    ↓
          ⚙️ Feature engineering
                    ↓
       📍 Geographic transformations
                    ↓
       🔄 Preprocessing pipeline
                    ↓
        🌳 Trained XGBoost model
                    ↓
           💰 Housing estimate
                    ↓
          🎨 Result on the frontend
```

1. The user enters district-level housing and geographic details.
2. FastAPI validates the submitted values.
3. The saved pipeline performs feature engineering, geographic transformations, imputation, and scaling.
4. The trained XGBoost model generates a housing-value estimate.
5. The API returns the prediction and its estimated dollar equivalent.
6. The frontend displays the result to the user.

## 📊 Model Evaluation

The trained XGBoost model achieved the following previously recorded results on the held-out test set:

| Metric | Result |
|---|---:|
| RMSE | ~0.40057 target units |
| Dollar-equivalent RMSE | ~$40,057 |
| R² Score | ~0.8769 |

**Interpretation**

- **RMSE:** The root mean squared prediction error was approximately $40,057 in dollar-equivalent units.
- **R²:** The model explained approximately 87.69% of the variance in the held-out target values.

These metrics describe performance on the evaluation dataset. They do not guarantee the same accuracy for every individual property.

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Aahana-ML/california-housing-2.0.git
cd california-housing-2.0
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

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

### 5. Open Haven

| Resource | URL |
|---|---|
| 🌇 Web Application | http://127.0.0.1:8000 |
| 📘 API Documentation | http://127.0.0.1:8000/docs |
| ❤️ Health Check | http://127.0.0.1:8000/health |

## 🔌 API Reference

### `POST /predict`

Accepts the following input features:

| Feature | Description |
|---|---|
| `MedInc` | Median income |
| `HouseAge` | Median house age |
| `AveRooms` | Average rooms per household |
| `AveBedrms` | Average bedrooms per household |
| `Population` | District population |
| `AveOccup` | Average household occupancy |
| `Latitude` | Geographic latitude |
| `Longitude` | Geographic longitude |

The endpoint returns the predicted value in units of $100,000 and its estimated dollar equivalent.

### `GET /health`

Reports the application's health status and the type of regression model loaded by the API.

Explore the interactive API documentation:

**[Open Haven API Docs →](https://california-housing-2-0.onrender.com/docs)**

## ⚠️ Limitations

- The model uses district-level features from the California Housing dataset rather than a property's full address or a live real-estate listing.
- Predictions are estimates, not formal appraisals or financial advice.
- Property condition, renovations, recent transactions, and other market factors may influence actual values.
- Model performance can vary across properties and geographic areas.

## 🌱 What This Project Demonstrates

Haven brings together several stages of a machine learning workflow:

- Data preprocessing and feature engineering
- Geographic feature construction
- Regression modeling and evaluation
- Saving and loading a fitted ML pipeline
- API development and input validation
- Frontend-backend integration
- Deployment of a machine learning application

## 🌇 Explore Haven

Ready to generate a housing value estimate?

<p align="center">
  <a href="https://california-housing-2-0.onrender.com/">
    <img src="https://img.shields.io/badge/Launch_Haven-🌇_Try_the_Live_Demo-2E8B57?style=for-the-badge" alt="Try Haven Live" />
  </a>
</p>

---

<p align="center">
  Built with Python, machine learning, and a little California sunshine. 🌇
  <br />
  <strong>Haven — A clearer view of California housing values.</strong>
</p>

## 🤝 Development & AI Acknowledgment

Haven was developed with the assistance of **ChatGPT (GPT)** throughout the development process.

ChatGPT helped guide the project across multiple stages, including backend development, frontend implementation, debugging, code refinement, and deployment. The frontend interface was built with ChatGPT's assistance using HTML, CSS, and JavaScript.

The machine learning workflow, model experimentation, feature engineering, evaluation, and integration were developed through an iterative process of learning, experimentation, testing, and AI-assisted problem-solving.

**Haven represents a collaborative development process between human learning and AI assistance**, with ChatGPT serving as a development partner throughout the project.

