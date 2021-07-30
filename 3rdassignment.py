name1 = input("Enter ur name\n")
name2 = input("Enter ur partner name\n")
name3 = name1+name2
lower_name = name3.lower()
a = lower_name.count("l")
b = lower_name.count("0")
c = lower_name.count("v")
d = lower_name.count("e")
love = a+b+c+d
if(love < 1 or love>9):
    print("Your love score is " , love ,"you go together like coke and mentos")
elif(love in range(4,6)):
    print("Your score is " , love ,"you are alright together")
else:
    print("Your score is " , love)
    