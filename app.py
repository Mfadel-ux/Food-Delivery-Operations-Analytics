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
BACKGROUND
===================================================== */

.stApp{
    background: linear-gradient(
        135deg,
        #081120 0%,
        #0f172a 40%,
        #111827 100%
    );
    color:white;
}

/* =====================================================
SIDEBAR
===================================================== */

section[data-testid="stSidebar"]{
    background:#081120;
    border-right:1px solid rgba(255,255,255,0.08);
}

/* =====================================================
HIDE STREAMLIT
===================================================== */

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

/* =====================================================
HEADER
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

    background: linear-gradient(
        145deg,
        rgba(15,23,42,0.95),
        rgba(30,41,59,0.85)
    );

    border:1px solid rgba(255,255,255,0.08);

    padding:28px;

    border-radius:22px;

    backdrop-filter: blur(14px);

    -webkit-backdrop-filter: blur(14px);

    box-shadow:
        0 8px 32px rgba(0,0,0,0.35),
        inset 0 1px 1px rgba(255,255,255,0.04);

    min-height:180px;

    transition:0.3s ease;
}

.metric-card:hover{

    transform:translateY(-4px);

    border:1px solid rgba(96,165,250,0.35);
}

.metric-title{

    color:#94a3b8;

    font-size:15px;

    font-weight:600;

    letter-spacing:0.5px;

    margin-bottom:18px;
}

.metric-value{

    font-size:44px;

    font-weight:800;

    line-height:1;

    margin-bottom:16px;
}

.metric-sub{

    color:#64748b;

    font-size:14px;
}

/* =====================================================
INSIGHT BOX
===================================================== */

.insight-box{

    background:rgba(255,255,255,0.04);

    border-left:4px solid #22c55e;

    padding:20px;

    border-radius:15px;

    color:white;

    margin-bottom:15px;
}

/* =====================================================
RECOMMENDATION BOX
===================================================== */

.recommend-box{

    background:rgba(255,255,255,0.04);

    border-left:4px solid #3b82f6;

    padding:20px;

    border-radius:15px;

    color:white;

    margin-bottom:15px;
}

/* =====================================================
SUMMARY BOX
===================================================== */

.summary-box{

    background: linear-gradient(
        145deg,
        rgba(15,23,42,0.95),
        rgba(30,41,59,0.85)
    );

    border:1px solid rgba(255,255,255,0.08);

    padding:22px;

    border-radius:20px;

    backdrop-filter: blur(12px);

    -webkit-backdrop-filter: blur(12px);

    box-shadow:
        0 8px 24px rgba(0,0,0,0.25);

    text-align:center;

    min-height:130px;

    transition:0.3s ease;
}

.summary-box:hover{

    transform:translateY(-4px);

    border:1px solid rgba(96,165,250,0.35);
}

.summary-title{

    color:#94a3b8;

    font-size:15px;

    font-weight:600;

    margin-bottom:14px;
}

