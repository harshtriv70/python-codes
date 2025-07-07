#write a recursive func to cal sum of all n  natural num 
# def natural_sum(n):
#     t = 0
#     for i in range(1,n+1):
#         t += i
#         i += 1
#     return t

# print(natural_sum(4))

# using recursion func

def natural(n):
    if(n==1):
        return 1
    return natural(n-1) + n

print(natural(4))