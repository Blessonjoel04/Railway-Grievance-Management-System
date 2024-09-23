# main.py
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from typing import Optional
from OCR import extract_text_from_image, extract_specific_details, generate_content, extract_details_from_response
from imageclassifier import classify
import os

from fastapi import FastAPI

app = FastAPI()

@app.post("/classify-image/")
async def classify_image(file: UploadFile = File(...)):
    try:
        # Save the uploaded image temporarily
        file_location = f"temp/{file.filename}"
        with open(file_location, "wb") as f:
            f.write(file.file.read())

        # Call the image classification function
        response = classify(file_location)
        
        # Clean up the temporary file
        os.remove(file_location)
        
        return JSONResponse(content={"classification": response})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post("/process-image/")
async def process_image(file: UploadFile = File(...)):
    try:
        # Save the uploaded image temporarily
        file_location = f"temp/{file.filename}"
        with open(file_location, "wb") as f:
            f.write(file.file.read())

        # Extract text from the image
        extracted_text = extract_text_from_image(file_location)

        # Extract specific details from the text
        extracted_details = extract_specific_details(extracted_text)

        # Generate content using Generative AI
        prompt = f"Based on the following extracted text from a train ticket, please provide detailed information:\n\n{extracted_text}"
        response_text = generate_content(prompt)

        # Extract additional details from the generated response
        response_details = extract_details_from_response(response_text)

        # Clean up the temporary file
        os.remove(file_location)
        
        return JSONResponse(content={"extracted_text": extracted_text, "details": response_details})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
