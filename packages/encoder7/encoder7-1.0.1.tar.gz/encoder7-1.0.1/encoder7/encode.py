"""This module provides a function for encoding a message."""

def shift(message, shift_amount):
    """Encodes a message by shifting each letter in the message by the shift_amount."""
    encoded_message = ""
    for letter in message:
        encoded_message += chr(ord(letter) + shift_amount)
    return encoded_message