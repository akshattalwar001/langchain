import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
import os
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

st.header('Research Tool')

paper_input = st.selectbox("Select Reaserch Paper Name", ["Attention is all you need","BERT:Pre-training of Bidirectional Transformers",
                                                          "GPT-3: Language models are few-shot Learners",
                                                          "Diffusion Models Best GANs on Image synthesis"])
style_input = st.selectbox("Select Explnation Style" ,["Beginner-Friendly",
                                                       "Technical",
                                                       "Code-Oriented",
                                                       "Mathematical"])
length_input = st.selectbox("Select Explanation Length", ["Short (1-2 Paragraphs)",
                                                          "Medium (3-5 paragraphs)",
                                                          "Long(detailed explanation)"])

prompt = f"""
You are an AI assistant that explains research papers.

Paper Title: "{paper_input}"
Explanation Style: {style_input}
Explanation Length: {length_input}

Please provide the explanation accordingly.
"""

if st.button('Submit'):
    result = model.generate_content(prompt)
    st.subheader("Explanation:")
    st.write(result.text)