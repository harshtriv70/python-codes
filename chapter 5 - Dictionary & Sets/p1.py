#write a program to create a dictionary of hindi words with values of as thier english translation.
words = { 
    "billi" : "Cat",
    "kutta" : "Dogesh",
    "sher" : "lion"
 }

asked = input("Enter a word to get English means : ")
print(words.get(asked))
print(words[asked])
print(words["billi"])