# Python HTTP/HTTPS Client

## Overview

This project is a simple yet powerful HTTP/HTTPS client implemented in Python. It demonstrates foundational knowledge of the **TCP/IP protocol suite**, HTTP communication, and secure HTTPS connections using Python's `socket` and `ssl` libraries. The client allows users to connect to web servers, send HTTP `GET` requests, and parse responses.

---

## Features

- **HTTP and HTTPS Support**: Establish secure connections using SSL/TLS for HTTPS.
- **Customizable Requests**: Users can specify the hostname, resource path, and protocol.
- **Header Parsing**: Extract and display the HTTP status code and key response headers.
- **Response Body Display**: View the initial portion of the server's response body.
- **Beginner-Friendly**: Clear structure and implementation, ideal for learning networking concepts.

---

## How It Works

1. **User Input**:
   - Hostname (e.g., `example.com`).
   - Protocol (HTTP or HTTPS).
   - Resource path (e.g., `/`).

2. **Connection**:
   - Uses `socket` for TCP/IP communication.
   - Wraps the socket with `ssl` for secure HTTPS communication if specified.

3. **Request Formatting**:
   - Sends an HTTP `GET` request to the server.

4. **Response Handling**:
   - Receives and parses the server’s response.
   - Displays the HTTP status code, headers, and part of the response body.

---

## Prerequisites

- Python 3.x
- Internet connection
- Basic knowledge of Python and networking concepts

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/http-https-client.git
   cd http-https-client
