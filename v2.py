import httpx
import os
import base64
import google.generativeai as genai

import os

from dotenv import load_dotenv
load_dotenv()

google_api_key = os.environ["GOOGLE_API_KEY"]
print (f"using api key {google_api_key}")


genai.configure(api_key=google_api_key)



model = genai.GenerativeModel(model_name = "gemini-1.5-pro")
image_path_1 = "20220508_140124.jpg"  # Replace with the actual path to your first image
image_path_2 = "car1.jpg" # Replace with the actual path to your second image

image_1 = httpx.get(image_path_1)
image_2 = httpx.get(image_path_2)

prompt = "Generate a list of all the objects contained in both images."

response = model.generate_content([
{'mime_type':'image/jpeg', 'data': base64.b64encode(image_1.content).decode('utf-8')},
{'mime_type':'image/jpeg', 'data': base64.b64encode(image_2.content).decode('utf-8')}, prompt])

print(response.text)