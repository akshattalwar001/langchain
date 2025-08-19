import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
import os
os.environ['HF_HOME']= 'D:/huggingface_cache'

llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)
model = ChatHuggingFace(llm=llm)
json_schema = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "description": "List of key themes discussed in the review",
      "items": {"type": "string"}
    },
    "pros": {
      "type": "array",
      "description": "All positive aspects of product",
      "items": {"type": "string"}
    },
    "cons": {
      "type": "array",
      "description": "All negative aspects of product",
      "items": {"type": "string"}
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["positive", "negative", "neutral"],
      "description": "Sentiment of the review"
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}

# Force Gemini to always return valid structured JSON using function_calling
structured_model = model.with_structured_output(json_schema)

# Input review text
review_text = """
I recently purchased the XPhone Pro Max, and while the hardware is outstanding,
the software leaves much to be desired. The build quality feels premium, the 
display is bright and vivid, and the battery easily lasts a full day even with 
heavy use. However, the pre-installed apps take up unnecessary space, and many 
cannot be uninstalled, which is frustrating. The user interface feels outdated 
compared to competitors like OnePlus and Samsung, with clunky animations and 
inconsistent icon designs. On the bright side, the camera delivers excellent 
photos in daylight and decent low-light performance. I really hope the company 
pushes a major software update to modernize the experience.
"""

# Ask the model for structured output
result = structured_model.invoke(f"""
You must return valid JSON that exactly matches this schema:
- key_themes: list of strings
- pros: list of strings
- cons: list of strings
- summary: string
- sentiment: one of ["positive", "negative", "neutral"]

Review:
{review_text}
""") or {}

# Print results
print("\n✅ Structured output received:")
print(result)