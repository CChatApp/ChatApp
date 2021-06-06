from string import ascii_letters
from random import choices


salt = "".join(choices(ascii_letters, k=35))
address = "0.0.0.0"
port = 9898
layer = 1
