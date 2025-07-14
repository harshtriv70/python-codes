# same as p4 but now replacing multiple words with #### in a file which contains it   


words = ["donkey","bad","banana"]

with open("p4demofile.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("p4demofile.txt", "w") as f :
    f.write(content)

