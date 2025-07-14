
def httpstatus(status):
    match status:
        case 200:
            return "OK"
        case 300:
            return "data missing"
        case 500:
            return "internal server error"
        case 404:
            return "Not found"
        case _:
            return "Unknown Status"
        
# print(httpstatus(3007))

# Merging 2 dictionary :

dict1 = {"a" : 1, "b" : 3}
dict2 = {"b" : 1, "c" : 3, 'f' : 4}

merged = dict1 | dict2
print(merged)


# mutiple context 

with (
    open("file1.txt") as f1,
    open("file2.txt") as f2
):
    pass
