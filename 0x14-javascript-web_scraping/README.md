# 0x14. JavaScript - Web scraping
This is a project that demonstrates how to use node.js to perform web scraping tasks. Web scraping is the process of extracting data from websites using various techniques. In this project, we use the request module to make HTTP requests and parse JSON responses from different APIs.
## Installation
To run this project, you need to have node.js and npm installed on your machine.
```
git clone https://github.com/ahmedmkamal313/alx-higher_level_programming.git
```
Install Node 14
```
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```
## Usage
To run any of the scripts in this project, use the following command:
```
node <script-name>.js <arguments>
```
For example, to run the script that prints the title of a Star Wars movie where the episode number matches a given integer, use the following command:
```
node 3-starwars_title.js 3
```
The output should be:
```
Return of the Jedi
```
## Scripts
This project contains the following scripts:

- [0-readme.js](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x14-javascript-web_scraping/0-readme.js): A script that reads and prints the content of a file.
- [1-writeme.js](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x14-javascript-web_scraping/1-writeme.js): A script that writes a string to a file.
- [2-statuscode.js](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x14-javascript-web_scraping/2-statuscode.js): A script that displays the status code of a GET request.
- [3-starwars_title.js](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x14-javascript-web_scraping/3-starwars_title.js): A script that prints the title of a Star Wars movie where the episode number matches a given integer.
- [4-starwars_count.js](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x14-javascript-web_scraping/4-starwars_count.js): A script that prints the number of movies where the character “Wedge Antilles” is present.
- [5-request_store.js](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x14-javascript-web_scraping/5-request_store.js): A script that gets the contents of a webpage and stores it in a file.
- [6-completed_tasks.js](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x14-javascript-web_scraping/6-completed_tasks.js): A script that computes the number of tasks completed by user id.
- [100-starwars_characters.js](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x14-javascript-web_scraping/100-starwars_characters.js): A script that prints all characters of a Star Wars movie.
- [101-starwars_characters.js](https://github.com/ahmedmkamal313/alx-higher_level_programming/blob/master/0x14-javascript-web_scraping/101-starwars_characters.js): A script that prints all characters of a Star Wars movie in the same order of the list “characters” in the /films/ response.
