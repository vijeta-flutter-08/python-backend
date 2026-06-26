class Conversation:

    def __init__(self):
        self.messages = []

    def send_message(self, message):
        self.messages.append(message)

    def show_messages(self):
        for message in self.messages:
            message.display()