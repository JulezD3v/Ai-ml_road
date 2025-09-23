#Loops vs Recursion
# 1. To show the difference between loops and recursion, we will implement solutions to find Fibonacci numbers in three different ways:
# 2. An implementation of the Fibonacci algorithm above using a for loop.
# 3. An implementation of the Fibonacci algorithm above using recursion.
# 4. Finding the nth Fibonacci number using recursion.

#Using For loop

prev1 = 0
prev2 = 1

print(prev1)
print(prev2)

for fibo in range(18):
    newFibo = prev2 +prev1
    print(newFibo)
    prev1 = prev2
    prev2 = newFibo

#Using Recursion
print(0)
print(1)

count = 2

def fibonacci(prevNum1, prevNum2):
    global count

    if count <= 19:# global variables can exist outside the function, be careful with them still
     newFibonacci = prevNum1 + prevNum2
     print(newFibonacci)

     prevNum1 = prevNum2
     prevNum2 = newFibonacci

     count += 1
     fibonacci(prevNum1,prevNum2)
    else:
       return
    

fibonacci(0,1)

# Finding the nth
# F(n) = f(n-1) + f(n-2)

def f(n):
   if n<= 1:
      return n
   
   else:
      return f(n-1) + f(n-2)
   

print(f(6))


 
 


