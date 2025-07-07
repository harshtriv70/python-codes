# spam detection if these words are present :  "make a lot of money", "buy now" , "click this"
p1 = "make a lot of money"
p2 = "buy now"
p3 = "click this"

message = input("Enter your comment : ")  #here we used "in" to check string is present in variable or not

if((p1 in message) or (p2 in message) or (p3 in message)):
    print("This message is spam")

else :
    print("This is not a spam")