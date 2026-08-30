# AI-Powered Agentic Phishing Detection System

This project is a multi-layered phishing detection system using **Agentic AI**. It orchestrates specialized agents to analyze URLs, page content, and visual branding (Computer Vision).

## Features

- **Coordinator Agent**: Orchestrates the analysis flow.
- **URL Analysis**: De-shortens URLs and extraction of lexical/semantic features.
- **Content Analysis**: LLM-based audit of HTML and text for social engineering.
- **Vision Verification**: Screenshot-based brand detection using Selenium & OpenCV.
- **Explainable AI (XAI)**: Generates human-readable "Security Reasoning Reports."
- **Dashboard**: Real-time monitoring via Streamlit.
- **Extension**: Chrome Manifest V3 extension for one-click scanning.

## Setup Instructions

### 1. Backend (FastAPI)
- Install dependencies: `pip install -r requirements.txt`
- Install Tesseract/OpenCV dependencies if required by your OS.
- Set up environment: Create a `.env` file and add `GOOGLE_API_KEY=your_gemini_key`.
- Run backend: `python backend/main.py`

### 2. Dashboard (Streamlit)
- Run dashboard: `streamlit run frontend/dashboard.py`

### 3. Browser Extension
- Open Chrome and navigate to `chrome://extensions/`
- Enable "Developer mode".
- Click "Load unpacked" and select the `extension/` folder.

### 4. Vision Templates
- Place brand logo images (e.g., `paypal.png`, `google_logo.jpg`) in `backend/templates/` to enable visual branding verification.

## Architecture
- **Orchestration**: Async Coordinator.
- **AI**: Google Gemini (LLM), OpenCV (CV), Scikit-learn (ML).
