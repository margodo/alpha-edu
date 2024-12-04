from flask import Flask, render_template, request
from bookstore_objects import *

bookstore_db = Bookstore('bookstore.db')

bookstore_db.create_table(table_name='bookstore', columns={
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "title": "TEXT",
        "author": "VARCHAR(255)",
        "year": "DATE",
        "genre": "TEXT",
        "price": "REAL",
        "amount": "INTEGER",
    })

# bookstore_db.add_book(
#     table_name='bookstore',
#     data = [
#         (None, 'Anna Karenina', 'Lev Tolstoj', '2022-10-21','Novel', 2100.50, 7),
#         (None, 'Crime and Punishment', 'Fyodor Dostoevsky', '2018-06-15','Novel', 1980.00, 10),
#         (None, 'Romeo and Juliette', 'William Shakespeare', '2020-02-28','Tragedy', 2050.40, 4),
#         (None, 'The Old Man and the Sea', 'Ernest Hemingway', '2016-04-14','Novel', 2430.70, 2),
#         (None, 'Lolita', 'Vladimir Nabokov', '2021-01-10','Novel', 1990.00, 5),
#         (None, 'The Autobiography of Benjamin Franklin', 'Benjamin Franklin', '2008-08-22','Autobiography', 2540.10, 4),
#         (None, 'Woe from Wit', 'Alexander Griboedov', '2015-12-14','Comedy', 1750.80, 9),
#         (None, 'Poems', 'Sergey Yesenin', '2017-03-11','Poem', 1670.50, 10),
#         (None, 'The Count of Monte Cristo', 'Alexandre Dumas', '2011-11-11','Novel', 4300.40, 4),
#         (None, 'All Quiet on the Western Front', 'Erich Maria Remarque', '2012-06-27','Autobiographical novel', 2230.10, 8),
#         (None, 'Hamlet', 'William Shakespeare', '2014-09-10','Tragedy', 1800.20, 1)
#     ])

all_books = bookstore_db.all_books(table_name='bookstore')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST" and '_method' not in request.form:
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        genre = request.form['genre']
        found_book = bookstore_db.search_book(
            table_name='bookstore', 
            condition=f"title= '{title}' and author='{author}' and year = '{year}' and genre='{genre}'"
        )
        return render_template('index.html', search_result=True, book=found_book[0])
    if request.method == 'POST' and '_method' in request.form and request.form['_method'] == 'PUT':
        id = request.form['id']
        desired_book = bookstore_db.search_book(table_name='bookstore', condition=f'id={id}')
        amount = desired_book[0][-1]
        if amount > 0:
            bookstore_db.update_books(
                table_name='bookstore',
                updates=f'amount = {amount-1}',
                condition=f'id={id}'
            )
            message = "Thank you for purchase"
        else:
            bookstore_db.delete(table_name='bookstore', condition=f'id={id}')
            message = "Sorry, this book is out of stock."
        return render_template('index.html', message=message)
    all_books = bookstore_db.all_books(table_name='bookstore')
    return render_template('index.html', books=all_books, search_result=False)

if __name__ == "__main__":
    app.run(debug=True)

bookstore_db.close_connection()