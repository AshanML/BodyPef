import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
df = pd.read_csv("bodyPerformance.csv")

# Render the Dashboard Page
def render_dashboard_page():
    st.set_page_config(layout="wide")
    st.title("Body Performance Dashboard")

    # Sidebar filters
    st.sidebar.title("Filters")

    # Gender filter
    selected_gender = st.sidebar.selectbox("Select Gender", df['gender'].unique())
    filtered_df = df[df['gender'] == selected_gender]

    # Class filter
    selected_class = st.sidebar.selectbox("Select Class", df['class'].unique())
    filtered_df = filtered_df[filtered_df['class'] == selected_class]

    # Age filter
    age_min = int(filtered_df['age'].min())
    age_max = int(filtered_df['age'].max())
    selected_age = st.sidebar.slider("Select Age", age_min, age_max, (age_min, age_max))
    filtered_df = filtered_df[(filtered_df['age'] >= selected_age[0]) & (filtered_df['age'] <= selected_age[1])]

    # Add a button to navigate to the prediction page
    st.sidebar.markdown("---")  # Add a horizontal line to separate elements
    if st.sidebar.button("Prediction Page--->"):
        st.session_state.page = "Prediction"

    # Create a 3x1 grid layout for visualizations
    container1 = st.container()
    col1, col2, col3 = st.columns(3)

    with container1:
        with col1:
            st.subheader("Weight vs Height")
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.scatterplot(data=filtered_df, x='weight_kg', y='height_cm', ax=ax)
            st.pyplot(fig)

        with col2:
            st.subheader("Weight vs Body Fat")
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.scatterplot(data=filtered_df, x='weight_kg', y='body fat_%', ax=ax)
            st.pyplot(fig)

        with col3:
            st.subheader("Diastolic vs Systolic")
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.scatterplot(data=filtered_df, x='diastolic', y='systolic', ax=ax)
            st.pyplot(fig)

     # Create another 3x1 grid layout for additional charts (container2)
    container2 = st.container()
    col4, col5, col6 = st.columns(3)

    with container2:
        with col4:
            st.subheader("Body Fat % vs Grip Force")
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.scatterplot(data=filtered_df, x='body fat_%', y='gripForce', ax=ax, color='red')
            st.pyplot(fig)

        with col5:
            st.subheader("Weight vs Sit-ups Counts")
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.scatterplot(data=filtered_df, x='weight_kg', y='sit-ups counts', ax=ax, color='orange')
            st.pyplot(fig)

        with col6:
            st.subheader("Weight vs Broad Jump (cm)")
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.scatterplot(data=filtered_df, x='weight_kg', y='broad jump_cm', ax=ax, color='brown')
            st.pyplot(fig)


    # Create a 2x1 grid layout for distribution plots (container3)
    container3 = st.container()
    col7, col8 = st.columns(2)

    with container3:
        with col7:
            st.subheader("Distribution of Diastolic")
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.histplot(data=filtered_df, x='diastolic', kde=True, color='cyan')
            st.pyplot(fig)

        with col8:
            st.subheader("Distribution of Systolic")
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.histplot(data=filtered_df, x='systolic', kde=True, color='magenta')
            st.pyplot(fig)





# Run the Streamlit app
if __name__ == "__main__":
    render_dashboard_page()
