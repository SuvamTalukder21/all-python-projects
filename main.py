import requests
from flask import Flask, render_template


app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(url=blog_url)
blog_posts = response.json()


@app.route("/")
def home():
    return render_template("index.html", all_posts=blog_posts)


@app.route("/post/<int:index>")
def show_post(index):
    return render_template("post.html", all_posts=blog_posts, blog_id=index)


if __name__ == "__main__":
    app.run(debug=True)
