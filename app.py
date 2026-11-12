import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Set up the page
st.set_page_config(page_title="Kineva - Giga Girls", page_icon="🏃‍♀️")
st.title("🏃‍♀️ Kineva: Biomechanics Analyzer")
st.write("**Team Giga Girls (HerHack)** - Detecting ACL injury risks in female athletes.")

# Upload button
uploaded_file = st.file_uploader("Upload a photo of a squat or jump landing...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.subheader("Original Image")
    st.image(image, use_container_width=True)

    st.write("⚙️ AI analyzing biomechanics...")

    # Process image for OpenCV
    image_np = np.array(image.convert('RGB'))
    h, w, c = image_np.shape
    
    # MVP DEMO: Draw a simulated "Biomechanical Tracking Grid" over the legs
    cv2.rectangle(image_np, (int(w*0.25), int(h*0.45)), (int(w*0.75), int(h*0.95)), (0, 255, 0), 4) # Target zone
    cv2.line(image_np, (int(w*0.5), int(h*0.45)), (int(w*0.5), int(h*0.95)), (255, 0, 0), 2) # Vertical axis
    cv2.line(image_np, (int(w*0.25), int(h*0.7)), (int(w*0.75), int(h*0.7)), (255, 0, 0), 2) # Knee line
    
    # Add data overlay
    cv2.putText(image_np, "VALGUS ANGLE: 19 DEG (RISK)", (int(w*0.28), int(h*0.42)), cv2.FONT_HERSHEY_SIMPLEX, max(0.5, w/1000), (255, 0, 0), 2)

    st.subheader("AI Analysis Result")
    st.image(image_np, use_container_width=True)
    
    # Give a mock result for the MVP demo
    st.error("⚠️ **Risk Detected:** 19-degree knee valgus (inward collapse) detected upon landing.")
    st.success("✅ **Recommendation:** Add single-leg glute bridges and lateral band walks to training routine.")
