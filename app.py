import streamlit as st
from streamlit_option_menu import option_menu

from utils.styles import load_css

from views.home import show_home
from views.diabetes import show_diabetes
from views.heart import show_heart
from views.parkinson import show_parkinson

st.set_page_config(
    page_title="Early Disease Prediction System",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load Custom CSS
load_css()

with st.sidebar:

    st.markdown("## 🩺")

    st.title("Early Disease Prediction")

    st.caption("Machine Learning Based Healthcare System")

    st.markdown("---")

    selected = option_menu(
        menu_title=None,
        options=[
            "Home",
            "Diabetes",
            "Heart Disease",
            "Parkinson's"
        ],
        icons=[
            "house",
            "activity",
            "heart-pulse",
            "person"
        ],
        default_index=0,
        styles={
            "container": {
                "padding": "0!important",
                "background-color": "#0E1117"
            },
            "icon": {
                "color": "#4CAF50",
                "font-size": "18px"
            },
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "4px",
                "--hover-color": "#1E88E5",
            },
            "nav-link-selected": {
                "background-color": "#1976D2",
            },
        },
    )

    st.markdown("---")

    st.info(
        """
### 👨‍💻 Developer

**Divyanshu Mishra**

B.Tech CSE (AI)

Machine Learning Project
"""
    )

if selected == "Home":
    show_home()

elif selected == "Diabetes":
    show_diabetes()

elif selected == "Heart Disease":
    show_heart()

elif selected == "Parkinson's":
    show_parkinson()

st.markdown("---")
st.caption("© 2026 • Early Disease Prediction System • Developed by Divyanshu Mishra")