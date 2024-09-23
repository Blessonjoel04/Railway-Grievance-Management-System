# Railway-Grievance-Management-System
An intelligent complaint classification system. It accepts user inputs (text and images) and uses machine learning models to classify grievances into predefined categories, providing real-time feedback. Developed using FastAPI, HTML, CSS, JavaScript, and Python

A brief description of what this project does and who it's for

This Project is a web-based application designed to streamline and automate the process of handling grievances related to railway services. It integrates various technologies to classify and manage user complaints efficiently.

Features:   
Complaint Classification: Utilizes machine learning models to classify user complaints into predefined categories.

User-Friendly Interface: Developed with HTML, CSS, and JavaScript to ensure a responsive and intuitive user experience.

FastAPI Backend: Handles user inputs and processes both text and image data through an API.

Grievance Submission: Users can submit complaints through dedicated forms, including details like issue type, incident date, and file uploads.

Integrated Chatbot: Provides instant assistance and information to users through a chatbot interface.

Dashboard and Analytics: Includes integration with Power BI for visualizing and analyzing data.

Technologies Used:
Frontend: HTML, CSS, JavaScript
Backend: FastAPI, Python
Machine Learning: Custom classification models using imageclassifier
Data Visualization: Power BI

# Contributers
Sam Robin Singh E - https://github.com/SamRobinSingh    
Visnu Sanjay Kumar P - https://github.com/vishnu24102005       
Nishaa R - https://github.com/Nishaa10  
Karpaga Mithuna S - https://github.com/mithuna357

# Deployment

To deploy this project run

```bash 
cd <path-to-your-project>
```
Then, Clone the repository using the command line,

```bash
git clone https://github.com/Blessonjoel04/Railway-Grievance-Management-System
```

The file `Frontend` contains the Machine Learning models and the HTML files. The `static` folder inside the `Frontend` folder contains two folders - `css` and `images`. It is used in enhancing the appearance for the frontend page. 

Now, change the directory to `Frontend` using, 

```bash
cd Frontend
```

Check the current directory using the command, 
```bash
pwd
```
If your current directory is your desired directory, then run the application using, 

```
uvicorn app:app --reload
```

It will provide you with a localhost link. Click on that and explore.