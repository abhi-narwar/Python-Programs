password=input("enter your password")
confirm_pass=input("please confirm your password")
if password==confirm_pass:
    print("sucess")
else:
    if password.casefold()==confirm_pass.casefold():
        print("please try again")
    else:
        print("password not match")
          
