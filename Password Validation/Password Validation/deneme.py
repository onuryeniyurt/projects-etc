'''
def IsValidPassword(password):
    if(len(password) >5 and len(password)<15):
        lowerCase = False
        upperCase = False
        num = False
        special = False
        for char in password:
            if(char.isdigit()):
                num= True
            if(char.islower()):
                lowerCase = True
            if(char.isupper()):
                upperCase = True
            if(not char.isalnum()):
                special = True
                
        return lowerCase and upperCase and num and special
    else:
        return False
'''

passw = input("Enter your password please.")

if(len(passw) >5 and len(passw)<15):
        lowerCase = False
        upperCase = False
        num = False
        special = False
        for char in passw:
            if(char.isdigit()):
                num = True
       
            if(char.islower()):
                lowerCase = True
             
            if(char.isupper()):
                upperCase = True
                
            if(not char.isalnum()):
                special = True  
 

else:
    print("Your password must be 5-15 characters long.")
    exit()

if (lowerCase and upperCase and num and special == True):
        print("Your password is strong enough!")

if(num==False):
        print("Your password need to be including at least one digit.")
if(lowerCase==False):
        print("Your password need to be including at least one lowercase character.")
if(upperCase==False):
        print("Your password need to be including at least one uppercase character.")
if(special==False):
        print("Your password need to be including at least one special character.")       
