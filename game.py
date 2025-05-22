import random
def check(com, user):
    if com==user:
        return 0
    if(com==1 and user==0):
        return -1
    if(com==1 and user==2):
        return -1
    if(com==2 and user==0):
        return -1
    return 1
com=random.randint(0,2)
user=int(input("Enter 0 for snake, 1 for water and 2 for gun"))
score=check(com,user)
print("You:",user)
print("Computer:",com)
if(score==0):
    print("Its a draw")
elif score==-1:
    print("Its a draw")
else:
    print("You Won")