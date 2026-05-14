import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

st.set_page_config(page_title="🚗 Car Price Predictor", page_icon="🚗")

st.title("🚗 Car Price Predictor")
st.markdown("Fill details of car, we'll predict the price!")

year = st.number_input("Year of car", min_value=2000, max_value=2024, value=2019)
km = st.number_input("KMs Driven", min_value=0, max_value=500000, value=30000)
fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

fuel_map = {"Petrol": 0, "Diesel": 1, "CNG": 2}
seller_map = {"Dealer": 0, "Individual": 1}
trans_map = {"Manual": 0, "Automatic": 1}

if st.button("Predict Price 🚀"):
    age = 2024 - year
    f = fuel_map[fuel]
    s = seller_map[seller]
    t = trans_map[transmission]
    
    # Simple formula-based estimate
    base = 800000
    price = base - (age * 40000) - (km * 0.8) + (f * 20000) + (t * 50000)
    price = max(price, 50000)
    
    st.success(f"💰 Estimated Price: ₹{price:,.0f}")
    st.balloons()
