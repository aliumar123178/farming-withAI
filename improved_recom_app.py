import streamlit as st
from improved_model import generate_storage_advice
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

st.set_page_config(page_title="Crop Storage Intelligence System", page_icon="🌱")

st.title("🌱 Crop Storage Intelligence System")
st.subheader("Optimized Preservation Strategies for Agricultural Products")

crop_name = st.text_input("Enter Crop Name:", placeholder="e.g., Wheat, Rice, Potatoes...")

if st.button("Get Storage Advice"):
    if not crop_name:
        st.warning("Please enter a crop name.")
    else:
        advice = generate_storage_advice(crop_name)
        st.success(advice)

st.markdown("---")
st.markdown("🔒 Certified Agricultural Storage Advisory | v2.1.0")
