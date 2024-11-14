drop database song;
create database song;

use song;

create table Album
(
	album_id int PRIMARY KEY auto_increment,
    album_name varchar(100),
    release_date DATE,
    album_genre varchar(20)
);

create table Song (
	song_id int PRIMARY KEY auto_increment,
    song_name varchar(100),
    length_sec int,
    album_id int,
    FOREIGN KEY (album_id) references Album(album_id)
);

create table Artist
(
	artist_id int PRIMARY KEY auto_increment,
    artist_name varchar(100)
);

create table Album_Artist
(
	artist_id int NOT NULL,
    album_id int NOT NULL,
    FOREIGN KEY (artist_id) references Artist(artist_id),
    FOREIGN KEY (album_id) references Album(album_id)
);



