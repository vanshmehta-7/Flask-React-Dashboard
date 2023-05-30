# Flask-React-Dashboard
This repository contains a Flask backend and React frontend for the Flask-React-Dashboard project.

## Project Overview
The Flask-React-Dashboard project is a web application that provides a dashboard for monitoring and analyzing various data metrics. The backend is built with Flask, a Python web framework, and provides API endpoints to fetch data from a PostgreSQL database. The frontend is built with React, a JavaScript library for building user interfaces, and consumes the backend API to display the data in an interactive dashboard.

## Prerequisites
To run the Flask-React-Dashboard locally using Docker Compose, you need to have the following dependencies installed:

- Docker
- Docker Compose

## Setup
1. Clone the repository to your local machine:
   ```shell
   git clone https://github.com/your-username/Flask-React-Dashboard.git

2. Change into the project directory:
   ```shell
   cd Flask-React-Dashboard
   
3. Build and run the containers using Docker Compose:
   ```shell
   docker-compose up --build

4. Open your web browser and navigate to http://localhost:8888 to access the React frontend.

## API Endpoints
The Flask backend provides the following API endpoints:

/temperature: Retrieves temperature data.

/ph: Retrieves pH data.

/distilled_oxygen: Retrieves distilled oxygen data.

/pressure: Retrieves pressure data.


## Project Structure
The project structure is as follows:

backend/: Contains the Flask backend code.

frontend/: Contains the React frontend code.

pgdata/: Volume for storing PostgreSQL data.

docker-compose.yaml: Configuration file for Docker Compose.

backend/local.env: Environment variables for the backend.


