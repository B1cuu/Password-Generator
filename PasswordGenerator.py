import random

lenght = 12
letters = "abcdefghijklmnoprstuwyz"
letters_upper = letters.upper()
numbers ="0123456789"
symbols = "!@#"

all_password = letters + letters_upper + numbers + symbols

password = "".join(random.sample(all_password, lenght))

print(password)