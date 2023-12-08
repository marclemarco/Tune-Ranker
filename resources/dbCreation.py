import sqlite3

conn = sqlite3.connect('resources/dataBase.db')
c = conn.cursor()

#c.execute('''
#    DROP TABLE artist;
#    DROP TABLE albums;
#    DROP TABLE tunes;
#    DROP TABLE creates;
#''')

c.execute('''
    CREATE TABLE IF NOT EXISTS artists (
        artistID INTEGER PRIMARY KEY,
        name TEXT,
        note REAL
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS albums (
        albumID INTEGER PRIMARY KEY,
        title TEXT,
        releaseDate TEXT,
        note REAL,
        review TEXT   
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS tunes (
        tuneID INTEGER PRIMARY KEY,
        albumID INTEGER,
        title TEXT,
        note REAL,
        review TEXT   
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS albums (
        artistID INTEGER,
        albumID INTEGER,
        PRIMARY KEY (
            artistID, albumID
        )  
    )
''')

conn.close()