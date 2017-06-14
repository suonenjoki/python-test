from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Terve World ja Suomi-Finland!"

if __name__ == "__main__":
    application.run()
