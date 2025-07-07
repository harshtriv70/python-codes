a = {
    "key":"value" ,
    "Harsh": 100,
    "rohan": 56,
    "shubham": 90,
    list: [1, 2, 3, 4],
}
# print(a[list])

# print(a.items())
# print(a.keys())
# print(a.values())
# a.update({"Harsh":99, "Mantasha":100})


# print(a.get("Harsh")) #both are same
# print(a['Harsh']) # both are same but 
# print(a.get("Harshuuuu")) #but here it will return """NONE"""
# print(a['Harshuuuu']) # RETURNS ERROR

# print(a.clear())
# new_dict = a.copy()
# print(new_dict)

#poping keys 
# a.pop("key","value") ## specificaly removes the key mentioned 
# print(a)
# a.popitem() ## removes the items in LIFO order (Last In First out)
# print(a)