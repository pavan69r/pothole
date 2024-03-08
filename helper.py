import ultralytics
from ultralytics import YOLO
import streamlit as st
import cv2
import supervision
import pickle
import pandas as pd
import numpy as np

import settings

def load_model(model_path):
    model = YOLO(model_path)
    return model

def _display_detected_frames(conf, model, st_frame, image, is_display_tracking=None, tracker=None):
    image = cv2.resize(image, (720, int(720*(9/16))))
    results = model.predict(image, conf=conf)
    annotated_frame = results[0].plot()
    st_frame.image(annotated_frame,
    caption='Detected Video',
    channels="BGR",
    use_column_width=True
)

def play_video(src, conf, model):
    if src == 'Stream':
        source_vid = st.sidebar.selectbox("Port: ",
                                  [1, 0])
    else:
        source_vid = st.sidebar.selectbox(
            "Choose a video...", settings.VIDEOS_DICT.keys())
        source_vid = str(settings.VIDEOS_DICT.get(source_vid))
    if st.sidebar.button('Detect Video Objects'):
        try:
            vid_cap = cv2.VideoCapture(source_vid)
            st_frame = st.empty()
            while (vid_cap.isOpened()):
                success, image = vid_cap.read()
                if success:
                    LoD = _display_detected_frames(conf,
                                             model,
                                             st_frame,
                                             image,
                                             )
                    print(LoD)
                else:
                    vid_cap.release()
                    break
        except Exception as e:
            st.sidebar.error("Error loading video: " + str(e))