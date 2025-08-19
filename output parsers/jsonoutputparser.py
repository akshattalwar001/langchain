import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser

# Load environment variables from .env file
load_dotenv()

# Set API key from environment
api_key = os.getenv("GOOGLE_API_KEY")

# Create model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=api_key)
parser=JsonOutputParser()
template = PromptTemplate(
    template="Give me the name, age and city of a fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={"format_instruction":parser.get_format_instructions()}
)
chain = template | model | parser
result=chain.invoke({})
print(result)
print(type(result))