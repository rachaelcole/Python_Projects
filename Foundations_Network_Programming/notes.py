import socket

'''
-	Network programming often involves selecting and using a library that already supports the network operations you
    need to perform
-	These libraries are built on lower-level network services available to Python
-	The virtualenv is where you should install python libraries
-	Raw network communication happens through byte strings
-	A sample protocol stack:
    o	Top: google geocoding API
    o	URL
    o	HTTP
    o	TCP
    o	IP
    o	Data link
-	Bytes are the binary numbers that computers transmit during communication
    o	Each byte is 8 bits of binary digits
-	Python will only convert strings/characters to and from bytes when you ask it to
-	Decoding: when bytes come into your app and you need to figure out what they mean
-	Encoding: taking strings from your app and turning them into bytes for transmission
'''
# Example 1-6. Decoding input bytes and encoding characters for output
if __name__ == '__main__':
    # Translating from bytes into Unicode characters
    input_bytes = b'\xff\xfe4\x001\x003\x00 \x00i\x00s\x00 \x00i\x00n\x00.\x00'
    input_characters = input_bytes.decode('utf-16')
    print(repr(input_characters))

    # Translating characters back into bytes before sending them
    output_characters = 'We copy you down, Eagle.\n'
    output_bytes = output_characters.encode('utf-8')
    with open('eagle.txt', 'wb') as f:
        f.write(output_bytes)

#  packet is a byte string whose length can range, which is transmitted as a single unit between network devices
# Example 1-7. Turning a hostname into an IP address
if __name__ == '__main__':
    hostname = 'www.python.org'
    addr = socket.gethostbyname(hostname)
    print(f'The IP address of {hostname} is {addr}')

'''
-	UDP uses each packet as a standalone message, is connectionless, not secure
-	TCP uses a stream of data that gets split into packets automatically, is connection-oriented, and secure
-	The connect() call lets the OS know ahead of time the remote address to which you want to send packets, so you can 
    simply supply data using send() and not have to repeat the server address again
-	Once you have run connect(), the OS will discard any incoming packets to your port whose return address doesn’t 
    match the address to which you have connected - this is not a form of security, however
'''

