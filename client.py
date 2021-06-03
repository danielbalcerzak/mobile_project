from message import Sms
from mobile_operator import MobileOperator as mo

class Client:
    def __init__(self, nr_tel, oper, max_sms, max_mms):
        self.nr_tel = nr_tel
        self.operator = oper
        self.max_liczba_sms = max_sms
        self.max_liczba_mms = max_mms
        self.historia_sms = []
        self.historia_mms = []
        self.historia_polaczen = []

    def send_sms(self, client, text):
        sms = Sms(self, client, text)
        self.operator.save_and_push(sms)


    def send_mms(self):
        pass

    def calling(self):
        pass

    def callin_action(self):
        pass

    def taking_item(self):
        pass
