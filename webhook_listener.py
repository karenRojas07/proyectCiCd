from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    print("📦 Webhook recibido: reconstruyendo contenedor...")
    subprocess.Popen(["sudo", "docker-compose", "up", "--build", "-d"])
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

