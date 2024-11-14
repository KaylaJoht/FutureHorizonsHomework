use song;


INSERT INTO album VALUES(null, "Origin of Symmetry", "2001/06/18", "Alternative Rock");
INSERT INTO album VALUES(null, "Pure Heroine", "2013/09/27", "Electronika");
INSERT INTO album VALUES(null, "Future Nostalgia", "2020/04/27", "Dance Pop");

INSERT INTO artist VALUES(null, "MUSE");
INSERT INTO artist VALUES(null, "Lorde");
INSERT INTO artist VALUES(null, "Dua Lipa");

INSERT INTO song VALUES(null, "New Born", 363, 1);
INSERT INTO song VALUES(null, "Bliss", 251, 1);
INSERT INTO song VALUES(null, "Space Dementia", 380, 1);
INSERT INTO song VALUES(null, "Hyper Music", 201, 1);
INSERT INTO song VALUES(null, "Plug in Baby", 218, 1);
INSERT INTO song VALUES(null, "Citizen Erased", 441, 1);
INSERT INTO song VALUES(null, "Micro Cuts", 218, 1);
INSERT INTO song VALUES(null, "Screenager", 260, 1);
INSERT INTO song VALUES(null, "Darkshines", 286, 1);
INSERT INTO song VALUES(null, "Feeling Good", 198, 1);
INSERT INTO song VALUES(null, "Megalomania", 279, 1);
INSERT INTO song VALUES(null, "Futurism", 211, 1);

INSERT INTO song VALUES(null, "Tennis Court", 198, 2);
INSERT INTO song VALUES(null, "400 Lux", 234, 2);
INSERT INTO song VALUES(null, "Royals", 250, 2);
INSERT INTO song VALUES(null, "Ribs", 258, 2);
INSERT INTO song VALUES(null, "Buzzcut Season", 246, 2);
INSERT INTO song VALUES(null, "Team", 193, 2);
INSERT INTO song VALUES(null, "Glory and Gore", 210, 2);
INSERT INTO song VALUES(null, "Still Sane", 188, 2);
INSERT INTO song VALUES(null, "White Teeth Teens", 216, 2);
INSERT INTO song VALUES(null, "A World Alone", 296, 2);
INSERT INTO song VALUES(null, "No Better", 170, 2);
INSERT INTO song VALUES(null, "Bravado", 221, 2);
INSERT INTO song VALUES(null, "Million Dollar Bills", 138, 2);
INSERT INTO song VALUES(null, "The Love Club", 201, 2);
INSERT INTO song VALUES(null, "Biting Down", 213, 2);
INSERT INTO song VALUES(null, "Swingin Party", 222, 2);

INSERT INTO song VALUES(null, "Future Nostalgia", 184, 3);
INSERT INTO song VALUES(null, "Don't Start Now", 183, 3);
INSERT INTO song VALUES(null, "Cool", 209, 3);
INSERT INTO song VALUES(null, "Physical", 193, 3);
INSERT INTO song VALUES(null, "Levitating", 203, 3);
INSERT INTO song VALUES(null, "Pretty Please", 194, 3);
INSERT INTO song VALUES(null, "Hallucinate", 208, 3);
INSERT INTO song VALUES(null, "Love Again", 258, 3);
INSERT INTO song VALUES(null, "Break My Heart", 221, 3);
INSERT INTO song VALUES(null, "Good in Bed", 218, 3);
INSERT INTO song VALUES(null, "Boys Will Be Boys", 166, 3);

Insert Into album_artist VALUES(1,1);
Insert Into album_artist VALUES(2,2);
Insert Into album_artist VALUES(3,3);

select artist.artist_name, album.album_name from album_artist 
INNER JOIN artist 
ON album_artist.artist_id = artist.artist_id
INNER JOIN album
ON album.album_id = album_artist.album_id;

describe album_artist;