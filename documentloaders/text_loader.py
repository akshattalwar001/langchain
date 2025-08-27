from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
loader = TextLoader("D:\Games\langchain\documentloaders\characters_aot_300_lines.txt", encoding="utf-8")
docs=loader.load()

print(docs[0])