# 0x0E. SQL - More queries
This project is a continuation of the SQL introduction project. It covers more topics and concepts related to SQL and relational databases, such as creating and managing users, privileges, primary keys, foreign keys, constraints, subqueries, joins, and unions.

![sql](https://i.ibb.co/CHTTCR6/blob-1.jpg)

## Requirements
- All files are executable and tested on `Ubuntu 14.04 LTS` using `MySQL 5.7` (version 5.7.8-rc)
- All SQL queries follow the MySQL style guide
- All SQL queries are commented

## Install MySQL 8.0 on Ubuntu 20.04 LTS
```
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.28-0ubuntu0.20.04.3 for Linux on x86_64 ((Ubuntu))
$
```
Connect to your MySQL server:
```
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 13
Server version: 8.0.28-0ubuntu0.20.04.3 (Ubuntu)

Copyright (c) 2000, 2022, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```
## Files
The following files are scripts that perform various SQL tasks:

| File	| Description |
| ---   | ---         |
| [0-privileges.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/0-privileges.sql)	| List all privileges of the users user_0d_1 and user_0d_2 |
| [1-create_user.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/1-create_user.sql)	| Create the user user_0d_1 with all privileges and password user_0d_1_pwd |
| [2-create_read_user.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/2-create_read_user.sql)	| Create the database hbtn_0d_2 and the user user_0d_2 with password user_0d_2_pwd and SELECT privilege on the database hbtn_0d_2 |
| [3-force_name.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/3-force_name.sql)	| Create the table force_name with id (INT) and name (VARCHAR(256), not null) |
| [4-never_empty.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/4-never_empty.sql)	| Create the table id_not_null with id (INT, default value = 1) and name (VARCHAR(256)) |
| [5-unique_id.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/5-unique_id.sql)	| Create the table unique_id with id (INT, default value = 1, must be unique) and name (VARCHAR(256)) |
| [6-states.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/6-states.sql)	| Create the database hbtn_0d_usa and the table states with id (INT, unique, auto-generated, not null, primary key) and name (VARCHAR(256), not null) |
| [7-cities.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/7-cities.sql) 	| Create the database hbtn_0d_usa and the table cities with id (INT, unique, auto-generated, not null, primary key), state_id (INT, not null, foreign key that references to id of the states table) and name (VARCHAR(256), not null) |
| [8-cities_of_california_subquery.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/8-cities_of_california_subquery.sql)	| List all the cities of California that can be found in the database hbtn_0d_usa, ordered by ascending city id |
| [9-cities_by_state_join.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/9-cities_by_state_join.sql)	| List all cities contained in the database hbtn_0d_usa, ordered by ascending city id |
| [10-genre_id_by_show.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/10-genre_id_by_show.sql)	| List all shows contained in hbtn_0d_tvshows that have at least one genre linked, in order of ascending tv_shows.title and tv_show_genres.genre_id |
| [11-genre_id_all_shows.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/11-genre_id_all_shows.sql)	| List all shows contained in hbtn_0d_tvshows regardless of having genres or not, in order of ascending tv_shows.title and tv_show_genres.genre_id |
| [12-no_genre.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/12-no_genre.sql)	| List all shows contained in hbtn_0d_tvshows without a genre linked, in order of ascending tv_shows.id |
| [13-count_shows_by_genre.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/13-count_shows_by_genre.sql)	| List all genres from hbtn_0d_tvshows and display the number of shows linked to each genre, in order of descending number of shows linked |
| [14-my_genres.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/14-my_genres.sql)	| List all genres of the show Dexter, in order of ascending genre name |
| [15-comedy_only.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/15-comedy_only.sql)	| List all comedy shows in the database hbtn_0d_tvshows, in order of ascending show title |
| [16-shows_by_genre.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0E-SQL_more_queries/16-shows_by_genre.sql)	| List all shows and their genres from the database hbtn_0d_tvshows, in order of descending number of genres linked |
