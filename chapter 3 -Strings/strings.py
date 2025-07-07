name = "harsh"
print(len(name)) #prints the length of the string

slice = name[0:3]
print(slice) #
 #last index is excluded "3"


a = name.capitalize()
print(a)

a = name.upper()
print(a)

name1 = "Harsh is a bad bad Bad badboy"
a = name1.replace("bad", "good")
print(a)

ar = "harhs"
iin = "123"
a = iin.isdigit() #checks if the string is a digit
b = ar.isalpha() #checks if the string is alphabetic
print(a)
print(b)

## escape sequences characters like \n, \t, \\
a = "Harsh\nTrivedi"
b= "Harsh\tTrivedi"
c = "Harsh\\Trivedi"
d = "Harsh \"Trivedi\"" #to print " in the string
print(a + "\n" + b + "\n" + c + "\n" + d)