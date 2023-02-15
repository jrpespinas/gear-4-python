"""
Develop a Sales application using the SOLID principles.

[x] S - Single Responsibility Principle
[ ] O - Open/Closed Principle
[ ] L - Liskov Substitution Principle
[ ] I - Interface Segragation Principle
[ ] D - Dependency Inversion Principle 

Single Responsibility Principle suggest that every class, module, or function should have one purpose.

"Evey class should have only one reason to change."

Changes:
1. Remove the pay() method from the Order class 
2. Implement PaymentProcessor class to separate the functionality from the Order class
3. Define individual payment methods for both debit and credit payment

"""


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


class PaymentProcessor:
    def pay_debit(self, order: Order, security_code):
        print("Processing debit payment type")
        print(f"Verifiying security code: {security_code}")
        order.set_status("paid")

    def pay_credit(self, order: Order, security_code):
        print("Processing credit payment type")
        print(f"Verifiying security code: {security_code}")
        order.set_status("paid")


def main() -> None:
    order = Order()
    payment = PaymentProcessor()

    order.add_item("Macbook Pro 14 M2", 1, 2733)
    order.add_item("iPhone 14 pro", 1, 1556)
    order.add_item("Airpods Pro Gen 2", 1, 271)

    payment.pay_debit(order, "7809221")


if __name__ == "__main__":
    main()
