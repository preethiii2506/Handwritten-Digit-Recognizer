from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Handwritten Digit Recognizer App Running"

if __name__ == "__main__":
    app.run(debug=True)
