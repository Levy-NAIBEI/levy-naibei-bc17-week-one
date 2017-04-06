def prime_Numbers(upperNum):
    #function to display prime numbers within an interval(0 to n)
    #prime numbers are divisible by 1 and itself and greater than 1 

    if(not isinstance(upperNum,int)):
        print("Only numbers")
        return
    elif(upperNum < 0):
        print("Invalid input")
        return
    else:
        for num in range(upperNum+1):
    
            if num >1:
                is_prime=1
                
                for k in range(2,num):
                    if(num%k==0):
                        is_prime=0
                        break    
                   
                if(is_prime):
                     print(num)     
                    
prime_Numbers(20)
                    
        
