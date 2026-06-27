import streamlit as st
from utils.model_loader import load_models


def show_parkinson():

    models = load_models()
    parkinson_model = models["parkinson"]

    st.title("🧠 Parkinson's Disease Prediction")

    st.write(
        "Enter the patient's voice analysis parameters below to predict the likelihood of Parkinson's Disease."
    )

    st.info(
        "These parameters are obtained from specialized voice analysis software."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        fo = st.number_input(
            "Average Vocal Frequency (MDVP:Fo)",
            format="%.6f",
            help="Average vocal frequency in Hertz."
        )

        f1 = st.number_input(
            "Maximum Vocal Frequency (MDVP:Fhi)",
            format="%.6f"
        )

        f2 = st.number_input(
            "Minimum Vocal Frequency (MDVP:Flo)",
            format="%.6f"
        )

        f3 = st.number_input(
            "Jitter (%)",
            format="%.6f"
        )

        f4 = st.number_input(
            "Jitter (Absolute)",
            format="%.6f"
        )

        f5 = st.number_input(
            "RAP",
            format="%.6f"
        )

        f6 = st.number_input(
            "PPQ",
            format="%.6f"
        )

        f7 = st.number_input(
            "DDP",
            format="%.6f"
        )

        f8 = st.number_input(
            "Shimmer",
            format="%.6f"
        )

        f9 = st.number_input(
            "Shimmer (dB)",
            format="%.6f"
        )

        f10 = st.number_input(
            "APQ3",
            format="%.6f"
        )

    with col2:

        f11 = st.number_input(
            "APQ5",
            format="%.6f"
        )

        f12 = st.number_input(
            "APQ",
            format="%.6f"
        )

        f13 = st.number_input(
            "DDA",
            format="%.6f"
        )

        f14 = st.number_input(
            "Noise-to-Harmonic Ratio (NHR)",
            format="%.6f"
        )

        f15 = st.number_input(
            "Harmonic-to-Noise Ratio (HNR)",
            format="%.6f"
        )

        f16 = st.number_input(
            "RPDE",
            format="%.6f"
        )

        f17 = st.number_input(
            "DFA",
            format="%.6f"
        )

        f18 = st.number_input(
            "Spread1",
            format="%.6f"
        )

        f19 = st.number_input(
            "Spread2",
            format="%.6f"
        )

        f20 = st.number_input(
            "D2",
            format="%.6f"
        )

        f21 = st.number_input(
            "PPE",
            format="%.6f"
        )

    st.divider()

    if st.button("🔍 Predict Parkinson's Disease", use_container_width=True):

        prediction = parkinson_model.predict([[
            fo, f1, f2, f3, f4,
            f5, f6, f7, f8, f9,
            f10, f11, f12, f13,
            f14, f15, f16, f17,
            f18, f19, f20, f21
        ]])

        st.subheader("Prediction Result")

        if prediction[0] == 1:

            st.error("🔴 High Risk of Parkinson's Disease")

            st.markdown("""
The Machine Learning model predicts that the patient is **likely to have Parkinson's Disease**.

### Recommendation

- 👨‍⚕️ Consult a neurologist.
- 🧪 Consider additional diagnostic tests.
- 🩺 Seek professional medical evaluation.
""")

        else:

            st.success("🟢 Low Risk of Parkinson's Disease")

            st.markdown("""
The Machine Learning model predicts that the patient is **not likely to have Parkinson's Disease**.

### Recommendation

- 🥗 Maintain a healthy lifestyle.
- 🏃 Stay physically active.
- 🩺 Continue regular health check-ups.
""")

    st.divider()

    with st.expander("📖 About Parkinson's Disease"):

        st.markdown("""
### What is Parkinson's Disease?

Parkinson's Disease is a progressive neurological disorder that affects movement and coordination.

### Common Symptoms

- Tremors
- Muscle stiffness
- Slow movement
- Balance problems
- Speech difficulties

### Prevention Tips

Although Parkinson's Disease cannot always be prevented, maintaining a healthy lifestyle and regular exercise may help reduce risk factors.

### Note

The parameters entered above are extracted from voice recordings using specialized voice analysis software.
""")