from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)


# print(f"configuration - {app.config}")


# breakpoint()


@app.route("/")
def hello_world():
    return "<p>Hello, World!1111</p>"  # First




@app.route("/name")
def one():
    return "<p>Hello, name!1111</p>"  # second  o/p Hello, name!1111


@app.route("/<name>")
def second(name):
    return f"Hello,  your name is display on browser {escape(name)}!"


@app.route("/postrandom/<username>", methods=["POST","GET"])
def third1(username):
    return f"Hello post method{username}"


@app.get("/getrandom")
def third():
    return "Hello get method"  # o/p Hello get method


@app.post("/postrandom")
def fourth():
    return "Hello post method"  # o/p Hello post method


@app.route("/post/<int:post_id>")
def fifth(post_id):
    return f"Hello dynamic type name method {post_id}"  # o/p Hello post method


@app.route("/welcome")
def six():
    return render_template("welcomepage.html")


cricketers = ["virat", "hardik", "rahul"]


@app.route("/cricketers")
@app.route("/cricketers/<string:all_>")
def seven(all_: None):
    return render_template("jinja.html",
                           all_=all,
                           cricketers=cricketers
                           )


# if __name__ == "__main__":
#     app.run()

if __name__ == "__main__":
    app.run(host="localhost", port=8888)
