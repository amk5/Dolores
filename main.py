import telebot
import constants
import subprocess

bot = telebot.TeleBot(constants.token)

#bot.send_message(302541761, "Hi, type a music you want to download")

upd = bot.get_updates()
last_upd = upd[-1]
message_from_user = last_upd.message.text


#video = subprocess.check_call('youtube-dl ytsearch:['+ str(message_from_user) +']')
subprocess.call('youtube-dl --audio-format mp3 -o ~/Desktop/%(title)s.%(ext)s ytsearch:['+ str(message_from_user) +']')

#import pdb; pdb.set_trace()

