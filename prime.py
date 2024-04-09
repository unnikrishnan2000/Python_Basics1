def Is_prime(x):
    for i in range (2,x):
         if(x==0 or x==1 or x==2):
              return("not_all_prime")
         elif x%i==0:
              return("Not_prime")
         else:
              return("Is_prime")  
n=int(input("enter"))            
a=Is_prime(n)   
print(a)   