CHANNELS = ["BBC", "Discovery", "TV1000"]


def check(func):
    def wrap(*args):
        self = args[0]
        if not self.channels:
            print('Channels list is empty!')
            return None

        return func(*args)

    return wrap


class TVController:
    cur_channel = 1

    def __init__(self, channels):
        self.channels = channels

    @check
    def first_channel(self):
        return self.channels[0]

    @check
    def last_channel(self):
        return self.channels[len(self.channels) - 1]

    @check
    def turn_channel(self, n):
        return self.channels[n-1]

    @check
    def next_channel(self):
        self.cur_channel += 1
        if self.cur_channel > len(self.channels):
            self.cur_channel = 1

        return self.channels[self.cur_channel-1]

    @check
    def previous_channel(self):
        self.cur_channel -= 1
        if self.cur_channel < 1:
            self.cur_channel = len(self.channels)

        return self.channels[self.cur_channel - 1]

    @check
    def current_channel(self):
        return self.channels[self.cur_channel-1]

    @check
    def is_exist(self, channel):
        if type(channel) == int and 1 <= channel <= len(self.channels):
            return "Yes"

        if type(channel) == str and channel in self.channels:
            return "Yes"

        return "No"


controller = TVController(CHANNELS)

print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist(4))
print(controller.is_exist("BBC"))
