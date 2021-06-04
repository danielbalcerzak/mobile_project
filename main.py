import depot as dp
from random import randint as rint
from random import choice

NUM_OF_ACTIONS = 100
MIN_KB = 1
MAX_KB = 6


def main():
    operator_list = dp.making_operator_list()
    users_list = dp.making_users_list(operator_list)
    txt = dp.sms_text("text.txt")
    for i in range(NUM_OF_ACTIONS):
        for user in users_list:
            action = rint(1, 3)
            if action == 1:
                user.send_sms(choice(users_list), txt)
            elif action == 2:
                user.send_mms(choice(users_list), rint(MIN_KB, MAX_KB))
            elif action == 3:
                user.calling(choice(users_list))

    for operator in operator_list:
        item_list = operator.get_list_of_items()
        operator.starting_process_in_queue(item_list)

    users_list[0].get_info()


if __name__ == '__main__':
    main()
