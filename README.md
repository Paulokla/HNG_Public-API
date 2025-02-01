Flask API for HNG12 Task
This is a simple Flask-based API that returns the following information in JSON format:

Registered Email Address: The email address used to register on the HNG12 Slack workspace.

Current Datetime: The current date and time in ISO 8601 format.

GitHub URL: The URL of the project's codebase on GitHub.

Features
Public API endpoint that returns JSON data.

Lightweight and easy to deploy.

Uses Python and Flask for simplicity and flexibility.

How It Works
The API has a single endpoint (/api) that responds to GET requests. When accessed, it returns a JSON object containing:

email: The registered email address.

current_datetime: The current timestamp in ISO 8601 format.

github_url: The GitHub repository URL of the project.