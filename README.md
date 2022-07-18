# Api Code challenge
For this challenge you will need to produce a service that will return the opening
"crawl" text from a random Star Wars film every time an endpoint is hit. As well as a
second service that returns a reverse of the text for the opening "crawl".

## Project overview
For this challenge, I have used the Django framework to run the application on local , this project has two directories , backend (that contains the configuration of the project ) and frontend (contains the templates , urls,views for the fron-end service).
navigation:
/: the root page shows a descending list of films for  the endpoint  random_crawl  and ascending list for the endpoint random_crawl_reverse  as results of  the GET request from https://swapi.dev/ API,  the list is linkable to a  endpoint that shows opening crawl information  

## Requirements
- Python3.x
- 
## Installation
- git clone https://github.com/imerx/Api-challenge.git
- Change to the downloaded folder using **cd Api-challenge**
- Create virtual environment **python -m venv venv**
- Activate the virtual environment using this comand **.\venv\Scripts\activate** on Windows or **source ~/cdiproject/venv/bin/activate** on Linux
- Install the system requirements  **pip install -r requirements.txt**
- Navigate to the project directory  **cd Api-challenge\project**
- Run the webserver python  manage.py runserver 0.0.0.0:8080 
- Open your browser and type http://localhost:8080/ or http://127.0.0.1:8080/
