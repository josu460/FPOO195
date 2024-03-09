import string
import random
class PasswordGenerator:
    def __init__(self, length=8, use_uppercase=True, use_special_chars=True):
        self.length = length
        self.use_uppercase = use_uppercase
        self.use_special_chars = use_special_chars

    def generate(self):
        chars = string.ascii_lowercase
        if self.use_uppercase:
            chars += string.ascii_uppercase
        if self.use_special_chars:
            chars += string.punctuation
        return ''.join(random.choice(chars) for _ in range(self.length))

