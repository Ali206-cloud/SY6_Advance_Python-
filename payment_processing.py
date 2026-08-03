from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    
# Payment Methods
class CreditCard(PaymentStrategy):
    def pay(self, amount):
        print(f"₹{amount:.2f} paid using Credit Card.")

class PayPal(PaymentStrategy):
    def pay(self, amount):
        print(f"₹{amount:.2f} paid using PayPal.")

class UPI(PaymentStrategy):
    def pay(self, amount):
        print(f"₹{amount:.2f} paid using UPI.")

class NetBanking(PaymentStrategy):
    def pay(self, amount):
        print(f"₹{amount:.2f} paid using Net Banking.")

class Crypto(PaymentStrategy):
    def pay(self, amount):
        print(f"₹{amount:.2f} paid using Cryptocurrency.")

# Context
class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def process(self, amount):
        self.strategy.pay(amount)

# Factory
def get_strategy(choice):
    return {
        1: CreditCard(),
        2: PayPal(),
        3: UPI(),
        4: NetBanking(),
        5: Crypto()
    }.get(choice)

# Main
def main():
    balance = 10000  # Initial Balance

    while True:
        print("=== PAYMENT SYSTEM ===")
        print("1. Credit Card")
        print("2. PayPal")
        print("3. UPI")
        print("4. Net Banking")
        print("5. Cryptocurrency")
        print("6. Check Balance")
        print("7. Exit")

        choice = int(input("Enter choice: "))

        if choice == 7:
            print("Thank you!")
            break

        if choice == 6:
            print(f"Current Balance: ₹{balance:.2f}")
            continue

        strategy = get_strategy(choice)
        if not strategy:
            print("Invalid choice!")
            continue

        amount = float(input("Enter amount: ₹"))

        if amount <= 0:
            print("Invalid amount!")
        elif amount > balance:
            print("Insufficient Balance!")
        else:
            PaymentProcessor(strategy).process(amount)
            balance -= amount
            print(f"Payment Successful! Remaining Balance: ₹{balance:.2f}")

if __name__ == "__main__":
    main()