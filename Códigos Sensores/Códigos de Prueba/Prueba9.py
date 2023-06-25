import network

ssid = "UNAL"
password = ""

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

while not wifi.isconnected():
    pass

print("Connected to Wi-Fi with IP address:", wifi.ifconfig()[0])