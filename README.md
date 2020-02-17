# fxrate

## ToDo:

- https://simpleit.rocks/python/django/generating-slugs-automatically-in-django-easy-solid-approaches/
- Homepage Währungstabelle nur 6 Reihen anzeigen
- Homepage 3 Posts nebeneinander
- Sprache Übersetzungen
- Durchschnitt von Währung errechnen und anzeigen 
- Windows flagge anzeigen
- Link zu anderen Websites
 

## ToRead:

- https://realpython.com/django-redirects/#django-redirects-a-super-simple-example

## Create fixture out of database data 

Load data from database into a fixture:
```
python3 manage.py dumpdata app.model --indent 5 > name.json
```

## Load test data into the database

Clear old data from databse:
```
python3 manage.py sqlflush | python3 manage.py dbshell
```

Load fixtures for user table:
```
python3 manage.py loaddata fixtures/users.json
```

Make sure you have loaded the user fixtures properly than, load fixtures for post table:
```
python3 manage.py loaddata blog/fixtures/posts.json
```
You will now have test posts in your database.

Insert 4 images into the media folder named like:
- fixture1.jpg 
- fixture2.jpg 
- fixture3.jpg 
- fixture4.jpg 

For currency exchange table do the following: 
```
python3 manage.py loaddata exchange/fixtures/currency.json
python3 manage.py loaddata exchange/fixtures/exchange-rate.json
```

## Make languages available 

To make translation files
```
django-admin makemessages --ignore venv  
```

To make changes in translations files available
```
msgfmt -o locale/de/LC_MESSAGES/django.mo locale/de/LC_MESSAGES/django.po
msgfmt -o locale/fa/LC_MESSAGES/django.mo locale/fa/LC_MESSAGES/django.po
```