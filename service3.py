
from flask import Flask, request
from flask import jsonify
import json

import requests as r

app = Flask(__name__)


@app.route("/search" , methods=['GET'])
def search():
    # ambil parameter dari request
    search_term = request.args.get('name')

    # ambil data dari service 6 (dataserver)
    data = r.get('http://localhost:5006/products').json()
    
    matching = [s for s in data if search_term.lower() in s['product_name'].lower()]

    return jsonify(matching)

if __name__ == '__main__':
    app.run(debug=True, port=5003)