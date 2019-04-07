import feedparser
from weather import Weather

class BOT:

	nickname = ""
	placeholder = ""
	Replies = dict()
	weather = Weather()

	def __init__(self, nickname, replies, placeholder):
		self.nickname = nickname
		replies[nickname] = replies.pop("@")
		for eachKey in replies.keys():
			replies[eachKey] = replies[eachKey].replace("@",nickname)
		self.Replies = replies
		self.placeholder = placeholder

	def has_reply(self, msg):
		for eachKey in self.Replies.keys():
			if "{}{}".format(self.placeholder,eachKey) in msg:
				return True
		return False

	def reply(self, msg):
		for eachKey in self.Replies.keys():
			if "{}{}".format(self.placeholder,eachKey) in msg:
				option = ''
				if len(msg.split(eachKey))>1:
					option = msg.split(eachKey,1)[1]
				if eachKey=="ansa":
					d = feedparser.parse('http://www.ansa.it/sito/notizie/topnews/topnews_rss.xml')
					headlines = []
					for eachFeed in d['items']:
						headlines.append(eachFeed['title']+ ' - ' +eachFeed['description'] + '['+ eachFeed['link'] +']')
					return headlines
				if eachKey=="weather":
					lookup = self.weather.lookup_by_location(option)
					condition = lookup.condition()
					return condition.text()
				return self.Replies[eachKey]
		return ""
