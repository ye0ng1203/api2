from flask import Flask, jsonify
from models1 import Stores

app = Flask(__name__)

@app.route('/')
def main():
	data = Stores.get_all()
	return jsonify(data)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port="8000", debug=True)
