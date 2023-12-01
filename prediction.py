import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the trained model
gb_model = joblib.load('GBmodel.joblib')

# Define class labels mapping
class_mapping = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}

# Render the Prediction Page
def render_prediction_page():
    st.title("Body Performance Prediction Page")

    # Add a sidebar for input fields
    st.sidebar.title("Enter User Data")
    gender = st.sidebar.radio("Gender", ["Female", "Male"])
    age = st.sidebar.number_input("Age", min_value=0, max_value=100)
    height_cm = st.sidebar.number_input("Height (cm)", min_value=0)
    weight_kg = st.sidebar.number_input("Weight (kg)", min_value=0)
    body_fat = st.sidebar.number_input("Body Fat (%)", min_value=0, max_value=100)
    diastolic = st.sidebar.number_input("Diastolic", min_value=0)
    systolic = st.sidebar.number_input("Systolic", min_value=0)
    grip_force = st.sidebar.number_input("Grip Force", min_value=0)
    sit_bend_forward = st.sidebar.number_input("Sit and Bend Forward (cm)", min_value=0)
    sit_ups_counts = st.sidebar.number_input("Sit-ups Counts", min_value=0)
    broad_jump_cm = st.sidebar.number_input("Broad Jump (cm)", min_value=0)

    # Use a form to force rendering of the model selection radio button
    with st.form("model_selection_form"):
        model_choice = st.radio("Select Model", ["Gradient Boosting"])
        submit_button = st.form_submit_button(label="Submit")

    # Determine the selected model
    model = rf_model if model_choice ==  gb_model

    # Make predictions
    if submit_button:
        # Prepare input data as a DataFrame
        input_data = pd.DataFrame({
            'age': [age],
            'gender': [1 if gender == 'Male' else 0],
            'height_cm': [height_cm],
            'weight_kg': [weight_kg],
            'body fat_%': [body_fat],
            'diastolic': [diastolic],
            'systolic': [systolic],
            'gripForce': [grip_force],
            'sit and bend forward_cm': [sit_bend_forward],
            'sit-ups counts': [sit_ups_counts],
            'broad jump_cm': [broad_jump_cm]
        })

        # Make predictions
        prediction = model.predict(input_data)

        # Map the class label to its corresponding value
        predicted_class = class_mapping.get(prediction[0], 'Unknown')

        # Display the prediction result
        st.success(f"Predicted Class: {predicted_class}")

        # Display input values and prediction summary
        st.subheader("Prediction Summary")
        st.write("Input Values:")
        st.write(f"Gender: {gender}")
        st.write(f"Age: {age}")
        st.write(f"Height (cm): {height_cm}")
        st.write(f"Weight (kg): {weight_kg}")
        st.write(f"Body Fat (%): {body_fat}")
        st.write(f"Diastolic: {diastolic}")
        st.write(f"Systolic: {systolic}")
        st.write(f"Grip Force: {grip_force}")
        st.write(f"Sit and Bend Forward (cm): {sit_bend_forward}")
        st.write(f"Sit-ups Counts: {sit_ups_counts}")
        st.write(f"Broad Jump (cm): {broad_jump_cm}")
        st.write("Prediction Summary:")
        st.write(f"Predicted Class: {predicted_class}")

            # Display images based on prediction
        if predicted_class == 'A':
            st.image('excellent.png', use_column_width=True)
        elif predicted_class in ['B', 'C']:
            st.image('moderate.png', use_column_width=True)
        elif predicted_class == 'D':
            st.image('bad.png', use_column_width=True)

    # Add buttons for navigation and logging out
    if st.button("Go to Dashboard"):
        st.session_state.page = "Dashboard"
    if st.button("Log Out"):
        st.session_state.page = "Home"


# Call the prediction page rendering function
if __name__ == "__main__":
    render_prediction_page()
