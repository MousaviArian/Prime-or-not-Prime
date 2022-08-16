def Prime_Or_NotPrime ():
   while True :
        Nomber = int(input ("Entre Nomber "))
        for i in range (1,Nomber):
            Value_of_prime = 1
            if Nomber % i == 0:
                Value_of_prime = 0
            break
        if Value_of_prime == 0:
            print("NotPrime")
        else :
            print("Prime")

Prime_Or_NotPrime ()
