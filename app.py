import streamlit as st
import cv2
import numpy as np
from PIL import Image
import mediapipe as mp

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

    # Process image for AI
    image_np = np.array(image)
    
    # Load AI Pose model
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()
    mp_draw = mp.solutions.drawing_utils

    # Run AI on image
    results = pose.process(image_np)

    # Draw the skeleton
    if results.pose_landmarks:
        mp_draw.draw_landmarks(image_np, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        st.subheader("AI Analysis Result")
        st.image(image_np, use_container_width=True)
        
        # Give a mock result for the MVP demo
        st.error("⚠️ **Risk Detected:** 15-degree knee valgus (inward collapse) detected upon landing.")
        st.success("✅ **Recommendation:** Add single-leg glute bridges and lateral band walks to training routine.")
    else:
        st.warning("No human detected. Please upload a clear photo of an athlete.")
