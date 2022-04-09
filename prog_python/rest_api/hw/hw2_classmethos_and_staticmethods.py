"""
This codding exercise requires you to complete two method implementations.
1. The franchise method, which takes in a store as argument. It should return
a new Store  object, with a name equals to the argument + "- franchise".
2. The store_details method, which also takes in a store as argument. It should
 return a string representing the argument.

A few examples:
    store = Store("Test")
    store2 = Store("Amazon")
    store2.add_item ("Keyboard", 250)

    Store.franchise(store) # returns a Store with name "Test - franchise"
    Store.franchise(store2) # returns "Amazon - franchise"

    store2.add_item("Keyboard", 250)
"""


class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def stock_price(self):
        return sum(item["price"] for item in self.items)

    @classmethod
    def franchise(cls, store):
        return cls(store.name + " + franchise")

    @staticmethod
    def store_details(store):
        return f"{store.name}, total stock price: {int(store.stock_price())}"

    def __repr__(self):
        return f"{self.name}"


store = Store("Test")
print(Store.franchise(store))

store2 = Store("Amazon")
store2.add_item("Keyboard", 250)

print(Store.store_details(store2))
print(Store.store_details(store))
