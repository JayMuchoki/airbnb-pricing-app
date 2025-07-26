# 🏠 Price It Right - Airbnb Price Prediction App

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://airbnb-pricing-app.streamlit.app/)



---

## 📌 Overview

**Price It Right** is a Streamlit web application that helps Airbnb hosts estimate nightly prices for listings based on various features like location, room type, and availability. This tool allows hosts to stay competitive and price their property accurately.

---
<img width="608" height="367" alt="Screenshot 2025-07-26 194127" src="https://github.com/user-attachments/assets/83726ddb-c7d6-457d-bf1f-cbd631f07b42" />


## 🚀 Features

- Predicts Airbnb listing price using a trained machine learning model
- User-friendly interface built with Streamlit
- Takes in features like:
  - Neighbourhood Group
  - Room Type
  - Latitude & Longitude
  - Minimum Nights
  - Number of Reviews
  - Reviews per Month
  - Availability per Year
  - Host’s Listing Count

---

## 🧠 Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **Machine Learning:** Scikit-learn
- **Model:** Regression (trained using Airbnb NYC dataset)
- **Deployment:** Streamlit Cloud

---

## 🧪 How to Use

1. Click this link to open the app: 👉 [Launch App](https://airbnb-pricing-app.streamlit.app/)
2. Enter your listing details in the sidebar form
3. Click on **"Predict Price"**
4. View the estimated nightly price for your Airbnb property!

---

## 🖼️ Demo Screenshot

<img width="608" height="367" alt="Screenshot 2025-07-26 194127" src="https://github.com/user-attachments/assets/eef8efdf-4242-4ce3-9f02-3977e0e20fca" />

---

## 📂 Project Structure

```bash
├── app.py                     # Streamlit app
├── model.pkl                  # Trained ML model
├── encoder.pkl                # Label encoder for categorical features
├── scaler (2).pkl             # Scaler for numerical features
├── airbnb_app_image.png       # App image/screenshot
├── README.md
