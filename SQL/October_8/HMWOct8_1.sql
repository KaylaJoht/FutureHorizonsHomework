CREATE DATABASE dcl_db;

CREATE USER 'user1' IDENTIFIED BY '123';

use dcl_db;

CREATE TABLE temp
(
	num INT,
    letter CHAR(1)
);

INSERT INTO temp VALUES(1, 'A');
INSERT INTO temp VALUES(2, 'B');

GRANT SELECT on dcl_db.* to 'user1';