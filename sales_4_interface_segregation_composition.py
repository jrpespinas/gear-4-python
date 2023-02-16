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
1. Using composition (more preferrable than inheritance since inheritance
    couples the functionality which results a large inheritance tree),
    create another class named SMSAuthorizer.
2. Implement verify_code() and is_verified() inside SMSAuthorizer
3. Subclasses of PaymentProcessor using the SMS auth functionality
    must now inject the authorizer in their constructors.
4. Remove the `verified` variable inside the constructors since SMSAuthorizer
    is responsible for storing the variable.
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


class SMSAuthorizer:
    authorized = False

    def verify_code(self, code):
        print(f"Verifying SMS code: {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: Order):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code, authorizer: SMSAuthorizer):
        self.authorizer = authorizer
        self.security_code = security_code

    def pay(self, order: Order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
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


class ApplePayPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code, authorizer: SMSAuthorizer):
        self.authorizer = authorizer
        self.security_code = security_code

    def pay(self, order: Order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")

        print("Processing Apple Pay payment type")
        print(f"Verifiying security code: {self.security_code}")
        order.set_status("paid")
        print(f"Paid: ${order.total_price()}")


class PayPalPaymentProcessor(PaymentProcessor):
    def __init__(self, email, authorizer: SMSAuthorizer):
        self.authorizer = authorizer
        self.email = email

    def pay(self, order: Order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing PayPal payment type")
        print(f"Verifiying email: {self.email}")
        order.set_status("paid")
        print(f"Paid: ${order.total_price()}")


def main() -> None:
    order = Order()
    authorizer = SMSAuthorizer()
    payment = PayPalPaymentProcessor("hello@gmail.com", authorizer)

    order.add_item("Macbook Pro 14 M2", 1, 2733)
    order.add_item("iPhone 14 pro", 1, 1556)
    order.add_item("Airpods Pro Gen 2", 1, 271)

    authorizer.verify_code("872348")
    payment.pay(order)


if __name__ == "__main__":
    main()
