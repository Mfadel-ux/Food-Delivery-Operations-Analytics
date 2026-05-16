# Food-Delivery-Operations-Analytics
This project analyzes food delivery operations data to uncover patterns affecting delivery performance, customer satisfaction, operational efficiency, and business performance. The project combines exploratory data analysis (EDA), feature engineering, and machine learning to simulate real-world operational analytics in modern food delivery.

The dataset contains operational metrics such as:
1. delivery time,
2. traffic conditions,
3. weather severity,
4. customer ratings,
5. delivery efficiency,
6. discounts,
7. order values,
8. and customer behavior indicators.

The objective of this project is to transform raw delivery data into actionable business insights and predictive operational intelligence.

# Business problem
Food delivery platforms face several operational challenges, including:
1. delayed deliveries,
2. fluctuating customer satisfaction,
3. inefficient delivery operations,
4. and operational bottlenecks during peak hours.

This project aims to answer several key business questions:
1. What factors most strongly affect delivery duration?
2. How do traffic and weather influence delivery performance?
3. Does operational efficiency improve customer satisfaction?
4. Which operational variables are the strongest predictors of delivery time?

# Project workflow
1. Data Cleaning
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Predictive Modeling
5. Model Evaluation
6. Business Insights & Recommendations

# Technologies Used 
| Category             | Tools                           |
| -------------------- | ------------------------------- |
| Programming Language | Python                          |
| Data Manipulation    | Pandas, NumPy                   |
| Data Visualization   | Matplotlib, Seaborn             |
| Machine Learning     | Scikit-learn                    |
| Notebook Environment | Google Colab / Jupyter Notebook |


# Exploratory Data Analysis (EDA)
## Operational Analysis
  1. Traffic impact On delivery time

 <img width="524" height="356" alt="image" src="https://github.com/user-attachments/assets/5a163c0f-82f0-47cb-935e-e1f8aeba6bc0" />


  2. Weather severity analysis

<img width="524" height="350" alt="image" src="https://github.com/user-attachments/assets/54c9dd0e-c185-4bdb-aa55-df4bf81745a1" />


  3. Delivery efficiency analysis

<img width="745" height="350" alt="image" src="https://github.com/user-attachments/assets/625d4e47-ec8c-4a65-ba4e-9cab0fa84ec5" />


## Customer Analaysis
  1. Customer Rating Distribution

<img width="529" height="353" alt="image" src="https://github.com/user-attachments/assets/ee736cde-d548-4715-8060-021e7a36e74f" />


  2. Loyalty Segmentation

<img width="637" height="353" alt="image" src="https://github.com/user-attachments/assets/55ed60fe-c541-47d1-8c23-9a2861fcf4cb" />


# Feature Engineering
Several business-oriented features were created to improve model performance and operational interpretability.

## Engineered Features
1. Peak hour indicator
2. Weekend indicator
3. High traffic flag
4. Severe weather flag
5. Customer value segmentation
6. Traffic-weather interaction feature

## Leakage Detection
During modeling, several target leakage features were identified and removed to ensure realistic model performance:
1. fast_delivery
2. delayed_delivery_flag
3. delivery_speed_km_per_min
4. prep_time_ratio

# Machine Learning Modeling
Objective

Predict delivery duration (delivery_time_minutes) using operational features.

| Model                   | Purpose                   |
| ----------------------- | ------------------------- |
| Linear Regression       | Baseline regression model |
| Random Forest Regressor | Nonlinear ensemble model  |

## Model Perfomance
| Model                   | MAE  | RMSE | R²    |
| ----------------------- | ---- | ---- | ----- |
| Linear Regression       | 0.43 | 1.39 | 0.998 |
| Random Forest Regressor | 4.94 | 6.20 | 0.966 |

**Key finding**
Linear Regression outperformed Random Forest, indicating that the dataset follows a highly linear operational structure.

# Key Business Insights
## Operation Insight
1. Delivery distance is the strongest factor affecting delivery duration.
2. Restaurant preparation time significantly contributes to operational delays.
3. Delivery efficiency score is associated with faster deliveries.

## Customer Insight
1. Longer delivery times reduce customer satisfaction.
2. Loyal customers tend to spend more per transaction.

## Financial Insight
1. Discounts do not always increase final transaction value.
2. Revenue distribution indicates the existence of high-value customer segments.

# Business Recomendation
## Operational recomendation
1. Improve route optimization for long-distance deliveries.
2. Increase delivery partner allocation during peak hours.
3. Improve restaurant preparation efficiency.

## Customer Experience Recomendations
1. Improve ETA Prediction System
2. Reduce operational delay to improve customer satisfaction

**Delay Prediction Model**
Objective

The Delay Prediction Model was developed to identify whether a food delivery order is likely to experience delivery delays based on operational and delivery-related features.

The primary goal of this model is to support proactive operational decision-making by detecting high-risk deliveries before the delivery process is completed.

## Modeling Approach

A binary classification approach was implemented where:

0 = On-Time Delivery
1 = Delayed Delivery

The delay threshold was determined using the median delivery duration to maintain balanced class distribution and improve classification performance.

## Features Used

The model utilized operational and delivery-related variables, including:

1. delivery distance,
2. traffic conditions,
3. weather severity,
4. preparation time,
5. delivery efficiency score,
6. delivery partner experience,
7. and financial delivery indicators.

Target leakage features were identified and removed to ensure realistic model performance and proper generalization capability.

## Models Evaluated

The following classification models were developed and evaluated:

1. Logistic Regression
2. Random Forest Classifier

## ROC Curve

<img width="519" height="347" alt="image" src="https://github.com/user-attachments/assets/e1436456-44d0-4a74-971d-6dcaa8417617" />


## Model Performance
| Model               | Accuracy | Precision | Recall | F1 Score |
| ------------------- | -------- | --------- | ------ | -------- |
| Logistic Regression | 97.1%    | 96.7%     | 97.3%  | 97.0%    |
| Random Forest       | 93.7%    | 92.3%     | 95.0%  | 93.6%    |


## Business Impact

The Delay Prediction Model can be used as an operational early warning system to:

1. detect high-risk deliveries,
2. improve ETA accuracy,
3. optimize delivery resource allocation,
4. reduce operational bottlenecks,
5. and improve customer satisfaction through proactive intervention.

# Project Structure
Food-Delivery-Operations-Analytics/
│
├── data/
├── notebooks/
│   ├── data_cleaning.ipynb
│   ├── exploratory_data_analysis.ipynb
│   ├── feature_engineering.ipynb
│   ├── predictive_modeling.ipynb
│   ├── Delay prediction model.ipynb
│
├── images/
├── dashboard/
├── README.md
└── requirements.txt

# Conclusion
This project demonstrates how data analytics and machine learning can be applied to optimize food delivery operations and improve customer experience.

The project combines:
1. operational analytics,
2. business intelligence,
3. feature engineering,
4. and predictive modeling

into a complete end-to-end analytics workflow suitable for real-world delivery platform scenarios.

**Author**

Muhammad Fadel
Data Analyst / Data Science Enthusiast

Muhammad Fadel
Data Analyst / Data Science Enthusiast
