from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
#from OCR import extract_text_from_image, extract_specific_details
from imageclassifier import classify_image  # Ensure this import matches your actual function name

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_form():
    try:
        # Adjust the path if your index1.html is not in the static directory
        with open("index1.html") as file:
            content = file.read()
        return HTMLResponse(content=content)
    except FileNotFoundError:
        return HTMLResponse("<html><body><h2>File Not Found</h2></body></html>", status_code=404)

# Serve HTML files
@app.get("/station_issue_grievance")
async def read_station_issue_grievance():
    return FileResponse("station_issue_grievance.html")
    
@app.post("/submit")
async def submit_complaint(
    file: UploadFile = File(...),
    description: str = Form(...),
    mobile: str = Form(...),
    pnr: str = Form(...),
    type: str = Form(...),
    sub_type: str = Form(...),
    incident_date: str = Form(...)
):
    try:
        # Save the uploaded file
        file_location = f"temp_{file.filename}"
        with open(file_location, "wb") as f:
            f.write(file.file.read())
        
        # Call classify_image with the path to the file and the description
        classification_result = classify_image(file_location, description)

        # Clean up the uploaded file
        os.remove(file_location)

        # Generate the response HTML with a styled message
        response_html = f"""
        <html>
        <head>
            <style>
                body {{
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                    margin: 0;
                    font-family: Arial, sans-serif;
                }}
                .result-container {{
                    text-align: center;
                    padding: 20px;
                    border: 1px solid #ddd;
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    background-color: #f9f9f9;
                }}
                .result-container h2 {{
                    color: #333;
                }}
                .result-container p {{
                    color: #555;
                }}
                .result-container a {{
                    display: inline-block;
                    margin-top: 10px;
                    padding: 10px 20px;
                    background-color: #007bff;
                    color: white;
                    text-decoration: none;
                    border-radius: 4px;
                }}
                .result-container a:hover {{
                    background-color: #0056b3;
                }}
            </style>
        </head>
        <body>
            <div class="result-container">
                <h2>Classification Result</h2>
                <p>{classification_result}</p>
                <a href="/">Go back</a>
            </div>
        </body>
        </html>
        """

        return HTMLResponse(content=response_html)

    except Exception as e:
        return HTMLResponse(f"<html><body><h2>Error</h2><p>{str(e)}</p><a href='/'>Go back</a></body></html>")
    
@app.get("/staff", response_class=HTMLResponse)
async def read_staff():
    return FileResponse("staff.html")

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    # Add login logic here
    # For demonstration, let's assume any credentials are valid
    return RedirectResponse(url="/staff", status_code=302)
