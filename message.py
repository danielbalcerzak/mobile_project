from datetime import datetime


class Message:

    date = datetime.now()

    def __init__(self, sender, recipient):
        self.from_who = sender
        self.msg_recipient = recipient
        self.msg_send_date = self.date.date()
        self.msg_send_time = self.date.time()
        self.msg_size = 1
        self.msg_status = False
        self.lifetime = 3
        self.msg_text = None

    def change_status(self):
        self.msg_status = not self.msg_status

    def get_info(self):
        print(f"From: {self.from_who}\n"
              f"To: {self.msg_recipient}\n"
              f"Date and Time: {self.msg_send_date}, {self.msg_send_time}")


class Sms(Message):
    def __init__(self, sender, recipient, text):
        super().__init__(sender=sender, recipient=recipient)
        self.msg_text = text
        self.msg_type = "sms"

    def get_info(self):
        super().get_info()
        print(f"Message: {self.msg_text}")


class Mms(Message):
    def __init__(self, sender, recipient, kB):
        super().__init__(sender=sender, recipient=recipient)
        self.msg_size = kB
        self.msg_type = "mms"


class Call(Message):
    def __init__(self, sender, recipient):
        super().__init__(sender=sender, recipient=recipient)
        self.msg_type = "call"
        self.react = None
        self.lifetime = 1
