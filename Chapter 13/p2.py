# write a program to filter a list of number which are divisible by 5

def div5(n):
    if(n%5 == 0):
        return True
    return False

l = [1,2,30,4,5,6,70,8,90]

a = list(filter(div5,l))
print(a)