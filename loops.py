#loops
#repeat
#for loop
for number in range(100):
    result=number**2
    if result %2==0:  #odd
        print(result)
##########################tik tok loops for odd and even
for number in range(100):
    result = number ** 2
    if result % 2 == 0:
        print("tik", number)  # odd
    if result % 2 != 0:
        print("tok", number)  # even
