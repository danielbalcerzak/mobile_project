from random import randint as rint
from message import Sms, Mms, Call

START_CALL_SEC = 1
END_CALL_SEC = 20


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

    def get_info(self):
        print(f"Phone number: {self.nr_tel}")
        print(f"Operator: {self.operator.name}")
        print(f"Prefix: {self.operator.prefix}")
        print(f"Short phone number: {self.short_nr_tel}")
        print(
            f"Memory for sms: {len(self.historia_sms_wychodzace) + len(self.historia_sms_przychodzace)} / "
            f"{self.max_liczba_sms}")
        print(f"\tsms sent: {len(self.historia_sms_wychodzace)}")
        print(f"\tsms received: {len(self.historia_sms_przychodzace)}")
        print(
            f"Memory for mms: {len(self.historia_mms_wychodzace) + len(self.historia_mms_przychodzace)} /"
            f" {self.max_pamiec_mms}")
        print(f"\tmms sent: {len(self.historia_mms_wychodzace)}")
        print(f"\tmms received: {len(self.historia_mms_przychodzace)}")
        print(f"Made calls:")
        print(f"\tanswer: "
              f"{len([call.action_of_the_recipient for call in self.historia_polaczen_wychodzace if call.action_of_the_recipient == 'answer'])}")
        print(f"\tmissed: "
              f"{len([call.action_of_the_recipient for call in self.historia_polaczen_wychodzace if call.action_of_the_recipient == 'missed'])}")
        print(f"\treject: "
              f"{len([call.action_of_the_recipient for call in self.historia_polaczen_wychodzace if call.action_of_the_recipient == 'reject'])}")
        print(f"Income calls:")
        print(f"\tanswer: "
              f"{len([call.action_of_the_recipient for call in self.historia_polaczen_przychodzace if call.action_of_the_recipient == 'answer'])}")
        print(f"\tmissed: "
              f"{len([call.action_of_the_recipient for call in self.historia_polaczen_przychodzace if call.action_of_the_recipient == 'missed'])}")
        print(f"\treject: "
              f"{len([call.action_of_the_recipient for call in self.historia_polaczen_przychodzace if call.action_of_the_recipient == 'reject'])}")
        print(f"-" * 30)

    def send_sms(self, client, text):
        sms = Sms(self, client, text)
        if self.checking_memory(self.max_liczba_sms, self.historia_sms_wychodzace + self.historia_sms_przychodzace):
            self.historia_sms_wychodzace.append(sms)
        self.operator.taking_action(sms)

    def send_mms(self, to, mms_size):
        mms = Mms(self, to, mms_size)
        if self.checking_memory(self.max_pamiec_mms, self.historia_mms_wychodzace + self.historia_mms_przychodzace):
            self.historia_mms_wychodzace.append(mms)
        self.operator.taking_action(mms)

    def calling(self, To):
        call = Call(self, To)
        self.historia_polaczen_wychodzace.append(call)
        self.operator.taking_action(call)

    @staticmethod
    def callin_action(item):
        if item.msg_type == "call":
            action = rint(1, 3)
            if action == 1:
                item.action_of_the_recipient = "answer"
                time_of_calling = rint(START_CALL_SEC, END_CALL_SEC)
                item.msg_size = time_of_calling
            elif action == 2:
                item.action_of_the_recipient = "missed"
            elif action == 3:
                item.action_of_the_recipient = "reject"

    @staticmethod
    def checking_memory(max_memory, memory):
        if max_memory > len(memory):
            return True
        else:
            return False

    def geting_item(self, item):
        self.callin_action(item)
        if item.msg_type == "sms":
            if self.checking_memory(self.max_liczba_sms, self.historia_sms_wychodzace + self.historia_sms_przychodzace):
                self.historia_sms_przychodzace.append(item)
        elif item.msg_type == "mms":
            if self.checking_memory(self.max_pamiec_mms, self.historia_mms_wychodzace + self.historia_mms_przychodzace):
                self.historia_mms_przychodzace.append(item)
        else:
            self.historia_polaczen_przychodzace.append(item)
