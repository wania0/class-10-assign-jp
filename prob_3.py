# Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.

# Solution :

class ShoppingCart:

    def __init__(self) :
        # instance attributes
        self.items = {}
        self.total_price = 0
    
    #instance methods
    def add_item(self, name, price):
        self.items[name] = price
        self.total_price = self.total_price + price
        print("Added", name, "for Rs.", price)

    def remove_item(self, name):
        if name in self.items:
            price = self.items.pop(name)
            self.total_price = self.total_price - price
            print(name, "is removed from the shopping cart.")
        else:
            print("Item not found")
    
    def total(self):
        print("Total price is: Rs.", self.total_price)
        
    def display_cart(self):
        print("Shopping Cart Items:")
        for name, price in self.items.items():
            print(name,"price is---> Rs.", price)

# instance 
cart = ShoppingCart()

# Add items 
cart.add_item("Ice cream", 200)
cart.add_item("Cherries", 300)
cart.add_item("Dates", 100)

# Display cart items and total price
cart.display_cart()
cart.total()

# Remove an item 
cart.remove_item("Banana")
cart.total()

cart.display_cart()
total = cart.total()


