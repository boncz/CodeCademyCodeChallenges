#Prime Number Finder
#Create a prime_finder() function that takes in a number, n, and returns all the prime numbers from 1 to n (inclusive). As a reminder, a prime number is a number that is only divisible by 1 and itself.
#For example, prime_finder(11) should return [2, 3, 5, 7, 11].


def PrimeFinder(num):
    primes = [] #Start with an empty list
    for number in range(0,num+1):  #going through each number in the range
        if number >= 1:  #only testing positive integers
            for i in range(2, number):  #testing each number for factors
                if (number % i) == 0:  # this would indicate number is not a prime
                    break  
            else:  
                primes.append(number)  #appends prime list if no factors are found

    print(primes)

#Testing a few out below:

PrimeFinder(12)
PrimeFinder(1)
PrimeFinder(9)