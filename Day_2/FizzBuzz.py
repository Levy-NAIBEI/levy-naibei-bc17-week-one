def solution(N):
    
    for i in range (1,N+1):
        if i % 3 == 0 and i % 5 == 0:
            print ("FizzBuzz")
        elif i % 3 == 0:
            print("FizzB")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print (i)
