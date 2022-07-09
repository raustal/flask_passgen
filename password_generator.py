import string
from random import choice


def passgen(length):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    special_char = string.punctuation
    numbers = string.digits
    generated_password = ''
    if 8 >= length >= 32:
        return "Password needs to be between 8 - 32 characters"
    else:
        while len(generated_password) < length:
            for character in choice(
                    lowercase + uppercase + special_char + numbers
            ):
                if len(generated_password) == 0 and character in special_char or character in numbers:
                    pass
                else:
                    generated_password += character
    return generated_password
