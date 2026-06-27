import streamlit as st


def load_css():

    st.markdown("""
    <style>

    /* =========================
       Main App
    ========================= */

    .main{
        padding-top: 1rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }

    /* =========================
       Headings
    ========================= */

    h1{
        color:#1565C0;
        font-weight:700;
    }

    h2{
        color:#1976D2;
        font-weight:600;
    }

    h3{
        color:#1E88E5;
    }

    /* =========================
       Sidebar
    ========================= */

    section[data-testid="stSidebar"]{
        background-color:#0F172A;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] p{
        color:white;
    }

    /* =========================
       Buttons
    ========================= */

    .stButton > button{

        width:100%;
        height:50px;

        background:#2563EB;
        color:white;

        border:none;
        border-radius:10px;

        font-size:16px;
        font-weight:600;

        transition:0.3s;
    }

    .stButton > button:hover{

        background:#1D4ED8;
        color:white;

        transform:translateY(-2px);

        box-shadow:0 6px 18px rgba(0,0,0,0.20);
    }

    /* =========================
       Input Boxes
    ========================= */

    .stNumberInput,
    .stTextInput,
    .stSelectbox{

        margin-bottom:12px;

    }

    /* =========================
       Alert Boxes
    ========================= */

    div[data-baseweb="notification"]{

        border-radius:12px;

    }

    /* =========================
       Divider
    ========================= */

    hr{
        margin-top:20px;
        margin-bottom:20px;
    }

    /* =========================
       Footer
    ========================= */

    footer{
        visibility:hidden;
    }

    #MainMenu{
        visibility:hidden;
    }

    header{
        visibility:hidden;
    }

    </style>
    """, unsafe_allow_html=True)