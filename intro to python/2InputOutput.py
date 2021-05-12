greeting = "Hello there young one. Welcome to Narnia. What it your name?"



def the_intro():
    print(greeting)
    char_name = input("please enter your name:  ")
    welcome_greeting = print("It is nice to have you here " + char_name + ". Walk with me as I tell you a story.")



def math_addition():
    x = float(input("please enter the first number to add: "))
    y = float(input("please enter the second number to add: "))
    z = x + y
    print(f"x + y = {z}")
    print(type(z))


math_addition()