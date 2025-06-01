import fitz  # PyMuPDF

def read_txt(file):
    return file.read().decode("utf-8")

def read_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text
