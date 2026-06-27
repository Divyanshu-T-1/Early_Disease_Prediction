import streamlit as st


def show_home():

    st.title("🩺 Early Disease Prediction System")

    st.markdown("""
### Welcome 👋

This application uses **Machine Learning** models to predict the likelihood of:

- 🩸 Diabetes
- ❤️ Heart Disease
- 🧠 Parkinson's Disease

Select a disease from the sidebar and enter the required medical details to get an instant prediction.
""")

    st.divider()

    st.subheader("🚀 Disease Prediction Modules")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success("🩸 Diabetes Prediction")
        st.write("""
✔ Glucose Level

✔ Blood Pressure

✔ BMI

✔ Insulin

✔ Age
""")

    with col2:
        st.success("❤️ Heart Disease Prediction")
        st.write("""
✔ Chest Pain

✔ Cholesterol

✔ Blood Pressure

✔ Maximum Heart Rate

✔ ECG Results
""")

    with col3:
        st.success("🧠 Parkinson's Prediction")
        st.write("""
✔ Voice Frequency

✔ Jitter

✔ Shimmer

✔ Harmonic Ratios

✔ 22 Voice Parameters
""")

    st.divider()

    st.subheader("✨ Why Choose This System?")

    c1, c2 = st.columns(2)

    with c1:
        st.success("⚡ Fast Predictions")
        st.success("🤖 Machine Learning Powered")
        st.success("🩺 Three Diseases Supported")

    with c2:
        st.success("📊 User Friendly Interface")
        st.success("🔒 Secure Local Prediction")
        st.success("🎓 Educational Project")

    st.divider()

    st.subheader("📌 About This Project")

    st.write("""
This project was developed using **Machine Learning** algorithms trained on publicly available healthcare datasets.

### Technologies Used

- 🐍 Python
- 🎈 Streamlit
- 🤖 Scikit-learn
- 📊 NumPy
- 🐼 Pandas

The objective of this application is to demonstrate how Machine Learning can assist in disease prediction based on patient medical information.
""")

    st.warning(
        "⚠️ This application is intended for educational purposes only and should not replace professional medical advice."
    )

    st.markdown("---")

