import network, time

ssid = 'PruebaEsp32'  # replace with your desired SSID
password = 'password'  # replace with your desired password

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)

print('ESP32 Access Point configured. SSID: %s, Password: %s' % (ssid, password))

while True:
    print('Waiting for clients to connect...')
    connected_clients = len(ap.status('stations'))
    print('%d clients connected.' % connected_clients)
    time.sleep(5)