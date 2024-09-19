import streamlit as st
import numpy as np
from pymongo import MongoClient
from keras.models import load_model

# Load your model
model = load_model('DL_optimized_model.h5')

# MongoDB connection
mongo_uri = "mongodb+srv://vvvb5:admin@cluster0.yhab1.mongodb.net/"
client = MongoClient(mongo_uri)
db = client['diabetes_data']
collection = db['collection1']

# User Inputs

# 1. Gender - radio button (0 for Male, 1 for Female)
gender = st.radio("Select your gender", options=["Male", "Female"])
gender_value = 0 if gender == "Male" else 1

# 2. Age - restrict input to numbers only
age = st.text_input("Enter your age", "")
if not age.isdigit():
    st.error("Please enter a valid number for age.")
else:
    age = int(age)

# 3. Weight (lbs) - allows decimals
weight = st.number_input("Enter your weight (lbs)", value=0.0)

# 4. Height (inches) - allows only numbers
height = st.number_input("Enter your height (inches)", value=0.0)

# 5. BMI Calculation based on the given formula
if height > 0:  # Avoid division by zero
    bmi = (weight / (height ** 2)) * 703
    st.write(f"Your calculated BMI is: {bmi:.2f}")
else:
    bmi = 0.0
    st.write("Please enter a valid height.")

# 6. Blood Pressure (BP)
bp = st.number_input("Enter your Blood Pressure (mmHg)", value=0)

# 7. Glucose level
glucose = st.number_input("Enter your Glucose level", value=0)

# If all inputs are valid, predict using the model
if st.button("Predict"):
    if isinstance(age, int) and weight > 0 and height > 0 and bp > 0 and glucose > 0:
        # Prepare input features (reshape to 1 sample, 5 features: gender, age, BMI, BP, Glucose)
        input_features = np.array([[gender_value, age, bmi, bp, glucose]])

        # Make the prediction
        prediction = model.predict(input_features)
        st.write("Prediction:", prediction)

        # Upload the prediction to MongoDB
        collection.insert_one({
            "gender": gender_value,
            "age": age,
            "weight": weight,
            "height": height,
            "bmi": bmi,
            "blood_pressure": bp,
            "glucose": glucose,
            "prediction": prediction.tolist()
        })

        st.success("Prediction and data saved to the database!")
    else:
        st.error("Please ensure all inputs are filled correctly.")