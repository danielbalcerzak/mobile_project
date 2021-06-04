import mobile_operator
import client
from random import randint as rint
from random import choice


NUM_OF_USERS = 1000
MIN_ITEM = 10
MAX_ITEM = 200
FIRST_NUM = 100000000
LAST_NUM = 999999999
SMS_LONG = 160
OPERATOR_DICT = {"era": "+10",
                 "idea": "+11",
                 "plus": "+12",
                 "play": "+13",
                 "redbull": "+14"}
USERS = []


def making_operator_list():
    return [mobile_operator.MobileOperator(operator) for operator in OPERATOR_DICT]


def open_file_to_text(file):
    with open(file, "r", encoding="utf-8") as text:
        return text.read()


def sms_text(file):
    text = open_file_to_text(file)
    sms_long = rint(1, SMS_LONG)
    start_text = rint(1, len(text)-sms_long)
    sms = text[start_text:start_text+sms_long]
    return sms


def making_users_list(oper):
    cell_nums = []
    while len(set(cell_nums)) != NUM_OF_USERS:
        num = rint(FIRST_NUM, LAST_NUM)
        cell_nums.append(num)
    for num in cell_nums:
        oper_rand = choice(oper)
        cl = client.Client(num, oper_rand, rint(MIN_ITEM, MAX_ITEM), rint(MIN_ITEM, MAX_ITEM))
        USERS.append(cl)
    userlist = USERS.copy()
    return userlist
