import random
import datetime
class Session:
    def __init__(self):
        self.id=random.getrandbits(64)
        self.startTime=datetime.datetime.now()
    def end(self):
        try:
            self.endTime=datetime.datetime.now()
        except Exception:
            self.endTime=0