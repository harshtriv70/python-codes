# make a file and poem and findout whete it contains twinkle word 
with open("poem.txt") as f:
    content = f.read()
    if("twinkle" in content): 
        print("twinkle is present")
    else:
        
        print("twinkle is not present")