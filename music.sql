CREATE TABLE artist (artist_id INTEGER PRIMARY KEY ASC,
                     artist_name TEXT);

CREATE TABLE albums (album_id INTEGER PRIMARY KEY ASC,
                     artist_id INTEGER,
                     album_title TEXT);

CREATE TABLE songs (song_id INTEGER PRIMARY KEY ASC,
                    song_name TEXT,
                    album_id INTEGER,
                    artist_id INTEGER,
                    track_number INTEGER,
                    song_length INTEGER);
