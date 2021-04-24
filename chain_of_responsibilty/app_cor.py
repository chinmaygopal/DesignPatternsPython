class Event:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Widget:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self,event):
        handler = 'handle_{}'.format(event)
        if hasattr(self,handler):
            method = getattr(self, handler)
            method(event)

        elif self.successor:
            self.successor.handle(event)

        elif hasattr(self,'handle_default'):
            self.handle_default(event)


class MainWindow(Widget):
    def handle_close(self,event):
        print('Main Window : {}'.format(event))

    def handle_default(self,event):
        print('Main Window Default {}:'.format(event))


class SendDialog(Widget):
    def handle_paint(self,event):
        print('SendDialog: {}'.format(event))


class MsgText(Widget):
    def handle_down(self,event):
        print('MsgText : {}'.format(event))


if __name__ == '__main__':
    mw_obj = MainWindow()
    sd_obj = SendDialog(mw_obj)
    msg_obj = MsgText(sd_obj)
    list_events = ["paint","down","unhandled","close"]
    for each_event in list_events:
        each_event = Event(each_event)
        print("Main Window processing event {}".format(each_event))
        mw_obj.handle(each_event)

        print("SendDialog processing event {}".format(each_event))
        sd_obj.handle(each_event)

        print("MsgTxt processing event {}".format(each_event))
        msg_obj.handle(each_event)
