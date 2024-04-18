# We will focus on the following topic for this chapter: 
- Introduction to REST APIs
- Making API requests
- Parsing API responses
- Desiging  and Developing a REST API

## In this project, we will create an API to manage and retrieve data related to "employees." We'll cover basic CRUD operations,. For this example, we'll use SQLite as the database.

app/
    ├── main.py
    ├── database.py
    ├── models.py
    ├── requirements.txt
    └── data.db
1. Install Dependencies: Create a virtual environment and install the required packages 
2. Database Setup: In this example,use SQLite as the database. Create a data.db file in the project directory.
3. Define Models: In models.py, define the data models for the employees.
In your example, the Employee class represents the data model for an employee with three fields: id, name, and department. Each field has a specified type (int, str) indicating the expected data type for that field.


4. Database Configuration: In database.py, set up the database connection using SQLite and create a sample employee table.


5. FastAPI Application: In main.py, implement the FastAPI application, including CRUD operations, and authentication,

@app.on_event("startup")
# create table

@app.get("/employees/")
# return table

@app.get("/employees/{employee_id}"
# return table based on employee id


@app.post("/employees/")
# insert data into the table

@app.delete("/employees/{employee_id}")
# delete data from a table using employee_id
@app.put("/employees/{employee_id}/{column}/{new_value}")
# update the table using employeeid and set new value of a column

6. Run the Application: Run the FastAPI application using uvicorn main:app --reload. The API will be available at http://127.0.0.1:8000.

Generate documentation using swagger UI
7. Test the API:
Access http://127.0.0.1:8000/docs to view the automatically generated Swagger documentation.
Use an API client (e.g., Postman or curl) to interact with the API endpoints.