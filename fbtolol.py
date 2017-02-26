import zxlolbot
import fbchat
fbid1 = "100000558890658"
fbid2 = "100001634566769"
fbid3 = "100001793100062"
fbid4 = "100001670174662"
class helloworld(zxlolbot.zxLoLBoT):

    def __init__(self, username, password, region="EUW"):
        zxlolbot.zxLoLBoT.__init__(self, username, password, region)
        self.add_event_handler("message", self.on_message)
    def on_message(self, args): #by default, message received by LoL bot is sent to
        msg=args["message"] #facebook user with id = fbid1
        receiver=andra
        parameter=msg[0]+msg[1] #if the message received by the bot starts with -a
        if parameter == "-a":  #the message is sent to fbid2
            msg=msg[2:]
            receiver=ady
        elif parameter == "-l": #if the message received by the bot starts with -l
            msg=msg[2:] #the message is sent to the last person that messaged you on facebook
            receiver=bot.last
        #print(bot.last)
        #bot.send(bot.last,args["message"])
        bot.send(receiver, msg)
    @zxlolbot.botcommand
    def hello(self, sender, args):
        """Replies Hello world to the sender
        Usage: hello
        Example: hello"""
        self.message(sender, "Hello world")
        print ("%s"%sender)
if __name__ == "__main__":
	lolbot = helloworld("user", "pass") #edit with your bot username and password
	lolbot.connect()
	
class EchoBot(fbchat.Client):
    last = "xd"
    def __init__(self,email, password, debug=False, user_agent=None):
        fbchat.Client.__init__(self,email, password, debug, user_agent)

    def on_message(self, mid, author_id, author_name, message, metadata):
        self.markAsDelivered(author_id, mid) #mark delivered
        self.markAsRead(author_id) #mark read
        sender_name = "unknown";
        if author_id == fbid1:
            sender_name="fb user 1"
        elif author_id == fbid2:
            sender_name="fb user 2"
        elif author_id == fbid3:
            sender_name="fb user 3"
        elif author_id == fbid4:
            sender_name="fb user 4"
        else: sender_name=author_id    #you can add more users
        #if you are not the author, echo
        if str(author_id) != str(self.uid):
            #self.send(author_id,'teti')
            lolbot.message("sum41567590@pvp.net/xiff", "%s said: %s"%(sender_name, message)) 
			#edit with your pvp.net id^
            print("%s said: %s"%(sender_name, message))
            self.last=author_id


bot = EchoBot("user1", "pass1") #edit with your facebook login details
bot.listen()