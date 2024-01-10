import streamlit as st
import pandas as pd
import plotly.express as px



st.set_page_config(
    page_title="Hand Gesture Language",
    page_icon=":bar_chart:",
    layout="wide",
    )
st.title("Hand Gesture Language")
st.subheader("Turning Hand Gesture to Text")
st.markdown("_Prototype v0.0.2_")

# open camera on streamlit
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils

mp_hands = mp.solutions.hands

# For webcam input:
cap = cv2.VideoCapture(0)
# display webcam
stframe = st.empty()

# add inputbox or textbox for result
st.text_area("Result", height=100)


