# Course Notes

## Introduction

- **Objective:** Explore APIs, understand their importance, and learn to build web applications using Flask.

## Key Topics:
1. **Understanding APIs**
2. **Learning about the Flask Web Framework**
3. **Running a Simple Flask Application**

---

## Understanding APIs and Their Importance

- **Definition:**  
  API (Application Programming Interface) is a bridge for communication between different software applications.
- **Role in Web Development:**  
  Facilitates interaction between web servers and clients (e.g., browsers, mobile apps).  
  - **Common data format:** JSON.
- **Examples of API Integration:**
  - Fetching weather data in apps.
  - Processing payments in e-commerce using APIs from payment gateways.
- **Benefits of APIs:**
  - Modular, maintainable, and scalable application development.

---

## What is Flask?

- **Definition:**  
  A lightweight Python web framework for building web applications quickly and efficiently.
- **Key Features:**
  - **Lightweight and Modular:** Choose only the components you need.
  - **Easy to Learn:** Beginner-friendly due to simple and flexible design.
  - **Extensible:** Add functionality using Flask extensions.

---

## Why Learn Flask?

- Simplicity and versatility make it ideal for beginners and professionals alike.

---

## Setting Up Flask

- **Installation:**  
  Install Flask locally using the following command:
  ```python
  pip install flask
  ```

# Launching a Flask Application with Gunicorn

## Introduction
- **Objective:** Learn how to serve a Flask application using Gunicorn for better performance and scalability.
- **Context:** Builds upon the previous lesson on setting up and running a simple Flask application using Flask's built-in server.

---

## Recap: Setting Up a Simple Flask App

- **Steps to Set Up a Basic Flask App:**
  1. Import the Flask library.
  2. Create a Flask app instance.
  3. Define routes to handle HTTP requests.
  4. Run the application using Flask's built-in development server.

- **Example Code:**
  ```python
  from flask import Flask  

    # Initialize a Flask app instance
    app = Flask(__name__)

    # Note: We won't need the app.run() block when using Gunicorn
  ```
  5. In this code:
  We import the `Flask` class from the `flask` module.
  We create an instance of the `Flask` class and call it `app`.

When using Gunicorn, there's no need for the `if __name__ == "__main__": app.run()` block, which was necessary when using the built-in Flask server.


## What is Gunicorn?

- **Definition:**  
  Gunicorn (Green Unicorn) is a Python WSGI HTTP server used to serve Flask applications.
  - **WSGI:** Web Server Gateway Interface, a specification enabling web servers to communicate with Python web applications.

- **Role of Gunicorn:**
  - Acts as a middleman between your Flask application and web clients (e.g., browsers, mobile apps).
  - Helps handle and manage HTTP requests efficiently.

- **Why Use Gunicorn?**
  - The built-in Flask server is suitable for development but struggles with high traffic.
  - Gunicorn supports **multiple workers**, allowing it to handle numerous requests simultaneously.
  - Improves the reliability and efficiency of your application.

- **Analogy:**  
  Imagine a web app that needs to process hundreds of requests per second.  
  - Flask's built-in server might falter under this load.  
  - Gunicorn ensures smooth handling of traffic, making your application production-ready.


## Why Use Gunicorn Over Flask’s Built-in Server?

### **Flask’s Built-in Server**
- **Pros:**
  - Simple to use and set up.
  - Ideal for development and testing.
- **Cons:**
  - Limited to development environments.
  - Struggles with:
    - High traffic.
    - Multiple simultaneous requests.
  - Not designed for production-level performance.

---

### **Gunicorn**
- **Pros:**
  - Highly configurable for various performance needs.
  - Supports multiple worker processes to handle high traffic efficiently.
  - Designed for production environments.
  - Ensures stability and performance.
- **Cons:**
  - Requires additional setup compared to Flask’s built-in server.

---

### **Key Benefit of Using Gunicorn**
- By deploying your Flask app with Gunicorn:
  - It can handle more users and higher traffic.
  - Ensures a better user experience in real-world, high-traffic scenarios.


## Installing Gunicorn

- **Step 1:** Open your terminal or command prompt.
- **Step 2:** Install Gunicorn using `pip`:

  ```bash
  pip install gunicorn
  ```

## Starting the Server with Gunicorn

### **Basic Command**
- Navigate to the directory containing your Flask app file.
- Run the following command to start the Gunicorn server:
  ```bash
  gunicorn filename:app
  ```
## Breaking Down the Command

### **Command Structure**
- `gunicorn`: The command to start Gunicorn.
- `filename:app`:
  - **Module name (`filename`)**: The name of the Python file containing your Flask app (e.g., `app.py` without the `.py` extension).
  - **Application instance (`app`)**: The Flask app instance defined in the file.

---

## Output

- When the command is executed:
  - The Gunicorn server starts successfully.
  - You will see output in the terminal indicating that Gunicorn is running.
- **Default Behavior:**
  - Gunicorn listens for incoming requests on `127.0.0.1` (localhost) at port `8000`.

## Specifying IP and Port

- To customize the IP address and port number, use the `-b` (bind) option:

  ```bash
  gunicorn -b 0.0.0.0:8080 filename:app
  ```

## Breaking Down the Options

- `-b 0.0.0.0:8080`:
  - **`0.0.0.0`**: Binds Gunicorn to all available IP addresses.
  - **`8080`**: Specifies the port number to listen on.

This configuration allows Gunicorn to handle requests from any IP address and on a custom port, ensuring flexibility and accessibility for your Flask application.
