class Account:
    def __init__(self, username):
        self.username = username
        self.__account_number = 'PL11 3333 4444 1111 2222'

    def show_num(self):
        print('Bank number', self.__account_number)

    def set_number(self, number):
        self.__account_number = number


user = Account('mrlyc2323')
user.show_num()
user.set_number('GB45 111111')
user.show_num()