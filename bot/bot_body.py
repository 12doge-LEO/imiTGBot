import os
import threading
import time,logging

import telegram

from db_connnector import imi_db_connector

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

class imiBot():
    def __init__(self):
        self.token = "1872215428:AAFEGNxBPGfskxE2sjWAo6jQczgCqo6_Vms"
        self.update_id = 0

        self.audio_files = {
            'meow1': './meow2.mp3'
        }

    def init(self):
        self.bot = telegram.Bot(token=self.token)
        print(self.bot.getMe())

    def update_audio_cache(self):
        self.audio_files = imi_db_connector.find({"type":"audio_info"})[0]["infos"]
        print(self.audio_files)
        for item in self.audio_files:
            if os.path.exists('../resources/audio/' + self.audio_files[item]):
                continue
            else:
                with open('../resources/audio/' + self.audio_files[item], 'wb') as f:
                    f.write(imi_db_connector.get_file(self.audio_files[item],collection='audio'))


    def create_audio_button(self):
        buttons =[]
        for item in self.audio_files:
            buttons.append(telegram.InlineKeyboardButton(text=item))
        markup = telegram.InlineKeyboardMarkup([buttons])
        return markup

    def response_file(self, filename: str,chat_id=''):
        self.update_audio_cache()
        markup = self.create_audio_button()
        self.bot.s
        self.bot.sendVoice(chat_id=chat_id, voice=open('./resources/audio/'+filename,'rb'))

    def handler(self):
        while True:
            print(f"time : {time.time()}")
            for update in self.bot.getUpdates(offset=self.update_id, timeout=10):
                self.update_id = update.update_id + 1
                print(update.message)
                if "/imi_boats" in update.message["text"]:
                    text = "没有哦"
                    chat_id = update.message["chat"]["id"]
                    self.bot.sendMessage(chat_id=chat_id, text=text)
                if "/imi_intro" in update.message["text"]:
                    text = '<a href="https://t.bilibili.com/516411530349545995?tab=2/">imi可爱！！</a>.'
                    chat_id = update.message["chat"]["id"]
                    self.bot.sendMessage(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
                if "/recorder" in update.message["text"]:
                    text = '<a href="https://live.bilibili.com/record/R1ax411w7U2">imi直播回放地址</a>.'
                    chat_id = update.message["chat"]["id"]
                    self.bot.sendMessage(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
                if "/live" in update.message["text"]:
                    text = '<a href="https://live.bilibili.com/blanc/22605466">imi直播间地址</a>.'
                    chat_id = update.message["chat"]["id"]
                    self.bot.sendMessage(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)
                if "/meow" in update.message["text"]:
                    chat_id = update.message["chat"]["id"]
                    t2 = threading.Thread(target=self.response_file,kwargs={"filename":"meow2.mp3","chat_id":chat_id})
                    t2.start()
                    continue

            time.sleep(1)

    def start(self):
        threads = []
        t1 = threading.Thread(target=self.handler)
        t1.start()
        t1.join()
