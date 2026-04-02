import streamlit as st
import pandas as pd
import os

st.title("🎓 Student Mental Health Data Collection")

# ---------- Student Info ----------
student_id = st.text_input("Student ID")
age = st.number_input("Age", 15, 40)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])

# ---------- Sleep ----------
sleep_hours = st.slider("Average Sleep Hours", 0, 12)

# ---------- Nutrition ----------
breakfast = st.selectbox("Do you take breakfast?", ["Yes", "No"])
lunch = st.selectbox("Do you take lunch?", ["Yes", "No"])
dinner = st.selectbox("Do you take dinner?", ["Yes", "No"])

# ---------- Physical Activity ----------
activity_level = st.selectbox("Activity Level", ["Low", "Medium", "High"])
exercise_minutes = st.slider("Daily Exercise Minutes", 0, 180)

# ---------- Emotional (Burnout - simplified MBI) ----------
q1 = st.slider("I feel emotionally drained by studies", 0, 6)
q2 = st.slider("I feel tired when I wake up", 0, 6)
q3 = st.slider("I feel stressed about exams", 0, 6)
q4 = st.slider("I feel motivated to study", 0, 6)

# ---------- Submit ----------
if st.button("Submit"):
    data = {
        "student_id": student_id,
        "age": age,
        "gender": gender,
        "sleep_hours": sleep_hours,
        "breakfast": breakfast,
        "lunch": lunch,
        "dinner": dinner,
        "activity_level": activity_level,
        "exercise_minutes": exercise_minutes,
        "burnout_q1": q1,
        "burnout_q2": q2,
        "burnout_q3": q3,
        "burnout_q4": q4
    }

    df = pd.DataFrame([data])

    file = "student_data.csv"

    if os.path.exists(file):
        df.to_csv(file, mode='a', header=False, index=False)
    else:
        df.to_csv(file, index=False)

    st.success("✅ Data submitted successfully!")
