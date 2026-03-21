import streamlit as st
import cv2
import numpy as np
from detection import detect_frame

# Must be the first Streamlit command
st.set_page_config(page_title="VisionTrack Analytics", page_icon="�", layout="wide", initial_sidebar_state="expanded")

def load_css():
    try:
        with open("assets/style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass

load_css()

# Sidebar - Controls
with st.sidebar:
    st.markdown("<h2 class='sidebar-title'>⚙️ Controls</h2>", unsafe_allow_html=True)
    
    # Input Selection
    mode = st.radio("Select Input Method", [ "Upload Image", "Use Webcam"], index=0)
    
    st.markdown("<hr class='sidebar-divider'>", unsafe_allow_html=True)
    
    if mode == "Upload Image":
        st.markdown("<p class='sidebar-label'>Upload an Image</p>", unsafe_allow_html=True)
        file = st.file_uploader("", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
    else:
        st.markdown("<p class='sidebar-label'>Webcam Controls</p>", unsafe_allow_html=True)
        start = st.button("▶️ Start Webcam", use_container_width=True)
        stop = st.button("⏹️ Stop Webcam", use_container_width=True)

# Main Area
st.markdown("""
<div class='dashboard-header'>
    <h1>🚦 VisionTrack Analytics</h1>
    <p class='subtitle'>Your AI-powered lens on urban mobility</p>
</div>
""", unsafe_allow_html=True)

# State for webcam
if "webcam_active" not in st.session_state:
    st.session_state.webcam_active = False

# IMAGE MODE
if mode == "Upload Image":
    if file:
        bytes_data = file.read()
        np_arr = np.frombuffer(bytes_data, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        with st.spinner("Analyzing image..."):
            result_img, counts = detect_frame(img)
        
        # Display image centered
        st.image(result_img, channels="BGR", use_container_width=True)

        # Metrics layout
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown(f"""
            <div class='metric-container'>
                <div class='metric-icon'>👤</div>
                <div class='metric-label'>People</div>
                <div class='metric-value'>{counts['people']}</div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class='metric-container'>
                <div class='metric-icon'>🚗</div>
                <div class='metric-label'>Vehicles</div>
                <div class='metric-value'>{counts['vehicles']}</div>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <div class='metric-container'>
                <div class='metric-icon'>🐾</div>
                <div class='metric-label'>Animals</div>
                <div class='metric-value'>{counts['animals']}</div>
            </div>
            """, unsafe_allow_html=True)
        with col4:
            st.markdown(f"""
            <div class='metric-container'>
                <div class='metric-icon'>🚦</div>
                <div class='metric-label'>Street Objects</div>
                <div class='metric-value'>{counts['street_objects']}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("📁 Please upload an image to start detection.")

# WEBCAM MODE
elif mode == "Use Webcam":
    if start:
        st.session_state.webcam_active = True
    if stop:
        st.session_state.webcam_active = False

    if st.session_state.webcam_active:
        cap = cv2.VideoCapture(0)
        
        frame_placeholder = st.empty()
        
        col1, col2, col3, col4 = st.columns(4)
        people_placeholder = col1.empty()
        vehicle_placeholder = col2.empty()
        animal_placeholder = col3.empty()
        street_placeholder = col4.empty()

        while st.session_state.webcam_active:
            ret, frame = cap.read()
            if not ret:
                st.error("Failed to access webcam.")
                st.session_state.webcam_active = False
                break

            result_img, counts = detect_frame(frame)
            frame_placeholder.image(result_img, channels="BGR", use_container_width=True)

            people_placeholder.markdown(f"""
            <div class='metric-container'>
                <div class='metric-icon'>👤</div>
                <div class='metric-label'>People</div>
                <div class='metric-value'>{counts['people']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            vehicle_placeholder.markdown(f"""
            <div class='metric-container'>
                <div class='metric-icon'>🚗</div>
                <div class='metric-label'>Vehicles</div>
                <div class='metric-value'>{counts['vehicles']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            animal_placeholder.markdown(f"""
            <div class='metric-container'>
                <div class='metric-icon'>🐾</div>
                <div class='metric-label'>Animals</div>
                <div class='metric-value'>{counts['animals']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            street_placeholder.markdown(f"""
            <div class='metric-container'>
                <div class='metric-icon'>🚦</div>
                <div class='metric-label'>Street Objects</div>
                <div class='metric-value'>{counts['street_objects']}</div>
            </div>
            """, unsafe_allow_html=True)

        cap.release()
    else:
        st.info("📷 Click 'Start Webcam' in the sidebar to begin live tracking.")
        # Empty state metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown("""
            <div class='metric-container'>
                <div class='metric-icon'>👤</div>
                <div class='metric-label'>People</div>
                <div class='metric-value'>0</div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class='metric-container'>
                <div class='metric-icon'>🚗</div>
                <div class='metric-label'>Vehicles</div>
                <div class='metric-value'>0</div>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div class='metric-container'>
                <div class='metric-icon'>🐾</div>
                <div class='metric-label'>Animals</div>
                <div class='metric-value'>0</div>
            </div>
            """, unsafe_allow_html=True)
        with col4:
            st.markdown("""
            <div class='metric-container'>
                <div class='metric-icon'>🚦</div>
                <div class='metric-label'>Street Objects</div>
                <div class='metric-value'>0</div>
            </div>
            """, unsafe_allow_html=True)

# Shared Footer
st.markdown("""
<div class='custom-footer'>
    © 2026 VisionTrack Analytics
</div>
""", unsafe_allow_html=True)
