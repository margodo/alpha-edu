import sqlite3

class QuoteDB:
    def __init__(self):
        self.connection = sqlite3.connect("quotes.db", check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS quotes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                quote TEXT,
                author TEXT
            )
        ''')
        self.connection.commit()

    def save_quote(self, user_id, quote, author):
        self.cursor.execute('''
            INSERT INTO quotes (user_id, quote, author)
            VALUES (?, ?, ?)
        ''', (user_id, quote, author))
        self.connection.commit()

    def get_saved_quotes(self, user_id):
        self.cursor.execute('''
            SELECT quote, author FROM quotes WHERE user_id = ?
        ''', (user_id,))
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
