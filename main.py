import sqlite3
from flask import Flask
from flask_cors import CORS

from database.database import Database
from routes.main import prepareRouter
from utils.errors import logError


def run():
    try:
        db = Database()
        connection = db.connect()
        db.prepareDatabase()

        app = Flask(__name__)

        # To enable our application to be accessible through below domains
        # "*" is a wild case to allow from everywhere
        CORS(app, resources={r"/*": {"origins": "*"}})

        # Prepare routes that are going to be available for our API
        prepareRouter(app, connection)

        # Runs the HTTP server on localhost:3000
        app.run(host="localhost", port=3000)

    except Exception as e:
        logError(e)
    finally:
        if connection:
            connection.close()


if __name__ == '__main__':
    run()
