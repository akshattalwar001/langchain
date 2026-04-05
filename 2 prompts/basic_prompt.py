from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

while True:
    user_input = input("Enter your prompt: ")

    if user_input.lower() == "exit":
        break

    result = llm.invoke(user_input)
    print("AI:", result.content)