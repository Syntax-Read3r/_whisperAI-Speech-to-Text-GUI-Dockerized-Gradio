import gradio as gr
import whisper

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
    inputs=gr.Audio(type="filepath"),  # Removed 'source="upload"'
    outputs="text",
    title="Whisper Speech-to-Text",
    description="Upload an audio file and get its transcription using OpenAI Whisper.",
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7010)
