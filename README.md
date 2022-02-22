# Flask-Todo
Source code and material for the ACM SWE Flask Workshop. 

## Getting Started

### Prerequisites
Make sure you have Python 3.6 (or later) and pip installed. 

### Running the Application
1. Clone this repository in the command line or terminal and run `cd Flask-Todo`.
2. Switch to the `starter` branch by running `git checkout starter`.
3. Set up Python virtual environment by running the following commands:

```bash
# create Python virtual environment 
python -m venv venv

# activate virtual environment (macOS and Linux)
source venv/bin/activate

# activate virtual environment (Windows)
venv\Scripts\activate.bat
```
4. Install the necessary packages listed in the requirements.txt file with `pip install -r requirements.txt`.
5. Create a new file called `.env` to store environment variables with the command `touch .env`.
6. Open the newly created `.env` file in a text editor and add the following lines:

```bash
FLASK_APP=todo.py
FLASK_DEBUG=1
```

7. Save the file and start the devlopment server with the command `flask run`.
8. Copy the URL in the the output of `flask run` and open it in your web browser to view the application. 
