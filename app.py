# ✅ Final Torch fix for Windows + Streamlit
import sys
sys.modules["torch.classes"] = None

# ✅ Multiprocessing fix
import multiprocessing
multiprocessing.set_start_method("spawn", force=True)

# ✅ Compatibility fixes
import os
os.environ["STREAMLIT_WATCHER_TYPE"] = "none"
os.environ["TORCH_DISABLE_JIT"] = "1"

import streamlit as st
from PIL import Image

# ✅ Streamlit Page Config
st.set_page_config(
    page_title="HealthAI",
    layout="centered",
    initial_sidebar_state="auto",
    page_icon="🩺"
)

# ✅ Import your feature modules
import patient_chat
import disease_prediction
import treatment_plans
import health_analytics

# ✅ Sidebar Navigation
page = st.sidebar.selectbox("🔍 Navigate", [
    "🏠 Home",
    "💬 Patient Chat",
    "🦠 Disease Prediction",
    "💊 Treatment Plans",
    "📊 Health Analytics"
])

# ✅ Home Page
if page == "🏠 Home":
    st.markdown("<h1 style='color:#0072C6;'>👨‍⚕️ Welcome to HealthAI 🏥</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:green; font-size:18px;'>💡 Your intelligent healthcare assistant powered by IBM Granite 🤖</p>", unsafe_allow_html=True)

    try:
        image = Image.open("healthai_logo.png")
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        st.image(image, width=300)
        st.markdown("</div>", unsafe_allow_html=True)
    except Exception:
        st.warning("⚠ Logo image not found. Please ensure 'healthai_logo.png' is in the same folder.")

    if st.button("💡 Click me for health tips"):
        tips = [
            "🩺 Eat more fruits and vegetables! 🍎🥦",
            "💤 Get at least 7-8 hours of sleep each night.",
            "🚶‍♀ Regular walking helps reduce blood pressure.",
            "💧 Stay hydrated – drink 2-3 liters of water daily.",
            "🧘‍♀ Practice mindfulness or meditation for stress relief.",
            "🦷 Brush and floss your teeth twice a day.",
            "🕒 Stick to a regular sleep schedule.",
            "📵 Reduce screen time before bed for better rest.",
            "🥗 Avoid junk food and eat balanced meals.",
            "🏃‍♀ Exercise at least 30 minutes a day to stay fit.",
            "🧴 Use sunscreen to protect your skin outdoors.",
            "🥤 Cut down on sugary drinks to control glucose levels."
        ]
        for tip in tips:
            st.success(tip)

    st.markdown("<p style='color:gray; font-size:12px;'>✨ Powered by IBM Granite, Streamlit & ❤ by Liki</p>", unsafe_allow_html=True)

# ✅ Feature Pages
elif page == "💬 Patient Chat":
    patient_chat.main()

elif page == "🦠 Disease Prediction":
    disease_prediction.main()

elif page == "💊 Treatment Plans":
    treatment_plans.main()

elif page == "📊 Health Analytics":
    health_analytics.main()
