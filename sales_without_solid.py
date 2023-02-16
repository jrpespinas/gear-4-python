"""
Develop a Sales application using the SOLID principles.

[ ] S - Single Responsibility Principle
[ ] O - Open/Closed Principle
[ ] L - Liskov Substitution Principle
[ ] I - Interface Segragation Principle
[ ] D - Dependency Inversion Principle

This file is the base application.
We will refactor this code to adhere to the SOLID principles
"""


class Order:
    items = []
    quantities = []
    prices = []
    status = "open"
    verified = False

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

    def auth_sms(self, code):
        self.verified = True

    def pay(self, payment_type, security_code):
        if payment_type == "debit":
            print("Processing debit payment type")
            print(f"Verifiying security code: {security_code}")
            self.status = "paid"
            print(f"Paid: ${self.total_price()}")
        elif payment_type == "credit":
            print("Processing credit payment type")
            print(f"Verifiying security code: {security_code}")
            self.status = "paid"
            print(f"Paid: ${self.total_price()}")
        else:
            raise Exception(f"Unknown payment type: {payment_type}")


def main() -> None:
    order = Order()
    order.add_item("Macbook Pro 14 M2", 1, 2733)
    order.add_item("iPhone 14 pro", 1, 1556)
    order.add_item("Airpods Pro Gen 2", 1, 271)

    order.pay("debit", "7809221")


if __name__ == "__main__":
    main()
