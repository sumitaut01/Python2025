#Declaring Protected and Private Methods
# In Python, you can control method access levels using naming conventions:
#
# Use a single underscore (_) before a method name to indicate it is protected meant to be used within class or its subclasses.
# Use a double underscore (__) to define a private method accessible only within class due to name mangling.
# Note: Unlike other programming languages, Python does not enforce access modifiers like public, private or protected at the language level. However, it follows naming conventions and uses a technique called name mangling to support encapsulation.
#
# Example: This example demonstrates how a protected method (_show_balance) and a private method (__update_balance) are used to control access. The private method updates balance internally, while protected method displays it. Both are accessed via a public method (deposit), showing how Python uses naming conventions for encapsulation.

class BankAccount:
    def __init__(self):
        self.balance = 1000

    def _show_balance(self):
        print(f"Balance: ₹{self.balance}")  # Protected method

    def __update_balance(self, amount):
        self.balance += amount  # Private method

    def deposit(self, amount):
        if amount > 0:
            self.__update_balance(amount)  # Accessing private method internally
            self._show_balance()  # Accessing protected method
        else:
            print("Invalid deposit amount!")


account = BankAccount()
account._show_balance()  # Works, but should be treated as internal
# account.__update_balance(500)  # Error: private method
account.deposit(500)  # Uses both methods internally