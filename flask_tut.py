from flask import Flask, render_template, url_for

app = Flask(__name__)

post = [
    {
        "title": "Post1",
        "author": "Jitu",
        "content": "Post Content",
        "date_posted": "20 November, 2001",
    },
    {
        "title": "Post2",
        "author": "Samarth",
        "content": "Post Content",
        "date_posted": "20 Augugst, 2005",
    },
]


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("/home.html", post=post)


@app.route("/about")
def about():
    return render_template("/about.html", title=about)


if __name__ == "__main__":
    app.run(debug=True)
