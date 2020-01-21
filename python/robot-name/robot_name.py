import secrets
import string

class Robot:
    def __init__(self):
        self.name = self.randomName();

    def reset(self):
        self.name = self.randomName();

    def randomName(self):
        letters = ''.join(secrets.choice(string.ascii_uppercase) for i in range(2));
        digits =  ''.join(secrets.choice(string.digits) for i in range(3));
        return letters+digits;