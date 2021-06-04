from datetime import datetime


class Message:

    date = datetime.now()

    def __init__(self, od, do):
        self.od = od
        self.do = do
        self.data = self.date.date()
        self.godzina = self.date.time()
        self.wielkosc = 1
        self.status = False

    def change_status(self):
        self.status = not self.status

    def get_info(self):
        print(f"From: {self.od}\nTo: {self.do}\nDate and Time {self.data}, {self.godzina}")


class Sms(Message):
    def __init__(self, od, do, tresc):
        super().__init__(od=od, do=do)
        self.tresc = tresc
        self.rodzaj = "sms"

    def get_info(self):
        super().get_info()
        print(f"Message: {self.tresc}")


class Mms(Message):
    def __init__(self, od, do, kB):
        super().__init__(od=od, do=do)
        self.wielkosc = kB
        self.rodzaj = "mms"


class Call(Message):
    def __init__(self, od, do):
        super().__init__(od=od, do=do)
        self.rodzaj = "call"
        self.action = None
