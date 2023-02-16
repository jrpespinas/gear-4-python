"""
Develop a Sales application using the SOLID principles.

[x] S - Single Responsibility Principle
[x] O - Open/Closed Principle
[x] L - Liskov Substitution Principle
[x] I - Interface Segragation Principle
[ ] D - Dependency Inversion Principle

Interface Segregation Principle suggests to make interfaces
(parent abstract classes) more specific, rather than generic.

For example, if we split the PaymentProcessor into another subclass named
PaymentProcessorWithSMSAuthentication that has an additional functionality of
authenticating transaction via SMS which is absent in CreditPaymentProcessor.

By avoiding the extraction of the SMS functionality in PaymentProcessor,
a violation occurs when we are forced to raise an Exception in one
of the subclasses such as CreditPaymentProcessor since this functionality
does not make sense in the subclass. (also a violation of Liskov Substitution)

Changes:
1. Using inheritance, create another subclass of the PaymentProcessor named
    PaymentProcessorWithSMSAuthentication
2. Inherit the auth_sms() from the PaymentProcessorWithSMSAuthentication in
    sub classes which uses the SMS authentication i.e Debit, Apple Pay, PayPal.
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


class PaymentProcessorWithSMSAuthentication(PaymentProcessor):
    @abstractmethod
    def auth_sms(self, code):
        pass


class DebitPaymentProcessor(PaymentProcessorWithSMSAuthentication):
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

    def pay(self, order: Order):
        print("Processing credit payment type")
        print(f"Verifiying security code: {self.security_code}")
        order.set_status("paid")
        print(f"Paid: ${order.total_price()}")


class ApplePayPaymentProcessor(PaymentProcessorWithSMSAuthentication):
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


class PayPalPaymentProcessor(PaymentProcessorWithSMSAuthentication):
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
