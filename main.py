from user import User, Admin
from message import Message
from conversation import Conversation

user1 = User(1, "Vijeta", "vijeta@gmail.com")
user2 = User(2, "Rahul", "rahul@gmail.com")

admin = Admin(100, "Super Admin", "admin@gmail.com")

conversation = Conversation()

conversation.send_message(
    Message(user1.name, "Hello Rahul!")
)

conversation.send_message(
    Message(user2.name, "Hi Vijeta!")
)

conversation.send_message(
    Message(user1.name, "How are you?")
)

print("----- Conversation -----")
conversation.show_messages()

print("\n----- Admin Actions -----")
admin.display()
admin.block_user(user2)