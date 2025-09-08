import requests
import time
import subprocess
import json

# SET THIS TO YOUR RENDER WEB APP URL, e.g. https://your-app.onrender.com/data
API_URL = "https://YOUR_RENDER_APP_URL/data"

def get_bytes_in():
    # dstat: get incoming bytes/sec (replace eth0 with your interface if needed)
    result = subprocess.check_output("dstat -n 1 1 | tail -n 1", shell=True).decode()
    # dstat output sample: "  0      0"
    try:
        bytes_in = int(result.split()[0])
    except Exception:
        bytes_in = 0
    return bytes_in

while True:
    bytes_in = get_bytes_in()
    ts = int(time.time())
    payload = {'bytes_in': bytes_in, 'timestamp': ts}
    try:
        requests.post(API_URL, json=payload, timeout=3)
        print(f"Pushed: {bytes_in} bytes at {ts}")
    except Exception as e:
        print(f"Failed: {e}")
    time.sleep(1)
