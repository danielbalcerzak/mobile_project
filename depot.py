import mobile_operator
import client
from random import randint as rint
from random import choice
from os.path import isfile


# client variables
START_CALL_SEC = 1
END_CALL_SEC = 20

# depot variables
NUM_OF_ACTIONS = 50
MIN_KB = 1
MAX_KB = 6
NUM_OF_USERS = 10
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

def start_operators_action(operator_list):
    for operator in operator_list:
        item_list = operator.get_list_of_items()
        operator.starting_process_in_queue(item_list, operator)


def start_send_and_call(users_list):
    for i in range(NUM_OF_ACTIONS):
        txt = sms_text("text.txt")
        for user in users_list:
            action = rint(1, 3)
            if action == 1:
                user.send_sms(choice(users_list), txt)
            elif action == 2:
                user.send_mms(choice(users_list), rint(MIN_KB, MAX_KB))
            elif action == 3:
                user.calling(choice(users_list))

def making_operator_list():
    return [mobile_operator.MobileOperator(operator) for operator in OPERATOR_DICT]


def open_file_to_text(file):
    with open(file, "r", encoding="utf-8") as text:
        return text.read()


def sms_text(file):
    text = open_file_to_text(file)
    sms_long = rint(1, SMS_LONG)
    start_text = rint(1, len(text)-sms_long)
    sms = text[start_text:start_text+sms_long].replace("\n", " ").replace(",", "")
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


def get_exception(default, exception, function, *args):
    try:
        return function(*args)
    except exception:
        return default


def save_data_delivered(item, operator):
    if operator.name == item.from_who.operator.name:
        if not isfile(f'operator_{item.from_who.operator.name}_bill.csv'):
            with open(f'operator_{item.from_who.operator.name}_bill.csv', 'w', encoding="utf8") as outfile:
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
                    if element is description_list[len(description_list)-1]:
                        outfile.write(element + '\n')
                    else:
                        outfile.write(element)
                        outfile.write(",")

        with open(f'operator_{item.from_who.operator.name}_bill.csv', 'a', encoding="utf8") as csvfile:
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
