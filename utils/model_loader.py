import pickle
import streamlit as st


@st.cache_resource
def load_models():

    models = {
        "diabetes": pickle.load(open("models/diabetes_model.pkl", "rb")),
        "heart": pickle.load(open("models/heart_model.pkl", "rb")),
        "parkinson": pickle.load(open("models/parkinson_model.pkl", "rb"))
    }

    return models