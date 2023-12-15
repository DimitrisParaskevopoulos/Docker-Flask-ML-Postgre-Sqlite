🚀 **ML prediction Web App**
The Flask application 🌐 is designed to provide predictions from a pre-trained machine learning model 🤖, specifically designed to tackle the famous Titanic dataset 🚢. This dataset is widely recognized in the data science community, and involves predicting the survival of passengers aboard the Titanic based on the following features: age, sex, and embarkation point.
After obtaining predictions from the simple classification model, the app is configured to save the results to a database. It supports two popular databases - PostgreSQL 🐘 and SQLite 📦. This app provides a flexible and modular structure, allowing developers to integrate their own pre-trained models and adapt the steps based on the specific requirements of their machine learning tasks. This app serves as a robust foundation for deploying machine learning models in a production environment 🚀.

🌈 **Key Features:**
- 🔄 Continuous predictions
- 📄 Database storage (PostgreSQL 🐘, SQLite 📦)
- 🧩 Modular structure for easy customization
- 🌍 Production-ready foundation

🤝 **Contribution:**
Contributions are welcome! Feel free to open issues, submit pull requests, or suggest improvements, especially for machine learning and MLops parts. Let's build this project together.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Setting Up](#setting-up)
- [Running](#running)
- [Testing](#testing)
  - [Testing PostgreSQL](#testing-postgresql)
  - [Testing SQLite](#testing-sqlite)

## Prerequisites

- [Docker](https://www.docker.com/) - Make sure Docker and Docker-compose are installed.

## Getting Started

Step-by-step instructions for setting up and running the app.

### Setting Up
 ```
git clone https://github.com/DimitrisParaskevopoulos/Docker-Flask-ML-Postgre-Sqlite.git
 ```
 ```
cd your-local-path/Docker-Flask-ML-Postgre-Sqlite
 ```

### Running
 ```
docker-compose -f docker-compose.prod.yml up -d --build
 ```
 ```
docker-compose -f docker-compose.prod.yml exec web python manage.py create_db
 ```

### Testing PostgreSQL
 ```
http://localhost:1337/prediction_request

 ```
 ```
curl --location "http://localhost:1337/predict" ^
--header "Content-Type: application/json" ^
--data "[{\"Age\": 85, \"Sex\": \"male\", \"Embarked\": \"S\"}, {\"Age\": 24, \"Sex\": \"female\", \"Embarked\": \"C\"}, {\"Age\": 3, \"Sex\": \"male\", \"Embarked\": \"C\"}, {\"Age\": 21, \"Sex\": \"male\", \"Embarked\": \"S\"}]"
 ```
 ```
http://localhost:1337/prediction_request

 ```

### Testing SQLite
 ```
docker-compose -f docker-compose.yml up -d --build
 ```
 ```
docker-compose -f docker-compose.yml exec web python manage.py create_db
 ```
 ```
http://localhost:1337/prediction_request

 ```
 ```
curl --location "http://localhost:1337/predict" ^
--header "Content-Type: application/json" ^
--data "[{\"Age\": 85, \"Sex\": \"male\", \"Embarked\": \"S\"}, {\"Age\": 24, \"Sex\": \"female\", \"Embarked\": \"C\"}]"
 ```
 ```
http://localhost:1337/prediction_request

 ```
