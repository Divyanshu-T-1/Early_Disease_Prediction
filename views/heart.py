import streamlit as st
from utils.model_loader import load_models


def show_heart():

    models = load_models()
    heart_model = models["heart"]

    st.title("❤️ Heart Disease Prediction")

    st.write(
        "Enter the patient's medical details below to predict the likelihood of heart disease."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            step=1
        )

        sex = st.selectbox(
            "Gender",
            ["Male", "Female"],
            help="Select the patient's gender."
        )

        cp = st.selectbox(
            "Chest Pain Type",
            [0, 1, 2, 3],
            help="""
0 = Typical Angina

1 = Atypical Angina

2 = Non-anginal Pain

3 = Asymptomatic
"""
        )

        trestbps = st.number_input(
            "Resting Blood Pressure (mm Hg)",
            min_value=0.0
        )

        chol = st.number_input(
            "Serum Cholesterol (mg/dL)",
            min_value=0.0
        )

        fbs = st.selectbox(
            "Fasting Blood Sugar > 120 mg/dL",
            [0, 1],
            help="0 = No, 1 = Yes"
        )

        restecg = st.selectbox(
            "Resting ECG Result",
            [0, 1, 2]
        )

    with col2:

        thalach = st.number_input(
            "Maximum Heart Rate Achieved",
            min_value=0.0
        )

        exang = st.selectbox(
            "Exercise Induced Angina",
            [0, 1],
            help="0 = No, 1 = Yes"
        )

        oldpeak = st.number_input(
            "ST Depression",
            format="%.1f"
        )

        slope = st.selectbox(
            "Slope of Peak Exercise ST Segment",
            [0, 1, 2]
        )

        ca = st.selectbox(
            "Major Vessels Colored",
            [0, 1, 2, 3]
        )

        thal = st.selectbox(
            "Thal",
            [0, 1, 2],
            help="""
0 = Normal

1 = Fixed Defect

2 = Reversible Defect
"""
        )

    st.divider()

    if st.button("🔍 Predict Heart Disease", use_container_width=True):

        prediction = heart_model.predict([[
            age,
            1 if sex == "Male" else 0,
            cp,
            trestbps,
            chol,
            fbs,
            restecg,
            thalach,
            exang,
            oldpeak,
            slope,
            ca,
            thal
        ]])

        st.subheader("Prediction Result")

        if prediction[0] == 1:

            st.error("🔴 High Risk of Heart Disease")

            st.markdown("""
The Machine Learning model predicts that the patient is **likely to have heart disease**.

### Recommendation

- ❤️ Consult a cardiologist.
- 🩺 Schedule further medical tests.
- 🥗 Maintain a heart-healthy diet.
- 🚶 Exercise regularly.
""")

        else:

            st.success("🟢 Low Risk of Heart Disease")

            st.markdown("""
The Machine Learning model predicts that the patient is **not likely to have heart disease**.

### Recommendation

- 🥗 Continue a healthy diet.
- 🚶 Stay physically active.
- 🩺 Monitor blood pressure and cholesterol regularly.
""")

    st.divider()

    with st.expander("📖 About Heart Disease"):

        st.markdown("""
### What is Heart Disease?

Heart disease refers to several conditions that affect the heart and blood vessels.

### Common Symptoms

- Chest pain
- Shortness of breath
- Fatigue
- Dizziness
- Pain in the left arm or jaw

### Prevention Tips

- ❤️ Eat a healthy diet.
- 🚭 Avoid smoking.
- 🏃 Exercise regularly.
- ⚖️ Maintain a healthy weight.
- 🩺 Get regular health check-ups.
""")