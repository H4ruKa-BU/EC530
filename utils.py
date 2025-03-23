def format_message(sender, receiver, content):
    return {
        'sender': sender,
        'receiver': receiver,
        'content': content
    }

# Example usage
if __name__ == '__main__':
    msg = format_message("Alice", "Bob", "Hey Bob!")
    print(msg)
