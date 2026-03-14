import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model

# Load model
model = load_model("electricity_lstm_model.keras")

# Load scaler
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Set page configuration
st.set_page_config(page_title="Electricity Consumption Forecasting", page_icon="⚡", layout="centered")

# Title
st.title("⚡ Electricity Consumption Forecasting (LSTM)")
st.write("Enter the last 60 electricity consumption values to predict the next value.")

# Input area
user_input = st.text_area(
    "Enter 60 values separated by commas",
    placeholder="4.216, 5.360, 5.374, 5.388, ..."
)

# Prediction
if st.button("Predict Next Consumption"):
    if user_input.strip() == "":
        st.warning("Please enter 60 values.")
    else:
        try:
            values = [float(x.strip()) for x in user_input.split(",")]

            if len(values) != 60:
                st.error("You must enter exactly 60 values.")
            else:
                input_data = np.array(values).reshape(-1, 1)
                scaled_input = scaler.transform(input_data)
                X_input = scaled_input.reshape(1, 60, 1)

                prediction = model.predict(X_input, verbose=0)
                predicted_value = scaler.inverse_transform(prediction)[0][0]

                st.success(f"Predicted Next Consumption Value: {predicted_value:.3f}")

        except Exception as e:
            st.error(f"Invalid input. Please enter only numeric values. Error: {e}")