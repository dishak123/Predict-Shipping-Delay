import streamlit as st
import numpy as np
import pickle
import time

# ✅ Load Model
model_path = "predictshipping.pkl"
try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("❌ Model file not found!")
    st.stop()

# ✅ Themed UI Styling
st.set_page_config(page_title="Shipping Delay Predictor", page_icon="📦", layout="wide")
st.markdown("""
    <style>
    body {background-color: #f0f9ff; color: #2c3e50; font-family: 'Poppins', sans-serif;}
    .stButton>button {background-color: #007bff; color: white; border-radius: 20px; font-size: 18px; padding: 10px 22px;}
    .title {font-size: 48px; font-weight: bold; color: #0077b6; text-align: center;}
    .subtitle {font-size: 22px; color: #023e8a; text-align: center; font-style: italic;}
    .about-section {padding: 15px; background-color: #dff6ff; border-radius: 15px; border-left: 5px solid #00b4d8; margin-bottom: 20px;}
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='title'>📦 Shipping Delay Predictor</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>🚚 Estimate shipping delays using ML predictions</div>", unsafe_allow_html=True)

with st.sidebar:
    st.header("📦 About the App")
    st.write("This app helps logistics and e-commerce teams predict delivery delays based on shipment features.")
    st.write("Built with machine learning and a focus on user-friendly experience.")
    st.header("💡 Tips")
    st.write("✔ Accurate inputs lead to better predictions.")
    st.write("✔ Use this tool for planning and optimization.")

# ✅ Input Fields
Product_Category = st.selectbox("📚 Product Category", [0, 1, 2, 3, 4], format_func=lambda x: ["Books", "Clothing", "Electronics", "Furniture", "Toys"][x])
Product_Weight = st.number_input("⚖ Product Weight (kg)", min_value=0.1, format="%.2f")
Shipping_Method = st.selectbox("🚚 Shipping Method", [0, 1, 2], format_func=lambda x: ["Express", "Overnight", "Standard"][x])
Distance = st.number_input("📍 Distance (km)", min_value=1)
Number_of_Items_in_Shipment = st.number_input("📦 Items in Shipment", min_value=1, step=1)
Mode_of_shipping = st.selectbox("🛫 Mode of Shipping", [0, 1, 2], format_func=lambda x: ["Air", "Ground", "Sea"][x])
Origin_City = st.selectbox("🏙 Origin City", [0, 1, 2, 3, 4], format_func=lambda x: ["Chicago", "Houston", "Los Angeles", "New York", "San Francisco"][x])
Destination_City = st.selectbox("🏙 Destination City", [0, 1, 2, 3, 4], format_func=lambda x: ["Chicago", "Houston", "Los Angeles", "New York", "San Francisco"][x])
Weather_Conditions = st.selectbox("🌦 Weather Conditions", [0, 1, 2, 3, 4], format_func=lambda x: ["Clear", "Fog", "Rain", "Snow", "Storm"][x])
Holiday_Indicator = st.radio("🎉 Is it a Holiday?", [0, 1], format_func=lambda x: ["No", "Yes"][x])
Warehouse_Processing_Time = st.number_input("🏭 Warehouse Processing Time (hrs)", min_value=1, step=1)
Traffic_Conditions = st.selectbox("🚦 Traffic Conditions", [0, 1, 2], format_func=lambda x: ["High", "Low", "Moderate"][x])

# ✅ Prediction Logic
if st.button("📊 Predict Delay"):
    with st.spinner('⏳ Calculating estimated delivery delay...'):
        time.sleep(2)
        input_features = [
            Product_Category, Product_Weight, Shipping_Method, Distance,
            Number_of_Items_in_Shipment, Mode_of_shipping, Origin_City,
            Destination_City, Weather_Conditions, Holiday_Indicator,
            Warehouse_Processing_Time, Traffic_Conditions
        ]
        try:
             prediction = model.predict(np.array(input_features).reshape(1, -1))
             if prediction[0] == 1:
                            st.error("🚨 Shipping Delay Detected: Yes")
                            st.info("📌 Consider notifying customers and adjusting delivery schedules.")
             else:
                            st.success("✅ No Shipping Delay Detected")
                            st.info("📌 Shipping is expected to be on time.")
        except Exception as e:
                st.error(f"❌ Prediction Error: {e}")

st.markdown("---")
