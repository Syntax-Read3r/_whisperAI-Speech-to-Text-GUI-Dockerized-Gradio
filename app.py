import sys
import os

# Add local whisper directory to Python path
LOCAL_WHISPER_PATH = os.path.join(os.path.dirname(__file__), "whisper")
sys.path.append(LOCAL_WHISPER_PATH)

import whisper
import gradio as gr

# Load Whisper model (adjust model size if needed)
model = whisper.load_model("small")

def transcribe_audio(audio_file):
    if not audio_file:
        return "Please upload an audio file."
    
    print(f"Processing file: {audio_file}")
    result = model.transcribe(audio_file)
    return result["text"]

# Create Gradio UI
iface = gr.Interface(
    fn=transcribe_audio,
    inputs=gr.Audio(type="filepath"),
    outputs="text",
    title="Whisper Speech-to-Text",
    description="Upload an audio file and get its transcription using OpenAI Whisper (local clone).",
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7010)
