# create an empty dict allow 4 frnds to enter thier names as key and thier fav lang as value .Assume that the name are unique 
 
d = {}
name = input("Enter your name : ")
lang = input("Enter your fav lang : ")
d.update({name:lang})

name = input("Enter your name : ")
lang = input("Enter your fav lang : ")
d.update({name:lang})

name = input("Enter your name : ")
lang = input("Enter your fav lang : ")
d.update({name:lang})

name = input("Enter your name : ")
lang = input("Enter your fav lang : ")
d.update({name:lang})


print(d)