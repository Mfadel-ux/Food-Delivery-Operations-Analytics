import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Food Delivery Delay Prediction",
    page_icon="🚚",
    layout="wide"
)

# =====================================================
# LOAD MODEL
# =====================================================

model = joblib.load(
    'delay_prediction_model.pkl'
)

feature_columns = joblib.load(
    'feature_columns.pkl'
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #0f172a;
    }

    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: white;
        margin-bottom: 0;
    }

    .subtitle {
        font-size: 18px;
        color: #94a3b8;
        margin-top: 0;
        margin-bottom: 30px;
    }

    .card {
        background-color: #1e293b;
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.25);
    }

    .risk-high {
        background-color: #7f1d1d;
        padding: 20px;
        border-radius: 15px;
        color: white;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
    }

    .risk-low {
        background-color: #14532d;
        padding: 20px;
        border-radius: 15px;
        color: white;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
    }

    .section-title {
        font-size: 28px;
        font-weight: 700;
        color: white;
        margin-bottom: 20px;
    }

    .insight-box {
        background-color: #1e293b;
        padding: 18px;
        border-radius: 12px;
        color: white;
        margin-bottom: 10px;
    }

    .recommend-box {
        background-color: #064e3b;
        padding: 18px;
        border-radius: 12px;
        color: white;
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)
# =====================================================
# HEADER
# =====================================================

st.markdown(
    """
    <p class="main-title">
        🚚 Food Delivery Delay Prediction System
    </p>

    <p class="subtitle">
        AI-Powered Operational Delivery Risk Analytics
    </p>
    """,
    unsafe_allow_html=True
)

# =====================================================
# SIDEBAR INPUT
# =====================================================

st.sidebar.header("📥 Delivery Information")

# =====================================================
# HIDDEN DEFAULT VALUES
# =====================================================

city_tier = 2

customer_age = 30
customer_loyalty_score = 5

order_hour = 14
order_day_of_week = 3
order_month = 6

# =====================================================
# OPERATIONAL CONDITIONS
# =====================================================

st.sidebar.header("⚙️ Operational Conditions")

delivery_distance_km = st.sidebar.slider(
    "Delivery Distance (km)",
    1.0,
    30.0,
    10.0
)

preparation_time_minutes = st.sidebar.slider(
    "Preparation Time (minutes)",
    5,
    60,
    20
)

traffic_level_score = st.sidebar.slider(
    "Traffic Level Score",
    1,
    10,
    5,
    help="0 = Smooth Traffic | 10 = Severe Congestion"
)

weather_severity_score = st.sidebar.slider(
    "Weather Severity Score",
    1,
    10,
    3,
    help="0 = Clear Weather | 10 = Severe Weather"
)

restaurant_rating = st.sidebar.slider(
    "Restaurant Rating",
    1.0,
    5.0,
    4.0
)

delivery_partner_rating = st.sidebar.slider(
    "Delivery Partner Rating",
    1.0,
    5.0,
    4.0
)

number_of_items = st.sidebar.slider(
    "Number of Items",
    1,
    10,
    3
)

delivery_partner_experience_years = st.sidebar.slider(
    "Driver Experience (Years)",
    0,
    15,
    5
)

delivery_efficiency_score = st.sidebar.slider(
    "Delivery Efficiency Score",
    1,
    10,
    6
)

# =====================================================
# FINANCIAL FEATURES
# =====================================================

st.sidebar.header("💰 Financial Information")

order_value = st.sidebar.slider(
    "Order Value",
    5.0,
    200.0,
    35.0
)

delivery_fee = st.sidebar.slider(
    "Delivery Fee",
    1.0,
    20.0,
    5.0
)

discount_amount = st.sidebar.slider(
    "Discount Amount",
    0.0,
    50.0,
    5.0
)

tip_amount = st.sidebar.slider(
    "Tip Amount",
    0.0,
    30.0,
    3.0
)

final_amount_paid = order_value + delivery_fee - discount_amount + tip_amount

# =====================================================
# FEATURE ENGINEERING
# =====================================================

is_peak_hour = 1 if (
    (11 <= order_hour <= 14) or
    (18 <= order_hour <= 21)
) else 0

is_weekend = 1 if order_day_of_week in [5,6] else 0

high_traffic = 1 if traffic_level_score >= 7 else 0

severe_weather = 1 if weather_severity_score >= 7 else 0

traffic_weather_interaction = (
    traffic_level_score * weather_severity_score
)

delivery_fee_per_km = (
    delivery_fee / delivery_distance_km
)


prep_time_ratio = (
    preparation_time_minutes /
    (delivery_distance_km + 1)
)

# =====================================================
# CATEGORICAL FEATURE ENGINEERING
# =====================================================

# Traffic Category
if traffic_level_score <= 3:
    traffic_category = 'Low'
elif traffic_level_score <= 7:
    traffic_category = 'Moderate'
else:
    traffic_category = 'High'

# Weather Category
if weather_severity_score <= 3:
    weather_category = 'Clear'
elif weather_severity_score <= 7:
    weather_category = 'Moderate'
else:
    weather_category = 'Severe'

# Loyalty Segment
if customer_loyalty_score <= 3:
    loyalty_segment = 'Low'
elif customer_loyalty_score <= 7:
    loyalty_segment = 'Regular'
else:
    loyalty_segment = 'VIP'

# Customer Value Segment
if order_value <= 25:
    customer_value_segment = 'Low Value'
elif order_value <= 80:
    customer_value_segment = 'Medium Value'
else:
    customer_value_segment = 'Premium'
    
# =====================================================
# BUILD INPUT DATAFRAME
# =====================================================

