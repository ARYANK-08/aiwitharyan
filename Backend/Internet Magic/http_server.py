import argparse
import socket
import threading
from pathlib import Path

# Buffer size for receiving data
BUFFER_SIZE = 1024
# Encoding type for strings
ENCODING = "utf-8"

def response_with_content(content, content_type="text/plain", code=200):
    """
    Generates an HTTP response with the specified content, content type, and status code.
    """
    return f"HTTP/1.1 {code} {get_status_message(code)}\r\nContent-Type: {content_type}\r\nContent-Length: {len(content)}\r\n\r\n{content}"

def get_status_message(code):
    """
    Retrieves the status message corresponding to an HTTP status code.
    """
    messages = {
        200: "OK",
        201: "Created",
        404: "Not Found"
    }
    return messages.get(code, "Unknown Status")  # Return message or default

def file_response(http_method, path, body, directory):
    """
    Handles file upload (POST) and retrieval (GET) based on the HTTP method.
    """
    file_path = Path(directory) / path.split('/')[-1]  # Get the file path
    content_type = "application/octet-stream"  # Default content type

    if http_method == "POST":
        # Handle file upload
        try:
            file_path.write_text(body)  # Write the body content to the file
            return response_with_content('', content_type, 201)  # Return Created response
        except Exception as e:
            print(f"Error writing file: {e}")  # Log any errors
            return response_with_content('Internal Server Error', content_type, 500)  # Return error response
    
    elif file_path.is_file():
        # Handle file retrieval
        try:
            # Determine content type based on file extension
            content_type = "text/plain" if file_path.suffix == '.txt' else "application/octet-stream"
            return response_with_content(file_path.read_text(), content_type)  # Return file content
        except Exception as e:
            print(f"Error reading file: {e}")  # Log any errors
            return response_with_content('Internal Server Error', content_type, 500)  # Return error response

def response(http_method, path, user_agent, body, directory):
    """
    Processes the request based on the HTTP method and requested path.
    """
    if path.startswith("/files"):
        # Handle requests for files
        response = file_response(http_method, path, body, directory)
        if response:
            return response
    elif path.startswith("/echo"):
        # Echo back the path after '/echo/'
        random_string = '/'.join(path.split('/')[2:])
        return response_with_content(random_string)
    elif path.startswith("/user-agent"):
        # Return the User-Agent string
        return response_with_content(user_agent if user_agent else 'User-Agent not found')
    elif path == "/":
        # Welcome message for the root path
        return response_with_content("Welcome!", content_type="text/plain")
    
    return response_with_content("Not Found", code=404)  # Return 404 if path not found

def parse_request(request):
    """
    Parses the incoming HTTP request to extract method, path, user agent, and body.
    """
    request_lines = request.split("\r\n")  # Split request into lines
    http_method, path, _ = request_lines[0].split(" ", 2)  # Extract method and path
    user_agent = None
    for line in request_lines:
        if line.startswith("User-Agent:"):
            # Extract User-Agent string
            user_agent = ' '.join(line.split(" ")[1:])
            break
    # Determine body content for POST requests
    body = request_lines[-1] if http_method == "POST" and len(request_lines) > 1 else None

    return http_method, path, user_agent, body  # Return parsed elements

def handle_client(client_socket, address, directory):
    """
    Handles communication with a connected client.
    """
    data = client_socket.recv(BUFFER_SIZE)  # Receive request data from client
    request = data.decode(ENCODING)  # Decode the request
    print(f"Request from {address}:\n{request}")  # Log the request

    http_method, path, user_agent, body = parse_request(request)  # Parse the request

    response_message = response(http_method, path, user_agent, body, directory)  # Generate response
    client_socket.sendall(response_message.encode(ENCODING))  # Send response to the client
    client_socket.close()  # Close the client socket

