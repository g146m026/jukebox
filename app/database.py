import sqlite3
from app.config import Config

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(Config.DB_PATH, check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS discs (
            slot_number INTEGER PRIMARY KEY,
            artist TEXT,
            album TEXT,
            year INTEGER,
            genre TEXT,
            notes TEXT
        )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS tracks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            slot_number INTEGER,
            track_number INTEGER,
            title TEXT,
            duration TEXT
        )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            slot_number INTEGER,
            track_number INTEGER
        )''')
        self.conn.commit()

    def get_connection(self):
        return self.conn
