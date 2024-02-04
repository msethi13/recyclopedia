import os
import wandb
from openai import OpenAI

def index():
    return "Hello, World!"

def getDataFromGPT():
    client = OpenAI(api_key="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")
    # Upload a file with an "assistants" purpose
    file_path = os.path.join(os.path.dirname(__file__), "can.png")
    file = client.files.create(
        file = open(file_path, "rb"),
        # file=open("can.png", "rb"),
        purpose='assistants'
    )

    # Add the file to the assistant
    assistant = client.beta.assistants.create(
        instructions="You are a recycling expert who can suggest ways to recylce, reuse, and reduce the product in the image",
        model="gpt-4-turbo-preview",
        tools=[{"type": "retrieval"}],
        file_ids=[file.id]
    )

    thread = client.beta.threads.create()

    client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content="Identify the image and suggest ways for the user to either recycle, reuse or reduce it in a step-by-step format.")

    run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant.id
        )

    while True:
        run_status = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

        if run_status.status == 'completed':
            messages = client.beta.threads.messages.list(thread_id=thread.id)
            break


    message_content = [message.content[0].text.value for message in messages.data if message.role == "assistant"]
    print(message_content)


