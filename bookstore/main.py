from flask import Flask, render_template
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

@app.route('/')
def home():
    return render_template('index.html', books = all_books)

if __name__ == "__main__":
    app.run(debug=True)