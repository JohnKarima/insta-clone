# Project Name 
InstaClone

# Project Description 
- A clone of the website for the popular photo app Instagram.

# Link to Live Project
- https://instaclone343.herokuapp.com

# Author 
- [John Karima](https://github.com/JohnKarima)

# Setup Instructions 

### Cloning
```
$ git clone https://github.com/JohnKarima/insta-clone
```
### Move into directory and install requirements
```
$ cd insta-clone

$ pip install -r requirements.txt 
```
### Install and activate a Virtual Environment
```
$ python3 -m venv virtual 

$ source virtual/bin/activate  
```
### Set-up a Database
```
Set your database User and Password 
```
### Make Migrations & Migrate
```
$ python manage.py makemigrations <DB Name> 

$ python manage.py migrate 
```
### Run the application
```
python manage.py runserver 
```
### Run the test for the application
```
$ python3 manage.py test instaapp
```

# Technologies Used
- Python
- Django
- Bootstrap
- pillow
- cloudinary
- crispy forms

# Contact Information
karimajohn24@gmail.com

# License Copyright 
- 2020, John Karima.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

