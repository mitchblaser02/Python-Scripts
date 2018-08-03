#PYTHON CSV ORGANIZER
#MITCH BLASER 2018

i = input("Enter CSV to sort (1, 2, 3): ") #Get the CSV from the user.
p = i.split(", ") #Turn the CSV into tuple.
o = sorted(p) #Set variable o to a sorted version of p.
for i in range(0, len(o)): #Loop for the amount of entries in o.
    print(o[i]) #Print out each entry sepertely (of the sorted "o" tuple.)
