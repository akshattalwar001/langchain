import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

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
parser = StrOutputParser()
chain = template1 | model | parser | template2 | model | parser
result=chain.invoke({"topic":"black hole"})
print(result)