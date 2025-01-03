import google.generativeai as genai

import os

from dotenv import load_dotenv
load_dotenv()

google_api_key = os.environ["GOOGLE_API_KEY"]
print (f"using api key {google_api_key}")


genai.configure(api_key=google_api_key)

model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]
)
response = chat.send_message("I have 2 dogs in my house.")
print(response.text)
response = chat.send_message("How many paws are in my house?")
print(response.text)