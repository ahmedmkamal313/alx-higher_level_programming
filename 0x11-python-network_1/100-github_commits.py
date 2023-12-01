#!/usr/bin/python3
"""
This module takes in a URL and an email address, sends a POST request to
http://0.0.0.0:5000/search_user with the email as a parameter using the
requests and sys packages. It also displays the id and name of the user
found or an error message if the response is not valid or empty.
"""

import requests
import sys

if __name__ == "__main__":
    # Get the URL and email address from the command line arguments
    url = sys.argv[1]
    email = sys.argv[2]
    # Send a POST request to the given URL with the email as a parameter
    response = requests.post(url, data={'email': email})
    # Get the response body as a string
    html = response.text
    # Print the response body
    print(html)
