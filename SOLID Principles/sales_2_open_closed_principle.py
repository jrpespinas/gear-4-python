"""
Develop a Sales application using the SOLID principles.

[x] S - Single Responsibility Principle
[x] O - Open/Closed Principle
[ ] L - Liskov Substitution Principle
[ ] I - Interface Segragation Principle
[ ] D - Dependency Inversion Principle

Open/Closed principle suggests that we should write code
that is open for extension (extend the existing code with new functionality),
but closed for modification (as much as possible).

For example, if we have a new payment function named Apple Pay,
we have to modify the PaymentProcessor class which is a violation for the
Open/Closed principle.

Changes:
1. Convert PaymentProcessor into an abstract class
2. Write subclasses and their respective methods
    for the different payment methods
"""
from abc import ABC, abstractmethod


class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

    def set_status(self, status):
        self.status = status


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: Order, security_code):
        pass

    @abstractmethod
    def auth_sms(self, code):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self):
        self.verified = False

    def auth_sms(self, code):
        print(f"Verifying SMS code: {code}")
        self.verified = True

    def pay(self, order: Order, security_code):
        print("Processing debit payment type")
        print(f"Verifiying security code: {security_code}")
        order.set_status("paid")
        print(f"Paid: ${order.total_price()}")


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self):
        self.verified = False

    def auth_sms(self, code):
        raise Exception("Does not implement SMS authentication")

    def pay(self, order: Order, security_code):
        print("Processing credit payment type")
        print(f"Verifiying security code: {security_code}")
        order.set_status("paid")
        print(f"Paid: ${order.total_price()}")


class ApplePayPaymentProcessor(PaymentProcessor):
    def __init__(self):
        self.verified = False

    def auth_sms(self, code):
        print(f"Verifying SMS code: {code}")
        self.verified = True

    def pay(self, order: Order, security_code):
        print("Processing Apple Pay payment type")
        print(f"Verifiying security code: {security_code}")
        order.set_status("paid")
        print(f"Paid: ${order.total_price()}")


def main() -> None:
    order = Order()
    payment = ApplePayPaymentProcessor()

    order.add_item("Macbook Pro 14 M2", 1, 2733)
    order.add_item("iPhone 14 pro", 1, 1556)
    order.add_item("Airpods Pro Gen 2", 1, 271)

    payment.auth_sms("872348")
    payment.pay(order, "7809221")


if __name__ == "__main__":
    main()
