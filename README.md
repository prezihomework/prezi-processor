Welcome to prezi-processor micro service!
===================

This repository contains a **Python3 & Django** based Web Application with SQLite database structure for representing Prezi data, provided by prezi-data-provider micro service.



How to install
-------------

- Install Python(3) - Help: [https://www.python.org/]()  
- Install dependencies by `pip install -r requirements.txt `
- Start the server by: python manage.py runserver


> **Note:**

> You might have use pip with proxy settings `--proxy <proxy.company.com:8080>` 



Features
-------------

Expected states of the Web App:

1. HomePage: 
[http://localhost:8000/processor/]()
2. Download data from backend:
[http://localhost:8000/processor/deserialize/]()
3. List all presentations or search for titles in Search page:
[http://localhost:8000/processor/search/]()
4. Sort presentations by data:
[localhost:8000/processor/search/sortByDate]()
5. Check contact in:
[localhost:8000/processor/contact/]()

Public site
-------------

[http://ec2-52-27-167-65.us-west-2.compute.amazonaws.com:8000/processor/]()
