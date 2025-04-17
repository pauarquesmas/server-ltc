from flask import Flask, request

app = Flask(__name__)

@app.route("/ipn", methods=["POST"])
def ipn():
    print("💸 Rebut IPN:", request.form.to_dict())
    return "OK", 200

@app.route("/")
def home():
    return "Servidor actiu ✅"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
