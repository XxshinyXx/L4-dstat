import os
from flask import Flask, request, render_template, jsonify
from collections import deque
from threading import Lock

app = Flask(__name__)
data_points = deque(maxlen=120)  # Keep last 2 minutes at 1s interval
lock = Lock()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def push_data():
    incoming = request.json.get('bytes_in')
    ts = request.json.get('timestamp')
    with lock:
        data_points.append({'timestamp': ts, 'bytes_in': incoming})
    return jsonify(status='ok')

@app.route('/chart-data', methods=['GET'])
def chart_data():
    with lock:
        return jsonify(list(data_points))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
