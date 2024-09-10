import random
import string
CharVal=string.ascii_letters+string.digits+string.punctuation
pass_len=10
password=""
for i in range(pass_len):
    password+=random.choice(CharVal)
print("Your random password is",password)