def main():
    """
    Main function to set up and run the HTTP server.
    """
    parser = argparse.ArgumentParser()  # Create argument parser
    parser.add_argument('--directory', type=str, required=True, help="Directory to store files")  # Add directory argument
    args = parser.parse_args()  # Parse command line arguments

    # Create a server socket listening on localhost at port 4221
    server_socket = socket.create_server(("localhost", 4221))
    server_socket.listen()  # Start listening for incoming connections

    print("Server is running on http://localhost:4221")

    try:
        while True:
            client_socket, address = server_socket.accept()  # Accept a new client connection
            client_thread = threading.Thread(target=handle_client, args=(client_socket, address, args.directory))  # Create a new thread for the client
            client_thread.start()  # Start the client thread
    except KeyboardInterrupt:
        print("Server is shutting down.")  # Handle graceful shutdown
    finally:
        server_socket.close()  # Ensure the server socket is closed

if __name__ == "__main__":
    main()  # Run the main function



# Simple HTTP Server

# This is a simple HTTP server implemented in Python. 
# It allows clients to send requests for file uploads, echoes strings, retrieves user-agent information, 
# and serves files from a specified directory. Additionally, it supports Gzip compression for responses.

# Features
# - Echo Endpoint: Returns a string specified in the URL.
# - User-Agent Endpoint: Returns the User-Agent string sent by the client.
# - File Uploads: Supports uploading files via POST requests.
# - File Retrieval: Serves files from a specified directory on the server.
# - Gzip Compression: Compresses responses for clients that support it.

# Getting Started

# Prerequisites
# - Python 3.x installed on your system.

# Installation
# 1. Clone the Repository (if applicable):
#    ```bash
#    git clone <repository-url>
#    cd <repository-name>
#    ```
# 2. Save the Server Code: Copy the provided server code into a file named `http_server.py`.

# Running the Server
# 1. Open a Terminal/Command Prompt.
# 2. Navigate to the Directory where `http_server.py` is saved.
# 3. Run the Server:
#    ```bash
#    python http_server.py --directory /path/to/your/directory
#    ```
#    Replace `/path/to/your/directory` with the actual path where you want to serve files from.

# Important Endpoints
# - Echo Endpoint: Returns the string that you send in the URL.
#   - Example:
#     ```bash
#     curl http://localhost:4221/echo/hello
#     ```

# - User-Agent Endpoint: Returns the User-Agent header from the request.
#   - Example:
#     ```bash
#     curl -A "TestUserAgent/1.0" http://localhost:4221/user-agent
#     ```

# - File Upload: Uploads a file to the server using a POST request.
#   - Example:
#     ```bash
#     curl -X POST -d "This is a test content" http://localhost:4221/files/testfile.txt
#     ```

# - Retrieve File: Gets a file from the server.
#   - Example:
#     ```bash
#     curl http://localhost:4221/files/testfile.txt
#     ```

# Code Explanation

# Imports
# - argparse: Used to handle command-line arguments.
# - socket: For creating the server and managing connections.
# - threading: Allows handling multiple client connections simultaneously.
# - gzip: To compress responses using Gzip.
# - io: To manage byte streams for compression.
# - pathlib: For easy manipulation of file paths.

# Main Functions
# 1. response_with_content(content, content_type="text/plain", code=200, compress=False):
#    - Generates an HTTP response with the specified content, type, and status code.
#    - If `compress` is set to `True`, the response content is compressed using Gzip.

# 2. file_response(http_method, path, body, directory):
#    - Handles file uploads (via POST) and retrieval (via GET).
#    - Saves uploaded content to a file and returns its content if it exists.

# 3. response(http_method, path, user_agent, body, directory):
#    - Routes requests to the appropriate handlers based on the requested path.
#    - Checks if the user agent supports Gzip compression and applies it if so.

# 4. parse_request(request):
#    - Parses the incoming HTTP request to extract the method, path, user agent, and body content.

# 5. handle_client(client_socket, address, directory):
#    - Manages the communication with connected clients, processes requests, and sends responses.

# 6. main():
#    - Sets up the server to listen for connections, accepts client connections, and spawns threads for handling them.

# Important Concepts
# - HTTP Methods: The server supports GET and POST methods. GET is used to retrieve resources, while POST is used to send data to the server.
# - Gzip Compression: This server can compress responses using Gzip, which reduces the amount of data sent over the network, improving performance for clients that support it.
# - Concurrency: The server can handle multiple client connections at the same time using threading, allowing for efficient request handling.

# Conclusion
# This simple HTTP server is a great starting point for understanding how web servers work. 
# You can expand its functionality or customize it for your needs.


