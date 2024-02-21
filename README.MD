API HANDLING IN PYTHON IN CLEAN AND SIMPLE CODE
This Python script implements a neat and clean code for fetching jokes from the JokeAPI and prints them to the console. It uses the requests library to make an HTTP GET request to the API endpoint and processes the response to display jokes.

Usage
Ensure you have Python installed on your system.

Install the required library using:

Copy code
pip install requests
Run the script:

Copy code
python script_name.py
Replace script_name.py with the actual name of your Python script.

Description
The script defines a function fetch_results() that sends a request to the JokeAPI and processes the response. It prints jokes to the console, distinguishing between those with a "setup" and a "delivery" and those without.

The main() function calls fetch_results() when the script is executed.

Dependencies
Python 3.x
requests library
Install the required library using the following command:

bash
Copy code
pip install requests
Error Handling
The script includes basic error handling to manage request exceptions and HTTP status codes. If an error occurs, it prints relevant information to the console.

License
This project is licensed under the MIT License - see the LICENSE file for details.
