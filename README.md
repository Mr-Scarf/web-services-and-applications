
# Web Services and Applications

**University**: Atlantic Technological University  
**Module**: Web Services and Applications   
**Class**: January 2026  
**Author**: David Scally  


This repository contains a combination of assignments, coursework and a final project that was completed for the **Web Services and Applications** module - see structure & contents below.

## Repository Structure & Contents

### assignments
Contains assignments completed as part of the module : 
    - **assignment02-carddraw.py** - Programme that shuffles,selects & prints slection of cards. 
    - **assignment03-cso.ipynb** - CSO Exchequer Historical Data retrieval code. 
        - **cso.json** -   Json file storing CSO Exchequer Historical Data.
    - **assignment04** - Reading & updating a text file from a github repository, then commiting changes back to github. 
    



### my-work
Contains coursework completed as part of the module.


### project
Contains project completed as part of the module. This will be further expanded on in **Project - Guinness Pint App** section.

### .gitignore
Tells Git which files to ignore in repository.

### requirements.txt
List of packages used in the analysis.

### README.md
This file, used to explain the layout of the repository & the project. 



# Project - Guinness Pint App*

## Purpose

The project is to create a web application using FLASK & RESTful APIs to perform CRUD (Create, Read, Update, Delete) operations on 
data stored in a database. 


This application allows users to view, add, update & delete Guinness prices for pubs in Maynooth.

## Live Application

Hosted on PythonAnywhere:

https://mrscarf.eu.pythonanywhere.com/

## Features

 - View all pint prices
 - Add a new pub & pint price
 - Update existing pint price
 - Delete pub/pints ENTRY

## API Endpoints

    - GET/pints -List all pint prices
    - GET/pints/<id> - List specific pint price by pub ID
    - POST/pints - Create a new pint entry
    - PUT/pints/<id> - Update an existing pint entry by pub ID
    - DELETE/pints/<id> - Delete a specific pint entry

## Project Structure

project/

- staticpages/
- pint_app.py
- pint_dao.py
- pints.db
- requirements.txt


1. **Clone the repository**

```bash
git clone https://github.com/Mr-Scarf/web-services-and-applications.git
cd web-services-and-applications/project
```

2. **Create a virtual environment**
```bash
python -m venv venv 
venv\Scripts\activate
```

3. **Install dependencies - see file 'requirements.txt'**

```bash
pip install -r requirements.txt
```

4. **Create the database**
```bash
python createschema.py
```

5. **Run the application**
```bash
python pint_app.py
```

6. **Open in browser:**

http://127.0.0.1:5000/


  


