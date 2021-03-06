# Mysite

## Installation
#### _instruction edited from https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-14-04_

### Requirements
An ubuntu 16.04 server with a non root account which has access to sudo.

### Lets install all the things
Update all of the respositorys and install the required packages
```bash
sudo apt-get update
sudo apt-get install python3 python3-dev libpq-dev postgresql postgresql-contrib nginx python3-venv
```

### Setup the Database
We will be using a PostgreSQL database.

login as the postgres user then loginto postrgreSQL. the account was created when you installed postgresql. All SQL commands **MUST** end with a semicolon (;)
```bash
sudo su - postgres 
psql
```

now craete the database
```SQL
CREATE DATABASE mysite;
```

then create a user which will allow us to interface with the database from django. We will be giving the account full access to the database. put your derired account password where it says -insert-password-here-. You need to surround it with single quotes.
```SQL
CREATE USER mysiteadmin WITH PASSWORD '-insert-password-here-';
GRANT ALL PRIVILEGES ON DATABASE mysite TO mysiteadmin;
```

now close psql by typing `\q` and log out of the postgres account by typing `exit`

### Setup django
now you need to clone my git reposiotry. This contains the django framework and all of the templates etc.
```bash
git clone https://www.github.com/lukespademan/mysite.git
cd mysite
```

next is creating the virtual environemnt, activiating it and installing the python packages
```bash
python3 -m venv venv
source venv/bin/activate
```
if you are on a development machine run `pip install -r dev_requirements.txt` but if you are on a production machine run `pip instal -r prod_requirements.txt`

you now need to create a database supersuser (which you will use to log into the admin interface) and run collect static (which puts all of the static files i.e. css, js, img in one place so that you webserver i.e. nginx and gunicorn can find them

```bash
./manage.py createsuperuser
./manage.py collectstatic
```

### running the server
if you are on a dev machine, all you need to do the run the server is type `python manage.py runserver` and then navigate to 127.0.0.1:8000 in your webbrowser to access it. but if you are on a production server you need to carry on following this tutorial.

type `deactivate` to exit the virtual environment.
