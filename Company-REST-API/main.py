from fastapi import FastAPI, HTTPException
from typing import List
from database import conn, cursor
from models import Employee

import logging

logging.basicConfig(level=logging.INFO, filename="logs/api_logs.log",
                    format="%(asctime)s:%(levelname)s:%(message)s")


app = FastAPI()

@app.on_event("startup")
async def startup():
    # Database setup
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT,
            department TEXT)'''
        )
    conn.commit()


@app.get("/employees/")
async def read_employees():
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    logging.info(f"Displayed files are: {employees}")
    return employees


@app.get("/employees/{employee_id}")
async def read_employee(employee_id: int):
    cursor.execute('SELECT * FROM employees WHERE id = ?', (employee_id,))
    employee = cursor.fetchone()

    if employee is None:
        logging.error(f"Employee with id : {employee_id} not found")
        raise HTTPException(status_code=404, detail="Employee not found")

    logging.info(f"The details of employee_id {employee_id} is : {employee}")
    return employee


@app.post("/employees/")
async def create_employee(employee: Employee):
    cursor.execute('INSERT INTO employees (name, department) VALUES (?, ?)',
                   (employee.name, employee.department))
    conn.commit()
    logging.info(f"The newly created employee is : {employee}")
    return employee


@app.delete("/employees/{employee_id}")
async def delete_employee(employee_id: int):
    cursor.execute('DELETE FROM employees WHERE id = ?', (employee_id,))
    conn.commit()
    return {"message": "Employee deleted successfully"}


@app.put("/employees/{employee_id}/{column}/{new_value}")
async def update_employee(employee_id: int, column: str, new_value: str):
    
    if column not in ['name', 'department']:
        raise HTTPException(status_code=400, detail="Invalid column name")
    cursor.execute(f'UPDATE employees SET {column} = ? WHERE id = ?', (new_value, employee_id))
    conn.commit()
    return {"message": "Employee information updated successfully"}
