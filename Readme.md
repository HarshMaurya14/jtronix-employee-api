# JTRONIX Employee Management API

A RESTful Employee Management API built with **Python, FastAPI, and Pydantic** as part of the JTRONIX Backend Internship Coding Assessment.

## 🚀 Live Demo

- **Live API:** https://jtronix-employee-api.onrender.com
- **Interactive API Documentation:** https://jtronix-employee-api.onrender.com/docs

Use the interactive Swagger documentation to explore and test the available endpoints.

## ✨ Features

- Retrieve all employees
- Filter employees by department
- Retrieve an employee by ID
- Create a new employee
- Update an employee's status
- Input validation using Pydantic
- Appropriate HTTP status codes and error handling
- Interactive API documentation with Swagger UI

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Validation:** Pydantic
- **Server:** Uvicorn
- **Deployment:** Render
- **Version Control:** Git and GitHub

## 📌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| GET | `/employees` | Retrieve all employees |
| GET | `/employees?department=Engineering` | Filter employees by department |
| GET | `/employees/{employee_id}` | Retrieve an employee by ID |
| POST | `/employees` | Create a new employee |
| PATCH | `/employees/{employee_id}/status` | Update employee status |

### Example: Create an Employee

**Request:** `POST /employees`

```json
{
  "name": "Neha Singh",
  "department": "Engineering"
}
```

The API creates the employee with a generated ID and an initial status of `Active`.

### Example: Update Employee Status

**Request:** `PATCH /employees/1/status`

```json
{
  "status": "Inactive"
}
```

Valid status values are `Active` and `Inactive`.

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/HarshMaurya14/jtronix-employee-api.git
cd jtronix-employee-api
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the server

```bash
python -m uvicorn main:app --reload
```

### 6. Open the API documentation

Visit http://127.0.0.1:8000/docs in your browser.

## 📂 Project Structure

```text
jtronix-employee-api/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 📝 Notes

- Employee records are stored in memory for this implementation.
- Data created through the API may reset when the application restarts or redeploys.
- This project demonstrates core backend concepts, REST API design, validation, and error handling.

## 👨‍💻 Author

**Harsh Maurya**

GitHub: [@HarshMaurya14](https://github.com/HarshMaurya14)

---

Built with Python and FastAPI for the JTRONIX Backend Internship Coding Assessment.
