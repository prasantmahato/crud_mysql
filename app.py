from flask import Flask, request

import mysql.connector
from datetime import datetime
from queries import Queries

app = Flask(__name__)

mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="employee")
mycursor = mydb.cursor()
q = Queries()  # Use query statements

# Route to list all employee with complete details
@app.route("/")
def root():
    cursor = mydb.cursor()
    cursor.execute(q.select)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return {"Employees:" : rows}, 200

# Route to drop table and create table
@app.route("/create")
def create():
    cursor = mydb.cursor()
    cursor.execute(q.drop)
    print("Employee Table dropped.")
    cursor.execute(q.create)
    print("Employee Table created.")
    return {"message": "Table Created"}, 201


# Route to save new record
@app.route("/insert", methods=["POST"])
def insert():
    name = request.form["name"]
    email = request.form["email"]
    dob = request.form["dob"]

    cursor = mydb.cursor()
    cursor.execute(q.insert, (name, email, dob))
    print(name," registered")
    mydb.commit()
    return {"message": "Employee Registered"}, 201

# Update record
@app.route("/update", methods=["POST"])
def update():
    # Updating employee by it's email ID
    name = request.form["name"]
    email = request.form["email"]

    cursor = mydb.cursor()
    cursor.execute(q.update, (name, email))
    print(email," updated")
    mydb.commit()
    return {"message": "Employee data Updated"}, 200


# Delete particular record by Email
@app.route("/delete", methods=["POST"])
def delete():
    # Delete employee by it's email ID
    email = request.form["email"]
    print(q.delete, (email,))

    cursor = mydb.cursor()
    cursor.execute(q.delete, (email,))
    print(email," deleted")
    mydb.commit()
    return {"message": "Employee Deleted"}, 200


if __name__ == "__main__":
    app.run(debug=True)
