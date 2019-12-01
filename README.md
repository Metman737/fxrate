# fxrate

### How to load test data into the database

Clear old data from databse:
```
python3 manage.py sqlflush | python3 manage.py dbshell
```

Load fixtures for user table:
```
python3 manage.py loaddata home/fixtures/users.json
```

Make sure you have loaded the user fixtures properly than, load fixtures for post table:
```
python3 manage.py loaddata home/fixtures/post.json
```
You will now have test data in your database.