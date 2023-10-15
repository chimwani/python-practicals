#if you are under 5 you are a kid 
#if you are 5-15 you are a big kid
#if you are 15-21 you are a bigger kid
#if you are over 21 you are old


age = int(input("what is your age ?" ))
if age <=5:
    print("you are a kid")
elif age <=15:
    print("you are a big kid")
elif age <=21:
    print("you are a bigger kid")
else :
    print("you are old")