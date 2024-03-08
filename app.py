# Python In-built packages
from pathlib import Path

# External packages
import streamlit as st
# Local Modules
import settings
import helper
import ultralytics
import cloudDyn


# Setting page layout
st.set_page_config(
    page_title="OptiPave",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page heading
st.title("OptiPave: Real-time Pothole Detection System")

# Sidebar
st.sidebar.header("ML Model Config")

# Model Options
confidence = float(st.sidebar.slider(
    "Select Model Confidence", 25, 100, 60)) / 100

# Selecting Detection Or Segmentation
model_path = Path(settings.SEGMENTATION_MODEL)

# Load Pre-trained ML Model
try:
    model = helper.load_model(model_path)
except Exception as ex:
    st.error(f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)
st.sidebar.header("Video Config")
source_radio = st.sidebar.radio(
    "Select Source", settings.SOURCES_LIST)
if source_radio:
    helper.play_video(source_radio, confidence, model)

else:
    st.error("Please select a valid source type!")