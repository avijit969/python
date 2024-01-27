import random
import string
# for alphabet list
alphabet = []
for letter in range(ord('a'), ord('z') + 1):
    alphabet.append(chr(letter))

for letter in range(ord('A'), ord('Z') + 1):
    alphabet.append(chr(letter))

# for numbers list
numbers = []
for num in range(0, 10):
    numbers.append(num)

# for punctuation list
punctuation_symbols = list(string.punctuation)
# print(punctuation_symbols)

# creating password list
password_list = []
# asking user for how many letters , alphabet and symbols they are want in their password ?
N_alphabet = int(input("how many alphabet you want in your password:"))
N_numbers = int(input("how many numbers you want in your password:"))
N_symbols = int(input("how many symbols you want in your password:"))

# creating alphabet password list
for i in range(0, N_alphabet):
    char = random.choice(alphabet)
    password_list += char
# creating numbers password list
for i in range(0, N_numbers):
    digit = random.choice(numbers)
    password_list += str(digit)
# creating symbols password list
for i in range(0, N_symbols):
    sym = random.choice(punctuation_symbols)
    password_list += str(sym)
# shuffling the password list
random.shuffle(password_list)
# convert shuffled password list into string
password = ""
for char in password_list:
    password += char
# finally print the password
print(f"your password is:{password}")
