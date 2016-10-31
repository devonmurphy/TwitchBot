import re
from time import sleep
import socket

HOST = "irc.twitch.tv"
PORT = 6667
NICK = "yxbljab"
PASS = "oauth:"
CHAN = "#yxbljab"
RATE = (20 / 30)
CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

def main_loop():
    try:
        s = socket.socket()
        s.connect((HOST, PORT))
        s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
        s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
        s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))
        connected = True
    except Exception as e:
        print(str(e))
        connected = False

    while connected:
        response = s.recv(1024).decode("utf-8")
        if response == "PING :tmi.twitch.tv\r\n":
            s.send("PONG :tmi.twitch.tv\r\n".encode())
            print("PONG")
        else:
            username = re.search(r"\w+", response).group(0)
            message = CHAT_MSG.sub("", response)
            
            if message == "!right\r\n":
                print "right"
            if message == "!left\r\n":
                print "left"
            if message == "!up\r\n":
                print "up"
            if message == "!down\r\n":
                print "down"
        print(username + ": " + message)
"""
            if message == "!test\r\n":
                print "correct message"
                chat(s, "Testing command received!")
"""

def chat(sock, msg):
    sock.send("PRIVMSG {} :{}\r\n".format(CHAN, msg).encode())

if __name__ == "__main__":
    main_loop()
