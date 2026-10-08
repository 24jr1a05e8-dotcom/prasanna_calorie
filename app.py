import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Prasanna Chowdary - Calorie Calculator",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- CUSTOM CSS --------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(16, 185, 129, 0.15), transparent 25%),
        radial-gradient(circle at 90% 15%, rgba(245, 158, 11, 0.16), transparent 25%),
        linear-gradient(135deg, #ecfdf5 0%, #ffffff 50%, #fffbeb 100%);
}

.main-title {
    text-align: center;
    font-size: 44px;
    font-weight: 800;
    margin-top: 10px;
    margin-bottom: 4px;
    background: linear-gradient(90deg, #059669, #f59e0b, #16a34a);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: titleFloat 2.5s ease-in-out infinite alternate;
}

.subtitle {
    text-align: center;
    color: #666;
    font-size: 17px;
    margin-bottom: 25px;
}

@keyframes titleFloat {
    from { transform: translateY(0); }
    to { transform: translateY(-5px); }
}

.hero {
    background: linear-gradient(135deg, #059669, #16a34a);
    color: white;
    padding: 24px;
    border-radius: 22px;
    text-align: center;
    box-shadow: 0 12px 30px rgba(5, 150, 105, 0.28);
    animation: heroFloat 3s ease-in-out infinite;
    margin-bottom: 25px;
}

.hero h2 {
    margin: 0;
    font-size: 28px;
}

.hero p {
    margin: 8px 0 0;
    opacity: 0.95;
}

@keyframes heroFloat {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-5px); }
}

.info-card {
    background: rgba(255,255,255,0.88);
    border: 1px solid rgba(5, 150, 105, 0.15);
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.07);
    margin-bottom: 18px;
}

.result-card {
    background: white;
    border-radius: 22px;
    padding: 28px;
    box-shadow: 0 12px 35px rgba(0,0,0,0.10);
    border-top: 7px solid #059669;
}

.calorie-total {
    background: linear-gradient(90deg, #059669, #16a34a);
    color: white;
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    font-size: 30px;
    font-weight: 800;
    margin-top: 18px;
    box-shadow: 0 8px 22px rgba(5,150,105,0.25);
}

.interpretation {
    background: #ecfdf5;
    border-left: 6px solid #059669;
    border-radius: 12px;
    padding: 16px;
    margin-top: 18px;
}

.tip {
    background: #fffbeb;
    border-left: 6px solid #f59e0b;
    border-radius: 12px;
    padding: 16px;
    margin-top: 14px;
}

.footer {
    text-align: center;
    color: #777;
    padding: 20px 0 5px;
    font-size: 14px;
}

div.stButton > button {
    border-radius: 12px;
    border: none;
    font-weight: 700;
    transition: 0.25s;
}

div.stButton > button:hover {
    transform: scale(1.03);
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ecfdf5, #fffbeb);
}

@media (max-width: 768px) {
    .main-title { font-size: 31px; }
    .subtitle { font-size: 14px; }
}
</style>
""", unsafe_allow_html=True)

# -------------------- HEADER --------------------
st.markdown(
    '<div class="main-title">Prasanna Chowdary - Calorie Calculator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Estimate your daily calorie requirement in a few simple steps 🥗</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="hero">
    <h2>🥗 Welcome to Prasanna's Calorie Calculator! 💪</h2>
    <p>Enter your personal and activity details to estimate your daily calorie requirement.</p>
</div>
""", unsafe_allow_html=True)

# -------------------- SIDEBAR --------------------
with st.sidebar:
    st.header("⚙️ Calculator Settings")

    unit_system = st.radio(
        "📏 Unit System",
        ["Metric (kg / cm)", "Imperial (lb / ft-in)"]
    )

    st.divider()

    st.info(
        "💡 This calculator provides an estimated calorie requirement "
        "using the entered personal and activity details."
    )

# -------------------- INPUTS --------------------
st.markdown("### 👤 Personal Details")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "🎂 Age (years)",
        min_value=1,
        max_value=120,
        value=21,
        step=1
    )

with col2:
    gender = st.selectbox(
        "⚧️ Gender",
        ["Male", "Female"]
    )

with col3:
    activity = st.selectbox(
        "🏃 Activity Level",
        [
            "Sedentary - little or no exercise",
            "Lightly Active - exercise 1-3 days/week",
            "Moderately Active - exercise 3-5 days/week",
            "Very Active - exercise 6-7 days/week",
            "Extra Active - intense exercise/physical job"
        ]
    )

st.markdown("### ⚖️ Body Measurements")

if unit_system == "Metric (kg / cm)":
    col4, col5 = st.columns(2)

    with col4:
        weight = st.number_input(
            "⚖️ Weight (kg)",
            min_value=1.0,
            max_value=500.0,
            value=60.0,
            step=0.5
        )

    with col5:
        height = st.number_input(
            "📏 Height (cm)",
            min_value=50.0,
            max_value=250.0,
            value=165.0,
            step=0.5
        )

