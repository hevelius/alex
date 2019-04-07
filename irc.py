import socket
import socks
import sys
import ssl

class IRC:

    #socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
    #socket.socket = socks.socksocket()

    irc = socks.socksocket()

    def __init__(self):
        self.irc.set_proxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
        #self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, chan, msg):
        self.irc.send("PRIVMSG %s :%s\r\n" % (chan, msg))

    def connect(self, server, port, chanpwd, botnick, botpassword):
        print "connecting to:"+server
        self.irc.connect((server, port))
        self.irc = ssl.wrap_socket(self.irc)
        print "recv 1", self.irc.recv(512)
        self.irc.send("PASS %s\r\n" % (botpassword))
        self.irc.send("NICK %s\r\n" % (botnick))
        self.irc.send("USER %s 8 * :%s\r\n" % (botnick, botnick))

    def quit(self):
    	self.irc.send("QUIT\r\n")
    	self.irc.shutdown(socket.SHUT_RDWR)
    	self.irc.close()

    def pong(self, msg):
	       self.irc.send('PONG ' + msg.split() [1] + '\r\n')

    def join(self, channel, chanpwd):
	       self.irc.send("JOIN " + channel + " " + chanpwd + "\n")

    def get_text(self):
        text=self.irc.recv(1024)
        return text
