from irc import *
from bot import *
import signal
import sys
import string
import ConfigParser
import ast
import logging
import time

config = ConfigParser.RawConfigParser()
config.read('default.cfg')

channels = config.get('base', 'channels').split(',')
chanpwd = config.get('base', 'chanpwd')
server = config.get('base', 'server')
nickname = config.get('base', 'nickname')
password = config.get('base', 'password')
port = int(config.get('base', 'port'))

placeholder = config.get('bot', 'placeholder')
replies = ast.literal_eval(config.get('bot','replies'))

print placeholder

irc = IRC()
bot = BOT(nickname,replies,placeholder)

#logger = logging.getLogger(__name__)
#logging.basicConfig(level=logging.INFO)

def signal_handler(signal, frame):
	irc.quit()
	sys.exit(0)

def init_logger():
	timestr = time.strftime("%Y%m%d-%H%M%S")
	fh = logging.FileHandler(timestr+".log")
	formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
	fh.setFormatter(formatter)
	#logger.addHandler(fh)

#init_logger()

def Main():
	signal.signal(signal.SIGINT, signal_handler)
	irc.connect(server, port, chanpwd, nickname, password)

	while True:
		text = irc.get_text()
		#logger.info(text)
		isInChannel = False
		channel = ''
		print text
		for eachChannel in channels:
			if eachChannel in text:
				isInChannel = True
				channel = eachChannel
		if "PRIVMSG" in text and isInChannel and bot.has_reply(text):
			botReply = bot.reply(text)
			if isinstance(botReply, list):
				for eachFeed in botReply:
					irc.send(channel, eachFeed.encode('utf-8').strip())
			else:
				irc.send(channel, botReply)
		if text.find('PING') != -1:
			irc.pong(text)
			for eachChannel in channels:
				irc.join(eachChannel,chanpwd)
		#if "KICK" in text and nickname in text:
		#	irc.join(channel,chanpwd)

Main()
exit(0)
