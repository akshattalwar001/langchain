import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
import os
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

st.header('Gemini Chatbot')
chat_history = []
while True:
    user_input = input('You:')
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result = model.generate_content(chat_history)
    chat_history.append(result.text)
    print("AI:",result.text)
print(chat_history)