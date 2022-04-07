"""
This codding exercise requires you complete an implementation of tree methods of
 class:

 1. The __init__ method, which should take an argument name. It should
 initialise self.name to be the argument, and self.items to be an empty list.

 2.

 3.
"""


class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def stock_price(self):
        return sum(item["price"] for item in self.items)


book_store = Store("Book store")
book_store.add_item("Once upon a time...", 100)
book_store.add_item("Jane Eyar", 99)
print(book_store.stock_price())
