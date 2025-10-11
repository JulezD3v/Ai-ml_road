#List. Starting off with sorted
nums = [5, 8, 0, 2]
sorted_nums = sorted(nums)     # save to a new variable to use later
print(nums, sorted_nums)  
nums.sort()
print(nums) # sorts it directly

langs =["Python", "JAVA","Dart", "Flutter"]

for myLang in langs:
    print(myLang)

for codes in langs:
    print(f"I can code with: {codes}")

height = 5

for i in range(1, height):
    spaces = " " * (height - i)
    xs = "x" * (2*i -1)

    print(spaces + xs)

#Write a Python program that prints an inverted pyramid of x’s based on user input. If the user enters 4, the output should be
 
for n in range(height, 0, -1):
    spaces = " "*(height - n)
    ns = "x" * (2* n - 1)
    print(spaces + ns)

names = ["Jane", "Robert" ," ", "June"]

print("\n Names:")
for name in names:
    if name.isalpha():
        print(name, end= " ")
        
print("\n \nItems: ")

items = ['a', '7', 'b', '4', 'x', '#', '9', 'Z']
for item in items:
    if item.isdigit():
        print(item, end=" ")

# Convert Celsius: Given a list of temperatures that are in Celsius, write 
# a loop that iterates over the list and outputs the temperature converted 
# into Fahrenheit. Hint: The conversion is “F = (9/5) ∗ C + 32”

temps = [32, 12, 44, 29]
#Output would be [89.6, 53.6, 111.2, 84.2]

print("\n \n Temp in Fehrenheit: ")
for temp in temps:
    fehrn = (temp * 9/5) + 32
    print(fehrn, end= " ")
