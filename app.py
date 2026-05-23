import streamlit as st
import pandas as pd
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

model = joblib.load("delay_prediction_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

/* =====================================================
GLOBAL
===================================================== */

.stApp{
    background: linear-gradient(
        135deg,
        #081120 0%,
        #0f172a 45%,
        #111827 100%
    );
    color:white;
}

/* Hide Streamlit */

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Sidebar */

section[data-testid="stSidebar"]{
    background:#081120;
    border-right:1px solid rgba(255,255,255,0.08);
}

/* =====================================================
TITLE
===================================================== */

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

/* =====================================================
SECTION TITLE
===================================================== */

.section-title{
    color:white;
    font-size:24px;
    font-weight:700;
    margin-bottom:20px;
}

/* =====================================================
METRIC CARD
===================================================== */

.metric-card{
    background: rgba(17,24,39,0.9);
    border:1px solid rgba(255,255,255,0.08);
    border-radius:20px;
    padding:28px;
    text-align:center;
    min-height:180px;

    box-shadow:
        0 4px 24px rgba(0,0,0,0.35);

    backdrop-filter: blur(12px);
}

.metric-title{
    color:#94a3b8;
    font-size:14px;
    font-weight:600;
    margin-bottom:15px;
}

.metric-value{
    font-size:42px;
    font-weight:800;
    margin-bottom:10px;
}

.metric-sub{
    color:#64748b;
    font-size:13px;
}

/* =====================================================
SUMMARY BOX
===================================================== */

.summary-box{
    background: rgba(17,24,39,0.9);
    border:1px solid rgba(255,255,255,0.08);
    border-radius:20px;
    padding:24px;
    text-align:center;
}

.summary-title{
    color:#94a3b8;
    font-size:14px;
    margin-bottom:10px;
}

.summary-value{
    color:white;
    font-size:28px;
    font-weight:700;
}

/* =====================================================
INSIGHT BOX
===================================================== */

.insight-box{
    background: rgba(255,255,255,0.04);
    border-left:4px solid #22c55e;
    padding:18px;
    border-radius:15px;
    color:white;
    margin-bottom:15px;
}

/* =====================================================
RECOMMEND BOX
===================================================== */

.recommend-box{
    background: rgba(255,255,255,0.04);
    border-left:4px solid #3b82f6;
    padding:18px;
    border-radius:15px;
    color:white;
    margin-bottom:15px;
}

/* =====================================================
PROGRESS BAR
===================================================== */

.stProgress > div > div > div > div{
    background: linear-gradient(
        90deg,
        #f59e0b,
        #ef4444
    );
}

/* =====================================================
SLIDER
===================================================== */

.stSlider > div[data-baseweb="slider"] > div{
    color:#f97316;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div style="margin-bottom:30px;">

<p class="main-title">
🚚 Delivery Delay Risk Prediction
</p>

<p class="subtitle">
ML-powered prediction based on operational factors
</p>

</div>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR
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
    5
)

weather_severity_score = st.sidebar.slider(
    "Weather Severity Score",
    1,
    10,
    3
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
    "Driver Experience",
    0,
    15,
    5
)

# =====================================================
# FEATURE ENGINEERING
# =====================================================

is_peak_hour = 1 if (
    (11 <= 14 <= 14) or
    (18 <= 20 <= 21)
) else 0

is_weekend = 0

high_traffic = 1 if traffic_level_score >= 7 else 0

severe_weather = 1 if weather_severity_score >= 7 else 0

prep_time_ratio = (
    preparation_time_minutes /
    (delivery_distance_km + 1)
)

traffic_weather_interaction = (
    traffic_level_score *
    weather_severity_score
)

# =====================================================
# INPUT DATAFRAME
# =====================================================

input_data = pd.DataFrame({

    "delivery_distance_km": [delivery_distance_km],
    "preparation_time_minutes": [preparation_time_minutes],
    "traffic_level_score": [traffic_level_score],
    "weather_severity_score": [weather_severity_score],
    "restaurant_rating": [restaurant_rating],
    "delivery_partner_rating": [delivery_partner_rating],
    "number_of_items": [number_of_items],
    "delivery_partner_experience_years": [
        delivery_partner_experience_years
    ],
    "is_peak_hour": [is_peak_hour],
    "is_weekend": [is_weekend],
    "high_traffic": [high_traffic],
    "severe_weather": [severe_weather],
    "prep_time_ratio": [prep_time_ratio],
    "traffic_weather_interaction": [
        traffic_weather_interaction
    ]
})

# =====================================================
# FEATURE ALIGNMENT
# =====================================================

for col in feature_columns:

    if col not in input_data.columns:
        input_data[col] = 0

input_data = input_data[feature_columns]

# =====================================================
# PREDICTION
# =====================================================

prediction = model.predict(input_data)[0]

probability = model.predict_proba(
    input_data
)[0][1]

# =====================================================
# RISK INFO
# =====================================================

risk_color = (
    "#ef4444"
    if probability >= 0.7
    else "#f59e0b"
    if probability >= 0.3
    else "#22c55e"
)

risk_text = (
    "HIGH"
    if probability >= 0.7
    else "MEDIUM"
    if probability >= 0.3
    else "LOW"
)

confidence = (
    probability
    if probability > 0.5
    else 1 - probability
)

# =====================================================
# PREDICTION OVERVIEW
# =====================================================

st.markdown("## 📊 Prediction Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Delay Risk",
        value=f"{probability:.1%}"
    )

with col2:
    st.metric(
        label="Confidence",
        value=f"{confidence:.1%}"
    )

with col3:
    st.metric(
        label="Risk Level",
        value=risk_text
    )

with col4:
    st.metric(
        label="Model Status",
        value="ACTIVE"
    )
    
# =====================================================
# GAUGE
# =====================================================

st.markdown(
    '<p class="section-title">📊 Predicted Delay Risk</p>',
    unsafe_allow_html=True
)

fig = go.Figure(go.Indicator(

    mode="gauge+number",

    value=probability * 100,

    number={
        "suffix":"%",
        "font":{
            "size":48,
            "color":"white"
        }
    },

    gauge={

        "axis":{
            "range":[0,100]
        },

        "bar":{
            "color":"#f97316"
        },

        "steps":[

            {
                "range":[0,30],
                "color":"#22c55e"
            },

            {
                "range":[30,70],
                "color":"#f59e0b"
            },

            {
                "range":[70,100],
                "color":"#ef4444"
            }
        ]
    }
))

fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    font={"color":"white"},
    height=400
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================================
# SUMMARY
# =====================================================

st.markdown("## 📋 Operational Summary")

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.metric(
        "Distance",
        f"{delivery_distance_km} km"
    )

with s2:
    st.metric(
        "Prep Time",
        f"{preparation_time_minutes} min"
    )

with s3:
    st.metric(
        "Traffic",
        f"{traffic_level_score}/10"
    )

with s4:
    st.metric(
        "Weather",
        f"{weather_severity_score}/10"
    )
    
# =====================================================
# INSIGHTS
# =====================================================

st.markdown(
    '<p class="section-title">📈 Operational Insights</p>',
    unsafe_allow_html=True
)

insights = []

if delivery_distance_km > 15:
    insights.append(
        "Long delivery distance significantly increases delay risk."
    )

if traffic_level_score >= 7:
    insights.append(
        "Heavy traffic congestion detected."
    )

if preparation_time_minutes > 30:
    insights.append(
        "Restaurant preparation bottleneck detected."
    )

if len(insights) == 0:
    insights.append(
        "Operational conditions appear stable."
    )

for insight in insights:

    st.markdown(f"""
    <div class="insight-box">
    📌 {insight}
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# RECOMMENDATIONS
# =====================================================

st.markdown(
    '<p class="section-title">✅ Recommendations</p>',
    unsafe_allow_html=True
)

recommendations = []

if traffic_level_score >= 7:
    recommendations.append(
        "Assign experienced drivers during heavy traffic."
    )

if delivery_distance_km > 15:
    recommendations.append(
        "Adjust ETA dynamically for long-distance delivery."
    )

if preparation_time_minutes > 30:
    recommendations.append(
        "Improve restaurant preparation workflow."
    )

if weather_severity_score >= 7:
    recommendations.append(
        "Notify customers proactively about weather delays."
    )

if len(recommendations) == 0:
    recommendations.append(
        "Current delivery operation appears efficient."
    )

for rec in recommendations:

    st.markdown(f"""
    <div class="recommend-box">
    ✅ {rec}
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
    "Developed by Muhammad Fadel | Food Delivery Operations Analytics"
)
