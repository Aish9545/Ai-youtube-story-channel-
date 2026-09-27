import os
from google import genai

api_key = os.environ["GEMINI_API_KEY"]

client = genai.Client(api_key=api_key)

prompt = """
Create one original cinematic YouTube story idea.

Requirements:
- English
- Emotional and suspenseful
- Suitable for a 20–30 minute story
- Completely original
- No copyrighted characters
- Give it a memorable title
- Give a 3–5 sentence plot summary
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)
