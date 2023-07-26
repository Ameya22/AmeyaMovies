## The Django movies app. 
## Install python3 if not installed before running following commands
```
$ python -m venv venv
$ source venv/Scripts/activate
$ pip install -r requirements.txt
$ cd imdb
$ python manage.py migrate
$ python manage.py collectstatic
$ python manage.py runserver

```

# AND your project running on local development server. 
# Go to your web browser & type http://127.0.0.1:8000/movies
