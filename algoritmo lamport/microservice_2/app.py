from flask import Flask, request, jsonify

app = Flask(__name__)

# Contador lógico para el Algoritmo de Lamport
lamport_clock = 0

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Microservice is running!"})

@app.route('/event', methods=['POST'])
def event():
    global lamport_clock
    data = request.get_json()

    # Incrementar el reloj Lamport al recibir un evento
    received_clock = data.get('lamport_clock', 0)
    lamport_clock = max(lamport_clock, received_clock) + 1

    return jsonify({
        "message": "Event processed",
        "lamport_clock": lamport_clock
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
