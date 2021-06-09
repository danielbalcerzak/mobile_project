import os
from random import randint as rint
from message import Sms, Mms, Call
import depot as dp
from os.path import isfile, isdir


class Client:
    def __init__(self, nr_tel, operator, max_sms, max_mms):
        self.operator = operator
        self.short_nr_tel = str(nr_tel)
        self.nr_tel = self.operator.prefix + self.short_nr_tel
        self.max_sms = max_sms
        self.max_mms_memo = max_mms
        self.sms_received_history = []
        self.sms_send_history = []
        self.mms_received_history = []
        self.mms_send_history = []
        self.call_received_history = []
        self.call_send_history = []

    def get_info(self):
        print(f"Phone number: {self.nr_tel}")
        print(f"Operator: {self.operator.name}")
        print(f"Prefix: {self.operator.prefix}")
        print(f"Short phone number: {self.short_nr_tel}")
        print(f"Memory for sms: {len(self.sms_send_history) + len(self.sms_received_history)} / {self.max_sms}")
        print(f"\tsms sent: {len(self.sms_send_history)}")
        print(f"\tsms received: {len(self.sms_received_history)}")
        print(f"Memory for mms: {len(self.mms_send_history) + len(self.mms_received_history)} / {self.max_mms_memo}")
        print(f"\tmms sent: {len(self.mms_send_history)}")
        print(f"\tmms received: {len(self.mms_received_history)}")
        print(f"Made calls:")
        print(f"\tanswer: {len([call.react for call in self.call_send_history if call.react == 'answer'])}")
        print(f"\tmissed: {len([call.react for call in self.call_send_history if call.react == 'missed'])}")
        print(f"\treject: {len([call.react for call in self.call_send_history if call.react == 'reject'])}")
        print(f"Received calls:")
        print(f"\tanswer: {len([call.react for call in self.call_received_history if call.react == 'answer'])}")
        print(f"\tmissed: {len([call.react for call in self.call_received_history if call.react == 'missed'])}")
        print(f"\treject: {len([call.react for call in self.call_received_history if call.react == 'reject'])}")
        print(f"-" * 30)

    def send_sms(self, client, text):
        sms = Sms(self, client, text)
        if self.checking_memory(self.max_sms, self.sms_send_history + self.sms_received_history):
            self.sms_send_history.append(sms)
        self.operator.taking_action(sms)

    def send_mms(self, to, mms_size):
        mms = Mms(self, to, mms_size)
        if self.checking_memory(self.max_mms_memo, self.mms_send_history + self.mms_received_history):
            self.mms_send_history.append(mms)
        self.operator.taking_action(mms)

    def calling(self, To):
        call = Call(self, To)
        self.call_send_history.append(call)
        self.operator.taking_action(call)

    @staticmethod
    def callin_action(item):
        if item.msg_type == "call":
            action = rint(1, 3)
            if action == 1:
                item.react = "answer"
                time_of_calling = rint(dp.START_CALL_SEC, dp.END_CALL_SEC)
                item.msg_size = time_of_calling
            elif action == 2:
                item.react = "missed"
            elif action == 3:
                item.react = "reject"

    @staticmethod
    def checking_memory(max_memory, memory) -> bool:
        if max_memory > len(memory):
            return True
        else:
            return False

    def getting_item(self, item):
        self.callin_action(item)
        if item.msg_type == "sms":
            if self.checking_memory(self.max_sms, self.sms_send_history + self.sms_received_history):
                self.sms_received_history.append(item)
            else:
                return False
        elif item.msg_type == "mms":
            if self.checking_memory(self.max_mms_memo, self.mms_send_history + self.mms_received_history):
                self.mms_received_history.append(item)
            else:
                return False
        else:
            self.call_received_history.append(item)

    @staticmethod
    def make_sattlement_for_user(item: object.__class__, user):
        if not isdir("Billing"):
            os.mkdir('Billing')
        if user.nr_tel == item.from_who.nr_tel:
            if not isfile(f'Billing/{user.nr_tel}'):
                with open(f'Billing/{user.nr_tel}', 'w', encoding="utf8") as outfile:
                    description_list = ['sender_phonenumber',
                                        'recipient_phonenumber',
                                        'send_date',
                                        'send_time',
                                        'msg_type',
                                        'msg_text',
                                        'msg_size']
                    for element in description_list:
                        if element is description_list[len(description_list) - 1]:
                            outfile.write(element + '\n')
                        else:
                            outfile.write(element)
                            outfile.write(",")
            with open(f'Billing/{user.nr_tel}', 'a', encoding="utf8") as csvfile:
                csvfile_info_list = [item.from_who.nr_tel,
                                     item.msg_recipient.nr_tel,
                                     item.msg_send_date,
                                     item.msg_send_time,
                                     item.msg_type,
                                     item.msg_text,
                                     item.msg_size]
                for info in csvfile_info_list:
                    if info is csvfile_info_list[len(csvfile_info_list) - 1]:
                        csvfile.write(str(info))
                        csvfile.write('\n')
                    else:
                        csvfile.write(str(info))
                        csvfile.write(",")
