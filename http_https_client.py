import socket
import ssl

def parse_headers(response):
    """Parse and extract headers from the HTTP response."""
    # Split response into headers and body
    headers, _, body = response.partition("\r\n\r\n")
    header_lines = headers.split("\r\n")
    status_line = header_lines[0]
    
    # Extract status code
    status_code = status_line.split(" ")[1]
    
    # Extract headers as a dictionary
    header_dict = {}
    for line in header_lines[1:]:
        key, _, value = line.partition(": ")
        header_dict[key] = value
    
    return status_code, header_dict, body

def http_client(host, port, resource, use_https):
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Wrap the socket in an SSL context for HTTPS
    if use_https:
        context = ssl.create_default_context()
        client_socket = context.wrap_socket(client_socket, server_hostname=host)

    try:
        # Connect to the server
        print(f"Connecting to {host} on port {port}...")
        client_socket.connect((host, port))
        print("Connection established!")

        # Prepare the HTTP GET request
        request = f"GET {resource} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
        print("Sending request:")
        print(request)

        # Send the HTTP GET request
        client_socket.sendall(request.encode())

        # Receive the response
        response = b""
        while True:
            data = client_socket.recv(4096)  # Receive data in chunks
            if not data:
                break
            response += data

        # Decode the response
        response_text = response.decode("utf-8", errors="ignore")

        # Parse headers and body
        status_code, headers, body = parse_headers(response_text)

        # Display the parsed information
        print("\n--- HTTP Response Headers ---")
        print(f"Status Code: {status_code}")
        for key, value in headers.items():
            print(f"{key}: {value}")

        print("\n--- Response Body ---")
        print(body[:500])  # Print the first 500 characters of the body

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the socket
        client_socket.close()
        print("Connection closed.")

# Run the HTTP/HTTPS client
if __name__ == "__main__":
    # Get user input
    print("Welcome to the HTTP/HTTPS Client!")
    host = input("Enter the hostname (e.g., example.com): ")
    use_https = input("Use HTTPS? (yes/no): ").strip().lower() == "yes"
    port = 443 if use_https else 80
    resource = input("Enter the resource path (e.g., /): ")

    # Run the client
    http_client(host=host, port=port, resource=resource, use_https=use_https)
