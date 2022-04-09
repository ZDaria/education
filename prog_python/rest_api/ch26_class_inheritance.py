class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconected")


printer = Device("Printer", "USB")
print(printer)
printer.disconnect()


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_page = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_page} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("You printer is not connected!")
        else:
            print(f"Printing {pages} pages.")
            self.remaining_page -= pages


printer = Printer("Xerox", "USB", 500)
printer.print(123)
print(printer)
printer.disconnect()
printer.print(30)
