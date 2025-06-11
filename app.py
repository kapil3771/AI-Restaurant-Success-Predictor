import streamlit as st
import numpy as np
import pandas as pd
import joblib
import plotly.express as px
import altair as alt
from streamlit_extras.add_vertical_space import add_vertical_space

# Load trained models
rf_classifier = joblib.load("rf_classifier.pkl")  # Classification Model
rf_regressor = joblib.load("rf_regressor.pkl")    # Regression Model

# Set page config
st.set_page_config(page_title="AI-Powered Restaurant Success Predictor", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    body { background-color: #0e1117; color: white; }
    .stApp { background-color: #0e1117; }
    .title { font-size: 50px; font-weight: bold; color: #FF4B4B; text-align: center; }
    .subheader { font-size: 30px; font-weight: bold; color: #E1E1E1; text-align: center; }
    .section-header { font-size: 30px; font-weight: bold; color: #FFD700; text-align: center; } 
    .glass-card {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 20px;
        backdrop-filter: blur(10px);
        box-shadow: 0px 4px 12px rgba(255, 255, 255, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Title & Header
st.markdown("<h1 class='title'>🍽️ AI-Powered Restaurant Success Predictor</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='subheader'>📊 Predict Success & Estimate Pricing with Machine Learning</h2>", unsafe_allow_html=True)
add_vertical_space(2)

# Hardcoded location, rest_type, and cuisine options
locations = ['Banashankari', 'Basavanagudi', 'Mysore Road', 'Jayanagar', 'Kumaraswamy Layout',
             'Rajarajeshwari Nagar', 'Vijay Nagar', 'Uttarahalli', 'JP Nagar', 'South Bangalore',
             'City Market', 'Nagarbhavi', 'Bannerghatta Road', 'BTM', 'Kanakapura Road',
             'Bommanahalli', 'CV Raman Nagar', 'Electronic City', 'HSR', 'Marathahalli',
             'Sarjapur Road', 'Wilson Garden', 'Shanti Nagar', 'Koramangala 5th Block',
             'Koramangala 8th Block', 'Richmond Road', 'Koramangala 7th Block', 'Jalahalli',
             'Koramangala 4th Block', 'Bellandur', 'Whitefield', 'East Bangalore',
             'Old Airport Road', 'Indiranagar', 'Koramangala 1st Block', 'Frazer Town',
             'RT Nagar', 'MG Road', 'Brigade Road', 'Lavelle Road', 'Church Street',
             'Ulsoor', 'Residency Road', 'Shivajinagar', 'Infantry Road', 'St. Marks Road',
             'Cunningham Road', 'Race Course Road', 'Commercial Street', 'Vasanth Nagar',
             'HBR Layout', 'Domlur', 'Ejipura', 'Jeevan Bhima Nagar', 'Old Madras Road',
             'Malleshwaram', 'Seshadripuram', 'Kammanahalli', 'Koramangala 6th Block',
             'Majestic', 'Langford Town', 'Central Bangalore', 'Sanjay Nagar', 'Brookefield',
             'ITPL Main Road, Whitefield', 'Varthur Main Road, Whitefield', 'KR Puram',
             'Koramangala 2nd Block', 'Koramangala 3rd Block', 'Koramangala', 'Hosur Road',
             'Rajajinagar', 'Banaswadi', 'North Bangalore', 'Nagawara', 'Hennur', 'Kalyan Nagar',
             'New BEL Road', 'Jakkur', 'Rammurthy Nagar', 'Thippasandra', 'Kaggadasapura',
             'Hebbal', 'Kengeri', 'Sankey Road', 'Sadashiv Nagar', 'Basaveshwara Nagar',
             'Yeshwantpur', 'West Bangalore', 'Magadi Road', 'Yelahanka', 'Sahakara Nagar', 'Peenya']

rest_types = ['Casual Dining', 'Cafe, Casual Dining', 'Quick Bites', 'Casual Dining, Cafe', 'Cafe',
              'Quick Bites, Cafe', 'Cafe, Quick Bites', 'Delivery', 'Mess', 'Dessert Parlor',
              'Bakery, Dessert Parlor', 'Pub', 'Bakery', 'Takeaway, Delivery', 'Fine Dining',
              'Beverage Shop', 'Sweet Shop', 'Bar', 'Beverage Shop, Quick Bites', 'Confectionery']

cuisine_options = ['North Indian, Mughlai, Chinese', 'Chinese, North Indian, Thai', 'Cafe, Mexican, Italian',
                   'North Indian, Street Food, Biryani', 'Chinese, Mughlai', 'North Indian, Chinese, Arabian, Momos']

# Sidebar Inputs
st.sidebar.title("🔍 Enter Restaurant Details")

location = st.sidebar.selectbox("📍 Select Location", sorted(locations))
rest_type = st.sidebar.multiselect("🍽️ Select Restaurant Type(s)", sorted(rest_types))
cuisines = st.sidebar.multiselect("🍜 Select Cuisine(s)", sorted(cuisine_options))
book_table = st.sidebar.radio("📅 Table Booking Available?", ["Yes", "No"])
votes = st.sidebar.slider("👍 Number of Votes", 0, 5000, 1000)

# Preprocess for model input
def hash_encode(val):
    return hash(val) % 1000

location_encoded = hash_encode(location)
rest_type_encoded = hash_encode(",".join(sorted(rest_type)))
cuisines_encoded = hash_encode(",".join(sorted(cuisines)))
book_table_encoded = 1 if book_table == "Yes" else 0

input_data = np.array([
    location_encoded,
    rest_type_encoded,
    cuisines_encoded,
    book_table_encoded,
    votes
]).reshape(1, -1)

# Prediction UI
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<p class='section-header'>🎯 Will Your Restaurant Succeed?</p>", unsafe_allow_html=True)

    if st.button("🔮 Predict Success", use_container_width=True):
        success_proba = rf_classifier.predict_proba(input_data)[0]
        success_percentage = success_proba[1] * 100
        failure_percentage = success_proba[0] * 100

        st.subheader(f"📊 Success Probability: {success_percentage:.2f}%")

        fig = px.pie(
            values=[success_percentage, failure_percentage],
            names=["Success", "Failure"],
            color=["Success", "Failure"],
            color_discrete_map={"Success": "green", "Failure": "red"}
        )
        st.plotly_chart(fig)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<p class='section-header'>💵 Estimate Restaurant Pricing</p>", unsafe_allow_html=True)

    if st.button("💲 Predict Approximate Cost", use_container_width=True):
        price_prediction = rf_regressor.predict(input_data)
        st.subheader(f"Estimated Cost for Two: ₹{round(price_prediction[0], 2)}")

        price_range = [price_prediction[0] - 200, price_prediction[0], price_prediction[0] + 200]
        price_labels = ["Lower Estimate", "Predicted Price", "Higher Estimate"]
        price_fig = px.bar(x=price_labels, y=price_range, title="📊 Price Estimation Range", color=price_labels)
        st.plotly_chart(price_fig)
    st.markdown("</div>", unsafe_allow_html=True)

# Optional: Success trend chart
st.markdown("<h2 class='section-header'>📈 Success Trends</h2>", unsafe_allow_html=True)
trend_data = pd.DataFrame({
    'Location': ["BTM", "Indiranagar", "Koramangala", "Whitefield"],
    'Success Rate (%)': [90, 80, 85, 70],
    'Avg Cost (₹)': [1200, 1500, 1300, 1100]
})

trend_chart = alt.Chart(trend_data).mark_bar().encode(
    x="Location",
    y="Success Rate (%)",
    color="Location"
).properties(title="📊 Success Rate Across Locations")

st.altair_chart(trend_chart, use_container_width=True)
