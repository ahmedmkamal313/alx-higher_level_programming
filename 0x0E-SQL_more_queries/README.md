# 0x0E. SQL - More queries
This project contains SQL scripts that demonstrate how to create users, manage privileges, use primary keys, foreign keys, constraints, subqueries, joins, and unions with MySQL.

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
