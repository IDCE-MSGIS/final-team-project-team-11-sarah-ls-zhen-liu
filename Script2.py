# Place necessary comments and code here. 
#this is an instruction for users
tempt=-999999
while(True):
    a=input("please select 1): Input the temperature; 2): Convert into centigrade; 3): Cloth suggestion; 4): Exit.\n")
    if(a==1):
        tempt=input("please enter the temperature in Fahrenheit:")
    elif(a==2):
        if(tempt>-999999):
            centi=(tempt-32.0)*5/9.0
            print "Centigrade is",round(centi,3)
        else:
            print("Please choose 1 first")
    elif(a==3):
        pass
    elif(a==4):
        print("thank you for your use!")
        break
    else:
        print("Please input the correct number")

