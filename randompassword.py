import random
lowercase_letters="abcdefghijklmnopqrstuvwxyz"
uppercase_letters=lowercase_letters.upper()
numbers=("0123456789")
symbols="(){}[],:;._-/\\?+*#"
lowercase, uppercase, num, symbol= True, True, True, True

all=""
if lowercase:
    all+=lowercase_letters
if uppercase:
    all+=uppercase_letters
if num:
    all+=numbers
if symbol:
    all+=symbols

strength=20
amount=5
for i in range(amount):
    password="".join(random.sample(all,strength))
    print(password)