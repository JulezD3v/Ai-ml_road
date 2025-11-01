def countdown (n):
    if n==0:
        print('Done')
    else:
        print(n)
        countdown(n-1)
        
    



# T(n) = T(n - 1) + c  c= time for * and call
#time grows linearly = T(n) = O(n)
#Factorial
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

    
countdown(5)
print(fact(6))

# Binary search cuts the proble in half T(n) = T(n/2) = O(log n)




