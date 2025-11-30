import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("fraud_detection_pipeline.pkl")

# App title
st.title("💳 Fraud Detection Prediction App")

st.markdown("""
### 🔍 Enter the transaction details below:
Fill in the details and click **Predict** to check if the transaction might be fraudulent.
""")

st.divider()

# --- Input fields ---
step = st.number_input("🕒 Step (Transaction Time Step)", min_value=1, value=1)

transaction_type = st.selectbox(
    "Transaction Type",
    ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"]
)

amount = st.number_input("💰 Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("🏦 Old Balance (Sender)", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("💸 New Balance (Sender)", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("🏦 Old Balance (Receiver)", min_value=0.0, value=5000.0)
newbalanceDest = st.number_input("💰 New Balance (Receiver)", min_value=0.0, value=6000.0)

# --- Prediction ---
if st.button("🔮 Predict"):
    # ✅ Create input DataFrame with correct column names
    input_data = pd.DataFrame([{
        "step": step,  # Make sure the name matches exactly
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    st.write("🔍 Debug: Input columns →", list(input_data.columns))  # temporary check

    try:
        prediction = model.predict(input_data)[0]
        st.subheader(f"🧩 Prediction Result: {(int(prediction))}")

        if prediction == 1:
            st.error("🚨 This transaction can be **fraudulent**!")
        else:
            st.success("✅ This transaction looks like it is **not a fraud**.")
    except Exception as e:
        st.error(f"❌ Error: {e}")































    
