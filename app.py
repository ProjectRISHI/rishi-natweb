from flask import Flask,request,render_template
from lib import gscrape

app = Flask(__name__)

chap_apply = "https://spreadsheets.google.com/feeds/list/1BPnZpUqYNw-W9NI8aCIfI-OqL4DNCZf2r1YfEb5gOB0/od6/public/basic?alt=json"
marq = "https://spreadsheets.google.com/feeds/list/15odV2nwZvLJLvBi5g51Ma8UsgN2WSCKiDt0JeyhEthw/od6/public/basic?alt=json"

chap_apply=gscrape.getEntry(chap_apply)
chap_apply=gscrape.getFeedList(chap_apply)
marq=gscrape.getEntry(marq)
marq=gscrape.getFeedList(marq)

@app.route('/')
def index():
	marquee=list()
	for dic in marq:
		marquee.append({"content":gscrape.getMarquee(dic),"link":gscrape.getMarqueeLink(dic)})
	return render_template("index.html", title="Home",marquee=marquee)

@app.route('/about')
def about():
	return render_template("about.html", title="About")

@app.route('/apply')
def apply():
	appl=list()
	for dic in chap_apply:
		appl.append({"chapter":gscrape.getChapter(dic),"due_date":gscrape.getDueDate(dic),"link":gscrape.getAppLink(dic),"contact":gscrape.getContactInfo(dic),"seal":gscrape.getSeal(dic)})
	return render_template("apply.html",title="Apply",appl=appl)

@app.route('/blog')
def blog():
	return render_template("blog.html", title="blog")

@app.route('/chapters')
def chapters():
	return render_template("chapters.html", title="Chapters")

@app.route('/donate')
def donate():
	return render_template("donate.html",title="Donate")

@app.route('/education')
def education():
	return render_template("education.html",title="Education")

@app.route('/error')
def error():
	return render_template("error.html",title="Error")

@app.route('/energy')
def energy():
	return render_template("energy.html",title="Energy")

@app.route('/health')
def health():
	return render_template("health.html",title="Health")

@app.route('/water')
def water():
	return render_template("water.html",title="Water")

@app.route('/income')
def income():
	return render_template("income.html",title="Income")

@app.route('/locations')
def locations():
	return render_template("locations.html",title="Locations")

@app.route('/methodology')
def methodology():
	return render_template("methodology.html",title="Methodology")

@app.route('/nat-apply')
def nat_apply():
	return render_template("nat-apply.html",title="National Application")

@app.route('/privacy-policy')
def privacy():
	return render_template("privacy-policy.html",title="Privacy Policy")

@app.route('/projects')
def projects():
	return render_template("projects.html",title="Projects")

@app.route('/rishi-pay')
def rishi_pay():
	return render_template("rishi-pay.html",title="RISHI Pay")

if __name__=="__main__":
	app.run(debug=False)