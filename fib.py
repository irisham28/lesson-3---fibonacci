def fibonacci(n):
    if n<=1:
        return n 
    else:
        #recursive :sum of 2 previous numbers 
        return fibonacci(n-1)+ fibonacci(n-2)

n=10
print(f"The first {n} terms of fibonacci series are : ")
for i in range(n):
    print(fibonacci(i), end= " ")

#best case: if n is 1 or 0 
#recursive/worst case if n>1 

#time complexity: O(2^n) worst case
#space complexity: O(n) - best case 

# for the factorials--> time and space complexiy :O(n)--> linear 

