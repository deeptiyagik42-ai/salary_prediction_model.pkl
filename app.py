
import streamlit as st
import pickle
import numpy as np

# Load the trained ML model
MODEL_FILE = "app.py"

try:
    with open(MODEL_FILE, "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error(f"Model file not found: {MODEL_FILE}")
    st.stop()
except Exception as e:
    st.error(f"Could not load model: {e}")
    st.stop()

# App title
st.title("Salary Prediction App")
st.write("Predict salary using Machine Learning")

# User input
experience = st.number_input(
    "Enter Years of Experience",
    min_value=0.0,
    max_value=60.0,
    value=1.0,
    step=0.5
)

# Predict salary
if st.button("Predict Salary"):
    try:
        input_data = np.array([[experience]])
        prediction = model.predict(input_data)

        st.success(
            f"Predicted Salary: ₹{float(prediction[0]):,.2f}"
        )
    except Exception as e:
        st.error(f"Prediction error: {e}")
