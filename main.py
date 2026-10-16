

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal

# Create the FastAPI application
app = FastAPI(title="JTRONIX Employee API")


# Sample employee records stored in memory
employees = [
    {
        "id": 1,
        "name": "Rahul Sharma",
        "department": "Engineering",
        "status": "Active"
    },
    {
        "id": 2,
        "name": "Priya Patel",
        "department": "HR",
        "status": "Active"
    },
    {
        "id": 3,
        "name": "Amit Verma",
        "department": "Engineering",
        "status": "Inactive"
    }
]


# Check whether the API is running
@app.get("/")
def home():
    return {"message": "JTRONIX Employee API is running"}


# Return the complete list of employees
@app.get("/employees")
def get_employees(department: str | None = None):
    if department:
        return [
            employee for employee in employees
            if employee["department"].lower() == department.strip().lower()
        ]

    return employees


# Find and return an employee using their ID
@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee

    # Return an error if the employee does not exist
    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )


# Define the information needed to create an employee
class EmployeeCreate(BaseModel):
    name: str = Field(min_length=1)
    department: str = Field(min_length=1)


# Allow only these two employee status values
class StatusUpdate(BaseModel):
    status: Literal["Active", "Inactive"]


# Add a new employee to the list
@app.post("/employees", status_code=201)
def create_employee(data: EmployeeCreate):
    name = data.name.strip()
    department = data.department.strip()

    # Make sure the name and department aren't empty
    if not name or not department:
        raise HTTPException(
            status_code=422,
            detail="Name and department cannot be empty"
        )

    # Assign an ID based on the highest existing ID
    new_id = max(
        (employee["id"] for employee in employees),
        default=0
    ) + 1

    # Create the new employee with Active status by default
    new_employee = {
        "id": new_id,
        "name": name,
        "department": department,
        "status": "Active"
    }

    employees.append(new_employee)
    return new_employee


# Change an employee's status using their ID
@app.patch("/employees/{employee_id}/status")
def update_employee_status(
    employee_id: int,
    data: StatusUpdate
):
    for employee in employees:
        if employee["id"] == employee_id:
            employee["status"] = data.status
            return employee

    # Return an error if the employee does not exist
    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )


# Return employees belonging to a specific department
@app.get("/employees/filter")
def filter_employees(department: str):
    return [
        employee for employee in employees
        if employee["department"].lower() == department.strip().lower()
    ]

