#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        """
        Initialize a new CashRegister instance.
        
        Args:
            discount: Integer representing percentage discount (0-100).
                     Defaults to 0 if not provided.
        """
        self.discount = discount  # This will trigger the setter
        self.total = 0
        self.items = []
        self.previous_transactions = []
    
    @property
    def discount(self):
        """
        Getter for discount attribute.
        Returns the private _discount value.
        """
        return self._discount
    
    @discount.setter
    def discount(self, value):
        """
        Setter for discount with validation.
        Ensures discount is an integer between 0-100 inclusive.
        Sets to 0 if validation fails.
        
        Args:
            value: The value to set as discount
        """
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0
    
    def add_item(self, item, price, quantity=1):
        """
        Adds an item to the cash register.
    
        Args:
            item: String name of the item
            price: Float price per individual item
            quantity: Integer number of items being purchased (defaults to 1)
    
        Updates:
            - Increases total by price * quantity
            - Adds item name to items array quantity times
            - Tracks transaction amount in previous_transactions
        """
        transaction_amount = price * quantity
        self.total += transaction_amount
    
        for _ in range(quantity):
          self.items.append(item)
    
        self.previous_transactions.append(transaction_amount)
    
    def apply_discount(self):
        """
        Applies the discount percentage to the current total.
        Permanently reduces the total by the discount percentage.
        
        Prints:
            - Message if no discount is available
            - Or confirms discount was applied
        """
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount

            if self.total == int(self.total):
              print(f"After the discount, the total comes to ${int(self.total)}.")
            else:
              print(f"After the discount, the total comes to ${self.total:.2f}.")

    
    def void_last_transaction(self):
        """
        Voids the last transaction by:
        - Removing the last transaction from previous_transactions
        - Subtracting that amount from the total
        - Removing the last item from the items array
        
        Prints error message if no transactions exist.
        """
        if len(self.previous_transactions) == 0:
            print("There are no transactions to void.")
        else:
            last_transaction = self.previous_transactions.pop()
            self.total -= last_transaction
            self.items.pop()