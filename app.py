import pandas as pd
import numpy as np
import joblib 
import streamlit as st

# Load model and transformers
model=joblib.load('model.pkl')
encoder=joblib.load('encoder.pkl')
scaler=joblib.load('scaler (2).pkl')

st.title("Price It Right: Your Airbnb Income Estimator")

st.header("Enter Property Details")

neighbourhood = st.selectbox("Neighbourhood Group", ['Manhattan', 'Brooklyn', 'Queens', 'Bronx', 'Staten Island'])
room_type = st.selectbox("Room Type", ['Entire home/apt', 'Private room', 'Shared room', 'Hotel room'])


latitude=st.number_input("latitude",value=40.776)
latitude = st.number_input("Latitude", value=40.776)
longitude = st.number_input("Longitude", value=-73.97)
minimum_nights = st.number_input("Minimum Nights", min_value=1, value=3)
number_of_reviews = st.number_input("Number of Reviews", min_value=0, value=100)
reviews_per_month = st.number_input("Reviews per Month", min_value=0.0, value=2.5)
availability_365 = st.number_input("Availability (Days per Year)", min_value=0, max_value=365, value=180)
calculated_host_listings_cleaned=st.number_input("calculated_host_listings_cleaned",value=6)

if st.button ('Predict Price'):
    user_input=pd.DataFrame({
        'neighbourhood_group': [neighbourhood],
        'room_type': [room_type],
        'latitude': [latitude],
        'longitude': [longitude],
        'minimum_nights': [minimum_nights],
        'number_of_reviews': [number_of_reviews],
        'reviews_per_month': [reviews_per_month],
        'availability_365': [availability_365],
        'calculated_host_listings_cleaned':[calculated_host_listings_cleaned]
    })
# we have inserted a dataframe so as we can be able to encode and scale ceratin value 

    cat_encode=encoder.transform(user_input[['neighbourhood_group', 'room_type']])
    num_scaled=scaler.transform(user_input.drop(['neighbourhood_group', 'room_type'], axis=1))

    final_input=np.concat([cat_encode,num_scaled],axis=1)
    prediction=model.predict(final_input)

    st.success(f'Predicted Price : ${prediction[0]:.2f}')


        
    