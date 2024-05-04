# python algorithm

# is the number prime


def isPrime():
    status = True
    print("Enter a number to see if it is prime: ")
    number = int(input())
    # print(type(number))
    
    for i in range( 2, int(number /2) ):
        if(number % i == 0):
            status = False
            break
            
    if(status):
        message = str(number) + " is prime"
    else:
        message = str(number) + " is not prime"
        
    return message

def repeat():
    print(isPrime())
    print("")
    
    print("Would you like to test another number? (Y/N)")
    yesNo = input().upper()
    if(yesNo == "Y"):
        print("")
        repeat()
    else:
        print("")
        print("Goodbye")

repeat()
