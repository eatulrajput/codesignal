from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a GET method endpoint
@app.route('/greet', methods=['GET'])
def get_endpoint():
    # Return a response message
    return "Hello! You have reached the GET endpoint!", 200

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
