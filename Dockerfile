# Use an official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt update && apt install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Install PyTorch separately from the PyTorch index
RUN pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Copy local project files (including local whisper folder)
COPY . .

# Install Python dependencies:
# - specific older Gradio version (3.50.2)
# - ffmpeg-python
# - local Whisper
RUN pip install --no-cache-dir gradio==3.50.2 ffmpeg-python
RUN pip install --no-cache-dir ./whisper

# Expose the Gradio port
EXPOSE 7010

# Run the app
CMD ["python", "app.py"]
