import depot
import random


def main():
    ac_val = 10000
    operator_list = depot.making_operator_list()
    users_list = depot.making_users_list(operator_list)

    for val in range(ac_val):
        for user in users_list:
            action = random.randint(1, 3)
            if action == 1:
                user.send_sms(random.choice(users_list), "d")
            elif action == 2:
                user.send_mms(random.choice(users_list), 22)
            elif action == 3:
                user.calling(random.choice(users_list))

    users_list[0].get_info()
    users_list[3].get_info()


if __name__ == '__main__':
    main()
