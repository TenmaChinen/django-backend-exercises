# django-backend-exercises

# Setup

1. Download the whole project
```
    repository
    ├── exercises
    │   ├── chapter-1
    │   │   │
    │   │   ├── exercise-1.py
    │   │   ├── ··
    │   │   ├── exercise-6.py
    │   │   │
    │   │   ├── solutions
    │   │   │   ├── solution-1.py
    │   │   │   ├── ···
    │   │   │   └── solution-6.py
    │   │   │
    │   │   ├── data.json
    │   │   └── ···
    │   │
    │   ├── ···
    │   ├── chapter-N
    │   ├── reset-db.bat
    │   └── setup-db.bat
    │   
    ├── mock-project <-- Ignore This
    ├── setup <-- Ignore This
    └── README.md <-- Ignore This
```
2. Open the `exercises` folder
3. Execute `setup-db.bat` to create the database for the Django project.
4. Make every chapter in the proper order because future chapters may be dependant on past ones.
4. If database starts to corrupt or appear strange records, execute the `reset-db.bat` files.

# Summary

## Chapter 1
[Click here to see the  Exercises](https://github.com/TenmaChinen/django-backend-exercises/tree/main/exercises/chapter-1)
1. How to load a JSON file using `json` module.
2. Save new records in Django database assigning the fields one by one-
3. Save new records using dictionary unpacking to code faster.

## Chapter 2
[Click here to see the  Exercises](https://github.com/TenmaChinen/django-backend-exercises/tree/main/exercises/chapter-2)
1. Get multiple records from an ID list using a single Query.
2. Learn how to save new records that contains