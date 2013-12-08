import json
from flask import Flask
from flask import render_template
from flask import request
import votes
import analytics

analytics.init('4645xq3bi2')
app = Flask(__name__)

def track(action, user="anonymous", **kwargs)
    analytics.track(user, action, kwargs)

@app.route("/", methods=["GET"])
def vote_summary():
    address = request.args.get("address")
    if address:
        summary = votes.vote_summary(address)
        if summary:
            track("Vote - Got results", user="anonymous", **summary)
            return render_template("hood.html", summary=summary)
        else:
            track("Vote - Address Not Found", address=address)
            return render_template("not_found.html")
    else:
        track("Vote - Hit home page")
        return render_template("search.html")

if __name__ == "__main__":
    app.run(debug=False)
        
