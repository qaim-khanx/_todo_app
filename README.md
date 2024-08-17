# To-Do App

## Overview

This project is a simple yet powerful To-Do application built using **FastAPI** and **SQLModel** with a PostgreSQL database. The application allows users to manage their tasks effectively by providing a RESTful API for creating, updating, and completing to-do items.

## Features

- **FastAPI**: Leverages the high-performance FastAPI framework for building the backend API.
- **SQLModel**: Uses SQLModel for ORM (Object-Relational Mapping) with PostgreSQL, ensuring easy database management and interaction.
- **CRUD Operations**: Supports full CRUD (Create, Read, Update, Delete) operations on to-do items.
- **Task Completion**: Allows users to mark tasks as completed.
- **Database Management**: Automatically handles the creation of tables and session management using FastAPI's dependency injection.
- **Testing**: Includes unit tests to ensure the reliability and correctness of the application.

## Project Structure

```bash
todo_app/
│
├── todo_app/
│   ├── __init__.py
│   ├── main.py               # Main application logic
│   ├── settings.py           # Application settings and configuration
│   └── __pycache__/          # Compiled Python files
│
├── tests/
│   ├── __init__.py
│   ├── test_main.py          # Unit tests for the application
│   └── __pycache__/          # Compiled Python test files
│
├── .env                      # Environment variables
├── pyproject.toml            # Project dependencies and metadata (managed by Poetry)
├── poetry.lock               # Locked dependency versions
├── README.md                 # Project documentation
└── .git/                     # Git version control directory
```

## Installation
### Prerequisites
- **Python** 3.8+
- **Poetry** for dependency management
- **PostgreSQL** database
### Setup
Clone the repository:
```
git clone <repository-url>
cd todo_app
```
### Install dependencies: 
Make sure you have Poetry installed. Then run:
```
poetry install
```
### Set up environment variables:
Create a .env file in the root directory and add your PostgreSQL database URL:
```
DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<database>
```
### Run the application: 
Start the FastAPI server:
```
poetry run uvicorn todo_app.main:app --reload
```
### Access the API: 
The application will be running at http://127.0.0.1:8000. You can interact with the API using tools like Postman or via the built-in Swagger UI at http://127.0.0.1:8000/docs.

## Usage
### API Endpoints
- **GET /todos/:** Retrieve a list of all to-do items.
- **POST /todos/:** Create a new to-do item.
- **PUT /todos/{id}/:** Update an existing to-do item.
- **DELETE /todos/{id}/:** Delete a to-do item.
- **PATCH /todos/{id}/complete/:** Mark a to-do item as completed.

## Example Request
Creating a new to-do item:

```
curl -X POST "http://127.0.0.1:8000/todos/" -H "Content-Type: application/json" -d '{
  "content": "Write a README file",
  "is_completed": false
}'
```

## Testing
To run the tests, simply execute:

```
poetry run pytest
```
This will run the unit tests located in the tests/ directory.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License.
