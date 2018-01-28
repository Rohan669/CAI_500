

""" Sieve of Erosthenes"""
from math import sqrt
n=input("enter the number upto which you want to find the primes\n")
n=int(n)
a=[i for i in range(2,n+1)]
prime_list=[]
non_prime_list=[]

"""Implementation of algorithm"""
a_logic=[[i,True] for i in a]
a_logic=dict(a_logic)
i=0

for i in range(2,int(sqrt(n)+1)):
    if a_logic[i]==True:
        j=0
        while i**2+j*i<=n:
            a_logic[i**2+j*i]=False
            j+=1
            
""" finding the prime number positions for false"""            
for i in a:
    if a_logic[i]==True:
        prime_list.append(i)
        print(i)
    else:
        non_prime_list.append(i)
        
        

        
    
    

    

