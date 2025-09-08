import time

# calculation module logic inside same file for simplicity
def area(length, width):
    return length * width

# simulate "loading" time
print("Calculating area, please wait...")
time.sleep(5)

# user input
length = float(input("Enter length: "))
width = float(input("Enter width: "))

# calculate
result = area(length, width)

print(f"The area of the rectangle is: {result}")
