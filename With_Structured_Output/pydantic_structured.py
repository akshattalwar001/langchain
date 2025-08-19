from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from typing import TypedDict, Optional
from typing_extensions import Annotated, Literal  # <-- Use typing_extensions
from pydantic import BaseModel, Field

# Load environment variables from .env file
load_dotenv()

# Set API key from environment
api_key = os.getenv("GOOGLE_API_KEY")

# Create model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=api_key)

class Review(BaseModel):
    key_themes: list[str] = Field(description="List of key themes discussed in the review")
    pros: Optional[list[str]] = Field(default=None, description="All positive aspects of product")
    cons: Optional[list[str]] = Field(default=None, description="All negative aspects of product")
    summary: list[str] = Field(description= "A brief summary of review")
    sentiment: Literal['positive', 'negative', 'neutral'] = Field(description="Sentiment of the review")

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