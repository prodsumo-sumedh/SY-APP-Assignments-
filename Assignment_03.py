from abc import ABC, abstractmethod

# Strategy Interface
class Payment_Strategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
      
# Concrete Strategy 1
class CreditCard_Payment(Payment_Strategy):
    def pay(self, amount):
        print(f"Payment of ${amount} processed using Credit Card.")
      
# Concrete Strategy 2
class DebitCard_Payment(Payment_Strategy):
    def pay(self, amount):
       print(f"Payment of ${amount} processed using Debit Card.")

# Concrete Strategy 3
class Upi_Payment(Payment_Strategy):
    def pay(self, amount):
       print(f"Payment of ${amount} processed using UPI.") 

# Concrete Strategy 4
class NetBanking_Payment(Payment_Strategy):
   def pay(self, amount):
       print(f"Payment of ${amount} processed using Net Banking.")

# Context Class
class PaymentProcessor:
   def __init__(self, strategy=None):
       self.strategy = strategy

   def set_strategy(self, strategy):
       self.strategy = strategy

   def process_payment(self, amount):
       if self.strategy is None:
           print("Please select a payment method.")
       else:
           self.strategy.pay(amount)
         

processor = PaymentProcessor()

while True:
    print("\n===== Payment Processing System =====")
    print("1. Credit Card")
    print("2. Debit Card")
    print("3. UPI")
    print("4. Net Banking")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
  
    if choice == 5:
        print("Thank you for using the Payment System!")
        break
      
    amount = float(input("Enter payment amount: "))

    if choice == 1:
        processor.set_strategy(CreditCard_Payment())
    elif choice == 2:
        processor.set_strategy(DebitCard_Payment())
    elif choice == 3:
        processor.set_strategy(Upi_Payment())
    elif choice == 4:
        processor.set_strategy(NetBanking_Payment())
    else:
        print("Invalid choice!")
        continue


    processor.process_payment(amount)


#Output
'''===== Payment Processing System =====
1. Credit Card
2. Debit Card
3. UPI
4. Net Banking
5. Exit
Enter your choice: 1
Enter payment amount: 545
Payment of $545.0 processed using Credit Card.

===== Payment Processing System =====
1. Credit Card
2. Debit Card
3. UPI
4. Net Banking
5. Exit
Enter your choice: 2
Enter payment amount: 299
Payment of $299.0 processed using Debit Card.

===== Payment Processing System =====
1. Credit Card
2. Debit Card
3. UPI
4. Net Banking
5. Exit
Enter your choice: 3
Enter payment amount: 356
Payment of $356.0 processed using UPI.

===== Payment Processing System =====
1. Credit Card
2. Debit Card
3. UPI
4. Net Banking
5. Exit
Enter your choice: 4
Enter payment amount: 395
Payment of $395.0 processed using Net Banking.

===== Payment Processing System =====
1. Credit Card
2. Debit Card
3. UPI
4. Net Banking
5. Exit
Enter your choice: 5
Thank you for using the Payment System!'''
