#PYTHON MORSE CODE ENCODER
#MITCH BLASER 2018


#Make the dictionary for english -> morse code conversion.
morseCode = {" ": " / ", "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----", "'": "'", ".": ".", ",": ","}

outputString = "" #Set outputString to blank string so it doesn't error out for the first passthrough.

print("Python Morse Code Encoder") #Print title/menus.
print("==============================================")
print("")
inputString = input("Input string to encode: ") #Ask user for input .
inputString = inputString.lower() #Turn all capitals to lowercase letters.
for i in range (0,len(inputString)): #Loop for the amount of characters in the string supplied from the user.
    currentMorseOutput = morseCode[inputString[i]] #Look up the morse code value of each character of inputString. Gets a new character every pass of the function.
    outputString = outputString + " " + morseCode[inputString[i]] #Adds the looked up morse code value to master ouutput string.
print("OUTPUT:" + outputString) #Prints the master output string after all passes are complete.
