# Chapter 2 : Save Records with Foreign Fields

## Exercise 1 - Save `Book` JSON data to Django database

```json
{
    "books": [
        {"id": 1, "title": "Harry Potter and the Sorcerer's Stone", "author": 1, "categories": [1, 2]},
        {"id": 2, "title": "Harry Potter and the Chamber of Secrets", "author": 1, "categories": [1, 2]},
        {"id": 3, "title": "Harry Potter and the Prisoner of Azkaban", "author": 1, "categories": [1, 2]},
        {"id": 4, "title": "The Lord of the Rings: The Fellowship of the Ring", "author": 2, "categories": [1, 4]},
        {"id": 5, "title": "The Lord of the Rings: The Two Towers", "author": 2, "categories": [1, 4]},
        {"id": 6, "title": "The Lord of the Rings: The Return of the King", "author": 2, "categories": [1, 4]},
        {"id": 7, "title": "It", "author": 3, "categories": [2, 3]},
        {"id": 8, "title": "The Shining", "author": 3, "categories": [3]},
        {"id": 9, "title": "Carrie", "author": 3, "categories": [2, 3]}
    ]
}
```

- Load the JSON data from `data.json`
- Save each book with only `id`, `title` and `author` ❗ ( Author must be instance )
- Display all the saved books `id` and `title`


## Exercise 2 - Get `Book` `Categories` ( ManyToMany Foreign Field )

- Import `Book` and `Category` models.
- Load the JSON data from `data.json`
- Iterate over the JSON `books` list
- Use single `filter` query to get `Category` instances from each book `categories` list.
```json
{
    "id": 9,
    "title": "Carrie",
    "author": 3,
    "categories": [2, 3] // <=== This are the Categories Id
}
```
```py
# Use the "fieldname__in" query to retrieve several instances that matches what is in the list
queryset = Category.object.filter( id__in = [2,3] )
```
- Iterate over the categories and print the `title` of the Book and each categories `name` 

## Exercise 3 - Update `Category` `ManyToMany Foreign Key` from each `Book`
- Import `Book` and `Category` models.
- Load the JSON data from `data.json`
- With book `id` from JSON `books` list, use `filter` method on `Book` Model to get the existing `book` instance from database.
- Check if the `Book` record exists.
- Use single `filter` query to get `Category` instances from each book `categories` list.
- Check if the `Category` queryset exists.
- If the queryset exists, set all the `Category` instances to the `category` field of `book` instance.
```py
# To set several instances on
book.category.set( queryset )
```
- Check if categories are saved quering and printing them in another loop.
```py
# To grab all the categories from book instance
queryset = book.categry.all()
```