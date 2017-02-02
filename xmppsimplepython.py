import sleekxmpp


class SendMsgBot(sleekxmpp.ClientXMPP):

    """
    Big parts from - http://sleekxmpp.com/getting_started/sendlogout.html (n1 Tutorial)
    A basic SleekXMPP bot that will log in, send a message,
    and then log out.
    """

    def __init__(self, jid, password, recipient, message):
        sleekxmpp.ClientXMPP.__init__(self, jid, password)
        self.recipient = recipient
        self.msg = message
        self.add_event_handler("session_start", self.start)

    def start(self, event):
        self.send_presence()

        self.send_message(mto=self.recipient,mbody=self.msg,mtype='chat')
        self.disconnect(wait=True)

def SendXMPP(msg):
   xmpp = SendMsgBot("JabberIDwithDomain-send@example.com", "JabberPassword", "to@example.com", str(msg)
   #xmpp.register_plugin('xep_0199')

   if xmpp.connect():
      xmpp.process(block=True)
      print("XMPP: Done")
   else:
      print("XMPP: Unable to connect.")
