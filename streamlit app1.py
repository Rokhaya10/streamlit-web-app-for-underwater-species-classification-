#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Streamlit 
import cv2
import torch
import tempfile
import streamlit as st

# Load Model YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def main():
    # App title in the Dashboard
    st.title("Underwater Species Classification")

    # Sidebar title
    st.sidebar.title("Setting")
    # Customize sidebar with width of 400px
    st.markdown(
        """
            <style>
                [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{width:400px;}
                [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{width:400px; margin-left:-400px;}
            </style>
        """,
        unsafe_allow_html=True
    )

    # Slider to pick the level of confidence
    st.sidebar.markdown("---")
    confidence = st.sidebar.slider("Confidence", min_value=0.0, max_value=1.0, value=0.25)
    st.sidebar.markdown("---")

    save_img = st.sidebar.checkbox("Save Video")
    custom_classes = st.sidebar.checkbox("Use Custom Classes")
    assigned_class_id = []

    # List of available classes (3)
    names = ["Coptodon", "Lyza", "Diplodus"]

    # MultiSelect for more classes to detect among the 3
    if custom_classes:
        assigned_class = st.sidebar.multiselect('Select the custom classes', list(names), default="Coptodon")

        for classe in assigned_class:
            assigned_class_id.append(names.index(classe))

    # Adding a video file uploader
    video_file_buffer = st.sidebar.file_uploader("Upload your video", type=["mp4", "mov", "avi", "asf", "m4v"])
    DEMO_VIDEO = "../test.mp4"
    # 
    tfflie = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False)

    # Read the input file from here
    if not video_file_buffer:
        vid = cv2.VideoCapture(DEMO_VIDEO)
        tfflie.name = DEMO_VIDEO
        dem_vid = open(tfflie.name, 'rb')
        demo_byte = dem_vid.read()

        st.sidebar.text("Input Video")
        st.sidebar.video(demo_byte)
    else:
        tfflie.write(video_file_buffer.read())
        dem_vid = open(tfflie.name, 'rb')
        demo_byte = dem_vid.read()

        st.sidebar.text("Input Video")
        st.sidebar.video(demo_byte)

    stframe = st.empty()
    st.sidebar.markdown("---")

    # Set up 3 columns
    col_1, col_2, col_3 = st.columns(3)

    with col_1:
        st.markdown("**Frame Rate**")
        col_1_text = st.markdown("0.0")

    with col_2:
        st.markdown("**Tracked Object**")
        col_2_text = st.markdown("0")

    with col_3:
        st.markdown("**Width**")
        col_3_text = st.markdown("0")





if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass 

