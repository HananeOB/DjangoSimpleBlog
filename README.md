# BlogProject

## How to set up

### Manual setup
Firstly, create a new directory and change to it:
```
mkdir blog-django && cd blog-django
```
Then, clone this repository to the current directory:
```
git clone https://github.com/HananeOB/BlogProject .
```

The database used for this project is SQLite.

Next, set up a virtual environment and activate it:
```
python -m venv env && source env/bin/activate
```
Install required packages:

`pip3 install -r requirements.txt`

Next, perform migration:
```
python manage.py migrate 
```
The setup is complete. Run a local server with
```
python manage.py runserver 
```
The blog should be available at localhost:8000.

The admin should be available at localhost:8000/admin.
