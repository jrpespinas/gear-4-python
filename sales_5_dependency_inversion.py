"""
Develop a Sales application using the SOLID principles.

[x] S - Single Responsibility Principle
[x] O - Open/Closed Principle
[x] L - Liskov Substitution Principle
[x] I - Interface Segragation Principle
[x] D - Dependency Inversion Principle

Dependency Inversion suggests that you need to make classes depend
on abstract classes rather than non-abstract classes.

For example, subclasses that use the SMSAuthorizer must not depend
on the concrete class. This ensures that you can swap between different
authorizers without breaking the subclasses.


Changes:
1. Implement an abstract class named Authorizer
2. Extend the Authorizer to the SMSAuthorizer subclass
3. As another example, implement another subclass of the authorizer
    named IsNotARobotAuthorizer
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


class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass


class SMSAuthorizer(Authorizer):
    authorized = False

    def verify_code(self, code):
        print(f"Verifying SMS code: {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class IsNotARobotAuthorizer(Authorizer):
    authorized = False

    def verify_is_not_a_robot(self, tiles):
        print(f"Verifying tiles chosen: {tiles}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: Order):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code, authorizer: Authorizer):
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
    def __init__(self, security_code, authorizer: Authorizer):
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
    def __init__(self, email, authorizer: Authorizer):
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
    is_not_a_robot_authorizer = IsNotARobotAuthorizer()
    # sms_authorizer = SMSAuthorizer()
    payment = PayPalPaymentProcessor(
        email="hello@gmail.com",
        authorizer=is_not_a_robot_authorizer
    )

    order.add_item("Macbook Pro 14 M2", 1, 2733)
    order.add_item("iPhone 14 pro", 1, 1556)
    order.add_item("Airpods Pro Gen 2", 1, 271)

    # authorizer.verify_code("872348")
    is_not_a_robot_authorizer.verify_is_not_a_robot([2, 5, 6, 9])
    payment.pay(order)


if __name__ == "__main__":
    main()
