"""
Customer Churn Predictor — Streamlit App

Lets a user enter a customer's profile and get a churn prediction with
a probability score. The prediction logic is currently MOCKED — it will
be replaced with the real trained model/scaler/encoder once Phase 9
(Model Saving) is complete.

Run with: streamlit run streamlit_app.py
"""

from dataclasses import dataclass
from typing import Any

import streamlit as st

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📉",
    layout="centered",
)

# Dropdown options taken directly from the training dataset's unique values,
# so the form never lets a user submit a category the model has never seen.
GENDER_OPTIONS = ["Female", "Male"]
YES_NO_OPTIONS = ["Yes", "No"]
MULTI_LINES_OPTIONS = ["No", "Yes", "No phone service"]
INTERNET_SERVICE_OPTIONS = ["DSL", "Fiber optic", "No"]
INTERNET_DEPENDENT_OPTIONS = ["No", "Yes", "No internet service"]
CONTRACT_OPTIONS = ["Month-to-month", "One year", "Two year"]
PAYMENT_METHOD_OPTIONS = [
    "Electronic check",
    "Mailed check",
    "Bank transfer (automatic)",
    "Credit card (automatic)",
]


@dataclass
class CustomerInput:
    """Holds one customer's raw form input, matching the dataset schema."""

    gender: str
    senior_citizen: bool
    partner: str
    dependents: str
    tenure: int
    phone_service: str
    multiple_lines: str
    internet_service: str
    online_security: str
    online_backup: str
    device_protection: str
    tech_support: str
    streaming_tv: str
    streaming_movies: str
    contract: str
    paperless_billing: str
    payment_method: str
    monthly_charges: float
    total_charges: float


# ---------------------------------------------------------------------------
# Model loading (placeholder until Phase 9 artifacts exist)
# ---------------------------------------------------------------------------


@st.cache_resource
def load_artifacts() -> dict[str, Any]:
    """
    Load the trained model, scaler, and encoder.

    TODO (Phase 9 handoff): replace this mock with:
        import joblib
        return {
            "model": joblib.load("models/model.pkl"),
            "scaler": joblib.load("models/scaler.pkl"),
            "encoder": joblib.load("models/encoder.pkl"),
        }
    """
    return {"model": None, "scaler": None, "encoder": None}


# ---------------------------------------------------------------------------
# Preprocessing (placeholder — must mirror the training pipeline exactly)
# ---------------------------------------------------------------------------


def preprocess_input(customer: CustomerInput, artifacts: dict[tr, Any]) -> Any:
    """
    Transform raw form input into the numeric format the model expects.

    TODO (Phase 9 handoff): this MUST use the same encoder/scaler objects
    fit during training (Phase 3). Re-fitting new ones here would silently
    produce wrong predictions, since category-to-number mappings could
    differ from what the model learned.
    """
    return customer  # mock: pass-through, unused by the mock predictor


# ---------------------------------------------------------------------------
# Prediction (MOCK — replace with artifacts["model"].predict_proba(...))
# ---------------------------------------------------------------------------


def predict_churn(customer: CustomerInput, artifacts: dict[str, Any]) -> tuple[str, float]:
    """
    Return (predicted_label, churn_probability).

    MOCK IMPLEMENTATION: a simple weighted heuristic standing in for a real
    model, so the UI can be built and tested before Phase 6-9 finish.
    Weights are illustrative only and carry no statistical meaning.
    """
    score = 0.3  # baseline risk

    if customer.contract == "Month-to-month":
        score += 0.25
    elif customer.contract == "One year":
        score += 0.05

    if customer.tenure < 12:
        score += 0.15
    elif customer.tenure > 48:
        score -= 0.15

    if customer.internet_service == "Fiber optic":
        score += 0.10

    if customer.tech_support == "No":
        score += 0.05

    if customer.monthly_charges > 80:
        score += 0.05

    if customer.paperless_billing == "Yes":
        score += 0.03

    probability = min(max(score, 0.02), 0.98)  # clamp to a believable range
    label = "Churn" if probability >= 0.5 else "No Churn"
    return label, probability


# ---------------------------------------------------------------------------
# UI: input form
# ---------------------------------------------------------------------------


