# Swiggy Delivery Time Prediction

## Project Overview

Swiggy Delivery Time Prediction is a Machine Learning project that predicts the estimated food delivery time based on order, customer, and delivery-related features.

Accurate delivery time prediction helps improve customer satisfaction, operational efficiency, and logistics planning for food delivery platforms.

---

## Problem Statement

Food delivery platforms often face challenges in providing accurate delivery time estimates due to various factors such as traffic, distance, weather conditions, and delivery partner availability.

Incorrect predictions can lead to:

* Poor customer experience
* Increased order cancellations
* Reduced customer trust
* Operational inefficiencies

This project aims to build a Machine Learning model that predicts delivery time as accurately as possible.

---

## Dataset

The project uses Swiggy delivery data containing information related to:

* Customer demographics
* Restaurant details
* Delivery partner information
* Order information
* Location-related features
* Delivery time

Dataset File:

swiggy_demographic.csv

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* XGBoost
* Optuna
* Jupyter Notebook

---

## Project Workflow

### 1. Data Collection

* Load Swiggy delivery dataset.
* Inspect dataset structure and features.

### 2. Data Cleaning

* Handle missing values.
* Remove inconsistencies.
* Fix data quality issues.

### 3. Exploratory Data Analysis (EDA)

* Analyze feature distributions.
* Study relationships between variables.
* Identify patterns affecting delivery time.

### 4. Data Preprocessing

* Label Encoding
* Feature Transformation
* Train-Test Split
* Feature Selection

### 5. Model Building

Multiple Machine Learning algorithms were trained and evaluated:

#### Linear Regression

Used as a baseline model.

#### K-Nearest Neighbors Regressor (KNN)

Predicts delivery time based on neighboring observations.

#### Decision Tree Regressor

Captures non-linear relationships between features.

#### Random Forest Regressor

Uses multiple decision trees to improve prediction accuracy.

#### XGBoost Regressor

Gradient boosting algorithm used for high-performance predictions.

---

## Hyperparameter Tuning

Optuna was used to optimize XGBoost hyperparameters.

Optimized parameters include:

* Number of estimators
* Maximum depth
* Learning rate
* Subsample ratio
* Column sample ratio

This improved overall model performance and generalization.

---

## Model Evaluation Metrics

The models were evaluated using:

### R² Score

Measures how well the model explains variance in delivery time.

### RMSE (Root Mean Squared Error)

Measures average prediction error.

### MAE (Mean Absolute Error)

Measures average absolute difference between actual and predicted delivery times.

---

## Best Model

After comparing multiple algorithms, the optimized XGBoost Regressor achieved the best performance and was selected as the final model.

---

## Applications

* Food Delivery Platforms
* Logistics Optimization
* Delivery Route Planning
* Customer Experience Enhancement
* Operational Decision Making

---

## Future Improvements

* Incorporate real-time traffic data.
* Integrate weather information.
* Deploy model using Flask or Streamlit.
* Build a live delivery time prediction dashboard.
* Use deep learning models for further improvement.

---

## Project Outcomes

* Built an end-to-end Machine Learning pipeline.
* Compared multiple regression algorithms.
* Performed hyperparameter optimization using Optuna.
* Improved prediction accuracy using XGBoost.
* Developed a scalable delivery time prediction solution.
