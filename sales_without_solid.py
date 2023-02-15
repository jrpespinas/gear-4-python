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

    def pay(self, payment_type, security_code):
        if payment_type == "debit":
            print("Processing debit payment type")
            print(f"Verifiying security code: {security_code}")
            self.status = "paid"
        elif payment_type == "credit":
            print("Processing credit payment type")
            print(f"Verifiying security code: {security_code}")
            self.status = "paid"
        else:
            raise Exception(f"Unknown payment type: {payment_type}")

def main() -> None:
    order = Order()
    order.add_item("Macbook Pro 14 M2", 1, 2733)
    order.add_item("iPhone 14 pro", 1, 1556)
    order.add_item("Airpods Pro Gen 2", 1, 271)

    print(order.total_price())
    order.pay("debit", "7809221")


if __name__ == "__main__":
    main()

