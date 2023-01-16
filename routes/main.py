from datetime import datetime
from flask import Flask,  request
from sqlite3 import Connection, Row as sqlite3Row

from utils.response import sendResponse
from utils.errors import logError


def prepareRouter(app: Flask, connection: Connection):
    def getCursor():
        connection.row_factory = sqlite3Row

        return connection.cursor()

    @app.route('/', methods=['GET'])
    def getHomepage():
        return sendResponse({"message": "Server running at http://localhost:3000"})

    @app.route("/api/notes", methods=['GET'])
    def getAllNotes():
        # args = request.args
        # queryParams = args.to_dict()
        # search = args.get("search", default="", type=str)
        notes = []

        try:
            cursor = getCursor()

            cursor.execute("""
                SELECT * FROM notes;
            """)

            rows = cursor.fetchall()

            for row in rows:
                note = {}

                note['id'] = row['id']
                note['name'] = row['name']
                note['content'] = row['content']
                note['createdAt'] = row['createdAt']
                note['updatedAt'] = row['updatedAt']

                notes.append(note)

            return sendResponse({"notes": notes})

        except Exception as e:
            logError(e)
            return sendResponse({"message": "Internal server error"}, 500)

    @app.route("/api/notes/<id>", methods=['GET'])
    def getOneNote(id):
        note = {}

        try:
            cursor = getCursor()

            cursor.execute(
                "SELECT * FROM notes WHERE id = ?",
                (id)
            )

            row = cursor.fetchone()

            if not row:
                return sendResponse({"note": None}, 404)

            note['id'] = row['id']
            note['name'] = row['name']
            note['content'] = row['content']
            note['createdAt'] = row['createdAt']
            note['updatedAt'] = row['updatedAt']

            return sendResponse({"note": note})

        except Exception as e:
            logError(e)
            return sendResponse({"message": "Internal server error"}, 500)

    @app.route("/api/notes/create", methods=['POST'])
    def createNote():
        try:
            note = request.get_json()
            cursor = getCursor()

            try:
                currentTimestamp = datetime.now()

                cursor.execute(
                    """
                    INSERT INTO notes (name, content, createdAt, updatedAt)
                    VALUES (?, ?, ?, ?)
                    """,
                    (note["name"], note["content"],
                     currentTimestamp, currentTimestamp)
                )
                cursor.connection.commit()

                return sendResponse({"message": "Successfully created a note"})
            except Exception as e:
                cursor.connection.rollback()
                raise Exception(e)

        except Exception as e:
            logError(e)
            return sendResponse({"message": "Internal server error"}, 500)

    @app.route("/api/notes/<id>", methods=['PUT'])
    def updateNote(id):
        try:
            note = request.get_json()
            cursor = getCursor()

            try:
                currentTimestamp = datetime.now()
                cursor.execute(
                    """
                    UPDATE notes SET name=?, content=?, updatedAt=?
                    WHERE id=?
                    """,
                    (note["name"], note["content"],
                     currentTimestamp, id)
                )
                cursor.connection.commit()

                return sendResponse({"message": "Successfully updated a note"})
            except Exception as e:
                cursor.connection.rollback()
                raise Exception(e)

        except Exception as e:
            logError(e)
            return sendResponse({"message": "Internal server error"}, 500)

    @app.route("/api/notes/<id>", methods=['DELETE'])
    def deleteNote(id):
        try:
            cursor = getCursor()

            try:
                cursor.execute(
                    """
                    DELETE from notes WHERE id = ?
                    """,
                    (id)
                )
                cursor.connection.commit()

                return sendResponse({"message": "Successfully deleted a note"})
            except Exception as e:
                cursor.connection.rollback()
                raise Exception(e)

        except Exception as e:
            logError(e)
            return sendResponse({"message": "Internal server error"}, 500)

    print("Prepared application routes")
