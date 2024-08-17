# To-Do App

## Overview

Welcome to the To-Do App! This project is designed to provide a straightforward yet efficient way to manage your tasks. Built with **FastAPI** and **SQLModel** and backed by a PostgreSQL database, this application offers a RESTful API for all your task management needs.

## Features

- **FastAPI**: Utilizes FastAPI's high-performance capabilities to deliver a robust backend.
- **SQLModel**: Leverages SQLModel for seamless ORM with PostgreSQL, simplifying database interactions.
- **CRUD Operations**: Fully supports Create, Read, Update, and Delete operations for to-do items.
- **Task Completion**: Easily mark tasks as completed to keep track of your progress.
- **Database Management**: Handles table creation and session management automatically through FastAPI’s dependency injection.
- **Testing**: Includes unit tests to ensure the application is reliable and performs as expected.

## Project Structure

Here's an overview of the project structure and its components:

```bash
todo_app/
│
├── todo_app/
│   ├── __init__.py
│   ├── main.py               # Contains the main application logic
│   ├── settings.py           # Configuration and settings
│   └── __pycache__/          # Compiled Python files
│
├── tests/
│   ├── __init__.py
│   ├── test_main.py          # Unit tests to validate functionality
│   └── __pycache__/          # Compiled Python test files
│
├── .env                      # Environment variables for configuration
├── pyproject.toml            # Dependencies and project metadata (managed by Poetry)
├── poetry.lock               # Locked versions of dependencies
├── README.md                 # Documentation for the project
└── .git/                     # Git version control directory
Installation
Prerequisites
Python 3.8+
Poetry for dependency management
PostgreSQL database
Setup
Clone the repository:

bash
Copy code
git clone <repository-url>
cd todo_app
Install dependencies:

Ensure you have Poetry installed, then run:

bash
Copy code
poetry install
Set up environment variables:

Create a .env file in the root directory and add your PostgreSQL database URL:

bash
Copy code
DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<database>
Run the application:

Start the FastAPI server with:

bash
Copy code
poetry run uvicorn todo_app.main:app --reload
Access the API
Once the server is running, access the API at http://127.0.0.1:8000. You can interact with the API using tools like Postman or through the Swagger UI available at http://127.0.0.1:8000/docs.

Usage
API Endpoints
GET /todos/: Retrieve a list of all to-do items.
POST /todos/: Create a new to-do item.
PUT /todos/{id}/: Update an existing to-do item.
DELETE /todos/{id}/: Delete a to-do item.
PATCH /todos/{id}/complete/: Mark a to-do item as completed.
Example Request
Creating a new to-do item:

bash
Copy code
curl -X POST "http://127.0.0.1:8000/todos/" -H "Content-Type: application/json" -d '{
  "content": "Write a README file",
  "is_completed": false
}'
Testing
To run the unit tests, execute:

bash
Copy code
poetry run pytest
This will run all tests located in the tests/ directory to ensure everything is working correctly.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.
