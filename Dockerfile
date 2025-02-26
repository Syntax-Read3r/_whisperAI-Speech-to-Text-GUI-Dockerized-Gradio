# Use an official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Clean up previous failed installs and clear cache
RUN apt update && apt install -y ffmpeg && rm -rf /var/lib/apt/lists/* && \
    pip cache purge && rm -rf /root/.cache/pip

# Install PyTorch separately from the PyTorch index
RUN pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Install Whisper and other dependencies from PyPI
RUN pip install --no-cache-dir openai-whisper gradio ffmpeg-python

# Copy application files
COPY . .

# Expose the Gradio port
EXPOSE 7010  

# Run the app
CMD ["python", "app.py"]
