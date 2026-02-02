import streamlit as st

st.set_page_config(
    page_title="Study Reminder App",

)

st.title("Study Reminder App")
st.write("This app helps you decide **when to revise a topic**.")

st.divider()

topic = st.text_input("Topic name", "Python Basics")

difficulty = st.selectbox(
    "Topic difficulty",
    ["Easy", "Medium", "Hard"]
)

study_time = st.slider(
    "How many minutes did you study?",
    10, 180, 60
)

revisions = st.slider(
    "How many times have you revised?",
    0, 5, 1
)

def predict_memory(difficulty, study_time, revisions):
    score = study_time + (revisions * 20)

    if difficulty == "Medium":
        score -= 10
    elif difficulty == "Hard":
        score -= 20

    if score >= 100:
        return "Good", "Revise after 1 week"
    elif score >= 60:
        return "Average", "Revise after 2 days"
    else:
        return "Low", "Revise today"

if st.button("Check Study Status"):
    level, advice = predict_memory(difficulty, study_time, revisions)

    st.success(f"Memory Level: {level}")
    st.info(f"Revision Advice: {advice}")

st.divider()
st.caption("Simple learning project")


