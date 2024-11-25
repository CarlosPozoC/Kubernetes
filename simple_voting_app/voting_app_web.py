from flask import Flask, request, render_template, redirect, url_for
import uuid  # For generating unique voter IDs

app = Flask(__name__)

# Store candidates and votes
candidates = {"Belchi": 0, "Tiger": 0}
voters = set()  # Track voter IDs to prevent duplicate voting

# Map to store generated voter IDs (optional for debugging purposes)
voter_id_map = {}

@app.route("/")
def index():
    # Generate a new unique voter ID for each session
    voter_id = str(uuid.uuid4())  # Generate a UUID
    voter_id_map[voter_id] = None  # Add to map to track usage
    return render_template("index.html", candidates=candidates, voter_id=voter_id)

@app.route("/vote", methods=["POST"])
def vote():
    voter_id = request.form.get("voter_id")
    candidate = request.form.get("candidate")

    if voter_id in voters:
        return "You have already voted!", 400

    if candidate not in candidates:
        return "Invalid candidate!", 400

    candidates[candidate] += 1
    voters.add(voter_id)
    voter_id_map[voter_id] = candidate  # Track the vote (optional)
    return redirect(url_for("results"))

@app.route("/results")
def results():
    return render_template("results.html", candidates=candidates)

if __name__ == "__main__":
    app.run(debug=True)

