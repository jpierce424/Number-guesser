import math 

def isPrime (num):
   num = abs (num) 
   if (num <= 1):
       print ("The number" , num , "is neither a prime number nor a composite number.\n")
       return False 
   for i in range (2, 2 + int(math.sqrt(num))):
       if (num % i) == 0:
           print ("The number",num,"is not a prime number...")
           print ("because",num,"divided by", i,"is" , num//i , "\n")
           return False 
   print("The number",num,"is a prime number.\n")
   return True 


def mains ():
    try:
        num = int(input('Enter an integer: '))
        isPrime (num)
        return "isPrime called!"
    except ValueError:
        print("Invalid input, Please enter a INTEGER only. QUITTING \n")
        return "ERROR"



if (__name__ == '__main__'):
    mains ()
