import datetime

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/time")
def get_time():
	return "<b style='color: blue'>%s</b>" % datetime.datetime.now().isoformat(" ")


@app.route("/checkout")
def show_checkout():
	return open("checkout.html").read()


@app.route("/ajax/foobar")
def checkout():
	item_ids = app.getvalue("item_list")

	# query database with item ids, compute total

	# charge credit card via stripe

	return "{status: 'ok'}"

if __name__ == "__main__":
    app.run()