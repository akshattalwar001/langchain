from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from typing import TypedDict, Optional
from typing_extensions import Annotated  # <-- Use typing_extensions

# Load environment variables from .env file
load_dotenv()

# Set API key from environment
api_key = os.getenv("GOOGLE_API_KEY")

# Create model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=api_key)

class Review(TypedDict, total=False):
    key_themes: Annotated[list[str], "List of key themes discussed in the review"]
    pros: Annotated[list[str], "Positive aspects of the product"]
    cons: Annotated[list[str], "Negative aspects of the product"]
    summary: Annotated[str, "Brief summary of the review"]
    sentiment: Annotated[str, "Sentiment: positive, negative, or neutral"]

# Force Gemini to always return valid structured JSON using function_calling
structured_model = model.with_structured_output(
    Review,
    method="function_calling"
)

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
print("\nSummary:", result["summary"])
print("Sentiment:", result["sentiment"])