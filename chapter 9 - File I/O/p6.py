

with open("log.txt") as f :
    content = f.read()

if("python" in content):
    print("Yes python is present in log")
else:
    print("no python is present in log")