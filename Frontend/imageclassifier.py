import google.generativeai as genai
import PIL.Image
import json
import re

# Configure the Generative AI model
genai.configure(api_key="AIzaSyCSZ84WVAVcr1WJr8kp3zwk6LNRV9qkXos")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def classify_image(image_path: str, comment: str) -> str:
    content = f"""
                You are an AI for Indian Railway Problem assistance AI. A passenger provides an image
                and sometimes just a textual description. I will give you a variety of problems,
                and you should identify the problem and give a detailed explanation. You don’t need to
                follow the exact format given but should provide useful information.

                Output format:
                {{
                "description": "Based on the image, the problem is related to...",
                "Department responsible": ['Medical Assistance', 'Security', 'Facilities for Women with Special needs', 'Electrical Equipment', 'Coach - Cleanliness', 'Punctuality', 'Water Availability', 'Coach - Maintenance', 'Catering & Vending Services', 'Staff Behaviour', 'Corruption/Bribery', 'Bedroll', 'Miscellaneous'],
                "response": "I will contact the respective department and take care of the situation. Please let me know if you need something else."
                }}

                Condition:
                If the image and the text given are not relevant, respond with: "I couldn't understand what you are saying. Can you be more specific?"
                """
    
    # Open the image
    im = PIL.Image.open(image_path)
    
    # Generate the AI response
    response = model.generate_content([content + comment, im])
    
    # Print the entire response to understand its structure
    print("Response Text:", response.text)

    # Function to extract department names from various possible formats
    def extract_departments(response_text):
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
    return response.text
