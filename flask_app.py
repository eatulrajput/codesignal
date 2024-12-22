from flask import Flask

# Initialize a Flask app instance
app = Flask(__name__)

# Check if the script is run directly (not imported)
if __name__ == "__main__":
    # Start the Flask development server
    app.run(host="0.0.0.0", port=5001)