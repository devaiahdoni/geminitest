import httpx
import os
import base64
import google.generativeai as genai


from dotenv import load_dotenv
load_dotenv()

google_api_key = os.environ["GOOGLE_API_KEY"]
print (f"using api key {google_api_key}")


genai.configure(api_key=google_api_key)


model = genai.GenerativeModel(model_name = "gemini-1.5-pro")
image_path = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Palace_of_Westminster_from_the_dome_on_Methodist_Central_Hall.jpg/2560px-Palace_of_Westminster_from_the_dome_on_Methodist_Central_Hall.jpg"

image = httpx.get(image_path)

prompt = "Caption this image."
prompt = "describe this image in detail and give me a detailed caption for it."
response = model.generate_content([{'mime_type':'image/jpeg', 'data': base64.b64encode(image.content).decode('utf-8')}, prompt])
print("_" * 80)
print(response.text)