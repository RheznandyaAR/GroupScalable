
from flask import Flask, jsonify

import requests as r

app = Flask(__name__)


@app.route("/recommendation")
def recommendation():
    # ambil data dari service 6 (dataserver)
    data = r.get('http://localhost:5006/products').json()

    try:
        data = sorted(data, key=lambda k: (k['rating'], k['sold']), reverse=True)
    except Exception as e:
        print(e)
        return jsonify({'message': 'error'})
    return jsonify(data[:10])

if __name__ == '__main__':
    app.run(debug=True, port=5002)