import pandas as pd
import numpy as np
import joblib
import streamlit as st

# Load the trained model and transformers
model = joblib.load('model.pkl')
encoder = joblib.load('encoder.pkl')
scaler = joblib.load('scaler (2).pkl')

# Set page configuration
st.set_page_config(page_title="Price It Right", page_icon="🏠", layout="centered")

# Title and description
st.markdown("<h1 style='text-align: center; color: #2c3e50;'>🏠 Price It Right</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #7f8c8d;'>Estimate the right price for your Airbnb property</h4>", unsafe_allow_html=True)
st.write("---")

# Sidebar for user input
st.sidebar.header("Enter Property Details")

neighbourhood = st.sidebar.selectbox("Neighbourhood Group", ['Manhattan', 'Brooklyn', 'Queens', 'Bronx', 'Staten Island'])
room_type = st.sidebar.selectbox("Room Type", ['Entire home/apt', 'Private room', 'Shared room', 'Hotel room'])

latitude = st.sidebar.number_input("Latitude", value=40.776)
longitude = st.sidebar.number_input("Longitude", value=-73.97)
minimum_nights = st.sidebar.number_input("Minimum Nights", min_value=1, value=3)
number_of_reviews = st.sidebar.number_input("Number of Reviews", min_value=0, value=100)
reviews_per_month = st.sidebar.number_input("Reviews per Month", min_value=0.0, value=2.5)
availability_365 = st.sidebar.number_input("Availability (Days per Year)", min_value=0, max_value=365, value=180)
calculated_host_listings_cleaned = st.sidebar.number_input("Host's Listing Count (Cleaned)", value=6)

# Prediction Button
if st.sidebar.button("💰 Predict Price"):
    user_input = pd.DataFrame({
        'neighbourhood_group': [neighbourhood],
        'room_type': [room_type],
        'latitude': [latitude],
        'longitude': [longitude],
        'minimum_nights': [minimum_nights],
        'number_of_reviews': [number_of_reviews],
        'reviews_per_month': [reviews_per_month],
        'availability_365': [availability_365],
        'calculated_host_listings_cleaned': [calculated_host_listings_cleaned]
    })

    # Encode categorical and scale numerical features
    cat_encoded = encoder.transform(user_input[['neighbourhood_group', 'room_type']])
    num_scaled = scaler.transform(user_input.drop(['neighbourhood_group', 'room_type'], axis=1))
    final_input = np.concatenate([cat_encoded, num_scaled], axis=1)

    # Make prediction
    prediction = model.predict(final_input)

    # Display result
    st.markdown("---")
    st.success(f"💸 Estimated Price per Night: **${prediction[0]:.2f}**")
    st.markdown("✔️ Use this price to stay competitive in the market and maximize your earnings!")

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: #95a5a6;'>Built with by Jay Muchoki | Airbnb Price Estimator</div>", unsafe_allow_html=True)
