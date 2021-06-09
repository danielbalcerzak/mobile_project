import depot as dp
from os.path import isfile, isdir
import os
import client


class MobileOperator:

    def __init__(self, name):
        self.name = name
        for operator in dp.OPERATOR_DICT:
            prefix = dp.OPERATOR_DICT[operator]
            if operator == self.name:
                self.prefix = prefix
                break
            else:
                self.prefix = None
        self.sms_sent_val = 0
        self.sms_received_val = 0
        self.mms_sent_val = 0
        self.mms_received_val = 0
        self.call_in_val = 0
        self.callout_val = 0
        self.sms_history = []
        self.mms_history = []
        self.call_history = []
        self.queue_items = []

    def taking_action(self, item):
        if item.from_who.operator.name == self.name:
            if item.msg_type == "sms":
                self.sms_history.append(item)
                self.sms_sent_val += 1
            elif item.msg_type == "mms":
                self.mms_history.append(item)
                self.mms_sent_val += 1
            else:
                self.call_history.append(item)
                self.callout_val += 1
        if item.msg_recipient.operator.name == self.name:
            if item.msg_type == "sms":
                self.sms_history.append(item)
                self.sms_received_val += 1
            elif item.msg_type == "mms":
                self.mms_history.append(item)
                self.mms_received_val += 1
            else:
                self.call_history.append(item)
                self.call_in_val += 1
        else:
            self.queue_items.append(item)

    def get_info(self):
        print("Operator name: ", self.name)
        print("Prefix: ", self.prefix)
        print("SMS sent: ", self.sms_sent_val)
        print("SMS income: ", self.sms_received_val)
        print("MMS sent: ", self.mms_sent_val)
        print("MMS income: ", self.mms_received_val)
        print("Call made: ", self.callout_val)
        print("Call received: ", self.call_in_val)

    def get_list_of_items(self) -> list:
        return self.queue_items

    @staticmethod
    def show_not_delivered(item):
        print(f"the {item.msg_type} "
              f"from {item.from_who.nr_tel} ({item.from_who.operator.name}) "
              f"to {item.msg_recipient.nr_tel} ({item.msg_recipient.operator.name}) was not delivered")

    def starting_process_in_queue(self, list_of_items, operator):
        while list_of_items:
            for item in list_of_items:
                if item.lifetime <= 0:
                    list_of_items.remove(item)

                    """Uncomment line if you want to show message undelivered in python terminal"""
                    item.from_who.operator.show_not_delivered(item)

                else:
                    if item.msg_recipient.getting_item(item) is False:
                        item.lifetime -= 1
                    else:
                        item.msg_recipient.getting_item(item)

                        """This line is responsible for writing the operator history to the file"""

                        dp.get_exception(None, AttributeError, self.save_data_delivered, item, operator)

                        "This line is responsible for making sattlement for user "

                        client.Client.make_sattlement_for_user(item, item.from_who)

                        list_of_items.remove(item)

    @staticmethod
    def save_data_delivered(item, operator):
        if not isdir("Operator_statement"):
            os.mkdir('Operator_statement')
        if operator.name == item.from_who.operator.name:
            if not isfile(f'Operator_statement/operator_{item.from_who.operator.name}_bill.csv'):
                with open(f'Operator_statement/operator_{item.from_who.operator.name}_bill.csv', 'w', encoding="utf8") \
                        as outfile:
                    description_list = ['sender_operator',
                                        'sender_prefix',
                                        'sender_phonenumber',
                                        'recipient_operator',
                                        'recipient_prefix',
                                        'recipient_phonenumber',
                                        'msg_type',
                                        'msg_text',
                                        'msg_size',
                                        'send_date',
                                        'send_time']
                    for element in description_list:
                        if element is description_list[len(description_list) - 1]:
                            outfile.write(element + '\n')
                        else:
                            outfile.write(element)
                            outfile.write(",")

            with open(f'Operator_statement/operator_{item.from_who.operator.name}_bill.csv', 'a', encoding="utf8") \
                    as csvfile:
                csvfile_info_list = [item.from_who.operator.name,
                                     item.from_who.operator.prefix,
                                     item.from_who.nr_tel,
                                     item.msg_recipient.operator.name,
                                     item.msg_recipient.operator.prefix,
                                     item.msg_recipient.nr_tel,
                                     item.msg_type,
                                     item.msg_text,
                                     item.msg_size,
                                     item.msg_send_date,
                                     item.msg_send_time]
                for info in csvfile_info_list:
                    if info is csvfile_info_list[len(csvfile_info_list) - 1]:
                        csvfile.write(str(info))
                        csvfile.write('\n')
                    else:
                        csvfile.write(str(info))
                        csvfile.write(",")
