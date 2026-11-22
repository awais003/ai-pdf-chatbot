from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel

from pdf_processor import extract_text
from ai_service import ask_gemini

app = FastAPI(title="AI PDF Chatbot")

documents = {}

class Question(BaseModel):
    document_id: str
    question: str

@app.post("/upload")
def upload_pdf(file: UploadFile = File(...)):
    # check uploaded file type
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(400, "Please upload PDF File")

    try:
        # extract pdf text
        pdf_bytes = file.file.read()
        text = extract_text(pdf_bytes)

        # generate a document ID
        document_id = str(len(documents) + 1)
        documents[document_id] = text

        return {
            "message": "PDF uploaded successfully",
            "document_id": document_id
        }

    except ValueError as e:
        raise HTTPException(400, str(e))

@app.post("/ask")
def ask_question(data: Question):
    # check weather the document exists
    document = documents.get(data.document_id)

    if not document:
        raise HTTPException(404, "Document not found")

    try:
        answer = ask_gemini(document, data.question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(500, f"AI request failed: {str(e)}")
