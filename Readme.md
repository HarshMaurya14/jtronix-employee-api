
# JTRONIX Employee API

A simple employee management REST API built with Python and FastAPI.

## Features

- Retrieve all employees
- Retrieve an employee by ID
- Create an employee
- Update employee status
- Filter employees by department

## Requirements

- Python
- FastAPI
- Uvicorn

## Setup

Create and activate a virtual environment.

Windows CMD:

```cmd
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```cmd
pip install -r requirements.txt
```

## Run the API

```cmd
python -m uvicorn main:app --reload
```

## API documentation

Open http://127.0.0.1:8000/docs in your browser.

## Note

Employee data is stored in memory and resets when the application restarts.
