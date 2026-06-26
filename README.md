# Chat Domain Models - Day 2

## Topics Covered

- Object-Oriented Programming (OOP)
- Classes
- Objects
- Constructors
- Methods
- Inheritance

## Project Structure

```
chat-domain-models/
│
├── user.py
├── message.py
├── conversation.py
├── main.py
└── README.md
```

## Description

This project demonstrates the fundamentals of Object-Oriented Programming in Python by implementing a simple chat system.

### User

Represents a chat user with basic information such as:

- User ID
- Name
- Email

### Message

Represents a message sent between users.
Each message contains:

- Sender
- Receiver
- Message Text

### Conversation

Manages all messages in a conversation.
Features:

- Store messages
- Send messages
- Display conversation history

### Inheritance

Demonstrates inheritance by creating an `Admin` class that extends the `User` class and includes additional functionality such as blocking a user.

## Learning Outcomes

- Create and use Python classes
- Work with constructors (`__init__`)
- Define and call class methods
- Create objects
- Understand object relationships
- Implement inheritance
- Organize code into multiple Python files

## Author

**Vijeta Chaudhary**

## Commit Message

```
feat: chat domain models
```
