'''
HTTP 1.1 is the most common version in use today (c.f. RFCs 7230-7235)
The Requests library is great for making HTTP requests, as is urllib
Port 80 is the standard port for plain-text HTTP conversations; port 443 for HTTPS
In HTTP, the client speaks first, transmitting a request that names a document
Once the entire request is on the wire, the client waits until it receives a complete response from
the server, indicating OK or an error
The client can't transmit a second request over the same socket until the server's response is finished
GET method is 'read'; POST method is 'write'
A sample HTTP request and response is as follows:

GET /ip HTTP/1.1                                          # This is the request; the request method is GET
User-Agent: curl/7.35.0
Host: localhost:8000
Accept: */*

HTTP/1.1 200 OK                                           # This is the response
Server: gunicorn/19.1.1
Date: Sat, 20 Sep 2014 00:18:00 GMT
Connection: close
Content-Type: application/json
Content-Length: 27                                        # gives length of the body in bytes
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true

{
    "origin": "127.0.0.1"
}

HTTP Status codes:
200 OK
301 Moved Permanently
303 See Other
304 Not Modified
307 Temporary Redirect
400 Bad Request
403 Forbidden
404 Not Found
405 Method Not Allowed
500 Server Error
501 Not Implemented
502 Bad Gateway

A web server is the code that holds a listening socket, runs accept() to receive new connections, and
parses each incoming HTTP request
'''
