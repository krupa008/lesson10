from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Привет, Милана!"

if __name__=="__main__":
    app.run()