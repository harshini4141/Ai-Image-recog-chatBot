# Q&A Chatbot
#from langchain.llms import OpenAI

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image

import google.generativeai as genai

# Configure Google Generative AI
genai.configure(api_key="AIzaSyCs-HIBoYQaBMH4OXkmpIdXFVEOxtADNZI")

## Function to load OpenAI model and get respones
def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-1.5-flash')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Conversational Image Recognition chatbot")

st.header("Conversational Image Recognition chatbot")

input="You are an AI-powered image captioning assistant. Your task is to generate accurate, context-aware, and descriptive captions for the given image. Ensure that the caption:1. Clearly describes the main subject, objects, and background. 2. Includes relevant details about colors, shapes, or textures. 3. Captures the action or event in the image (if applicable). 4. Is concise yet informative, ideally under 20 words. 5. Uses natural and grammatically correct language.Now, analyze the provided image and generate a caption."

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Generate Caption")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)
