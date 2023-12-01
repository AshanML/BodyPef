import streamlit as st
import pandas as pd
import dashboard

# Function to check user credentials
def authenticate_user(username, password):
    try:
        user_data = pd.read_csv('user_data.csv', dtype=str)
    except FileNotFoundError:
        return False  # No registered users

    if username in user_data['Username'].values and \
       password == user_data.loc[user_data['Username'] == username, 'Password'].values[0]:
        st.session_state.username = username  # Store the username in session state
        return True

    return False

def render_login_page():
    st.title("Welcome to Login Page")

    # Create a login form
    st.subheader("Login to Your Account")
    username = st.text_input("Username", key="login_username")  # Unique key for the username input
    password = st.text_input("Password", type="password", key="login_password")  # Unique key for the password input

    # Login button with a unique key
    login_button_key = "login_button"  # Assign a unique key
    if st.button("Login", key=login_button_key):
        # Replace with your authentication logic here
        if authenticate_user(username, password):
            st.success("Logged in successfully!")
            st.session_state.page = "Dashboard"  # Navigate to the Dashboard page
        else:
            st.error("Invalid credentials. Please try again.")

    # Only show a link to the registration page if the user is not logged in
    if "username" not in st.session_state:
        st.markdown("Don't have an account? [Register](#register)")

# Call the login page rendering function
if __name__ == "__main__":
    render_login_page()
