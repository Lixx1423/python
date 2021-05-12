import random

def whatsfordinner():
    print("What sounds good?")

    print("Chinese")

    print("Italian")

    print("Mexican")

    print("Japanese")

    print("Random")

    answer = input("Please input one of the above: ")

    random_number = random.randint(1,3)
    raddad = random.randint(1,4)

    if answer == "Chinese":
        print("Try this place called")
        if random_number == 1:
            print("Main Moon")
        elif random_number == 2:
            print("Imperial Garden")
        elif random_number == 3:
            print("China Star")

    if answer == "Italian":
        print("Try this place called")
        if random_number == 1:
            print("AngeNettas Cafe")
        elif random_number == 2:
            print("Bella Napoli")
        elif random_number == 3:
            print("Belleria Pizza")

    if answer == "Mexican":
        print("Try this place called")
        if random_number == 1:
            print("Tequila Jalisco")
        elif random_number == 2:
            print("Los Gallos")
        elif random_number == 3:
            print("El Cowboy Tex Mex Grille")

    if answer == "Japanese":
        print("Try this place called")
        if random_number == 1:
            print("Hana Japanese")
        elif random_number == 2:
            print("Hanami Express")
        elif random_number == 3:
            print("izumi")

    if answer == "Random":
        if raddad == 1:
            print("Try this place called")
            if random_number == 1:
                print("Main Moon")
            elif random_number == 2:
                print("Imperial Garden")
            elif random_number == 3:
                print("China Star")

        if raddad == 2:
            print("Try this place called")
            if random_number == 1:
                print("AngeNettas Cafe")
            elif random_number == 2:
                print("Bella Napoli")
            elif random_number == 3:
                print("Belleria Pizza")

        if raddad == 3:
            print("Try this place called")
            if random_number == 1:
                print("Tequila Jalisco")
            elif random_number == 2:
                print("Los Gallos")
            elif random_number == 3:
                print("El Cowboy Tex Mex Grille")
        
        if raddad == 4:
            print("Try this place called")
            if random_number == 1:
                print("Hana Japanese")
            elif random_number == 2:
                print("Hanami Express")
            elif random_number == 3:
                print("izumi")


whatsfordinner()