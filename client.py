from message import Sms, Mms, Call

class Client:
    def __init__(self, nr_tel, oper, max_sms, max_mms):
        self.operator = oper
        self.short_nr_tel = str(nr_tel)
        self.nr_tel = self.operator.prefix + self.short_nr_tel
        self.max_liczba_sms = max_sms
        self.max_pamiec_mms = max_mms
        self.historia_sms_przychodzace = []
        self.historia_sms_wychodzace = []
        self.historia_mms_przychodzace = []
        self.historia_mms_wychodzace = []
        self.historia_polaczen_przychodzace = []
        self.historia_polaczen_wychodzace = []

    def send_sms(self, client, text):
        sms = Sms(self, client, text)
        self.operator.taking_action(sms)

    def send_mms(self, to, mms_size):
        mms = Mms(self, to, mms_size)
        self.operator.taking_action(mms)

    def calling(self, To):
        call = Call(self, To)
        self.operator.taking_action(call)

    def callin_action(self):
        pass

    def geting_item(self, item):
        if item.rodzaj == "sms":
            if len(self.historia_sms_przychodzace)+len(self.historia_sms_wychodzace) <= self.max_liczba_sms:
                self.historia_sms_przychodzace.append(item)
        elif item.rodzaj == "mms":
            memory = 0
            for mms in self.historia_mms_przychodzace:
                memory += mms.wielkosc
            if memory <= self.max_pamiec_mms:
                self.historia_mms_przychodzace.append(item)
        else:
            self.historia_polaczen_przychodzace.append(item)

