# Docker-Flask-ML-Postgre-Sqlite
The Flask application is designed to provide predictions from a pre-trained machine learning model. After obtaining predictions from the model, the app is configured to save the results to a database.
It provides support for two popular databases - PostgreSQL and SQLite. 
This app provides a flexible and modular structure, allowing users to integrate their own pre-trained models and adapt the preprocessing steps based on the specific requirements of their machine learning tasks. 
It serves as a robust foundation for deploying machine learning models in a production environment.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Setting Up](#setting-up)
- [Running](#running)
- [Testing](#Testing)

## Prerequisites

- [Docker](https://www.docker.com/) - Make sure Docker is installed and running.

## Getting Started

Step-by-step instructions for setting up and running your app.

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
curl --location 'http://localhost:1337/predict' \
--header 'Content-Type: application/json' \
--data '[{"Age": 85, "Sex": "male", "Embarked": "S"}, {"Age": 24, "Sex": "female", "Embarked": "C"}, {"Age": 3, "Sex": "male", "Embarked": "C"}, {"Age": 21, "Sex": "male", "Embarked": "S"}]'
 ```
 ```
http://localhost:1337/prediction_request

 ```

### Testing SQLite
 ```
docker-compose -f docker-compose.prod.yml exec web python manage.py create_db
 ```
 ```
curl --location 'http://localhost:1337/predict' \
--header 'Content-Type: application/json' \
--data '[{"Age": 85, "Sex": "male", "Embarked": "S"}, {"Age": 24, "Sex": "female", "Embarked": "C"}, {"Age": 3, "Sex": "male", "Embarked": "C"}, {"Age": 21, "Sex": "male", "Embarked": "S"}]'
 ```
