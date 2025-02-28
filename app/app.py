from flask import Flask, render_template

app = Flask(__name__)  # Create a Flask app instance

@app.route("/")
def home():
    return render_template("index.html")  # Loads homepage

@app.route("/blog")
def blog():
    return render_template("blog.html")  # Loads blog page

if __name__ == "__main__":
    app.run(debug=True)