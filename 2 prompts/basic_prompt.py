import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
import os
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

st.header('Research Tool')

user_input = st.text_input('Enter your prompt')

if st.button('Submit'):
    result = model.generate_content(user_input)
    st.write(result.text)