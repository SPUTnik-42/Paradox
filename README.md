# [PARADOX](https://paradox-hunt-2.herokuapp.com/)
> Paradox is website made for online Cryptic hunt through python django by [Ushnik Nath](https://www.ushniknath.com/). This is made as the capstone project for CS50 course on edx


## Visit the app at https://paradox-hunt-2.herokuapp.com/

### watch youtube video at https://www.youtube.com/watch?v=FL1t7KqMxF8

## Functionality

- Login/Logout (authentication)
- Registrations
- User Profile Page
- Question page
- Hint Page
- Leaderboard
- Admin Functions
  - Log Page (shows the answer log of each participant real time)
  - Disqualification of teams
- Django Admin Functions
  - Modify the database tables
 
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Paradox.

```bash
pip install virtualenv
```
```bash
virtualenv capstone_env
```

```bash
source capstone/Scripts/activate
```

```bash
pip install -r requirements.txt
```

```bash
python manage.py runserver
```



> For viewing the admin function use the username test_7 and the password poo@onastick


## Distinctiveness and Complexity
>
>This project is different from any of the previous projects, it is made for in an entirely new genre of websites ,i.e a type of quiz website where the user and the website give input and react in real time. This project was insiped by the lack of python based websites in our school technology club, although it is primarily made for CS50 but it is ready for deployment for real world use. It never can be categorized under the bracket of the previous projects submitted
>
>This project uses more than 5 tables in the database, with more than three interconnected fields and tables, it includes more than 8 views in the app directory and has adequate number of html and css files. Most of the backend is in python or the django template language.The authentication and registration is fully secured using hashed passwords and other security measures.

## Files and Directory

- capstone
  - settings.py : general settings for the django app , specially configured for deployment
  - urls.py : url for the admin, genreal view and static files
- paradox
  - migrations: different migrations into the database taken into account during the process of making the app
  - static : contains all the css and image files
  - templates : containes all the html files made with django template language
  - admin.py : registers the tables so that it can be viewed in the admin page
  - models.py : containes all the table models for the database
  - urls.py : contains all the url for the general view i.e most of the url paths are stored here
  - views.py : contains all the view functions so that the templates can be rendered
- staticfiles: contains all the css and image files for deployment (made using collectstatic command)
- db.sqlite3 : the actual database made using sqlite3
- procfile: deployment purposes
- requirements.txt: contains all the dependencies and modules used in the project

>
> Some of the files and folders have been ommited from the directory structure as they dont hold significant value in the project except for specific machine they are used in 


## I hope that you have enjoyed the project and tried it out yourself.....


[ 😘 Ushnik Nath](https://www.ushniknath.com/)