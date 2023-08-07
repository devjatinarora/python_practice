m1 = int(input("Enter marks of subject 1"))
m2 = int(input("Enter marks of subject 2"))
m3 = int(input("Enter marks of subject 3"))

if (m1<33 or m2<33 or m3<33):
    print("You are fail because your marks are less than 33% in one of the subjects")

elif((m1+m2+m3)/3 <40):
    print("You are fail because your total percentage is less than 40%")

else:
    print("Congratulations you are passed")