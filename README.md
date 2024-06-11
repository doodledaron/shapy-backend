-# Django Project - Shapy Backend

This is a project built with Django and REST Framework

## Table of Contents

- [Project Setup](#project-setup)
- [Apps](#apps)
- [Features](#features)

## Project Setup

1. create virtual environment (after cloneing)
```
pipenv shell
```

2. install dependencies from requirements 
```
pip install -r requirements.txt
```

3.database configurations (settings.py)
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER' : 'your_database_user',
        'PASSWORD' : 'your_database_user_password',
        'HOST' : '127.0.0.1',
        'PORT' : '3306'
    }

}
```

4. make migrations and migrate
```
python manage.py makemigrations
python manage.py migrate
```

5. run server
```
python manage.py runserver
```


## Apps
### main
Django app for admin panel

### main_user
Django app for user panel


## Features
### Djoser Token Based Authentication
- Simple token authentication are used for login/signup. No additional authentication features such as reset password, rememeber user, etc.
- No password rules are set, default is used
   
### Real time udpates between admin panel and user panel using Websockets
- Signals in main(admin) will detect changes everytime admin add/edit/delete the Shape model
- The websocket will receive update and update the UI automatically
  





