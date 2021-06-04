import mobile_operator
import client
import random

num_of_users = 10
min_item = 10
max_item = 200
first_num = 100000000
last_num = 999999999
operator_dict = {"era": "+10",
                 "idea": "+11",
                 "plus": "+12",
                 "play": "+13",
                 "redbull": "+14"}
users = []


def making_operator_list():
    return [mobile_operator.MobileOperator(operator) for operator in operator_dict]


def making_users_list(oper):
    cell_nums = []
    while len(set(cell_nums)) != num_of_users:
        num = random.randint(first_num, last_num)
        cell_nums.append(num)
    for num in cell_nums:
        oper_rand = random.choice(oper)
        cl = client.Client(num, oper_rand, random.randint(min_item, max_item), random.randint(min_item, max_item))
        users.append(cl)
    userlist = users.copy()
    return userlist
