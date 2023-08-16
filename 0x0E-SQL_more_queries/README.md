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
| [4-first_table.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/4-first_table.sql)	| Create a table called first_table |
| [5-full_table.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/5-full_table.sql)	| Print the full description of first_table |
| [6-list_values.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/6-list_values.sql)	| List all rows of first_table |
| [7-insert_value.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/7-insert_value.sql) 	| Insert a new row in first_table |
| [8-count_89.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/8-count_89.sql)	| Display the number of records with id = 89 in first_table |
| [9-full_creation.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/9-full_creation.sql)	| Create and fill a table called second_table |
| [10-top_score.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/10-top_score.sql)	| List the score and name of all records of second_table ordered by score (descending) |
| [11-best_score.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/11-best_score.sql)	| List the score and name of all records with a score >= 10 in second_table ordered by score (descending) |
| [12-no_cheating.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/12-no_cheating.sql)	| Update the score of Bob to 10 in second_table |
| [13-change_class.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/13-change_class.sql)	| Delete all records with a score <= 5 in second_table |
| [14-average.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/14-average.sql)	| Compute the average score of all records in second_table |
| [15-groups.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/15-groups.sql)	| List the number of records with the same score in second_table ordered by number of records (descending) |
| [16-no_link.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/16-no_link.sql)	| List all rows of second_table without using a JOIN or a subquery |
