#   Resume-Builder

## Clone the project

```bash
Project Root Directory: `/home/projects/
git clone <remote url>
git clone <git@github.com:Ashuthoughtwin/resumemaker.git>
```
##  Change into project directory

```bash
cd <project_name>
```
##  Create Environment file
Go to the Project DIR folder then create .env file with below contents :-

```bash
'NAME': 'my_db',
'USER': 'user',
'PASSWORD': 'password',
'HOST': 'localhost',
'PORT': '5432',
```
##  Install Python

```bash
sudo apt-get update && sudo apt-get install python3.7 virtualenv
```
## Activate the environment
```bash
source venv/bin/activate
```
##  Install Dependencies

```bash
pip install -r requirements.txt
```

## Install PostgreSQL
###  If we need postgres :

```bash
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -sc)-pgdg main" > /etc/apt/sources.list.d/PostgreSQL.list'
sudo apt-get update
sudo apt-get install postgresql-latest
```
##  Migrate Database

```bash
python manage.py makemigrations
python manage.py migrate
```
## Create super user

```bash
python manage.py createsuperuser
```

##  Finally, run the development server(Local server):

```bash
python manage.py runserver
```
Note:The project will be available at --> 127.0.0.1:8000

## Procfile
```bash
web: gunicorn resume_maker.wsgi
```
## Features

- It tracks all the information of Job, Jobseeker, Skills ect.
- Manage the information of Job. Shows the information and description of the Resume.
- All the fields such as Resume, Individual, Qualification are validated and does not   take invalid values.
- There are choices available for resume format for users as per their qualification   and requirements.
- Export documents as PDF.

