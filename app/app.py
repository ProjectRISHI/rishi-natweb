import os
from flask import Flask,request,render_template
from time import time
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database=os.environ['database'], 
                            user=os.environ['user'], 
                            password=os.environ['pass'], 
                            host=os.environ['host'], port="5432")

cur = conn.cursor() 

@app.route('/')
def index():
	# marquee=get_marquee()
	# chap=get_appfeed()
	# return render_template("index.html", title="Home",chapters=chap)
	return render_template("index.html", title="Home")

@app.route('/about')
def about():
	cur.execute('''SELECT * FROM users''') 
	data = cur.fetchall()
	conn.close()
	return render_template("about.html", title="About", national=data)

# @app.route('/apply')
# def apply():
# 	# chap=get_appfeed()
# 	return render_template("apply.html",title="Apply",appl=chap)

@app.route('/blog')
def blog():
	return render_template("blog.html", title="Blog")

# @app.route('/chapters')
# def chapters():
# 	# memfeed=get_member_feed()
# 	# chap=get_appfeed()
# 	# return render_template("chapters.html", title="Chapters",
# 	# 	chapter=chap,uclae=memfeed[0],ucbe=memfeed[1],ucsde=memfeed[2],
# 	# 	ucde=memfeed[3],ucie=memfeed[4],nue=memfeed[5],ucre=memfeed[6],
# 	# 	usce=memfeed[7],cppe=memfeed[8],purduee=memfeed[9],drexele=memfeed[10])
# 	return render_template("chapters.html", title="Chapters")

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