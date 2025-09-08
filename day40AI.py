for num in range(2,10,2):#multiples of 2
    print(f"Value: {num}")

name = "Snow White"
for letter in name:
    print(f"Spell it out: {letter}")

for numb in range(5):
    if numb == 3:
        break
    print(numb)

# #1. Divisible by Three: Write a for loop that prints out all numbers from 1 to 100
# that are divisible by three.
# 2. Only Vowels: Ask for user input, 

for div in range(1,100,3):
    print(f"The numbers divisible by tree are: {div} ")

vowels =[ "a","e","i","o","u"]
for char in "Hello I'm Joanna Dollsine":
    if char.lower() in vowels:
        print(char)


for i in range(2):
    for j in range(3):

        print(j,i)
   
# 1. Remove Duplicates: Remove all duplicates from the list below. Hint: Use the
# .count( ) method. The output should be [‘Bob’, ‘Kenny’, ‘Amanda’]
# >>> names = ['Bob', 'Kenny', 'Amanda', 'Bob', 'Kenny']

names = ['Bob', 'Kenny', 'Amanda', 'Bob', 'Kenny']

while name in names:
    print(names.count("Bob"))