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
        return """
<html>
<head><title>Votes for your ward</title></head>
<body>
See what the voting patterns are in your ward:

For example, try:  <a href="/?address=12 Thicket St, Cape Town">12 Thicket street, Cape Town</a>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=False)
        
