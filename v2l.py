import PIL.Image
import os

import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

google_api_key = os.environ["GOOGLE_API_KEY"]
print (f"using api key {google_api_key}")


genai.configure(api_key=google_api_key)


image_path_1 = "path/to/your/image1.jpeg"  # Replace with the actual path to your first image
image_path_2 = "path/to/your/image2.jpeg" # Replace with the actual path to your second image
image_path_1 = "20220508_140124.jpg"  # Replace with the actual path to your first image
image_path_2 = "car1.jpg" # Replace with the actual path to your second image
image_path_2 = "20221225_142044.jpg" # Replace with the actual path to your second image
sample_file_1 = PIL.Image.open(image_path_1)
sample_file_2 = PIL.Image.open(image_path_2)

#Choose a Gemini model.
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

prompt = "Write an advertising jingle based on the items in both images."
prompt = "Return a bounding box for each of the objects in this image in [ymin, xmin, ymax, xmax] format."

response = model.generate_content([prompt, sample_file_1, sample_file_2])

print(response.text)