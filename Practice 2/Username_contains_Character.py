username = input("Enter the name: ")
char = len(username)

if(char>10):
    print("This name contains more than 10 alphabets")

elif(char==10):
    print("This name cotains 10 alphabets")

else:
    print("This name has less than 10 alphabets")