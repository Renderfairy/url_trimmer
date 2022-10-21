# URL Trimmer App

Simple url shortener app written in Python Django

### Features:
- Users registration
- Url shorening
- Storing shortened URLs

### How to run
1. Clone repo 
2. Copy .env-default and fill in required environmental variables in env directory.
3. For pip create new virtual environment
```cmd
pip install -r reqirements.txt
```
or
```cmd
pipenv install
```

4. Create PostgreSQL database with name from env/.env
5. Run
```cmd
python manage.py migrate
```

6. Run
```cmd
python manage.py runserver
```
7. Start using.

### Test
The app has about 80% coverage in tests

To run:
```cmd
pytest
```



