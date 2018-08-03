morseCode = {" ": " / ", "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----", "'": "'", ".": ".", ",": ","}
outputString = ""
inputString = input("Input string to encode: ")
inputString = inputString.lower()
for i in range (0,len(inputString)):
    outputString = outputString + " " + morseCode[inputString[i]]
print("OUTPUT:" + outputString)
