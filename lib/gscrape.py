import urllib2
import json

def getEntry(url):
	response = urllib2.urlopen(url)
	html = response.read()
	html = json.loads(html)
	feed=html["feed"]
	return feed["entry"]

def getDueDate(dic):
	return str(dic["content"]["$t"]).split(',')[2].split(':')[1].strip()

def getAppLink(dic):
	return str(dic["content"]["$t"]).split(',')[3].split(' ')[2].strip()

def getContactInfo(dic):
	return str(dic["content"]["$t"]).split(',')[1].split(':')[1].strip()

def getSeal(dic):
	return str(dic["content"]["$t"]).split(',')[0].split(' ')[1].strip()

def getChapter(dic):
	return str(dic["title"]["$t"])

def getFeedList(obj):
	y=list()
	for x in obj:
		y.append(x)
	return y

def getMarquee(dic):
	return str(dic["content"]["$t"]).split(',')[0].split(':')[1].strip()

def getMarqueeLink(dic):
	return str(dic["content"]["$t"]).split(',')[1].split(' ')[2].strip()