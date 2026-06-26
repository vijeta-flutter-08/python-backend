class Message:

    def __init__(self, sender, text):
        self.sender = sender
        self.text = text

    def display(self):
        print(f"{self.sender}: {self.text}")