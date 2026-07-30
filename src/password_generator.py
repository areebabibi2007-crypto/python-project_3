import string
import random

class PasswordGenerator:
    def __init__(self):
        # Yahan characters define hone chahiye:
        self.characters = string.ascii_letters + string.digits + string.punctuation

    def generate(self, length):
        password = "".join(random.choice(self.characters) for _ in range(length))
        return password