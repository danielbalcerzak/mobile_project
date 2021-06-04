import depot


class MobileOperator:
    def __init__(self, name):
        self.name = name
        for operator in depot.OPERATOR_DICT:
            prefix = depot.OPERATOR_DICT[operator]
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
            item.msg_recipient.operator.taking_action(item)
            item.msg_recipient.geting_item(item)

    def get_info(self):
        print("Nazwa: ", self.name)
        print("Prefix: ", self.prefix)
        print("SMS wychodzace: ", self.sms_sent_val)
        print("SMS przychodzace: ", self.sms_received_val)
        print("MMS wychodzace: ", self.mms_sent_val)
        print("MMS przychodzace: ", self.mms_received_val)
        print("POLACZENIA wychodzace: ", self.callout_val)
        print("POLACZENIA przychodzace: ", self.callin_val)
