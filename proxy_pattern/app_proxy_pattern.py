from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):

    @abstractmethod
    def do_pay(self, amt):
        pass


class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None
        self.balance = 100

    def __get_account(self):
        self.account = self.card  # Assume card number is account number

    def __has_funds(self,amt):
        return_val = True
        if amt <= self.balance:
            print("Bank : User has enough funds")

        else:
            print("Bank: Sorry User has insufficient funds")
            return_val = False

        return return_val

    def set_card(self,card):
        self.card = card

    def do_pay(self, amt):
        do_pay_ok = True
        if self.__has_funds(amt):
            print("Bank: paying the merchant")
        else:
            do_pay_ok = False

        return do_pay_ok


class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()

    def do_pay(self, amt):
        card = input("proxy: please enter your card no.")
        self.bank.set_card(card)
        return self.bank.do_pay(amt)


class User:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} wants to buy shirt")
        self.debit_card = DebitCard()
        self.is_purchased = None

    def make_payment(self,amt):
        self.is_purchased = self.debit_card.do_pay(amt)

    def __del__(self):
        if self.is_purchased:
            print(f"{self.name} buys the shirt")
        else:
            print(f"{self.name} should earn more! :-( ")


if __name__ == "__main__":
    usr_obj = User("Chinmay")
    shirt_price = 23
    usr_obj.make_payment(shirt_price)