else:
    col4, col5, col6 = st.columns(3)

    with col4:
        weight_lb = st.number_input(
            "⚖️ Weight (lb)",
            min_value=2.0,
            max_value=1000.0,
            value=132.0,
            step=1.0
        )

    with col5:
        height_ft = st.number_input(
            "📏 Height (feet)",
            min_value=1,
            max_value=8,
            value=5,
            step=1
        )

    with col6:
        height_in = st.number_input(
            "📏 Height (inches)",
            min_value=0,
            max_value=11,
            value=5,
            step=1
        )

# -------------------- CALCULATION --------------------
if unit_system == "Metric (kg / cm)":
    weight_kg = weight
    height_cm = height
else:
    weight_kg = weight_lb * 0.453592
    total_inches = (height_ft * 12) + height_in
    height_cm = total_inches * 2.54

# Mifflin-St Jeor BMR formula
if gender == "Male":
    bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
else:
    bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161

activity_factors = {
    "Sedentary - little or no exercise": 1.2,
    "Lightly Active - exercise 1-3 days/week": 1.375,
    "Moderately Active - exercise 3-5 days/week": 1.55,
    "Very Active - exercise 6-7 days/week": 1.725,
    "Extra Active - intense exercise/physical job": 1.9
}

activity_factor = activity_factors[activity]
daily_calories = bmr * activity_factor

# -------------------- CALORIE RESULT --------------------
st.markdown("### 🔥 Your Estimated Calorie Requirement")

c1, c2, c3 = st.columns(3)

c1.metric("🔥 BMR", f"{bmr:,.0f} kcal/day")
c2.metric("🏃 Activity Factor", f"{activity_factor:.3f}")
c3.metric("🥗 Daily Calories", f"{daily_calories:,.0f} kcal/day")

st.markdown("### 📋 Result")

if st.button("🔥 Calculate My Calories", use_container_width=True):
    now = datetime.now().strftime("%d-%m-%Y %I:%M %p")

    if daily_calories < 1600:
        interpretation = (
            "Your estimated daily calorie requirement is relatively low. "
            "Focus on balanced, nutrient-rich meals and regular activity."
        )
    elif daily_calories < 2200:
        interpretation = (
            "Your estimated daily calorie requirement is in a moderate range. "
            "A balanced diet with regular physical activity can support your routine."
        )
    elif daily_calories < 2800:
        interpretation = (
            "Your estimated daily calorie requirement is moderately high. "
            "Choose nutritious meals and match food intake with your activity level."
        )
    else:
        interpretation = (
            "Your estimated daily calorie requirement is high. "
            "Higher activity levels can require more energy from balanced meals."
        )

    st.markdown(f"""
    <div class="result-card">
        <h2 style="text-align:center;">🥗 PRASANNA'S CALORIE CALCULATOR</h2>
        <p style="text-align:center;color:#777;">Estimated Daily Calorie Requirement</p>
        <hr>

        <p><b>Age:</b> {age} years</p>
        <p><b>Gender:</b> {gender}</p>
        <p><b>Weight:</b> {weight_kg:.1f} kg</p>
        <p><b>Height:</b> {height_cm:.1f} cm</p>
        <p><b>Activity:</b> {activity}</p>
        <p><b>Calculated At:</b> {now}</p>

        <div class="calorie-total">
            ESTIMATED DAILY CALORIES<br>
            {daily_calories:,.0f} kcal/day
        </div>

        <div class="interpretation">
            <b>📊 Simple Interpretation</b><br><br>
            {interpretation}
        </div>

        <div class="tip">
            <b>💡 Healthy Reminder</b><br><br>
            Calorie requirements are estimates and can vary from person to person.
            For personalized nutrition or medical advice, consult a qualified
            healthcare or nutrition professional.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.success("✅ Calorie requirement calculated successfully!")
    st.balloons()

    result_text = f"""PRASANNA'S CALORIE CALCULATOR
Estimated Daily Calorie Requirement

Age: {age} years
Gender: {gender}
Weight: {weight_kg:.1f} kg
Height: {height_cm:.1f} cm
Activity: {activity}

BMR: {bmr:.0f} kcal/day
Activity Factor: {activity_factor:.3f}
Estimated Daily Calories: {daily_calories:.0f} kcal/day

Interpretation:
{interpretation}

Note:
Calorie requirements are estimates and can vary from person to person.
For personalized nutrition or medical advice, consult a qualified
healthcare or nutrition professional.
"""

    st.download_button(
        "📥 Download Calorie Result",
        data=result_text,
        file_name="prasanna_chowdary_calorie_result.txt",
        mime="text/plain",
        use_container_width=True
    )

st.markdown("""
<div class="footer">
    🚀 Built with Python + Streamlit | Prasanna Chowdary | Calorie Calculator Project
</div>
""", unsafe_allow_html=True)
