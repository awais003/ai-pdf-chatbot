
# AI PDF Chatbot with Python & FastAPI

A beginner-friendly AI application that allows users
to upload PDF documents and ask questions about
their content using Google's Gemini AI.

## Features

- Upload PDF documents
- Extract text using PyMuPDF
- Ask questions about uploaded documents
- Generate answers using Gemini AI
- Interactive API documentation with FastAPI

## Technologies

- Python
- FastAPI
- Google Gemini API
- PyMuPDF
- Uvicorn

## Project Structure

ai-pdf-chatbot/
├── main.py
├── pdf_processor.py
├── ai_service.py
├── requirements.txt
├── .env.example
└── README.md

## Installation

### 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/ai-pdf-chatbot.git

cd ai-pdf-chatbot

### 2. Create a virtual environment

python -m venv .venv

### 3. Activate the environment

Windows:

.venv\Scripts\activate

Linux / macOS:

source .venv/bin/activate

### 4. Install dependencies

pip install -r requirements.txt

### 5. Configure environment variables

Create a `.env` file and add your Gemini API key:

GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-3.1-flash-lite

Get your API key:
https://aistudio.google.com/apikey

### 6. Run the application

uvicorn main:app --reload

### 7. Open API documentation

http://127.0.0.1:8000/docs

## How to Use

1. Open the FastAPI documentation.
2. Find the POST /upload endpoint.
3. Upload a PDF document.
4. Copy the returned document_id.
5. Open the POST /ask endpoint.
6. Enter the document_id and your question.
7. Execute the request to receive an AI-generated answer.

## Limitations

- Documents are stored temporarily in memory.
- Uploaded documents are lost when the server restarts.
- Scanned PDFs without selectable text are not supported.
- Large PDFs may exceed the model's context limits.
- This is a learning project, not a production-ready service.

## License

MIT License
