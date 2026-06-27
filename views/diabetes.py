import streamlit as st
from utils.model_loader import load_models


def show_diabetes():

    models = load_models()
    diabetes_model = models["diabetes"]

    st.title("🩸 Diabetes Prediction")

    st.write(
        "Enter the patient's medical details below to predict the likelihood of diabetes."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        pregnancies = st.number_input(
            "Number of Pregnancies",
            min_value=0,
            step=1,
            help="Total number of pregnancies."
        )

        glucose = st.number_input(
            "Glucose Level (mg/dL)",
            min_value=0.0,
            help="Normal fasting glucose: 70–99 mg/dL."
        )

        blood_pressure = st.number_input(
            "Blood Pressure (mm Hg)",
            min_value=0.0,
            help="Enter the patient's resting blood pressure."
        )

        skin_thickness = st.number_input(
            "Skin Thickness (mm)",
            min_value=0.0,
            help="Triceps skin fold thickness."
        )

    with col2:

        insulin = st.number_input(
            "Insulin Level",
            min_value=0.0,
            help="2-Hour serum insulin."
        )

        bmi = st.number_input(
            "Body Mass Index (BMI)",
            min_value=0.0,
            format="%.2f",
            help="Normal BMI is approximately 18.5–24.9."
        )

        diabetes_pedigree = st.number_input(
            "Diabetes Pedigree Function",
            min_value=0.000,
            format="%.3f",
            help="Indicates hereditary diabetes likelihood."
        )

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            step=1
        )

    st.divider()

    if st.button("🔍 Predict Diabetes", use_container_width=True):

        prediction = diabetes_model.predict([[
            pregnancies,
            glucose,
            blood_pressure,
            skin_thickness,
            insulin,
            bmi,
            diabetes_pedigree,
            age
        ]])

        st.subheader("Prediction Result")

        if prediction[0] == 1:

            st.error("🔴 High Risk of Diabetes Detected")

            st.markdown("""
The Machine Learning model predicts that the patient is **likely to have diabetes**.

### Recommendation

- 👨‍⚕️ Consult a healthcare professional.
- 🧪 Consider further medical tests.
- 🥗 Maintain a healthy diet.
- 🏃 Exercise regularly.
""")

        else:

            st.success("🟢 Low Risk of Diabetes")

            st.markdown("""
The Machine Learning model predicts that the patient is **not likely to have diabetes**.

### Recommendation

- 🥦 Continue a healthy lifestyle.
- 🚶 Stay physically active.
- 🩺 Schedule regular health check-ups.
""")

    st.divider()

    with st.expander("📖 About Diabetes"):

        st.markdown("""
### What is Diabetes?

Diabetes is a chronic disease that affects how your body regulates blood sugar (glucose).

### Common Symptoms

- Frequent urination
- Excessive thirst
- Increased hunger
- Fatigue
- Blurred vision
- Unexplained weight loss

### Prevention Tips

- 🥗 Eat a balanced diet.
- 🏃 Exercise regularly.
- ⚖️ Maintain a healthy weight.
- 🚭 Avoid smoking.
- 🩺 Have regular medical check-ups.
""")