from app.database import Database
from app.models import Disc, Track

class LibraryService:
    def __init__(self):
        self.db = Database().get_connection()

    def get_all_discs(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM discs")
        return [Disc(**row) for row in map(lambda x: dict(zip([c[0] for c in cursor.description], x)), cursor.fetchall())]

    def search_discs(self, query: str):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM discs WHERE artist LIKE ? OR album LIKE ? OR slot_number LIKE ?", (f"%{query}%", f"%{query}%", f"%{query}%"))
        return [Disc(**row) for row in map(lambda x: dict(zip([c[0] for c in cursor.description], x)), cursor.fetchall())]

    def get_disc(self, slot: int):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM discs WHERE slot_number=?", (slot,))
        row = cursor.fetchone()
        if row:
            return Disc(**dict(zip([c[0] for c in cursor.description], row)))
        return None

    def get_tracks(self, slot: int):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM tracks WHERE slot_number=?", (slot,))
        return [Track(**row) for row in map(lambda x: dict(zip([c[0] for c in cursor.description], x)), cursor.fetchall())]
