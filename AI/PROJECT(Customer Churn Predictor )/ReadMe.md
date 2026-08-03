# 📉 Customer Churn Predictor

A machine learning project that predicts whether a telecom customer is likely to churn (cancel their service), built with Python, scikit-learn, and Streamlit.

> **Status:** 🚧 In progress. EDA and model training are underway. The Streamlit app UI is complete but currently uses a **mocked prediction function** until the trained model is integrated.

---

## Overview

Customer churn — when a customer stops using a company's service — is expensive to fix after the fact but often predictable in advance. This project uses the IBM Telco Customer Churn dataset to build a classification model that flags at-risk customers, paired with an interactive Streamlit app for exploring predictions.

## Features

- Exploratory Data Analysis (EDA) covering distributions, correlations, and churn-driving factors
- Data preprocessing pipeline (encoding, scaling, train/test split)
- Multiple trained classification models (Logistic Regression, Decision Tree, Random Forest) compared on standard metrics
- Feature importance analysis to explain *why* the model predicts churn
- Interactive Streamlit web app for real-time predictions with probability scores

## Dataset

**IBM Telco Customer Churn Dataset** — 7,043 customer records, 21 features including:

- **Demographics:** gender, senior citizen status, partner/dependents
- **Account info:** tenure, contract type, payment method, billing preferences
- **Services:** phone, internet, online security, tech support, streaming, etc.
- **Billing:** monthly charges, total charges
- **Target:** `Churn` (Yes/No)

## Folder Structure

```
Customer-Churn-Predictor/
│
├── app/
│   └── streamlit_app.py       # Streamlit UI (mocked predictions for now)
│
├── data/
│   └── dataset.csv            # IBM Telco Customer Churn dataset
│
├── notebooks/
│   └── churn_analysis.ipynb   # EDA, preprocessing, model training
│
├── models/                    # (to be added) saved model.pkl, scaler.pkl, encoder.pkl
│
├── requirements.txt
└── README.md
```

## Technologies Used

- **Python 3**
- **pandas / numpy** — data manipulation
- **matplotlib / seaborn** — visualization
- **scikit-learn** — model training and evaluation
- **joblib** — model persistence
- **streamlit** — web app deployment

## Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd Customer-Churn-Predictor
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the notebook for EDA and model training:
   ```bash
   jupyter notebook notebooks/churn_analysis.ipynb
   ```

4. Launch the Streamlit app:
   ```bash
   cd app
   streamlit run streamlit_app.py
   ```

## Model Performance

*Not yet available — model training and evaluation are in progress (Phases 6–7). This section will be updated with accuracy, precision, recall, F1, and AUC scores once complete.*

## Screenshots

*Placeholder — to be added once the app UI is finalized.*

`![App Screenshot](assets/screenshot-home.png)`

## Future Improvements

- Integrate trained model into the Streamlit app (currently using mocked predictions)
- Add SHAP-based explainability for individual predictions
- Experiment with Gradient Boosting / XGBoost for improved performance
- Handle class imbalance with SMOTE and compare against `class_weight='balanced'`
- Deploy app publicly (e.g., Streamlit Community Cloud)

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
