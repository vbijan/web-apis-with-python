from flask import Flask, jsonify, request

# Intitialise the app
app = Flask(__name__)

# Define what the app does
# @app.route("/greet", methods=["GET"])
@app.get("/greet")
def index():
    """
    TODO:
    1. Capture first name & last name
    2. If either is not provided: respond with an error
    3. If first name is not provided and second name is provided: respond with "Hello Mr <second-name>!"
    4. If first name is provided byt second name is not provided: respond with "Hello, <first-name>!"
    5. If both names are provided: respond with a question, "Is your name <fist-name> <second-name>
    """
    #if name(data) is passed as a query string, capture it and use it programmetically.
    # 1. Capture first name & last name
    fname = request.args.get("fname")
    lname = request.args.get("lname")

    # 2. If either is not provided: respond with an error
    if not fname and not lname:
        return ({"status": "error"})
    
    # 3. If first name is not provided and second name is provided: 
    # respond with "Hello Mr <second-name>!"
    elif not fname and lname:
        response = {"data": f"Hello My {lname}!"}
    #4. If first name is provided byt second name is not provided: 
    # respond with "Hello, <first-name>!"
    elif fname and not lname:
        response = {"data": f"Hello {fname}!"}

    # 5. If both names are provided: 
    # respond with a question, "Is your name <fist-name> <second-name>
    else:
        response = {"data": f"Is your name {fname} {lname}?"}

    return jsonify(response)