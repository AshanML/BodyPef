import streamlit as st
from login import render_login_page
from register import render_register_page
from dashboard import render_dashboard_page
from prediction import render_prediction_page

# Define session state to keep track of the current page
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Navigation buttons
if st.session_state.page == "Home":
    if st.button("Login"):
        st.session_state.page = "Login"
    if st.button("Register"):
        st.session_state.page = "Register"

# Redirect to the appropriate page
if st.session_state.page == "Login":
    render_login_page()
elif st.session_state.page == "Register":
    render_register_page()
elif st.session_state.page == "Dashboard":
    render_dashboard_page()
elif st.session_state.page == "Prediction":
    render_prediction_page()
