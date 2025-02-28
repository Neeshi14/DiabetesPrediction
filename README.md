# DiabetesPrediction
# Diabetes Prediction Web Application

This repository contains a web application built with Flask that predicts whether a person has diabetes based on several input features. The model used for prediction is a Linear Regression model trained on the Pima Indians Diabetes Dataset.

## Overview

This project aims to create a simple web interface for a diabetes prediction model. Users can input relevant health metrics, and the application will return a prediction of whether the individual is likely to have diabetes.

## Dataset

The dataset used for training the model is the Pima Indians Diabetes Dataset, available on Kaggle or UCI Machine Learning Repository.

## Features

The dataset includes the following features:

* **Glucose:** Glucose level.
* **Insulin:** Insulin level.
* **BMI:** Body Mass Index.
* **DiabetesPedigreeFunction:** Diabetes Pedigree Function.
* **Age:** Age.
* **Outcome:** (Target variable) 0 or 1, where 1 indicates diabetes.

## Dependencies

* Python 3.x
* Pandas
* NumPy
* Scikit-learn
* Flask
* Pickle

## Installation

1.  **Download the dataset:**

    Download the `diabetes.csv` dataset and place it in the same directory as the script.

2.  **Train and save the model:**

    Run the provided python code to train the model and save the scaler and model using pickle.

    ```bash
    python your_training_script.py
    ```

3.  **Run the Flask Application:**

    Run the `app.py` script to start the Flask web application.

    ```bash
    python app.py
    ```

    The application will be accessible at `http://127.0.0.1:5000/` in your web browser.

## Usage

1.  Open the web application in your browser.
2.  Fill in the input fields with the required health metrics.
3.  Click the "Predict" button.
4.  The application will display the prediction result.

## Model Details

* **Model:** Linear Regression
* **Preprocessing:** StandardScaler is used to scale the input features.
* **Training:** The model is trained on the Pima Indians Diabetes Dataset.
* **Saving:** The trained model and scaler are saved using pickle for later use in the web application.
* **Evaluation:** The model achieves an accuracy of approximately 76.62% on the test set.

## File Structure

* `diabetes.csv`: The dataset file.
* `app.py`: The Flask web application script.
* `scaler.pkl`: The saved StandardScaler object.
* `model.pkl`: The saved Linear Regression model.
* `templates/index.html`: The HTML template for the web interface.
* `your_training_script.py`: The python code to train and save the model.

## Future Improvements

* Implement a more robust model such as Logistic Regression, Random Forest, or Gradient Boosting.
* Improve the user interface with better styling and error handling.
* Add more features to the prediction model.
* Deploy the application to a cloud platform.
* Add input validation to the web application.
* Add more detailed result output.
* Add data visualization.
