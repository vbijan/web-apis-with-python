# dictionary-api-python-flask/app.py
from flask import Flask, request, jsonify, render_template
from model.dbHandler import match_exact, match_like

app = Flask(__name__)


@app.get("/")
def index():
    """
    DEFAULT ROUTE
    This method will
    1. Provide usage instructions formatted as JSON
    """
    response = {"usage": "/dict?=<word>"}
    # Since this is a website with front-end, we don't need to send the usage instructions
    return jsonify(response)


@app.get("/dict")
def dictionary():
    """
    DEFAULT ROUTE
    This method will
    1. Accept a word from the request
    2. Try to find an exact match, and return it if found
    3. If not found, find all approximate matches and return
    """

    words = request.args.getlist("word")

    if not words:
        return jsonify({"data": "Not a valid word or no word provided."})
    
    response = {"words": []}

    for word in words:
        # exact match
        definations = match_exact(word)
        if definations:
            response["words"].append({"status": "success", "word":word, "Data":definations})
        else:
            definations = match_like(word)
            if definations:
                response["words"].append({"status": "partial", "data":definations, "word": word})
            else:
                response["words"].append({"status": "error", "data": "word not found", "word": word})
    return jsonify(response)

if __name__ == "__main__":
    app.run()
