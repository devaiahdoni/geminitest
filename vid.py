import PIL.Image
import os

#import markdown

import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

google_api_key = os.environ["GOOGLE_API_KEY"]
print (f"using api key {google_api_key}")


genai.configure(api_key=google_api_key)


# Upload the video and print a confirmation.
video_file_name = "SampleVideo.mp4"

print(f"Uploading file...")
video_file = genai.upload_file(path=video_file_name)
print(f"Completed upload: {video_file.uri}")


import time

# Check whether the file is ready to be used.
while video_file.state.name == "PROCESSING":
    print('.', end='')
    time.sleep(10)
    video_file = genai.get_file(video_file.name)

if video_file.state.name == "FAILED":
  raise ValueError(video_file.state.name)

# Create the prompt.
prompt = "Summarize this video. Then create a quiz with answer key based on the information in the video."

# Choose a Gemini model.
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# Make the LLM request.
print("Making LLM inference request...")
response = model.generate_content([video_file, prompt],
                                  request_options={"timeout": 600})

# Print the response, rendering any Markdown
print(response.text)


# Create the prompt.
prompt = "Transcribe the audio from this video, giving timestamps for salient events in the video. Also provide visual descriptions."

# Choose a Gemini model.
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# Make the LLM request.
print("Making LLM inference request...")
response = model.generate_content([video_file, prompt],
                                  request_options={"timeout": 600})
print(response.text)


import google.generativeai as genai

print("My files:")
for f in genai.list_files():
    print("  ", f.name)
    
#import google.generativeai as genai

#myfile = genai.upload_file( "poem.txt")

#myfile.delete()

# try:
#     # Error.
#     model = genai.GenerativeModel("gemini-1.5-flash")
#     result = model.generate_content([myfile, "Describe this file."])
# except google.api_core.exceptions.PermissionDenied:
#     pass   