import getpass as yo

def check_boolean():
    print(10 > 9)
    print(10 == 9)
    print(10 < 9)
# check_boolean()

def boolean_condition():
     username =input("Please enter your name: ")
     password = yo.getpass("Please enter your password: ")
     if username == "admin" and password == "ninjacoder":
         print("Welcome most awesome nerd. You have entered Nerd Inc.")
     else:
         print("Your username and pasword are incorrect.")
         try_again = input("Would you like to try again? y or n ")
         if try_again == "y":
             boolean_condition()
         else:
             print("Have a good day. You are not admitted to Nerd Inc.")
boolean_condition()