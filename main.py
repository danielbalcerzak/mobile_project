import client
import mobile_operator
import depot

def main():
    plus = mobile_operator.MobileOperator("plus")
    play = mobile_operator.MobileOperator("play")

    daniel = client.Client("231231", plus, 12, 14)
    michal = client.Client("34324", plus, 12, 14)
    adam = client.Client("34324", play, 12, 14)
    daniel.send_sms(adam, "bkajs")
    print("#"*20)
    plus.get_info()
    print("#" * 20)
    play.get_info()

if __name__ == '__main__':
    main()