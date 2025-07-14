#findout in which line python is present in log file

with open("log.txt") as f :
    lines = f.readlines()
    # print(line)

lineno = 1
for line in lines:
    if("python" in line):
        print(f"python is present in lineno : {lineno}")
        break
    lineno += 1
  
else : 
    print("No python is not present in any line")


# if("python" in content):
#     print("Yes python is present in log")
# else:
#     print("no python is present in log")