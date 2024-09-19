# Diabetes Prediction Triangle Model Prototype

This project is designed to build a predictive model for diabetes using demographic and lifestyle data. The model predicts whether an individual is at risk of pre-diabetes, type 2 diabetes, or gestational diabetes based on user input. 
The system is built using a deep learning model deployed through a Streamlit application and stores user data and predictions in a MongoDB database.

The application consists of three main components:

1. Frontend (Streamlit Application)
2. Backend (Deep Learning Model)
3. Database (MongoDB)

The frontend of the application is developed using Streamlit, a Python framework that allows for the rapid creation of interactive web applications.

Key Features:
1. User Inputs: The app collects data from users through a series of input fields, including gender, age, weight, height, blood pressure, and glucose levels.
2. BMI Calculation: Automatically calculates BMI based on height and weight inputs.
3. Prediction Button: After inputting all required data, users can click the "Predict" button to receive their diabetes risk prediction.
4. Error Handling: Input validations ensure that users enter correct data formats, enhancing the reliability of predictions.

The backend model is a deep learning neural network built using TensorFlow and Keras. It has been optimized to provide accurate predictions of diabetes outcomes based on input features such as age, gender, BMI, blood pressure, and glucose levels.

MongoDB is used to store the input data and prediction results. This allows for the persistence of user data, which can be valuable for later analysis.

## How It Works:
After a prediction is made, the user data and results are uploaded to MongoDB.
Each record includes demographic and biometric data along with the prediction output.

Connecting the Components
1. Streamlit Frontend collects user inputs and sends them to the backend model for prediction.
2. Backend Model processes the inputs and returns a prediction result.
3. MongoDB Database stores the data for each prediction instance, facilitating continuous improvement and analysis.
