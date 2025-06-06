from fastapi import FastAPI, UploadFile, File
import pytesseract
from PIL import Image
import io

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Wasserstoff!"}

@app.post("/ocr")
async def extract_text(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))
        text = pytesseract.image_to_string(image)
        return {"extracted_text": text}
    except Exception as e:
        return {"error": str(e)}
