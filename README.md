
# Ai Chatbot 😎

A conversational AI chatbot built with **Python**, **Gradio**, using **Gemini API**.

---

## Features

- 💬 Chat with an AI assistant
- 🖼️ Upload images for multimodal conversations (if supported by your Gemini API key)
- ⚡ Fast, interactive web interface powered by Gradio
- 🔒 API key managed securely via Hugging Face Spaces secrets

---

## Usage

1. **Clone or Fork this Space**  
   Or create your own Space on [Hugging Face Spaces](https://huggingface.co/spaces).

2. **Set your Gemini API Key**  
   - Go to your Space's **Settings > Secrets**.
   - Add a secret named `GOOGLE_API_KEY` with your Gemini API key as the value.

3. **Run the App**  
   The app will launch automatically on Spaces.  
   If running locally:
   ```bash
   pip install -r requirements.txt
   python app.py
   ```

---

## Configuration

This Space uses:

- **Gradio SDK**: v5.44.1
- **Main file**: `app.py`
- **Python dependencies**: see `requirements.txt`

---

## Reference

- [Gradio Documentation](https://www.gradio.app/docs/)
- [Gemini API Documentation](https://ai.google.dev/)
- [Hugging Face Spaces Config Reference](https://huggingface.co/docs/hub/spaces-config-reference)

---


*Built with ❤️ using Python, Gradio, and Gemini
