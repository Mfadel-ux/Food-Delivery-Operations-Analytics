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


🚚 Delivery Delay Prediction Model
📌 Project Objective

This machine learning model predicts whether a food delivery order is likely to experience a delivery delay based on operational conditions such as:

1. Delivery distance
2. Traffic congestion
3. Weather severity
4. Restaurant preparation time
5. Driver quality
6. Peak operational hours

The objective is to help food delivery platforms proactively identify operational risks and improve customer experience through data-driven decisions.

🎯 Business Problem

Food delivery platforms frequently face operational inefficiencies that lead to:

1. Late deliveries
2. Poor customer satisfaction
3. Increased refunds
4. Higher operational costs

This project aims to build an operational risk prediction system that can classify whether an order is at risk of delay before delivery completion.

🧠 Machine Learning Approach
Target Variable

The target variable is generated using the 75th percentile of delivery time:
delay_threshold = df_delay[
    'delivery_time_minutes'
].quantile(0.75)

df_delay['is_delayed'] = (
    df_delay['delivery_time_minutes']
    > delay_threshold
).astype(int)

Why Quantile 75%?

Orders above the 75th percentile are considered operationally abnormal because they take significantly longer than typical deliveries.

This approach:

1. Creates a dynamic threshold based on data distribution
2. Avoids arbitrary manual labeling
3. Helps focus on operational outliers

⚙️ Selected Features

The model only uses operational features that are realistically available before delivery completion.
| Feature                           | Description                     |
| --------------------------------- | ------------------------------- |
| delivery_distance_km              | Delivery travel distance        |
| preparation_time_minutes          | Restaurant preparation duration |
| traffic_level_score               | Traffic congestion level        |
| weather_severity_score            | Weather condition severity      |
| restaurant_rating                 | Restaurant service quality      |
| delivery_partner_rating           | Driver performance rating       |
| number_of_items                   | Order complexity                |
| delivery_partner_experience_years | Driver experience               |
| is_peak_hour                      | Peak-hour indicator             |
| is_weekend                        | Weekend indicator               |
| high_traffic                      | High traffic binary flag        |
| severe_weather                    | Severe weather binary flag      |
| prep_time_ratio                   | Prep time relative to distance  |
| traffic_weather_interaction       | Combined operational pressure   |


🚫 Leakage Prevention

Several features were intentionally excluded to avoid data leakage.
| Feature                 | Reason                                            |
| ----------------------- | ------------------------------------------------- |
| delivery_time_minutes   | Directly defines the target                       |
| delayed_delivery_flag   | Already contains delay outcome                    |
| refund_flag             | Known after delivery completion                   |
| customer_rating         | Available after delivery                          |
| final_amount_paid       | Post-transaction information                      |
| estimated_delivery_time | Potentially correlated with actual target outcome |


Classification Report
| Class    | Precision | Recall | F1-score |
| -------- | --------- | ------ | -------- |
| No Delay | 0.98      | 0.92   | 0.95     |
| Delay    | 0.78      | 0.94   | 0.85     |


🔍 Feature Importance Insights

Top operational contributors to delivery delays:

Delivery Distance
Traffic Level
Severe Weather
Preparation Time
Peak Hour Operations

Negative coefficients do not indicate "bad features."
They simply mean that higher values reduce the probability of delivery delay.

Example:

Higher driver ratings reduce delay risk
Better operational quality improves delivery reliability


📈 Operational Insights

The model reveals that delivery delays are primarily driven by operational bottlenecks rather than customer behavior.

Main operational risk factors:

Long travel distances
Heavy traffic congestion
Severe weather conditions
Slow restaurant preparation

This makes the model highly useful for:

ETA optimization
Dynamic driver allocation
Operational monitoring
Real-time risk prediction systems


🖥️ Interactive Dashboard

The project includes a Streamlit dashboard for real-time operational simulation and delay prediction.

1. Dashboard Features
2. Real-time delay probability prediction
3. Operational risk monitoring
4. Interactive scenario simulation
5. Risk contributor visualization
6. Operational recommendation engine

UI Link :
https://food-delivery-operations-analytics-dja9y6evnvzsxyjircgnzd.streamlit.app/

<img width="1919" height="866" alt="image" src="https://github.com/user-attachments/assets/9a34e763-d231-47e1-a9a0-f0f6b4f78ccc" />








**Author**

Muhammad Fadel
Data Analyst / Data Science Enthusiast

Muhammad Fadel
Data Analyst / Data Science Enthusiast
