import os
from flask import Flask,request,render_template
from time import time
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

app = Flask(__name__)

user=quote_plus(os.environ['user'])
password= quote_plus(os.environ['pass'])

uri = "mongodb+srv://"+user+":"+password+"@cluster0.kgvimec.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.rishi_natweb
users = db["users"]
chapter_data = db["chapters"]

@app.route('/')
def index():
	chapters_data = chapter_data.find({"is_active":True})
	return render_template("index.html", title="Home",chapters=chapters_data)

@app.route('/about')
def about():
	data = users.find()
	return render_template("about.html", title="About", national=data)

# @app.route('/apply')
# def apply():
# 	# chap=get_appfeed()
# 	return render_template("apply.html",title="Apply",appl=chap)

@app.route('/blog')
def blog():
	return render_template("blog.html", title="Blog")

@app.route('/chapters')
def chapters():
	chapters_data = chapter_data.find({"is_active":True})
	return render_template("chapters.html", title="Chapters",chapters=chapters_data)

@app.route('/donate')
def donate():
	# chap=get_appfeed()
	# return render_template("donate.html",title="Donate",chapters=chap)
	return render_template("donate.html",title="Donate")

# @app.route('/education')
# def education():
# 	return render_template("education.html",title="Education")

# @app.route('/error')
# def error():
# 	return render_template("error.html",title="Error")

# @app.route('/energy')
# def energy():
# 	return render_template("energy.html",title="Energy")

# @app.route('/health')
# def health():
# 	return render_template("health.html",title="Health")

# @app.route('/water')
# def water():
# 	return render_template("water.html",title="Water")

# @app.route('/income')
# def income():
# 	return render_template("income.html",title="Income")

# @app.route('/locations')
# def locations():
# 	return render_template("locations.html",title="Locations")

# @app.route('/methodology')
# def methodology():
# 	return render_template("methodology.html",title="Methodology")

# @app.route('/nat-apply')
# def nat_apply():
# 	return render_template("nat-apply.html",title="National Application")

# @app.route('/privacy-policy')
# def privacy():
# 	return render_template("privacy-policy.html",title="Privacy Policy")

# @app.route('/projects')
# def projects():
# 	return render_template("projects.html",title="Projects")

# @app.route('/rishi-pay')
# def rishi_pay():
# 	return render_template("rishi-pay.html",title="RISHI Pay")

# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('error.html',title="Error"), 404

# @app.errorhandler(500)
# def internal_server_error(e):
#     return render_template('error.html', title="Error"), 500

if __name__=="__main__":
	app.run(debug=False)