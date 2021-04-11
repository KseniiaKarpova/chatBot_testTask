import threading
from session import Session
import emotions
import random
import datetime
import query

class Bot():
    def __init__(self):
        self.last = ''
        self.start_chat()
        self.start_timer()
        self.idClient = random.getrandbits(16)
        self.db = query.DATABASE()

    def start(self):
        while True:
            if not self.chat.isAlive():
                self.timer.cancel()
                self.start_chat()
                self.start_timer()
            if not self.timer.isAlive():
                self.chat.join()
                self.start_chat()
                self.start_timer()


    def timer_message(self):
        print("\nБеседа обнуляется")
        self.last=''
        if self.session != None:
            self.session.end()
            self.db.end_session(self.session)
        self.session=None

    def get_emoji(self):
        emj=str(input('You:'))
        self.timeMessage=datetime.datetime.now()
        if self.last=='':
            self.session=Session()
            self.db.new_session(self.session)
        self.db.new_message(self.timeMessage, self.session.id,emj,self.idClient)
        self.change_mood(emj)



    def start_chat(self):
        self.chat = threading.Thread(target=self.get_emoji)
        self.chat.start()

    def start_timer(self):
        self.timer = threading.Timer(61.0, self.timer_message)
        self.timer.start()

    def print_message(self,text):
        print(f'BOT: {text}')

    def INFO(self,info):
        print(f'[INFO] {info}')

    def restart(self):
        #self.start_chat()
        self.start_timer()

    def change_mood(self,emj):
        self.print_message(emotions.choise_text(emj,self,self.last))

