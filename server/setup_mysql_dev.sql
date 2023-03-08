#!/usr/bin/env bash

-- setting up MySQL enviroment
-- creating database namCREATE DATABASE IF NOT EXISTS $MYSQL_DB;
CREATE DATABASE IF NOT EXISTS Event_db;
CREATE USER IF NOT EXISTS 'Nat'@'localhost' IDENTIFIED BY 'NATSEIKWA510';
-- granting the new user created all privileges
GRANT ALL PRIVILEGES ON Event_db.* TO 'Nat'@'localhost';
FLUSH PRIVILEGES;
-- granting the select privilege to the user
GRANT SELECT ON performance_schema.* TO 'Nat'@'localhost';
FLUSH PRIVILEGES;
GRANT USAGE ON *.* TO 'Nat'@'localhost';
