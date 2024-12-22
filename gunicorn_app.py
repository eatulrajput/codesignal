from flask import Flask  

# Initialize a Flask app instance
app = Flask(__name__)

# Note: We won't need the app.run() block when using Gunicorn