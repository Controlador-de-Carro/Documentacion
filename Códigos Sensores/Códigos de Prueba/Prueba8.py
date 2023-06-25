import network
import time
import ujson
from machine import Pin
import socket

ssid = 'MyESP32AP'  # replace with your desired SSID
password = 'password'  # replace with your desired password

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)

print('ESP32 Access Point configured. SSID: %s, Password: %s' % (ssid, password))
print('IP address:', ap.ifconfig()[0])

# Define the HTTP response
def http_response(connected_clients):
    return 'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: %d\r\n\r\n%s' % (len(connected_clients), ujson.dumps(connected_clients))

# Create a new socket and listen for incoming connections
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(1)
print('HTTP server started on port 80')

# Main loop - handle incoming connections
while True:
    conn, addr = s.accept()
    print('Connection from %s' % str(addr))
    # Receive and parse the request
    request = conn.recv(1024)
    request = str(request)
    request_method = request.split(' ')[0]
    # Send the HTTP response with the number of connected clients
    if request_method == 'GET':
        connected_clients = len(ap.status('stations'))
        response = http_response({'connected_clients': connected_clients})
        conn.send(response.encode())
    # Close the connection
    conn.close()
