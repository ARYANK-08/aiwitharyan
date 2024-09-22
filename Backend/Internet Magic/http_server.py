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
