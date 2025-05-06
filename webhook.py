from flask import Flask, request
import os
import subprocess

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    if request.method == "POST":
        repo_path = "/home/karen/python-cicd"
        try:
            subprocess.run(["git", "-C", repo_path, "pull"], check=True)
            return "Código actualizado correctamente", 200
        except subprocess.CalledProcessError as e:
            return f"Error al actualizar el código: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

