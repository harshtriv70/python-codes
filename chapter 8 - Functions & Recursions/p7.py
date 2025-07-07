#fun to remove given word from the list and strip it at the same time
def removee(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))    #strip fun bus suru aur last me se word remove karta hai not from midddle 
    return n

l = ["harnnsh", "allon", "nmonon", "noon"]

print(removee(l, "n"))


# for items in l :
#     print()
    