def render_input_form() -> CustomerInput | None:
    """Render the grouped input form. Returns CustomerInput on submit, else None."""
    st.subheader("Customer Details")

    with st.form("churn_form"):
        st.markdown("**Demographics**")
        col1, col2, col3 = st.columns(3)
        gender = col1.selectbox("Gender", GENDER_OPTIONS)
        senior_citizen = col2.checkbox("Senior Citizen")
        partner = col3.selectbox("Has Partner", YES_NO_OPTIONS)
        dependents = st.selectbox("Has Dependents", YES_NO_OPTIONS)

        st.markdown("**Account & Contract**")
        col1, col2 = st.columns(2)
        tenure = col1.number_input("Tenure (months)", min_value=0, max_value=72, value=12)
        contract = col2.selectbox("Contract Type", CONTRACT_OPTIONS)
        col1, col2 = st.columns(2)
        paperless_billing = col1.selectbox("Paperless Billing", YES_NO_OPTIONS)
        payment_method = col2.selectbox("Payment Method", PAYMENT_METHOD_OPTIONS)

        st.markdown("**Services**")
        col1, col2 = st.columns(2)
        phone_service = col1.selectbox("Phone Service", YES_NO_OPTIONS)
        multiple_lines = col2.selectbox("Multiple Lines", MULTI_LINES_OPTIONS)
        internet_service = st.selectbox("Internet Service", INTERNET_SERVICE_OPTIONS)

        col1, col2 = st.columns(2)
        online_security = col1.selectbox("Online Security", INTERNET_DEPENDENT_OPTIONS)
        online_backup = col2.selectbox("Online Backup", INTERNET_DEPENDENT_OPTIONS)
        col1, col2 = st.columns(2)
        device_protection = col1.selectbox("Device Protection", INTERNET_DEPENDENT_OPTIONS)
        tech_support = col2.selectbox("Tech Support", INTERNET_DEPENDENT_OPTIONS)
        col1, col2 = st.columns(2)
        streaming_tv = col1.selectbox("Streaming TV", INTERNET_DEPENDENT_OPTIONS)
        streaming_movies = col2.selectbox("Streaming Movies", INTERNET_DEPENDENT_OPTIONS)

        st.markdown("**Billing**")
        col1, col2 = st.columns(2)
        monthly_charges = col1.number_input(
            "Monthly Charges ($)", min_value=0.0, max_value=200.0, value=70.0, step=0.5
        )
        total_charges = col2.number_input(
            "Total Charges ($)", min_value=0.0, max_value=10000.0, value=840.0, step=1.0
        )

        submitted = st.form_submit_button("Predict Churn", use_container_width=True)

    if not submitted:
        return None

    return CustomerInput(
        gender=gender,
        senior_citizen=senior_citizen,
        partner=partner,
        dependents=dependents,
        tenure=tenure,
        phone_service=phone_service,
        multiple_lines=multiple_lines,
        internet_service=internet_service,
        online_security=online_security,
        online_backup=online_backup,
        device_protection=device_protection,
        tech_support=tech_support,
        streaming_tv=streaming_tv,
        streaming_movies=streaming_movies,
        contract=contract,
        paperless_billing=paperless_billing,
        payment_method=payment_method,
        monthly_charges=monthly_charges,
        total_charges=total_charges,
    )


# ---------------------------------------------------------------------------
# UI: results
# ---------------------------------------------------------------------------


def render_results(label: str, probability: float) -> None:
    """Display the prediction, probability, and confidence."""
    st.subheader("Prediction Result")

    if label == "Churn":
        st.error(f"⚠️ Prediction: **{label}**")
    else:
        st.success(f"✅ Prediction: **{label}**")

    col1, col2 = st.columns(2)
    col1.metric("Churn Probability", f"{probability:.1%}")
    confidence = probability if label == "Churn" else 1 - probability
    col2.metric("Model Confidence", f"{confidence:.1%}")

    st.progress(probability)

    st.caption(
        "⚠️ This prediction uses a placeholder mock model, not a trained "
        "ML model. Real predictions will be enabled once the trained "
        "model artifacts are integrated (Phase 9)."
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    st.title("📉 Customer Churn Predictor")
    st.write(
        "Enter a customer's profile below to estimate their likelihood "
        "of churning (canceling their service)."
    )

    artifacts = load_artifacts()
    customer = render_input_form()

    if customer is not None:
        processed = preprocess_input(customer, artifacts)
        label, probability = predict_churn(processed, artifacts)
        render_results(label, probability)


if __name__ == "__main__":
    main()
