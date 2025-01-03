import google.generativeai as genai
import os
from dotenv import load_dotenv()
load_dotenv()

google_api_key = os.environ["GOOGLE_API_KEY"]

#genai.configure(api_key="AIzaSyD6YPlN6hwPMvxD3naRYdw3FItpEGC0vsw")
genai.configure(api_key=google_api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)