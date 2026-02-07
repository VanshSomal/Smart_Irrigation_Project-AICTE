import streamlit as st
import numpy as np
import joblib  # or pickle if needed
import pandas as pd

# ---- Load the trained model ----
model = joblib.load("Farm_Irrigation_System.pkl")

# ---- UI Theme and Header ----
st.set_page_config(page_title="KrishiMind", page_icon="💧", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #E0F7FA; /* Page background */
    }
    [data-testid="stSidebar"] {
        background-color: #B2EBF2; /* Sidebar background */
    }
    h1, h2, h3, h4, h5, h6, p, div, label {
        color: #004D40; /* Text color */
    }
    div.stButton > button {
        background-color: #26C6DA; /* Button color */
        color: white;
        border-radius: 10px;
        font-weight: bold;
    }
    div.stButton > button:hover {
        background-color: #00ACC1;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- Title Section ----
st.markdown(
    """
    <h1 style='
        font-size: 5em;
        color: #004D40;
        text-align: center;
    '>
    🌾 KrishiMind
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown("## 💧 **AI-powered irrigation management for efficient water use.**", unsafe_allow_html=True)
st.image("farm_image.jpg", caption="Efficient Watering for Every Crop", use_container_width=True)

st.subheader("Enter scaled sensor values (0 to 1) to predict sprinkler status")

# ---- Sidebar ----
with st.sidebar:
    st.title("💡 Project Info")
    st.write("**KrishiMind**")
    st.write("**Internship:** AICTE Virtual Internship Cycle 2")
    st.write("**Developer:** Vansh Somal")
    st.write("**Model:** Farm_Irrigation_System.pkl")

# ---- Weather Condition ----
st.markdown("### 🌦️ Weather Condition")
weather = st.selectbox("Select Current Weather", ["Sunny ☀️", "Cloudy 🌥️", "Rainy 🌧️"])
st.write(f"Selected weather: {weather}")

if weather == "Rainy 🌧️":
    st.warning("🌧️ Rain detected! Sprinklers may stay OFF to save water.")

# ---- Collect Sensor Inputs ----
sensor_values = []
for i in range(20):
    val = st.slider(f"Sensor {i}", min_value=0.0, max_value=1.0, value=0.5, step=0.01, key=f"sensor_{i}")
    sensor_values.append(val)

# ---- Predict Button ----
if st.button("🔍 Predict Sprinklers", key="predict_btn"):
    input_array = np.array(sensor_values).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    st.markdown("### Prediction:")
    cols = st.columns(4)  # 4 columns for better layout

    for i, status in enumerate(prediction):
        with cols[i % 4]:
            st.metric(label=f"Sprinkler {i} (Parcel_{i})", value="🟢 ON" if status == 1 else "🔴 OFF")

    # ---- Additional Insights ----
    active = np.sum(prediction)
    total = len(prediction)
    water_used = active * 10  # Example: each sprinkler uses 10 liters

    st.write("---")
    st.success(f"✅ {active}/{total} sprinklers are active ({(active/total)*100:.1f}%)")
    st.info(f"💧 Estimated total water usage: {water_used} liters")
    st.progress(int((active / total) * 100))

# ---- Sensor Input Visualization ----
st.markdown("### Sensor Input Visualization")
st.bar_chart(np.array(sensor_values))

avg_val = np.mean(sensor_values)
if avg_val < 0.3:
    st.warning("🌱 Soil too dry — increase irrigation frequency.")
elif avg_val > 0.7:
    st.info("🌤️ Soil moisture is high — irrigation not needed today.")
else:
    st.success("✅ Soil moisture optimal.")

# ---- Upload CSV Option ----
st.markdown("### 📈 Upload Past Irrigation Data (optional)")
uploaded = st.file_uploader("Upload CSV file", type="csv")

if uploaded:
    df = pd.read_csv(uploaded)
    st.line_chart(df)

# ---- Irrigation Tips ----
st.markdown("### 🌱 Irrigation Tips")
st.info("💡 Water plants early in the morning to reduce evaporation.")
st.info("🌾 Avoid overwatering — let the soil partially dry between irrigations.")
st.info("🌤️ Consider weather before irrigation to save water.")

# ---- Footer ----
st.markdown("---")
st.markdown("<h5 style='text-align: center;'>Made with ❤️ by Vansh Somal</h5>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>AICTE Virtual Internship Cycle 2</p>", unsafe_allow_html=True)
