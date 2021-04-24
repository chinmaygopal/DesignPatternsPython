class Target:
    # defines the default behaviour available to the client i.e. client interface
    def operation(self) -> str:
        return "default target behaviour"


class Adaptee:
    # contains incompatible code
    def service_operation(self):
        return "dlroW olleH"


class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def operation(self):
        msg = self.adaptee.service_operation()
        msg = msg[::-1]

        return msg

client = Adaptee()
client = Adapter(client)
print(client.operation())