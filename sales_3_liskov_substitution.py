"""
Develop a Sales application using the SOLID principles.

[x] S - Single Responsibility Principle
[x] O - Open/Closed Principle
[x] L - Liskov Substitution Principle
[ ] I - Interface Segragation Principle
[ ] D - Dependency Inversion Principle

Liskov Substitution suggests when a class inherits from another class,
the program shouldn't break and you shouldn't need to hack
anything to use the subclass.

For example, if we have a new payment function named PayPal that uses
email instead of security code, a violation of this principle occurs
when you abuse the `security_code` variable to perform
a different functionality.

Changes:
1. Remove the security_code variable from the abstract method
2. Place the security_code in the constructor of their respective subclasses
3. Place the email in the constructor of the Paypal payment subclass
"""
from abc import ABC, abstractmethod


class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def set_status(self, status):
        self.status = status


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: Order):
        pass

    @abstractmethod
    def auth_sms(self, code):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False

    def auth_sms(self, code):
        print(f"Verifying SMS code: {code}")
        self.verified = True

    def pay(self, order: Order):
        print("Processing debit payment type")
        print(f"Verifiying security code: {self.security_code}")
        order.set_status("paid")
        print(f"Paid: ${order.total_price()}")


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False

    def auth_sms(self, code):
        print(f"Verifying SMS code: {code}")
        self.verified = True

    def pay(self, order: Order):
        print("Processing credit payment type")
        print(f"Verifiying security code: {self.security_code}")
        order.set_status("paid")
        print(f"Paid: ${order.total_price()}")


class ApplePayPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False

    def auth_sms(self, code):
        print(f"Verifying SMS code: {code}")
        self.verified = True

    def pay(self, order: Order):
        print("Processing Apple Pay payment type")
        print(f"Verifiying security code: {self.security_code}")
        order.set_status("paid")
        print(f"Paid: ${order.total_price()}")


class PayPalPaymentProcessor(PaymentProcessor):
    def __init__(self, email):
        self.email = email
        self.verified = False

    def auth_sms(self, code):
        print(f"Verifying SMS code: {code}")
        self.verified = True

    def pay(self, order: Order):
        print("Processing PayPal payment type")
        print(f"Verifiying email: {self.email}")
        order.set_status("paid")
        print(f"Paid: ${order.total_price()}")


def main() -> None:
    order = Order()
    payment = PayPalPaymentProcessor("hello@gmail.com")

    order.add_item("Macbook Pro 14 M2", 1, 2733)
    order.add_item("iPhone 14 pro", 1, 1556)
    order.add_item("Airpods Pro Gen 2", 1, 271)

    payment.auth_sms("872348")
    payment.pay(order)


if __name__ == "__main__":
    main()
