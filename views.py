import os
import wandb
from openai import OpenAI
# import cv2
# import matplotlib.image as mpimg
import base64
from pathlib import Path
def index():
    return "Hello, World!"

# def encode_image(image_path):
#   with open(image_path, "rb") as image_file:
#     return base64.b64encode(image_file.read()).decode('utf-8')

# def getDataFromGPT():
#     client = OpenAI(api_key="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")
#     # Upload a file with an "assistants" purpose
#     file_path = os.path.join(os.path.dirname(__file__), "IMG_3336.jpeg")
#     file = client.files.create(
#         # file=open("can.png", "rb"),
#         # file = mpimg.imread(file_path),
#         file = Path(file_path),
#         # file = encode_image("IMG_3336.jpeg"),
#         purpose='assistants'
#     )

#     # Add the file to the assistant
#     assistant = client.beta.assistants.create(
#         instructions="You are a recycling expert who can suggest ways to recylce, reuse, and reduce the product in the image",
#         model="gpt-4-0125-preview",
#         tools=[{"type": "retrieval"}],
#         file_ids=[file.id]
#     )

#     thread = client.beta.threads.create()

#     client.beta.threads.messages.create(
#             thread_id=thread.id,
#             role="user",
#             content="Identify the image and suggest ways for the user to recycle.")

#     run = client.beta.threads.runs.create(
#             thread_id=thread.id,
#             assistant_id=assistant.id
#         )

#     while True:
#         run_status = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

#         if run_status.status == 'completed':
#             messages = client.beta.threads.messages.list(thread_id=thread.id)
#             break


#     message_content = [message.content[0].text.value for message in messages.data if message.role == "assistant"]
#     print(message_content)


import base64
import requests

def getDataFromGPT():
    # OpenAI API Key
    api_key = "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"

    # Function to encode the image
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    # Path to your image
    image_path = "IMG_3338.jpeg"

    # Getting the base64 string
    base64_image = encode_image(image_path)

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }

    payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "Identify the image and suggest ways for the user to recycle"
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            }
        ]
        }
    ],
    "max_tokens": 1000
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    return response.json()['choices'][0]['message']['content']

