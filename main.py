import telebot
import constants
import subprocess
import os

bot = telebot.TeleBot(constants.token)


def getUpdate():
    bot.polling(none_stop=False, interval=0)
    upd = bot.get_updates()
    last_upd = upd[-1]
    message = last_upd.message.text
    return message


def cleanFile():

    path = 'C:\\Users\Amin Kasimov\Desktop\Music'
    files = sorted(os.listdir(path), key=lambda x: os.path.getctime(os.path.join(path, x))) #lambda is an anonymous function
    if "Thumbs.db" in files: files.remove("Thumbs.db")
    return files[-1]  #returns the latest file (they are listed by order of creation)

def downloadMusic(message):

    subprocess.call("youtube-dl -x --audio-format mp3 -o ~/Desktop/Music/%(title)s.%(ext)s ytsearch:" + message.replace(" ", "") +"")

def retrieveMusic():

    rel_path = "\Music" + """\\""" + cleanFile()
    script_dir = os.path.dirname("""C:\\Users\Amin Kasimov\Desktop\ """)  # <-- absolute dir the script is in
    path = script_dir + rel_path
    abs_file_path = os.path.join(path)
    audio = open(abs_file_path, 'rb')
    return audio


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi, I am Dolores, let me find your favorite songs :)")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    downloadMusic(message.text)
    bot.send_audio(str(message.from_user.id), retrieveMusic())



getUpdate()
