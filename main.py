from depot import making_operator_list, making_users_list, start_send_and_call, start_operators_action


def main():
    operator_list = making_operator_list()
    users_list = making_users_list(operator_list)
    start_send_and_call(users_list)
    start_operators_action(operator_list)

    users_list[0].get_info()


if __name__ == '__main__':
    main()
