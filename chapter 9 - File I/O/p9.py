# see wheather files have same content or not


with open("log.txt") as f :
    content1 = f.read()

with open("log_copy.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("yes files have same content")
else:
    print("No files have same content")