import google.generativeai as genai
import easyocr
import PIL.Image
import os
import re
from fpdf import FPDF

# Configure the Generative AI model
genai.configure(api_key="AIzaSyCSZ84WVAVcr1WJr8kp3zwk6LNRV9qkXos")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

# Function to extract text from image
def extract_text_from_image(image_path):
    image = PIL.Image.open(image_path)
    results = reader.readtext(image)
    text = " ".join([result[1] for result in results])
    return text

# Function to extract specific details from the text
def extract_specific_details(text):
    details = {}

    # Extract Name, Age, Gender
    name_pattern = r"Name\s(\S+)\s(\d+)\s([MF])"
    name_match = re.search(name_pattern, text)
    if name_match:
        details["Name"] = name_match.group(1)
        details["Age"] = name_match.group(2)
        details["Gender"] = name_match.group(3)

    # Extract Booking Status
    booking_status_pattern = r"CNF/S7/\d+"
    booking_status_match = re.search(booking_status_pattern, text)
    if booking_status_match:
        details["Booking Status"] = booking_status_match.group(0)

    # Extract Quota
    quota_pattern = r"Quota\s+([A-Z]+)"
    quota_match = re.search(quota_pattern, text)
    if quota_match:
        details["Quota"] = quota_match.group(1)

    # Extract Distance
    distance_pattern = r"Distance\s+(\d+\s+KM)"
    distance_match = re.search(distance_pattern, text)
    if distance_match:
        details["Distance"] = distance_match.group(1)

    # Extract Ticket Printing Time
    time_pattern = r"Ticket Printing Time\s+(\d{2}:\d{2}\s+\d{2}-[A-Za-z]{3}-\d{4})"
    time_match = re.search(time_pattern, text)
    if time_match:
        details["Ticket Printing Time"] = time_match.group(1)

    # Extract PNR
    pnr_pattern = r"PNR\s+(\d+)"
    pnr_match = re.search(pnr_pattern, text)
    if pnr_match:
        details["PNR"] = pnr_match.group(1)

    # Extract Train No./Name
    train_pattern = r"Train No./ Name\s+(\d+/\S+)"
    train_match = re.search(train_pattern, text)
    if train_match:
        details["Train No./ Name"] = train_match.group(1)

    # Extract Class
    class_pattern = r"Class\s+([A-Z]+\s\([A-Z]+\))"
    class_match = re.search(class_pattern, text)
    if class_match:
        details["Class"] = class_match.group(1)

    # Extract Boarding From and To stations
    boarding_pattern = r"Boarding From\s+(\S+)\sTo\s(\S+)"
    boarding_match = re.search(boarding_pattern, text)
    if boarding_match:
        details["Boarding From"] = boarding_match.group(1)
        details["To"] = boarding_match.group(2)

    # Extract Departure and Arrival times
    times_pattern = r"Departure\\s+([\d:]+\s+\d{2}-[A-Za-z]{3}-\d{4})\s+Arrival\\s+([\d:]+\s+\d{2}-[A-Za-z]{3}-\d{4})"
    times_match = re.search(times_pattern, text)
    if times_match:
        details["Departure"] = times_match.group(1)
        details["Arrival"] = times_match.group(2)

    return details

# Function to generate content using Generative AI
def generate_content(prompt):
    response = model.generate_content(prompt)
    return response.text

# Function to create a PDF file with the extracted details
def create_pdf(details, pdf_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Passenger Details", ln=True, align='C')
    for key, value in details.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True, align='L')

    pdf.output(pdf_path)

# Main logic to handle the AI response based on user input
content = """
            You are an AI for Indian Railway Problem assistance AI, a passenger gives image
            and sometimes they don't and just tell the problem in text. I will give a variety of problems,
            you tell me "What is the problem" and give a detailed explanation of the problem.
            You don't have to exactly give me the response I gave you. You can change the output format too.

            Output format:
            {
            ex: based on image food is not good, someone is sitting on my seat, like a variety of problems "
            Department responsible: ["Cleaning","Police","Food","Ticket Issue"]
            "I will contact the respective department and take care of the situation.
            Please let me know if you need something else."
            }
            Condition:
            If the image and the text given are not relevant, give the responses like "I couldn't understand what you are saying. Can you be more specific?"
"""

# Prompt the user for the complaint
comment = input("Hello, I am your AI assistant. Can you tell me what's wrong in the picture or text? ")

# Set up the image for analysis
image_path = "D:\\SIH\\food.jpeg"
im = PIL.Image.open(image_path)

# Run the AI model based on complaint category
if any(ticketing in comment for ticketing in ["Unreserved Ticketing", "Reserved Ticketing", "Refunds of Tickets"]):
    # Extract text from the image
    extracted_text = extract_text_from_image(image_path)
    print("Extracted Text:", extracted_text)

    # Extract specific details
    extracted_details = extract_specific_details(extracted_text)
    print("Extracted Details:", extracted_details)

    # Generate content based on extracted text
    prompt = f"Based on the following extracted text from a train ticket, please provide information on the department or problem:\n\n{extracted_text}"
    response_text = generate_content(prompt)
    print("Generated Response:", response_text)
else:
    # Generate AI response using the first model
    response = model.generate_content([content + comment, im])
    print(response.text)