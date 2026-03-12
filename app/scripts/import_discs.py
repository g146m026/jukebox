import csv
import sqlite3
import re
from ..config import Config

def normalize_disc(row):
    # Slot
    slot = row.get('Disc') or row.get('slot') or row.get('slot_number')
    if slot:
        try:
            slot = int(slot)
        except Exception:
            slot = None
    # Artiste
    artist = row.get('Artiste') or row.get('artist')
    if artist:
        artist = artist.strip()
    # Album
    album = row.get('Album') or row.get('album')
    if album:
        album = album.strip()
    # Année
    year = row.get('year')
    if not year and album:
        # Recherche année dans album
        match = re.search(r'(19\d{2}|20\d{2})', album)
        if match:
            year = match.group(1)
    if year:
        try:
            year = int(year)
        except Exception:
            year = None
    # Genre
    genre = row.get('genre')
    if genre:
        genre = genre.strip()
    # Notes
    notes = row.get('notes')
    if notes:
        notes = notes.strip()
    return slot, artist, album, year, genre, notes

def import_discs(csv_path):
    conn = sqlite3.connect(Config.DB_PATH)
    cursor = conn.cursor()
    # Création des tables si absentes
    cursor.execute('''CREATE TABLE IF NOT EXISTS discs (
        slot_number INTEGER PRIMARY KEY,
        artist TEXT,
        album TEXT,
        year INTEGER,
        genre TEXT,
        notes TEXT
    )''')
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            slot, artist, album, year, genre, notes = normalize_disc(row)
            if slot and (artist or album):
                cursor.execute("INSERT OR IGNORE INTO discs (slot_number, artist, album, year, genre, notes) VALUES (?, ?, ?, ?, ?, ?)",
                    (slot, artist, album, year, genre, notes))
    conn.commit()
    conn.close()

def main():
    import_discs("/workspaces/jukebox/Feuille de calcul sans titre - Feuille 1.csv")
    print("Import terminé.")

if __name__ == "__main__":
    main()
