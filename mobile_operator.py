import depot as dp

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
        self.callin_val = 0
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
                self.callin_val += 1
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
        print("Call received: ", self.callin_val)

    def get_list_of_items(self):
        return self.queue_items

    @staticmethod
    def show_not_delivered(item):
        print(f"the {item.msg_type} "
              f"from {item.from_who.nr_tel} ({item.from_who.operator.name}) "
              f"to {item.msg_recipient.nr_tel} ({item.msg_recipient.operator.name}) was not delivered")

    @staticmethod
    def starting_process_in_queue(self, list_of_items, operator):
        while list_of_items:
            for item in list_of_items:
                if item.lifetime <= 0:
                    list_of_items.remove(item)
                    # item.from_who.operator.show_not_delivered(item)
                else:
                    if item.msg_recipient.getting_item(item) is False:
                        item.lifetime -= 1
                    else:
                        item.msg_recipient.getting_item(item)
                        dp.get_exception(None, AttributeError, dp.save_data_delivered, item, operator)
                        list_of_items.remove(item)
