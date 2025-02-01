Flask API for HNG12 Task
This is a simple Flask-based API that returns the following information in JSON format:

Registered Email Address: The email address used to register on the HNG12 Slack workspace.

Current Datetime: The current date and time in ISO 8601 format with UTC timezone (e.g., 2024-03-14T12:34:56Z).

GitHub URL: The URL of the project's codebase on GitHub.

This project is built using Python and Flask, making it lightweight, easy to deploy, and highly customizable.

Setup Instructions
Prerequisites
Python 3.7 or higher.

Flask (install via pip).

Steps to Run Locally
Clone the repository:

git clone https://github.com/Paulokla/HNG_Public-API
cd your-repo
Install the required dependencies:

pip install Flask
Run the Flask application:

python app.py
Access the API at: http://127.0.0.1:5000/api

API Documentation
Endpoint
URL: /api
Method: GET

Request Format
No request body or parameters are required.

Response Format
The API returns a JSON object with the following fields:

email: The registered email address.

current_datetime: The current timestamp in ISO 8601 format with UTC timezone (ends with 'Z').

github_url: The GitHub repository URL of the project.

http://127.0.0.1:5000/api
Example Response
{
"email": "paulokla654@gmail.com",
"current_datetime": "2024-03-14T12:34:56Z",
"github_url": "https://github.com/Paulokla/HNG_Public-API"
}

Deployment
The API is deployed to a publicly accessible endpoint for easy access. It is hosted on Render (or any other platform of your choice), ensuring fast response times (< 500ms).

Public Endpoint
https://hng-public-api-z4es.onrender.com

Deployment Steps
Sign up for a free account on Render (or another platform like Heroku, AWS, etc.).

Connect your GitHub repository to Render.

Configure the deployment settings:

Set the runtime to Python.

Specify the command to run the app: python app.py.

Deploy the application.

Backlink
This project is built using Python and Flask. If you're looking to hire skilled Python developers, check out:
👉 [Hire Python Developers at HNG](https://hng.tech/hire/python-developers)

Performance
The API is optimized for fast response times:

Average response time: < 500ms.

Lightweight and scalable for high traffic.
