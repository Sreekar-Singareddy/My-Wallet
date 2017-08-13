from functionality import Login_Functionality, Register_Functionality
from exceptions.Main_Menu_Exceptions import InvalidOptionException
# print(" + ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ + ")
# print("$ PyWallet Welcomes You..! $")
# print(" + ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ + ")

print("Choose an option from below:\n")
print("============================")
end=False
count = 0
while(end==False and count<3):
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    print("============================")
    try:
        option=input()
        if(option.isdigit() and (int(option)>=1 and int(option)<=3)):
            if(int(option)==1):
                print("Login screen")
                # Now the control goes to login() method in the Customer class
                Login_Functionality.login()
                
            if(int(option)==2):
                Register_Functionality.register()
                
            if(int(option)==3):
                print("Thank you")
                end=True    
        else:
            count += 1
            raise InvalidOptionException()
    
    except InvalidOptionException as exp:
        print(exp)
    
    except:
        print("Something seems wrong... We are working on it\nVist back after a while :)")
    
else:
    if count == 3:
        print("Limit Exceeded!")
    