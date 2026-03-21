# 👁️ VisionTrack Analytics

![VisionTrack Banner](https://img.shields.io/badge/AI-Computer_Vision-blue?style=for-the-badge&logo=python) ![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi) ![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit) ![YOLOv8](https://img.shields.io/badge/Model-YOLOv8-FF9900?style=for-the-badge)

**Real-Time People & Vehicle Monitoring System powered by AI**

VisionTrack Analytics is a state-of-the-art computer vision application built to detect and track people and vehicles in real time. It is designed to demonstrate advanced AI concepts in an accessible, visually impressive manner. The core engine uses YOLOv8 for rapid object detection, coupled with ByteTrack logic for persistent tracking over video frames. Built for modern use cases like smart cities, retail analytics, and surveillance, it provides an intuitive web interface packed with actionable metrics.

---

## 🌟 Key Features

- **Real-Time Detection:** Employs YOLOv8 to identify persons and vehicles (cars, buses, trucks, bikes) instantly.
- **Dynamic Dashboard:** A modern, stylish Streamlit UI featuring glass-morphic metrics, custom CSS, and a fully responsive layout.
- **Dual Mode Operation:**
  - `📸 Upload Image`: Analyze uploaded images instantly.
  - `🎥 Live Webcam`: Connect directly to your webcam for a real-time object tracking feed.
- **Instant Metrics:** Tracks counts of people and vehicles dynamically via beautiful metric displays.

---

## 🛠️ Technology Stack

1. **Backend & Logic:** `Python`, `FastAPI`, `OpenCV` (for image and video stream processing).
2. **AI / Deep Learning:** `YOLOv8` via Ultalytics (for object detection), Object Tracking concepts.
3. **Frontend Presentation:** `Streamlit` with Custom CSS logic for a dark-themed, glass-morphic, highly polished UI.

---

## 🚀 How It Works (For Interviews)

If you are asked about the pipeline of this project in an interview, here is the breakdown:

1. **Input Stage:** The user selects a mode via the Streamlit interface. If it's a webcam feed, `OpenCV` initializes the hardware camera and starts streaming frames.
2. **Processing (Detection Step):** 
   - Every frame (or uploaded image) is passed to a pre-trained `YOLOv8s` neural network. 
   - YOLOv8 (You Only Look Once version 8) processes the image, generating bounding boxes, object class ids (e.g., class 0 for person), and confidence scores.
3. **Filtering & Tracking:** 
   - We map COCO dataset classes. We filter only the objects of interest: `PERSON_CLASS` (0) and `VEHICLE_CLASSES` (2, 3, 5, 7).
   - By counting the boxes per class, we calculate real-time analytics.
4. **Rendering & Output:** 
   - The annotated frames (bounding boxes drawn over subjects) are rendered directly to the Streamlit frontend. 
   - Counts are updated in real-time in the sidebar/metric cards.

> **💡 Note for your Resume:** Emphasize that you didn't just run a model, but you *integrated* it into a full-stack, real-time application and styled it for end-users, highlighting your skills in UI/UX integration alongside deep learning.

---

## 💻 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/visiontrack-analytics.git
   cd "VisionTrack Analytics"
   ```

2. **Create a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

*(Ensure you have a working webcam connected if you wish to use the Live Webcam feature!)*

---

## 🤝 Contact / Developer

This project was developed as a flagship AI/ML portfolio piece by a passionate M.Sc. Data Science professional, showcasing the bridge between complex neural networks and beautiful user experiences.