input_data = pd.DataFrame({
    'city_tier': [city_tier],
    'customer_age': [customer_age],
    'customer_loyalty_score': [customer_loyalty_score],
    'order_hour': [order_hour],
    'order_day_of_week': [order_day_of_week],
    'order_month': [order_month],
    'delivery_distance_km': [delivery_distance_km],
    'preparation_time_minutes': [preparation_time_minutes],
    'traffic_level_score': [traffic_level_score],
    'weather_severity_score': [weather_severity_score],
    'restaurant_rating': [restaurant_rating],
    'delivery_partner_rating': [delivery_partner_rating],
    'order_value': [order_value],
    'delivery_fee': [delivery_fee],
    'discount_amount': [discount_amount],
    'tip_amount': [tip_amount],
    'final_amount_paid': [final_amount_paid],
    'number_of_items': [number_of_items],
    'delivery_partner_experience_years': [delivery_partner_experience_years],
    'delivery_efficiency_score': [delivery_efficiency_score],
    'is_peak_hour': [is_peak_hour],
    'is_weekend': [is_weekend],
    'high_traffic': [high_traffic],
    'severe_weather': [severe_weather],
    'traffic_weather_interaction': [traffic_weather_interaction],
    'delivery_fee_per_km': [delivery_fee_per_km],
    'prep_time_ratio': [prep_time_ratio],
    'traffic_category': [traffic_category],
    'weather_category': [weather_category],
    'loyalty_segment': [loyalty_segment],
    'customer_value_segment': [customer_value_segment]
})

# =====================================================
# FEATURE ALIGNMENT
# =====================================================
# =====================================================
# ONE HOT ENCODING
# =====================================================

categorical_cols = [
    'traffic_category',
    'weather_category',
    'loyalty_segment',
    'customer_value_segment'
]

input_data = pd.get_dummies(
    input_data,
    columns=categorical_cols,
    drop_first=True
)

# =====================================================
# FEATURE ALIGNMENT
# =====================================================

for col in feature_columns:

    if col not in input_data.columns:
        input_data[col] = 0

# Reorder columns
input_data = input_data[
    feature_columns
]

st.write(feature_columns)

st.write(input_data.T)
# =====================================================
# PREDICTION
# =====================================================

prediction = model.predict(input_data)[0]

probability = model.predict_proba(
    input_data
)[0][1]

# =====================================================
# MAIN RESULT SECTION
# =====================================================

st.divider()

col1, col2 = st.columns([1,1])

with col1:

    st.markdown(
        '<p class="section-title">🚨 Delay Prediction</p>',
        unsafe_allow_html=True
    )

    if prediction == 1:

        st.markdown(
            f"""
            <div class="risk-high">
                HIGH DELAY RISK<br>
                {probability:.1%}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="risk-low">
                LOW DELAY RISK<br>
                {(1-probability):.1%}
            </div>
            """,
            unsafe_allow_html=True
        )

with col2:

    st.markdown(
        '<p class="section-title">📊 Delay Probability</p>',
        unsafe_allow_html=True
    )

    fig = go.Figure(go.Indicator(

        mode = "gauge+number",

        value = probability * 100,

        number = {
            'suffix': "%",
            'font': {'size': 42}
        },

        gauge = {

            'axis': {
                'range': [0, 100],
                'tickwidth': 1
            },

            'bar': {
                'color': "#ef4444"
            },

            'steps': [
                {'range': [0, 30], 'color': "#22c55e"},
                {'range': [30, 70], 'color': "#f59e0b"},
                {'range': [70, 100], 'color': "#ef4444"}
            ]
        }
    ))

    fig.update_layout(
        paper_bgcolor="#0f172a",
        font={'color': "white"},
        height=320,
        margin=dict(l=20, r=20, t=40, b=20)
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
# =====================================================
# OPERATIONAL INSIGHTS
# =====================================================

st.divider()

st.subheader("📈 Operational Insights")

insights = []

if delivery_distance_km > 15:
    insights.append(
        "Long delivery distance significantly increases delay probability."
    )

if traffic_level_score >= 7:
    insights.append(
        "Heavy traffic congestion detected."
    )

if preparation_time_minutes > 30:
    insights.append(
        "Restaurant preparation time may create operational bottlenecks."
    )

if delivery_efficiency_score < 5:
    insights.append(
        "Low delivery efficiency may affect delivery performance."
    )

if len(insights) == 0:
    insights.append(
        "Operational conditions appear stable."
    )

for insight in insights:

    st.markdown(
        f"""
        <div class="insight-box">
            📌 {insight}
        </div>
        """,
        unsafe_allow_html=True
    )

# =====================================================
# RECOMMENDATION ENGINE
# =====================================================

st.divider()

st.subheader("✅ Operational Recommendations")

recommendations = []

if traffic_level_score >= 7:
    recommendations.append(
        "Assign experienced drivers during high traffic periods."
    )

if delivery_distance_km > 15:
    recommendations.append(
        "Adjust ETA dynamically for long-distance deliveries."
    )

if preparation_time_minutes > 30:
    recommendations.append(
        "Prioritize restaurant preparation workflow."
    )

if weather_severity_score >= 7:
    recommendations.append(
        "Notify customers proactively about weather-related delays."
    )

if len(recommendations) == 0:
    recommendations.append(
        "Current delivery operation appears efficient."
    )

for rec in recommendations:

    st.markdown(
        f"""
        <div class="recommend-box">
            ✅ {rec}
        </div>
        """,
        unsafe_allow_html=True
    )

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
    "Developed by Muhammad Fadel | Food Delivery Operations Analytics"
)
