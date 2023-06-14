#Project: Password Generator v1.0
#Autor: Kimie
#Version: 1.0

import random

#Strings Alphabet, Number and Symbols
alphabet = 'abcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'
symbols = '!@#$%&*+-_|\?/()'

#Welcome message to the user
print('*********************************************')
print('******Welcome to the Password Generator******')
print('*********************************************')

#Lenght of the password
print('\nQual a quantidade de caracteres?')
lenght = int(input().upper().strip())

#Leters
print('\nDeseja incluir letras maiúsculas? [Sim] [Não] [Nenhum]')
letter = input().upper().strip()

#Numbers
print('\nDeseja incluir números? [Sim] [Não]')
number = input().upper().strip()

#Symbols
print('\nDeseja incluir símbolos? [Sim] [Não]')
symbol = input().upper().strip()

#String of Output
password = ''

#String of random options
options = ''

#Decision estructure of options


if(letter == "SIM"):
    options = options + alphabet.upper()

if(letter == "NÃO"):
    options = options + alphabet

if(number == 'SIM'):
    options = options + numbers

if(symbol == 'SIM'):
    options = options + symbols

#Looping
while len(password) < lenght:

    password = password + random.choice(options)

print("A sua senha é: ", password)
input()