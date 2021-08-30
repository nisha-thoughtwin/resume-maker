# resume-builder
##Backend python code

## Clone the project
Clone the project:
```bash
Project Root Directory: `/home/projects/
git clone <remote url>
git clone <git@github.com:Ashuthoughtwin/resumemaker.git>
```
##  Change into project directory

```bash
cd <project_name>
```

## Features

- It tracks all the information of Job, Jobseeker, Skills ect.
- Manage the information of Job. Shows the information and description of the Resume.
- All the fields such as Resume, Individual, Qualification are validated and does not   take invalid values.
- There are choices available for resume format for users as per their qualification   and requirements.
- Export documents as PDF.

##  Create Environment file
Go to the Project DIR folder then create .env file with below contents :-

```bash
'NAME': 'my_db',
'USER': 'admin',
'PASSWORD': 'server@2020',
'HOST': 'localhost',
'PORT': '5432',
```
Note : Copy above data and paste it in the setting.py file and change the db data according to your db creadentials.
Note : Make sure not to push the settings file in repo

##  Install Python

```bash
sudo apt-get update && sudo apt-get install python3.7 virtualenv
```
## Activate the environment
```bash
source venv/bin/activate
```

## Install PostgreSQL
##  If we need postgres :

```bash
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -sc)-pgdg main" > /etc/apt/sources.list.d/PostgreSQL.list'
sudo apt-get update
sudo apt-get install postgresql-latest
```
## Another Database
##  DB squlite
```bash
'ENGINE': 'django.db.backends.sqlite3',
'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
```
##  Install Dependencies

```bash
pip install -r requirements.txt
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
##  Finally, run the development server(Hosting server):
```bash
http://3.129.249.97/
```

## Procfile
```bash
web: gunicorn resume_maker.wsgi
```


