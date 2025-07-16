# storeing tables using list comprehension in table.txt

n = int(input("Enter a Numbers : "))

table = [n*i for i in range(1,11)]

print(table)

with open("table.txt", "a") as f :
    f.write(f"Table of {n} : {table} \n")