## Railway-Grievance-Management-System
An intelligent complaint classification system. It accepts user inputs (text and images) and uses machine learning models to classify grievances into predefined categories, providing real-time feedback. Developed using FastAPI, HTML, CSS, JavaScript, and Python

## Contributers
Sam Robin Singh E - https://github.com/SamRobinSingh
Visnu Sanjay Kumar P - https://github.com/vishnu24102005
Nishaa R - https://github.com/Nishaa10
Karpaga Mithuna S - https://github.com/mithuna357

## Deployment

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