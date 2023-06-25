import network
import usocket as socket

ssid = "UNAL"
password = ""

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

while not wifi.isconnected():
    pass

print("Connected to Wi-Fi with IP address:", wifi.ifconfig()[0])

ap_ssid = "ESP32-AP"
ap_password = "password"

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ap_ssid, password=ap_password)

print("Wi-Fi IP address:", wifi.ifconfig()[0])
print("Access point IP address:", ap.ifconfig()[0])

def handle_request(conn):
    request = conn.recv(1024)
    response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n<html><body><h1>Mire profe logre algo en la vida</h1></body></html>"
    conn.send(response)
    conn.close()

s = socket.socket()
s.bind(('0.0.0.0', 80))
s.listen(1)

while True:
    conn, addr = s.accept()
    handle_request(conn)
