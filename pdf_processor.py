import fitz

def extract_text(pdf_file):
    # open the PDF direclty from uploaded bytes
    document = fitz.open(stream=pdf_file, filetype="pdf")

    text = ""

    # Extract text from every page
    for page in document:
        text += page.get_text()

    document.close()

    if not text.strip():
        raise ValueError("No readable text found in PDF")

    return text