import json
from flask import Flask
from flask import render_template
from flask import request
import votes

app = Flask(__name__)

@app.route("/", methods=["GET"])
def vote_summary():
    address = request.args.get("address")
    if address:
        summary = votes.vote_summary(address)
        return render_template("hood.html", summary=summary)
    else:
        return render_template("search.html")

if __name__ == "__main__":
    app.run(debug=False)
        
