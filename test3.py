import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()

google_api_key = os.environ["GOOGLE_API_KEY"]
print (f"using api key {google_api_key}")


genai.configure(api_key=google_api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.", stream=True)
chunkcount =1
for chunk in response:
    print(chunk.text)
    print("_" * 80)
    print (f"chunk count {chunkcount}")
    chunkcount = chunkcount +1 