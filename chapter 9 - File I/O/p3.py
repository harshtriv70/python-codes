# vwrite a python program to  generate tables from 2 to 20 and write it to diffrent files under table folder 

def generatetable(n):
    table = ""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"
    
    with open(f"tables/table_{n}.txt","w") as f:
        f.write(table)


for i in range(2,11):
    generatetable(i)