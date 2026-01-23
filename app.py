import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from datetime import date

st.set_page_config(
    page_title="Forgetting Curve Predictor",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
.title {
    font-size: 42px;
    font-weight: 800;
    color: #1f2937;
}
.subtitle {
    font-size: 18px;
    color: #6b7280;
}
.card {
    background: linear-gradient(135deg, #ffffff, #f9fafb);
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
.advice {
    background-color: #ecfeff;
    padding: 20px;
    border-left: 6px solid #06b6d4;
    border-radius: 12px;
}
.center {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="center title">🧠 Personalized Forgetting Curve Predictor</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="center subtitle">Predict memory retention and get smart revision suggestions</div>',
    unsafe_allow_html=True
)

st.divider()

st.markdown("## 📘 Learning Details")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    topic = st.text_input("📚 Topic Name", "Machine Learning Basics")
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    difficulty = st.selectbox("⚡ Difficulty Level", ["Easy", "Medium", "Hard"])
    st.markdown('</div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    study_time = st.slider("⏱ Study Time (minutes)", 10, 180, 60)
    st.markdown('</div>', unsafe_allow_html=True)

revision_count = st.slider("🔁 Number of Revisions Done", 0, 10, 2)

analyze = st.button("🚀 Predict Retention")

# PREDICTION LOGIC
if analyze:
    base_retention = {"Easy": 0.75, "Medium": 0.6, "Hard": 0.45}
    k = base_retention[difficulty]

    days = np.arange(0, 30)
    retention = np.exp(-k * days) + (revision_count * 0.05)
    retention = np.clip(retention, 0, 1)

    final_retention = retention[7] * 100

    st.divider()
    st.markdown("## 📊 Retention Analysis")

    r1, r2 = st.columns(2)

    with r1:
        st.markdown('<div class="card center">', unsafe_allow_html=True)
        st.metric("📈 Retention after 7 Days", f"{final_retention:.1f}%")
        st.progress(final_retention / 100)
        st.markdown('</div>', unsafe_allow_html=True)

    with r2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        fig, ax = plt.subplots()
        ax.plot(days, retention * 100)
        ax.set_xlabel("Days")
        ax.set_ylabel("Memory Retention (%)")
        ax.set_title("Forgetting Curve")
        st.pyplot(fig)
        st.markdown('</div>', unsafe_allow_html=True)


    st.markdown("## 🤖 AI Revision Advice")

    if final_retention < 40:
        msg = "Revise within **24 hours** and use active recall techniques."
    elif final_retention < 70:
        msg = "Schedule a **revision after 3 days** for better retention."
    else:
        msg = "Great retention! Do a **weekly quick review**."

    st.markdown(f'<div class="advice">💡 {msg}</div>', unsafe_allow_html=True)

st.divider()
st.markdown(
    "<div class='center'>Built as part of CODTECH Internship • Machine Learning Project</div>",
    unsafe_allow_html=True
)

