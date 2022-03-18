from flask import Flask, make_response, render_template
from flask_restful import Api
from flask_cors import CORS
import mcstatus

app = Flask(__name__)
api = Api(app)
CORS(app)


@app.route("/", methods=["GET"])
def index():
    return make_response(render_template("index.html"))


@app.route("/poll/", methods=["GET"])
def placeholder():
    return "Nothing to see here"


@app.route("/poll/<target>", methods=["GET"])
def poll(target):
    server = mcstatus.MinecraftServer.lookup(target).status()

    payload = {"description": server.description,
               "version": server.version.name,
               "players": {"online": server.players.online,
                           "max": server.players.max}}

    return payload


def main():
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
