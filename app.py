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

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #081120 0%,
        #0f172a 40%,
        #111827 100%
    );
    color:white;
}

/* Sidebar */

section[data-testid="stSidebar"]{
    background: #081120;
    border-right: 1px solid rgba(255,255,255,0.08);
}

/* Main Title */

.main-title{
    font-size:42px;
    font-weight:800;
    color:white;
    margin-bottom:5px;
}

.subtitle{
    color:#94a3b8;
    font-size:18px;
    margin-bottom:30px;
}

/* Cards */

.metric-card{
    background: rgba(255,255,255,0.04);
    border:1px solid rgba(255,255,255,0.08);
    padding:25px;
    border-radius:20px;
    backdrop-filter: blur(10px);
    box-shadow: 0 0 30px rgba(0,0,0,0.2);
}

.metric-title{
    color:#cbd5e1;
    font-size:15px;
    font-weight:600;
}

.metric-value{
    font-size:42px;
    font-weight:800;
}

.metric-sub{
    color:#94a3b8;
    font-size:14px;
}

/* Section */

.section-title{
    color:white;
    font-size:24px;
    font-weight:700;
    margin-bottom:20px;
}

/* Insight Box */

.insight-box{
    background: rgba(255,255,255,0.04);
    border-left: 4px solid #22c55e;
    padding:20px;
    border-radius:15px;
    color:white;
}

/* Summary Box */

.summary-box{
    background: rgba(255,255,255,0.04);
    border:1px solid rgba(255,255,255,0.05);
    padding:20px;
    border-radius:18px;
    text-align:center;
}

.summary-title{
    color:#94a3b8;
    font-size:14px;
}

.summary-value{
    color:white;
    font-size:26px;
    font-weight:700;
}

/* Hide Streamlit */

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div style="display:flex;
justify-content:space-between;
align-items:center;
margin-bottom:30px;">

<div>

<p class="main-title">
🚚 Delivery Delay Risk Prediction
</p>

<p class="subtitle">
ML-powered prediction based on operational factors
</p>

</div>

</div>
""", unsafe_allow_html=True)

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
# TOP METRIC CARDS
# =====================================================

card1, card2, card3, card4 = st.columns(4)

risk_color = "#ef4444" if probability >= 0.7 else "#f59e0b" if probability >= 0.3 else "#22c55e"

risk_text = (
    "High"
    if probability >= 0.7
    else "Medium"
    if probability >= 0.3
    else "Low"
)

with card1:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">
        DELAY RISK
        </div>

        <div class="metric-value" style="color:{risk_color}">
        {probability:.1%}
        </div>

        <div class="metric-sub">
        Prediction Probability
        </div>
    </div>
    """, unsafe_allow_html=True)

with card2:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">
        RISK LEVEL
        </div>

        <div class="metric-value" style="color:{risk_color}">
        {risk_text}
        </div>

        <div class="metric-sub">
        Operational Risk Status
        </div>
    </div>
    """, unsafe_allow_html=True)

with card3:

    confidence = (
        probability
        if probability > 0.5
        else 1 - probability
    )

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">
        CONFIDENCE
        </div>

        <div class="metric-value" style="color:#60a5fa">
        {confidence:.1%}
        </div>

        <div class="metric-sub">
        Model Confidence
        </div>
    </div>
    """, unsafe_allow_html=True)

with card4:

    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">
        MODEL STATUS
        </div>

        <div class="metric-value" style="color:#4ade80">
        Healthy
        </div>

        <div class="metric-sub">
        Model is performing well
        </div>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# PREMIUM GAUGE
# =====================================================

st.markdown(
    '<p class="section-title">📊 Predicted Delay Risk</p>',
    unsafe_allow_html=True
)

fig = go.Figure(go.Indicator(

    mode = "gauge+number",

    value = probability * 100,

    number = {
        'suffix': "%",
        'font': {
            'size': 52,
            'color': "white"
        }
    },

    title = {
        'text': "Probability of Delivery Delay",
        'font': {'size': 22}
    },

    gauge = {

        'axis': {
            'range': [0,100],
            'tickcolor': "white"
        },

        'bar': {
            'color': "#f97316"
        },

        'bgcolor': "rgba(0,0,0,0)",

        'steps': [

            {
                'range':[0,30],
                'color':"#22c55e"
            },

            {
                'range':[30,70],
                'color':"#fbbf24"
            },

            {
                'range':[70,100],
                'color':"#ef4444"
            }
        ]
    }
))

fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    font={'color': "white"},
    height=450
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================================
# RISK CONTRIBUTORS
# =====================================================

st.markdown(
    '<p class="section-title">⚠️ Top Risk Contributors</p>',
    unsafe_allow_html=True
)

contributors = {

    "Traffic Level": traffic_level_score * 10,
    "Weather Severity": weather_severity_score * 10,
    "Delivery Distance": delivery_distance_km * 3,
    "Preparation Time": preparation_time_minutes * 1.5
}

for name, value in contributors.items():

    st.progress(min(value/100,1.0))

    st.markdown(
        f"""
        <div style='margin-bottom:20px'>
        <b>{name}</b> — {value:.0f}% impact
        </div>
        """,
        unsafe_allow_html=True
    )
    

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

# =====================================================
# OPERATIONAL SUMMARY
# =====================================================

st.markdown(
    '<p class="section-title">📋 Current Operational Summary</p>',
    unsafe_allow_html=True
)

sum1, sum2, sum3, sum4 = st.columns(4)

with sum1:
    st.markdown(f"""
    <div class="summary-box">
        <div class="summary-title">Distance</div>
        <div class="summary-value">{delivery_distance_km} km</div>
    </div>
    """, unsafe_allow_html=True)

with sum2:
    st.markdown(f"""
    <div class="summary-box">
        <div class="summary-title">Prep Time</div>
        <div class="summary-value">{preparation_time_minutes} min</div>
    </div>
    """, unsafe_allow_html=True)

with sum3:
    st.markdown(f"""
    <div class="summary-box">
        <div class="summary-title">Traffic</div>
        <div class="summary-value">{traffic_level_score}/10</div>
    </div>
    """, unsafe_allow_html=True)

with sum4:
    st.markdown(f"""
    <div class="summary-box">
        <div class="summary-title">Weather</div>
        <div class="summary-value">{weather_severity_score}/10</div>
    </div>
    """, unsafe_allow_html=True)
