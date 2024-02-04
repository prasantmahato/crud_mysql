# API for CRUD Functions with Flask &  MySQL

## Steps to Execute

Clone the repo and move to directory

```bash
git clone https://github.com/prasantmahato/crud_mysql
cd crud_mysql
```

Execute depending on the Operating System

```bash
source venv/bin/activate    # MacOS or Linux
.\venv\Scripts\activate     # Windows
```

Install the required packages and run the server

```bash
pip3 install -r requirements.txt
flask run
```

## View All Employees

```bash
curl --location 'http://127.0.0.1:5000/'
```

## Create Table Employee

```bash
curl --location 'http://127.0.0.1:5000/create'
```

## Insert New Employee

```bash
curl --location 'http://127.0.0.1:5000/insert' \
--form 'name="Prasant"' \
--form 'email="prasant@gmail.com"' \
--form 'dob="2000-03-14"'
```

## Update Employee by Email

```bash
curl --location 'http://127.0.0.1:5000/update' \
--form 'name="Prasant Mahato"' \
--form 'email="prasant@gmail.com"' \
```

## Delete Employee Record

```bash
curl --location 'http://127.0.0.1:5000/delete' \
--form 'email="prasant@gmail.com"'
```
