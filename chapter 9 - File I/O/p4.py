# replacing word donkey with #### in a file which contains it 
word = "donkey"

with open("p4demofile.txt") as f:
    content = f.read()

contentnew = content.replace(word, "#####")

with open("p4demofile.txt", "w") as f :
    f.write(contentnew)

