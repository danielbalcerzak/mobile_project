from random import randint as rint
from message import Sms, Mms, Call

START_CALL_SEC = 1
END_CALL_SEC = 20


class Client:
    def __init__(self, nr_tel, operator_name, max_sms, max_mms):
        self.operator_name = operator_name
        self.short_nr_tel = str(nr_tel)
        self.nr_tel = self.operator_name.prefix + self.short_nr_tel
        self.max_sms = max_sms
        self.max_mms_memo = max_mms
        self.sms_income_history = []
        self.sms_received_history = []
        self.mms_income_history = []
        self.mms_received_history = []
        self.call_income_history = []
        self.call_received_history = []

    def get_info(self):
        print(f"Phone number: {self.nr_tel}")
        print(f"Operator: {self.operator_name.name}")
        print(f"Prefix: {self.operator_name.prefix}")
        print(f"Short phone number: {self.short_nr_tel}")
        print(
            f"Memory for sms: {len(self.sms_received_history) + len(self.sms_income_history)} / "
            f"{self.max_sms}")
        print(f"\tsms sent: {len(self.sms_received_history)}")
        print(f"\tsms received: {len(self.sms_income_history)}")
        print(
            f"Memory for mms: {len(self.mms_received_history) + len(self.mms_income_history)} /"
            f" {self.max_mms_memo}")
        print(f"\tmms sent: {len(self.mms_received_history)}")
        print(f"\tmms received: {len(self.mms_income_history)}")
        print(f"Made calls:")
        print(f"\tanswer: {len([call.react for call in self.call_received_history if call.react == 'answer'])}")
        print(f"\tmissed: {len([call.react for call in self.call_received_history if call.react == 'missed'])}")
        print(f"\treject: {len([call.react for call in self.call_received_history if call.react == 'reject'])}")
        print(f"Income calls:")
        print(f"\tanswer: {len([call.react for call in self.call_income_history if call.react == 'answer'])}")
        print(f"\tmissed: {len([call.react for call in self.call_income_history if call.react == 'missed'])}")
        print(f"\treject: {len([call.react for call in self.call_income_history if call.react == 'reject'])}")
        print(f"-" * 30)

    def send_sms(self, client, text):
        sms = Sms(self, client, text)
        if self.checking_memory(self.max_sms, self.sms_received_history + self.sms_income_history):
            self.sms_received_history.append(sms)
        self.operator_name.taking_action(sms)

    def send_mms(self, to, mms_size):
        mms = Mms(self, to, mms_size)
        if self.checking_memory(self.max_mms_memo, self.mms_received_history + self.mms_income_history):
            self.mms_received_history.append(mms)
        self.operator_name.taking_action(mms)

    def calling(self, To):
        call = Call(self, To)
        self.call_received_history.append(call)
        self.operator_name.taking_action(call)

    @staticmethod
    def callin_action(item):
        if item.msg_type == "call":
            action = rint(1, 3)
            if action == 1:
                item.react = "answer"
                time_of_calling = rint(START_CALL_SEC, END_CALL_SEC)
                item.msg_size = time_of_calling
            elif action == 2:
                item.react = "missed"
            elif action == 3:
                item.react = "reject"

    @staticmethod
    def checking_memory(max_memory, memory):
        if max_memory > len(memory):
            return True
        else:
            return False

    def geting_item(self, item):
        self.callin_action(item)
        if item.msg_type == "sms":
            if self.checking_memory(self.max_sms, self.sms_received_history + self.sms_income_history):
                self.sms_income_history.append(item)
        elif item.msg_type == "mms":
            if self.checking_memory(self.max_mms_memo, self.mms_received_history + self.mms_income_history):
                self.mms_income_history.append(item)
        else:
            self.call_income_history.append(item)
