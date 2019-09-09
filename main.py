from flask import Flask, request, jsonify
from code_builder import CodeBuilder
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)


@app.route("/identify", methods=["POST"])
def identify():

    data = request.json

    code_script = data["codeScript"]
    next_raw_line = data["nextLine"]

    code_builder_obj = CodeBuilder()

    code_script, intent, query = code_builder_obj.add_next_line(code_script, next_raw_line)

    return jsonify({"newCode": code_script, "intent": intent, "query": query})


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
