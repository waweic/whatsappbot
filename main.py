#!/usr/bin/python

import whatsappbot

bot = whatsappbot.Bot()

while (not bot.start()):
    pass

while (not bot.getchat("Changeme")):
    pass

while (not bot.sendmessage("Spam") or True):
    pass
