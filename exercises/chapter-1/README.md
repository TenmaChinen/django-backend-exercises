# Chapter 1 : Save basic Records

## Exercise 1 - JSON Data
- Load the JSON data from `data.json` using `json` library.

## Exercise 2 - Saving Book Categories
```json
{
    "categories": [
        {"id": 1, "name": "Fantasy"},
        {"id": 2, "name": "Mystery"},
        {"id": 3, "name": "Horror"},
        {"id": 4, "name": "Adventure"},
        {"id": 5, "name": "Sci-Fi"},
      ],
}
```
- Import the Category Model
- Get the `categories` list from the loaded dictionary.
- For loop over categories list.
- Save every category assigning the `id` and the `name` in Django database.

## Exercise 3 - Display Saved Categories
- Import the Category Model
- Get all the categories from database
- Iterate over the queryset and print the category `id` and `name` fields.

## Exercise 4 - Update `Sci-Fi` Category

- Import the Category Model
- Get `Sci-Fi` record using `filter` by the `id` (which is `5`).
- Check if exists.
- If the `Sci-Fi` record exists, update the name to `Science-Fiction`.
- Print all categories name to check that `Sci-Fi` has been updated.

## Exercise 5 - Delete `Science-Fiction` Category

- Import the Category Model
- Using `filter` method, get the `Science-Fiction` record by the `name`, not the `id`.
- Check if exists.
- If the `Science-Fiction` record exists, delete it.
- Print all categories name to check that `Science-Fiction` has been deleted.

## Exercise 6 - Save Authors JSON list
```json
{
    "authors": [
        {"id": 1, "name": "J.K. Rowling"},
        {"id": 2, "name": "Tolkien"},
        {"id": 3, "name": "Stephen King"}
    ],
}
```
- Import the Author Model
- Load the `data.json` and get the `authors` list.
- Iterate over each `author_data` and use the `dictionary unpacking` or `keyword arguments unpacking` to set the Author instance.
```py
author = `Author( **author_data )`
```
- Display every author saved in Django database.