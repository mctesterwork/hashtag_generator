import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=API_KEY)

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["You are a content creator and need hashtags that are related to the following topic \"software\". Make sure you use the best hashtags based on market analysis and current trends in that topic. The hashtags selected should not include any specific brand or platform name. AVOID INCLUDING ANY OTHER INFORMATION OR STATEMENT THAT IS NOT THE HASHTAGS. Stick to displaying the hashtags only."]
  },
  {
    "role": "model",
    "parts": ["#softwaredevelopment\n#programming\n#coding\n#softwareengineering\n#software\n#devops\n#softwarearchitecture\n#softwarequalityassurance\n#softwareproductmanagement\n#softwaresecurity"]
  },
])

def getHashtags(numOfHashtags=10, topic="software"):
    convo.send_message(f"Use exact same instructions as last prompt, but now display {numOfHashtags} hashtags for topic {topic}")
    return convo.last.text