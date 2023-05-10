m1=int(input("enter the marks for 1st subject:"))
m2=int(input("enter the marks for 2nd subject:"))
m3=int(input("enter the marks for 3rd subject:"))

overAll=(m1+m2+m3)/3

if(overAll>=40):
    if(m1>=33 and m2>=33 and m3>=33):
        print("you have passed the exam")
    else:
        print("you have not passed the exam due to one subjects")
else:
    print("you have not passed the exam due to the overall percentage")