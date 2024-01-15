from app import app
from flask import render_template
from dotenv import load_dotenv
import os

load_dotenv()


@app.route("/")
@app.route("/index")
def index():
    client_id = os.getenv.get("CLIENT_ID")
    client_secret = os.getenv.get("CLIENT_SECRET")

    print(f"{client_id=}")
    print(f"{client_secret=}")

    user = {"username": "Ngoc"}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)


# Helper methods
# def generate_random_string(length: int):
#     possible_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
#     values =
