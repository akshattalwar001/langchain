import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env file
load_dotenv()

# Set API key from environment
api_key = os.getenv("GOOGLE_API_KEY")

# Create model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=api_key)

# First template: detailed report
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

# Second template: summary
template2 = PromptTemplate(
    template="Write a 5 line summary on the following text:\n{text}",
    input_variables=["text"]
)

# Step 1: Generate report
prompt1 = template1.invoke({"topic": "black hole"})
result = model.invoke(prompt1)

# Step 2: Generate summary from report
prompt2 = template2.invoke({"text": result.content})
result1 = model.invoke(prompt2)

print(result1.content)