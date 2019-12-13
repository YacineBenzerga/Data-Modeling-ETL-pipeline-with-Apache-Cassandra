

# Create queries
create_song_lib = "CREATE TABLE IF NOT EXISTS song_library "
create_song_lib += "(sessionId int, itemInSession int,artist text,song text,length float,PRIMARY KEY (sessionId, itemInSession))"

create_artist_user_lib = "CREATE TABLE IF NOT EXISTS artist_user_library "
create_artist_user_lib += "(itemInSession int, artist text, song text, firstName text, lastName text, userId int, sessionId int,PRIMARY KEY(userId,sessionId,itemInSession))"


create_user_song_lib = "CREATE TABLE IF NOT EXISTS user_per_song "
create_user_song_lib += "(firstName text, lastName text, song text, PRIMARY KEY(song))"


# Insert queries
insert_song_lib = "INSERT INTO song_library (sessionId,itemInSession,artist,song,length)"
insert_song_lib += "VALUES (%s,%s,%s,%s,%s)"

insert_artist_user_lib = "INSERT INTO artist_user_library (itemInSession,artist,song,firstName,lastName,userId,sessionId)"
insert_artist_user_lib += "VALUES (%s,%s,%s,%s,%s,%s,%s)"

insert_user_song_lib = "INSERT INTO user_per_song (firstName,lastName,song)"
insert_user_song_lib += "VALUES (%s,%s,%s)"
