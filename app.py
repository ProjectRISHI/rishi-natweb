import os
from flask import Flask,request,render_template
from flask_cache import Cache
from flask_compress import Compress
from lib import gscrape
from time import time

chap = "1BPnZpUqYNw-W9NI8aCIfI-OqL4DNCZf2r1YfEb5gOB0"
marq = "15odV2nwZvLJLvBi5g51Ma8UsgN2WSCKiDt0JeyhEthw"
natmem = "1VTqQ4nyNBbff_ykGOGt0vdnRly8r93ja01sJVWVCgmw"
uclaexec= "19hPOVSAqWRPMGoVySLVjMoywA2o4ukMS3tRoEh8SmXY"
ucbexec = "17KCKd-x8WL5NJHL1dnFex3zHAfSGCqrqCsC0q6Fqljw"
ucsdexec = ""
ucdexec = "19AzcQmIH7r94H1QV0qpP89lOKWWkLdvBjIEMw7ibHUU"
uciexec = "1YalAaHrQH8b9Fd41sWw9-komgr70-vBPE8SV2oo5mzY"
nuexec = "1EcKGSB41tkJhRVVOAvS5hOs0cd2dZAnk7dfW3leg5V0"
ucrexec = "1qdgh2YRp13qg1i5ZZXaLwzkR1hODkBOsaddrcPVPMYo"
uscexec = ""
cppexec = ""
purdueexec = ""

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 300
app.cache=Cache(app)
Compress(app)

@app.cache.cached(key_prefix="marquee")
def get_marquee():
	return gscrape.getMarqueeFeed(marq)

@app.cache.cached(key_prefix="appfeed")
def get_appfeed():
	return gscrape.getAppFeed(chap)

@app.cache.cached(key_prefix="natmem")
def get_national_members():
	return gscrape.getMemberFeed(natmem)

@app.cache.cached(key_prefix="memberfeed")
def get_member_feed():
	return map(gscrape.getMemberFeed,(uclaexec,ucbexec,
		ucsdexec,ucdexec,uciexec,nuexec,ucrexec,uscexec,cppexec,purdueexec))

@app.route('/')
def index():
	marquee=get_marquee()
	return render_template("index.html", title="Home",marquee=marquee)

@app.route('/about')
def about():
	nat_mem=get_national_members()
	return render_template("about.html", title="About", national=nat_mem)

@app.route('/apply')
def apply():
	chap=get_appfeed()
	return render_template("apply.html",title="Apply",appl=chap)

@app.route('/blog')
def blog():
	return render_template("blog.html", title="Blog")

@app.route('/chapters')
def chapters():
	memfeed=get_member_feed()
	chap=get_appfeed()
	return render_template("chapters.html", title="Chapters",
		chapter=chap,uclae=memfeed[0],ucbe=memfeed[1],ucsde=memfeed[2],
		ucde=memfeed[3],ucie=memfeed[4],nue=memfeed[5],ucre=memfeed[6],
		usce=memfeed[7],cppe=memfeed[8],purduee=memfeed[9])

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

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html',title="Error"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', title="Error"), 500


if __name__=="__main__":
	app.run(debug=False)