from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Your Basic Details</h1>
    <p><b>Name:</b> Raghu Vamshidhar Reddy</p>
    <p><b>Profession:</b> IT Student / Intern</p>
    <p><b>Education:</b> Master's in Information Systems Technologies</p>
    <p><b>Current Goal:</b> Applying for IT Internship</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
