def primeFactorization(lower, higher):
    # Declaring
    primeSmall = []
    primeBig = []
    gcd = 1
    
    # Breaking the numbers into prime numbers
    prime = 2
    
    while lower > 1:
        
        if (lower % prime == 0):
            primeSmall.append(prime)
            lower = lower / prime
        else:
            prime = prime + 1
    
    prime = 2
    
    while higher > 1:
        
        if (higher % prime == 0):
            primeBig.append(prime)
            higher = higher / prime
        else:
            prime = prime + 1
    
    # Finding common prime factors    
    common = []
    
    for i in primeSmall:
        if i in primeBig:
            common.append(i)
            primeBig.remove(i)
    
    # Multiplying the common numbers
    for i in common:
        gcd = i * gcd
    
    return gcd

print(primeFactorization(36, 66))



def breakingIntoPrimenumbers(lower):
    
    primeSmall = []
    
    prime = 2
    
    while lower > 1:
        
        if (lower % prime == 0):
            primeSmall.append(prime)
            lower = lower / prime
        else:
            prime = prime + 1
            
    return primeSmall 
    
breakingIntoPrimenumbers(36)


def findCommonValues(myList1, myList2):
   
    global common
    common = []
    for i in myList1:
        if i in myList2:
            common.append(i)
            myList2.remove(i)
    return common
    
myList1 = breakingIntoPrimenumbers(36)
myList2 = breakingIntoPrimenumbers(66)

print(findCommonValues(myList1, myList2))    


def newPrimeFactorization(lower, higher):
    # Declaring
    primeSmall = []
    primeBig = []
    gcd = 1
    
    # Breaking the numbers into prime numbers
    #breakingIntoPrimenumbers(36)
    #breakingIntoPrimenumbers(66)
    
    # implement breakingIntoPrimenumbers()
    # implement breakingIntoPrimenumbers()
    myList1 = breakingIntoPrimenumbers(lower)
    myList2 = breakingIntoPrimenumbers(higher)
    
    # Finding common prime factors    
    findCommonValues(myList1, myList2)
    
    
    # Multiplying the common numbers
    for i in common:
        gcd = i * gcd
    return gcd, common

newPrimeFactorization(36, 66)


def listDividers(num):
    listOfDividers= [1]
    firstDivider= 2
    
    
    while num >= firstDivider:
        
        if (num % firstDivider == 0):
            listOfDividers.append(firstDivider)
            firstDivider = firstDivider + 1

        else:
            firstDivider = firstDivider + 1

    return listOfDividers 
listDividers(6)


def getGcd(number1,number2):
    divider1= listDividers(number1)
    divider2= listDividers(number2)
    common_dividers= findCommonValues(divider1,divider2)
    return common_dividers[-1], common_dividers 
getGcd(4, 6)