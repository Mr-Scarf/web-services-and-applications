
# This code creates a simple REST server using the Flask framework in Python.
from flask import Flask   

# Create a Flask application instance
app = Flask(__name__)

@app.route('/')  # Define a route for the root URL
def index():
    return "Hello, World!"  # Return a simple response when the root URL is accessed

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application in debug mode
    

