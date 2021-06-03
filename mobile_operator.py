class MobileOperator:
    operator_dict = {"plus": "+12", "play": "+13"}
    def __init__(self, nazwa, ):
        self.nazwa = nazwa
        for operat in self.operator_dict:
            prefix = self.operator_dict[operat]
            if operat == self.nazwa:
                self.prefix = prefix
                break
            else:
                self.prefix = None
        self.ilosc_sms_wychodzacych = 0
        self.ilosc_sms_przychodzacych = 0
        self.ilosc_mms_wychodzacych = 0
        self.ilosc_mms_przychodzacych = 0
        self.ilosc_polaczen_przychodzacych = 0
        self.ilosc_polaczen_wychodzacych = 0
        self.historia_sms = []
        self.historia_mms = []
        self.historia_polaczen = []

    def save_and_push(self, item):
        if item.od.operator.nazwa == self.nazwa:
            if item.rodzaj == "sms":
                self.historia_sms.append(item)
                self.ilosc_sms_wychodzacych +=1
            elif item.rodzaj == "mms":
                self.historia_mms.append(item)
                self.ilosc_mms_wychodzacych += 1
            else:
                self.historia_polaczen.append(item)
                self.ilosc_polaczen_wychodzacych += 1
        if item.do.operator.nazwa == self.nazwa:
            if item.rodzaj == "sms":
                self.historia_sms.append(item)
                self.ilosc_sms_przychodzacych +=1
            elif item.rodzaj == "mms":
                self.historia_mms.append(item)
                self.ilosc_mms_przychodzacych += 1
            else:
                self.historia_polaczen.append(item)
                self.ilosc_polaczen_przychodzacych += 1
        else:
            item.do.operator.save_and_push(item)

    def get_info(self):
        print("Nazwa: ", self.nazwa)
        print("Prefix: ",self.prefix)
        print("SMS wychodzace: ",self.ilosc_sms_wychodzacych)
        print("SMS przychodzace: ",self.ilosc_sms_przychodzacych)
        print("MMS wychodzace: ",self.ilosc_mms_wychodzacych)
        print("MMS przychodzace: ",self.ilosc_mms_przychodzacych)
        print("POLACZENIA wychodzace: ",self.ilosc_polaczen_wychodzacych)
        print("POLACZENIA przychodzace: ",self.ilosc_polaczen_przychodzacych)
