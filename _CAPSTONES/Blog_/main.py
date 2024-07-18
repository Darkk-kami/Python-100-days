from flask import Flask, render_template
from post import Post
import requests

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
posts = [Post(post["id"], post["title"], post["subtitle"], post["body"]) for post in response]


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route("/post/<int:num>")
def blog(num):
    req_post = None
    for post in posts:
        if post.id == num:
            req_post = post
    return render_template("post.html", posts=req_post)


if __name__ == "__main__":
    app.run(debug=True)
