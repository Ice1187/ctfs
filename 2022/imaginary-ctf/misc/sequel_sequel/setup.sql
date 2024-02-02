CREATE USER 'ethan'@'127.0.0.1' IDENTIFIED BY 'p4ssw0rd10';
CREATE DATABASE ictf;
USE ictf;
CREATE TABLE ictf (flag varchar(255));
INSERT INTO ictf (flag) VALUES ('ictf{REDACTED}');
GRANT SELECT ON ictf.ictf TO 'ethan'@'127.0.0.1'
