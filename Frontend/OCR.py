import google.generativeai as genai
import easyocr
import PIL.Image
import re

# Configure the Generative AI model
genai.configure(api_key="AIzaSyCSZ84WVAVcr1WJr8kp3zwk6LNRV9qkXos")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

def extract_text_from_image(image_path):
    image = PIL.Image.open(image_path)
    results = reader.readtext(image)
    text = " ".join([result[1] for result in results])
    return text

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
    times_pattern = r"Departure\s+([\d:]+\s+\d{2}-[A-Za-z]{3}-\d{4})\s+Arrival\s+([\d:]+\s+\d{2}-[A-Za-z]{3}-\d{4})"
    times_match = re.search(times_pattern, text)
    if times_match:
        details["Departure"] = times_match.group(1)
        details["Arrival"] = times_match.group(2)

    return details

def generate_content(prompt):
    response = model.generate_content(prompt)
    return response.text

def process_image(image_path):
    # Step 1: Extract text from image
    extracted_text = extract_text_from_image(image_path)

    # Step 2: Extract specific details
    details = extract_specific_details(extracted_text)

    # Step 3: Generate content using the extracted text as prompt
    generated_content = generate_content(extracted_text)

    return {"details": details, "generated_content": generated_content}

# Example usage
result = process_image("D:\SIH\Frontend\Train_ticket_TK518095875i48_pages-to-jpg-0001.jpg")
print(result["details"])
print(result["generated_content"])
