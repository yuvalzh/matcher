# Matcher

## Description

The goal of this project is to provide a plan that will find candidates whose match the job requirements and returns the best ones.
The project is written with python 3.10.5 using django framework 4.2.0

## Installations

### installs Python

Get the latest version of Python at https://www.python.org/downloads/ or with your operating system’s package manager.

### installs Django

This is the recommended way to install Django:

```
$ python -m pip install Django
$ python -m pip install -e django/
```

### Connecting Databases with Django project MySQLClient

Install mysqlclient using pip-

```
$pip install mysqlclient
```

Create a database in MySQL, Open MySQL command line client

```
mysql1> CREATE DATABASE matcher
```

## Run the server

Open PowerShell in the project.

Apply the migrations: (make sure you have a local MySQL running)

```
$ python manage.py migrate
```

Run the development server:

```
$ python manage.py runserver
```

By default, the runserver command starts the development server on the internal IP at port 8000.

### Models diagram

![image](https://user-images.githubusercontent.com/44950256/175806962-fba61345-29c0-4dd5-b882-a67d9cf5819a.png)

## Server -

The server implemented using Django and provide one endpoint.

### Search route

This endpoint provides search mechanism for candidates.

```
GET/matcherProject/findBestCandidates/?job_title =${JOB_TITLE}
```

The response is a list of candidates if there are ones

### For example

#### Request -

```
GET/matcherProject/findBestCandidates/?job_title=software developer
```

#### Response-

(1, 'software developer')
(2, 'software developer')

## Bonus:

When I got this task, I started to read a little bit about full text search and indexing,
I understand that these topics are not so familiar with rational DBs.
in addition, Django framework at its current version doesn’t have full support to full text search.
As a result, in my solution, I wrote SQL Hard coded, which is wrong in my opinion.
But I am happy to be exposed to these interesting topics.
