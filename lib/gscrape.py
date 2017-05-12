import urllib2
import json


def getURL(key):
	return "https://spreadsheets.google.com/feeds/list/"+str(key)+"/od6/public/basic?alt=json"

def getEntry(url):
	response = urllib2.urlopen(url)
	html = response.read()
	html = json.loads(html)
	feed=html["feed"]
	return feed["entry"]

def getTitle(dic):
	return str(dic["title"]["$t"])

def getPosition(dic):
	return str(dic["content"]["$t"]).split(',')[0].split(':')[1].strip()

def getEmail(dic):
	return str(dic["content"]["$t"]).split(',')[1].split(':')[1].strip()

def getPhoto(dic):
	return str(dic["content"]["$t"]).split(',')[2].split(' ')[2].strip()

def getDueDate(dic):
	return str(dic["content"]["$t"]).split(',')[2].split(':')[1].strip()

def getAppLink(dic):
	return str(dic["content"]["$t"]).split(',')[3].split(' ')[2].strip()

def getContactInfo(dic):
	return str(dic["content"]["$t"]).split(',')[1].split(':')[1].strip()

def getSeal(dic):
	return str(dic["content"]["$t"]).split(',')[0].split(' ')[1].strip()

def getTitle(dic):
	return str(dic["title"]["$t"])

def getHashtag(dic):
	return str(dic["content"]["$t"]).split(',')[4].split(':')[1].strip()

def getMarquee(dic):
	return str(dic["content"]["$t"]).split(',')[0].split(':')[1].strip()

def getMarqueeLink(dic):
	return str(dic["content"]["$t"]).split(',')[1].split(' ')[2].strip()

def getFeedList(key):
	url=getURL(key)
	obj=getEntry(url)
	y=[x for x in obj]
	return y

# Feed Code Below
def getMarqueeFeed(key):
	feed=getFeedList(key)
	feed_list=[{"content":getMarquee(dic),"link":getMarqueeLink(dic)} for dic in feed]
	return feed_list

def getAppFeed(key):
	feed=getFeedList(key)
	feed_list=[{"chapter":getTitle(dic),"hashtag":getHashtag(dic),"due_date":getDueDate(dic),"link":getAppLink(dic),"contact":getContactInfo(dic),"seal":getSeal(dic)} for dic in feed]
	return feed_list

def getMemberFeed(key):
	if key:
		feed=getFeedList(key)
		mem=[{"name":getTitle(dic),"email": getEmail(dic),"position":getPosition(dic),"photo": getPhoto(dic)} for dic in feed]
		return mem
	else:
		return [{"name":"","email":"","position":"","photo": ""}] 
