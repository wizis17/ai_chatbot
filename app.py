import gradio as gr
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env file

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash')  # or 'gemini-pro-vision' for images

conversation_history = []  # to store the chat history

def chat(message, image, history):
    parts = []
    if message:
        parts.append({"text": message})
    if image is not None:
        with open(image.name, "rb") as f:
            image_bytes = f.read()
        parts.append({
            "inline_data": {
                "mime_type": "image/png",
                "data": image_bytes
            }
        })
    conversation_history.append({"role": "user", "parts": parts})

    try:
        response = model.generate_content(conversation_history)
        conversation_history.append({"role": "model", "parts": [{"text": response.text}]})
        return response.text
    except Exception as e:
        return "Error: " + str(e)

with gr.Blocks() as demo:
    gr.Markdown(
        """
        <style>
        .icon-upload .wrap {
            min-width: 28px !important;
            max-width: 28px !important;
            min-height: 28px !important;
            max-height: 28px !important;
            padding: 0 !important;
        }
        .icon-upload .file-preview {
            display: none !important;
        }
        .icon-upload label {
            width: 28px !important;
            height: 28px !important;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            background: #f3f4f6;
            cursor: pointer;
            font-size: 1.1em;
            border: 1px solid #e0e0e0;
        }
        </style>
        """
    )
    gr.Markdown(
        "<h1 style='text-align:center; font-family:sans-serif;'>AI Chatbot</h1>"
    )
    chatbot = gr.Chatbot(label="Chatbot", type="messages")
    with gr.Row():
        txt = gr.Textbox(placeholder="Type a message", show_label=False, scale=8)
        img = gr.File(label="📎", file_types=["image"], file_count="single", elem_classes=["icon-upload"], scale=1)
        send = gr.Button("Send", scale=2)

    history = gr.State([])

    def respond(message, image, history):
        response = chat(message, image, history)
        history = history or []
        # Append user message and bot response as dicts
        history = history + [
            {"role": "user", "content": message},
            {"role": "assistant", "content": response}
        ]
        return history, "", None

    # Use gr.Examples with run_on_click=True to auto-send example messages
    gr.Examples(
        examples=[
            ["Heyyy!", None],
            ["What is python?", None],
            ["What is the weather in Tokyo?", None]
        ],
        inputs=[txt, img],
        outputs=[chatbot, txt, img],
        fn=respond,
        cache_examples=False,
        run_on_click=True,
        label="Examples"
    )

    send.click(respond, [txt, img, history], [chatbot, txt, img])
    txt.submit(respond, [txt, img, history], [chatbot, txt, img])

demo.launch()