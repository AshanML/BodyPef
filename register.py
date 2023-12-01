import streamlit as st
import pandas as pd

# Function to save new user registration to a CSV file
def save_user_to_csv(username, password):
    user_data = pd.DataFrame({'Username': [username], 'Password': [password]})

    try:
        # Check if the CSV file exists, and if not, create it
        with open('user_data.csv', 'x') as file:
            user_data.to_csv(file, index=False, header=True)
    except FileExistsError:
        # If the file already exists, append the new user data to it
        with open('user_data.csv', 'a') as file:
            user_data.to_csv(file, index=False, header=False)

def render_register_page():
    st.title("Registration Page")

    # Create a registration form
    st.subheader("Create a New Account")
    new_username = st.text_input("New Username", key="register_username")
    new_password = st.text_input("New Password", type="password", key="register_password")

    # Registration button with a unique key
    register_button_key = "register_button"
    if st.button("Register", key=register_button_key):

        if register_new_user(new_username, new_password):
            st.success("Registration successful! You can now log in.")
            st.markdown("Already have an account? [Login](#login)")  # Add a link to the login page with a unique key
        else:
            st.error("Username already exists. Please choose a different one.")

    # Add a link to the login page with a unique key
    login_button_key = "login_button"
    if st.button("Login", key=login_button_key):
        st.session_state.page = "Login"

# Function to register a new user
def register_new_user(username, password):
    # Check if the username already exists in the CSV file
    user_data = pd.read_csv('user_data.csv', dtype=str)
    if username in user_data['Username'].values:
        return False  # Username already exists

    # Save the new user to the CSV file
    save_user_to_csv(username, password)
    return True  # Registration successful

# Call the register page rendering function
if __name__ == "__main__":
    render_register_page()
