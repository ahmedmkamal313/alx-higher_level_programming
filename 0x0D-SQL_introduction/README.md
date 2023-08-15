# 0x0D. SQL - Introduction
This project is an introduction to SQL and relational databases. It covers the basics of data definition language (DDL), data manipulation language (DML), subqueries, and functions.

![sql](https://media.licdn.com/dms/image/C5612AQHPCxpt-G7C1w/article-cover_image-shrink_600_2000/0/1521919680457?e=2147483647&v=beta&t=B9hVQaW7rlFo20VB7fycFcyqUXUF3c6wMw4UIE9JeLs)

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
| [0-list_databases.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/0-list_databases.sql)	| List all databases |
| [1-create_database_if_missing.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/1-create_database_if_missing.sql)	| Create a database if it does not exist |
| [2-remove_database.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/2-remove_database.sql)	| Delete a database if it exists |
| [3-list_tables.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/3-list_tables.sql)	| List all tables of a database |
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
## Adnavced tasks files:
- [100-move_to_utf8.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/100-move_to_utf8.sql): This file contains a SQL script that converts the entire database hbtn_0c_0 to UTF8 character set and collation1. UTF8 is a widely used encoding that supports the full range of Unicode characters2.
- [101-avg_temperatures.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/101-avg_temperatures.sql): This file contains a SQL script that displays the average temperature (in Fahrenheit) by city ordered by descending temperature5. The script uses the AVG function to calculate the mean value of the temperature column, and the GROUP BY clause to group the rows by city6.
- [102-top_city.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/101-avg_temperatures.sql): This file contains a SQL script that displays the top 3 cities with the highest average temperature (in Fahrenheit) in July and August9. The script uses the WHERE clause to filter the rows by month, and the LIMIT clause to limit the number of rows returned10.
- [103-max_state.sql](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x0D-SQL_introduction/103-max_state.sql): This file contains a SQL script that displays the max temperature of each state, ordered by state name13. The script uses the MAX function to find the highest value of the temperature column, and the ORDER BY clause to sort the rows by state14.
