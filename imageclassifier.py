import google.generativeai as genai
genai.configure(api_key="AIzaSyCSZ84WVAVcr1WJr8kp3zwk6LNRV9qkXos")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
import PIL.Image
import re
import json

def classify(image):
# Assuming genai and the model are properly defined and initialized.
    model = genai.GenerativeModel("gemini-1.5-flash")
    content = """
                You are an AI for Indian Railway Problem assistance AI, a passenger gives image
                and sometimes they don't and just tell the problem in text. I will give a variety of problems,
                you tell me " What is the problem " and give a detailed explanation of the problem.
                You don't have to exactly give me the response I gave you. You can change the output format too.

                output format
                {
                ex: based on image food is not good, someone is set on my seat, like a variety of problems "
                Department responsible: ['Medical Assistance', 'Security', 'Facilities for Women with Special needs', 'Electrical Equipment', 'Coach - Cleanliness', 'Punctuality', 'Water Availability', 'Coach - Maintenance', 'Catering & Vending Services', 'Staff Behaviour', 'Corruption/Bribery', 'Bedroll', 'Miscellaneous']
                "I will contact the respective department and take care of the situation.
                Please let me know if you need something else."
                }
                condition:
                If the image and the text given are not relevant, give the response like "I couldn't understand what you are saying. Can you be more specific"
    """

    comment = input("Hello I am your AI assistant. Can you tell me what's wrong in the picture: ")
    im = PIL.Image.open(image)

    response = model.generate_content([content + comment, im])

    # Print the entire response to understand its structure
    print("Response Text:", response.text)

    # Function to extract department names from various possible formats
    def extract_departments(response_text):
        # Normalize response text for easier processing
        response_text = response_text.replace("'", '"')  # Replace single quotes with double quotes
        
        try:
            # Try to parse the text as JSON
            response_json = json.loads(response_text)
            departments = response_json.get("Department responsible", [])
            return [dep.strip() for dep in departments]
        except json.JSONDecodeError:
            # If JSON parsing fails, use regex as fallback
            department_match = re.search(r'"Department responsible": \[(.*?)\]', response_text)
            if department_match:
                departments_str = department_match.group(1)
                departments = [dep.strip().strip('"').strip("'") for dep in departments_str.split(',')]
                return departments
            else:
                return ["Could not find the department in the response."]

    # Extract and print departments
    departments = extract_departments(response.text)
    for department in departments:
        print(department)

