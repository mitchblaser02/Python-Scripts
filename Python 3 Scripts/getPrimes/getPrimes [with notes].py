#PYTHON PRIME NUMBER GENERATOR
#MITCH BLASER 2018
p = int(input("Enter number to get primes from 1 to: ")) #Get the range to look for primes in and assign it to variable p.
currentCheck = 0 #Ensure currentCheck has a value in it at start of program.
for i in range(1,p): #Loop for the range of prime numbers defined by the user.
    currentCheck = currentCheck + 1 #Increment currentCheck by 1 each pass.
    divCount = 0 #Reset divCount each pass.
    for i in range(1,p+1): #Loop for the value of "p"(highest number in user-defined range)
        divResult = currentCheck / i #Divide the current number we are checking by the current pass of the above loop.
        if divResult.is_integer() == True: #If the result from the line above is an integer we increment divCount.
            divCount = divCount + 1 #This holds the value of how many clean divisions we get.
    if divCount == 2: #If there are only two clean divisors of the number:
        print("NUMBER " + str(currentCheck) + " is a prime number.") #We tell the user that the current number is a prime number.