.summary-value{

    color:white;

    font-size:32px;

    font-weight:800;
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

/* =====================================================
REMOVE EXTRA MARGIN
===================================================== */

div[data-testid="stMarkdownContainer"] p{
    margin-bottom:0;
}

</style>
""", unsafe_allow_html=True)# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.markdown("## ⚙️ Operational Conditions")

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
    (18 <= 14 <= 21)
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
# BUILD INPUT DATAFRAME
# =====================================================

input_data = pd.DataFrame({

    'delivery_distance_km': [delivery_distance_km],
    'preparation_time_minutes': [preparation_time_minutes],
    'traffic_level_score': [traffic_level_score],
    'weather_severity_score': [weather_severity_score],
    'restaurant_rating': [restaurant_rating],
    'delivery_partner_rating': [delivery_partner_rating],
    'number_of_items': [number_of_items],
    'delivery_partner_experience_years': [delivery_partner_experience_years],
    'is_peak_hour': [is_peak_hour],
    'is_weekend': [is_weekend],
    'high_traffic': [high_traffic],
    'severe_weather': [severe_weather],
    'prep_time_ratio': [prep_time_ratio],
    'traffic_weather_interaction': [traffic_weather_interaction]
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

probability = model.predict_proba(input_data)[0][1]

# =====================================================
# RISK COLOR
# =====================================================

risk_color = (
    "#ef4444"
    if probability >= 0.7
    else "#f59e0b"
    if probability >= 0.3
    else "#22c55e"
)

risk_text = (
    "High"
    if probability >= 0.7
    else "Medium"
    if probability >= 0.3
    else "Low"
)

# =====================================================
# TOP METRIC CARDS
# =====================================================

card1, card2, card3, card4 = st.columns(4)

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

with card3:

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
        Model performing normally
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

st.markdown('<div class="metric-card">', unsafe_allow_html=True)

fig = go.Figure(go.Indicator(

    mode="gauge+number",

    value=probability * 100,

    number={
        'suffix': "%",
        'font': {
            'size': 52,
            'color': "white"
        }
    },

    title={
        'text': "Probability of Delivery Delay",
        'font': {'size': 24}
    },

    gauge={

        'axis': {
            'range': [0, 100],
            'tickcolor': "white"
        },

        'bar': {
            'color': "#f97316"
        },

        'bgcolor': "rgba(0,0,0,0)",

        'steps': [

            {
                'range': [0,30],
                'color': "#22c55e"
            },

            {
                'range': [30,70],
                'color': "#f59e0b"
            },

            {
                'range': [70,100],
                'color': "#ef4444"
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

st.markdown('</div>', unsafe_allow_html=True)

# =====================================================
# TOP CONTRIBUTORS
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

    st.markdown(f"""
    <div style="
        display:flex;
        justify-content:space-between;
        color:white;
        margin-bottom:5px;
        font-weight:600;
    ">
        <span>{name}</span>
        <span>{value:.0f}%</span>
    </div>
    """, unsafe_allow_html=True)

    st.progress(min(value/100,1.0))

# =====================================================
# INSIGHTS
# =====================================================

st.markdown(
    '<p class="section-title">📈 Operational Insights</p>',
    unsafe_allow_html=True
)

if probability >= 0.7:

    insight = """
    High delivery risk detected.
    Traffic congestion and preparation time
    are the main contributors.
    """

elif probability >= 0.3:

    insight = """
    Moderate operational risk detected.
    Delivery conditions should be monitored.
    """

else:

    insight = """
    Operational conditions appear stable.
    """

st.markdown(f"""
<div class="insight-box">
📌 {insight}
</div>
""", unsafe_allow_html=True)

# =====================================================
# SUMMARY
# =====================================================

st.markdown(
    '''
    <p class="section-title">
    📋 Current Operational Summary
    </p>
    ''',
    unsafe_allow_html=True
)

# =====================================================
# SUMMARY CSS
# =====================================================

st.markdown("""
<style>

.summary-box{

    background: linear-gradient(
        145deg,
        rgba(15,23,42,0.95),
        rgba(30,41,59,0.85)
    );

    border:1px solid rgba(255,255,255,0.08);

    padding:22px;

    border-radius:20px;

    backdrop-filter: blur(12px);

    -webkit-backdrop-filter: blur(12px);

    box-shadow:
        0 8px 24px rgba(0,0,0,0.25);

    text-align:center;

    transition:0.3s ease;

    min-height:130px;
}

.summary-box:hover{
    transform: translateY(-4px);
    border:1px solid rgba(96,165,250,0.4);
}

.summary-title{

    color:#94a3b8;

    font-size:15px;

    font-weight:600;

    margin-bottom:14px;

    letter-spacing:0.5px;
}

.summary-value{

    color:white;

    font-size:32px;

    font-weight:800;

    line-height:1.2;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# SUMMARY CARDS
# =====================================================

sum1, sum2, sum3, sum4 = st.columns(4)

with sum1:

    st.markdown(f"""
    <div class="summary-box">

        <div class="summary-title">
        🚚 Distance
        </div>

        <div class="summary-value">
        {delivery_distance_km:.1f} km
        </div>

    </div>
    """, unsafe_allow_html=True)

with sum2:

    st.markdown(f"""
    <div class="summary-box">

        <div class="summary-title">
        ⏱️ Prep Time
        </div>

        <div class="summary-value">
        {preparation_time_minutes} min
        </div>

    </div>
    """, unsafe_allow_html=True)

with sum3:

    st.markdown(f"""
    <div class="summary-box">

        <div class="summary-title">
        🚦 Traffic
        </div>

        <div class="summary-value">
        {traffic_level_score}/10
        </div>

    </div>
    """, unsafe_allow_html=True)

with sum4:

    st.markdown(f"""
    <div class="summary-box">

        <div class="summary-title">
        🌧️ Weather
        </div>

        <div class="summary-value">
        {weather_severity_score}/10
        </div>

    </div>
    """, unsafe_allow_html=True)
# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
    "Developed by Muhammad Fadel | Food Delivery Operations Analytics"
)
