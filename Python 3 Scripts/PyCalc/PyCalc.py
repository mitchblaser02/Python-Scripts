print(''' 
 _______              ______             __           
/       \            /      \           /  |          
$$$$$$$  | __    __ /$$$$$$  |  ______  $$ |  _______ 
$$ |__$$ |/  |  /  |$$ |  $$/  /      \ $$ | /       |
$$    $$/ $$ |  $$ |$$ |       $$$$$$  |$$ |/$$$$$$$/ 
$$$$$$$/  $$ |  $$ |$$ |   __  /    $$ |$$ |$$ |      
$$ |      $$ \__$$ |$$ \__/  |/$$$$$$$ |$$ |$$ \_____ 
$$ |      $$    $$ |$$    $$/ $$    $$ |$$ |$$       |
$$/        $$$$$$$ | $$$$$$/   $$$$$$$/ $$/  $$$$$$$/ 
          /  \__$$ |                                  
          $$    $$/     The Python Calculator.                              
           $$$$$$/
           
           ''') ##Print a nice multi-line title.
while True: #Loop everything after this code forever.
    a = float(input("Enter your first numeral: ")) #Get the first number from the user.
    o = input("Enter an operator (*, -, +, /): ") #Get the operator from the user.
    b = float(input("Enter your second numeral: "))#Get the second number from the user.

    if o == "*": print(a*b) #Check what operation the user has chosen and write out the answer.
    elif o == "-": print(a-b) #Check what operation the user has chosen and write out the answer.
    elif o == "+": print(a+b) #Check what operation the user has chosen and write out the answer.
    elif o == "/": print(a/b) #Check what operation the user has chosen and write out the answer.
    else: print("invalid operator") #Check what operation the user has chosen and write out the answer.
