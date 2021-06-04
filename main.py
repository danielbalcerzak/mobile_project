import depot
import random
import mobile_operator


def main():
    ac_val = 10
    operator_list = depot.making_operator_list()
    users_list = depot.making_users_list(operator_list)
    for user in users_list:
        action = random.randint(1, 3)
        for act in range(ac_val):
            if action == 1:
                user.send_sms(random.choice(users_list), "d")
            elif action == 2:
                user.send_mms(random.choice(users_list), 22)
            elif action == 3:
                user.calling(random.choice(users_list))

    for i in users_list:
        print(i.nr_tel, ":", len(i.historia_sms_przychodzace))



if __name__ == '__main__':
    main()
