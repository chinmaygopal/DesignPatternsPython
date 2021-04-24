import abc


class Notify:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def notify(self):
        pass


class NotifyByEmail(Notify):  # concrete component
    def notify(self):
        return "Notified via E-Mail"


class NotificationDecorator(Notify):
    def __init__(self, component):  # the compositions to maintain the hierarchy of component objs
        self._component = component

    @property
    def component(self):
        return self._component

    def notify(self):
        self._component.notify()


class NotifyByTelegram(NotificationDecorator):
    def notify(self):
        print(self.component.notify())  # access the 'wrapped' object
        return ("Notified ny Telegram")


class NotifyBySkype(NotificationDecorator):
    def notify(self):
        print(self.component.notify())
        return ("Notified by Skype")


def client_exec(component):
    print(f"FINALLY: {component.notify()}")


if __name__ == "__main__":
    simple = NotifyByEmail()
    client_exec(simple)

    print("\n Execution with Decorator")
    complex = NotifyByTelegram(simple)
    complex = NotifyBySkype(complex)
    client_exec(complex)
