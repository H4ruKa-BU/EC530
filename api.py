from flask import Flask, request, jsonify

app = Flask(__name__)
messages = []

@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    messages.append(data)
    return jsonify({"status": "Message received."}), 200

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages), 200

if __name__ == '__main__':
    app.run(debug=True, port=8000)
