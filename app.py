import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

st.title("🍽 Restaurant Rating Predictor")

st.write("Enter restaurant details:")

# Create input fields dynamically
input_data = []

for col in columns:
    value = st.number_input(f"Enter {col}", value=0.0)
    input_data.append(value)

if st.button("Predict Rating"):
    input_array = np.array([input_data])
    prediction = model.predict(input_array)
    st.success(f"Predicted Rating: {prediction[0]:.2f}")
