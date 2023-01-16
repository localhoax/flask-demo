from flask import json, Response


def sendResponse(data, status=200):
    return Response(
        response=json.dumps(data),
        status=status,
        mimetype='application/json'
    )
