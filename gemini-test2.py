import google.generativeai as genai

import os
import PIL.Image
from dotenv import load_dotenv
load_dotenv()

google_api_key = os.environ["GOOGLE_API_KEY"]
print (f"using api key {google_api_key}")


genai.configure(api_key=google_api_key)


#model = genai.GenerativeModel("gemini-1.5-flash")
#response = model.generate_content("Write a story about a magic backpack.")
#print(response.text)

model = genai.GenerativeModel("gemini-1.5-flash")
organ = PIL.Image.open("20220508_140124.jpg")
organ = PIL.Image.open("car3.webp")
organ = PIL.Image.open("car1.jpg")
response = model.generate_content(["Tell me about this picture", organ])
#organ = PIL.Image.open( "organ.jpg")
#response = model.generate_content(["Tell me about this instrument", organ])

print(response.text)
