# write a program to greet all the person stored in a list l and which starts with "s"
l = ["Harry", "Subham", "Harsh","Soni","Sonu"]
for name in l:
    # if(name[0].lower() == "s" ):
    #     print(f"Good Morning {name}")
    # ----or---- 
    if(name.lower().startswith("s")):#1st it will convert all names in lower case then it will see start letter is "s" or not
        print(f"Good Morning {name}")