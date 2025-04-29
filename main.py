import art as a
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Money": 0,
}
PASSWORD ="tanq567300"
while True:
    user=input(f"{a.logo} \nWhat would you like?(Espresso/Latte/Cappuccino): ").lower()
    if user == 'off':
        print("Turning off...")
        break
    elif user == 'espresso' or user == 'e':

        quarters = int(input("How many quarters?: "))


        dimes = int(input("How many dimes?: "))


        nickles = int(input("How many nickles?: "))


        pennies = int(input("How many pennies?: "))

        dollars= (quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)
        esp = MENU['espresso']
        esp_cost = esp['cost']
        esp_ing = esp['ingredients']
        esp_water = esp_ing['water']
        esp_coffee = esp_ing['coffee']
        if dollars== esp_cost:
            resources['Money']+= dollars
            resources['water'] -= esp_water
            resources['coffee'] -= esp_coffee
            if resources['water']<0 or resources['coffee']<0:
                print("\n"*20)
                print("insufficient resources!")
                print("Money Refunded")
                resources['Money'] -= dollars
                resources['water'] += esp_water
                resources['coffee'] += esp_coffee

                continue
            print("\n"*20)
            print("Your Espresso is ready!☕")
            print(f"resources left -->\n {resources}")
            continue

        elif dollars> esp_cost:
            change = dollars-esp_cost
            print("\n"*20)
            print(f"here's your change 🙌 ${change}")
            resources['Money'] += esp_cost
            resources['water'] -= esp_water
            resources['coffee'] -= esp_coffee
            if resources['water'] < 0 or resources['coffee'] < 0:
                print("\n"*20)
                print("insufficient resources!")
                print("Money Refunded")
                resources['Money'] -= esp_cost
                resources['water'] += esp_water
                resources['coffee'] += esp_coffee
                continue
            print("Your Espresso is ready!☕")
            print(f"resources left -->\n {resources}")

        elif dollars<esp_cost:
            print("\n"*20)
            print(f"Insufficient funds for the type of drink. Money refunded💸: ${dollars}")
            continue

    elif user == 'latte' or user == 'l':
        quarters = int(input("How many quarters?: "))

        dimes = int(input("How many dimes?: "))

        nickles = int(input("How many nickles?: "))

        pennies = int(input("How many pennies?: "))

        dollars = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
        esp = MENU['latte']
        esp_cost = esp['cost']
        esp_ing = esp['ingredients']
        esp_water = esp_ing['water']
        esp_coffee = esp_ing['coffee']
        esp_milk = esp_ing['milk']
        if dollars == esp_cost:
            resources['Money'] += dollars
            resources['water'] -= esp_water
            resources['coffee'] -= esp_coffee
            resources['milk'] -= esp_milk
            if resources['water'] < 0 or resources['coffee'] < 0 or resources['milk']<0:
                print("\n"*20)
                print("insufficient resources!")
                print("Money Refunded")
                resources['Money'] -= dollars
                resources['water'] += esp_water
                resources['coffee'] += esp_coffee
                resources['milk'] += esp_milk
                continue
            print("\n"*20)
            print("Your Latte is ready!☕")
            print(f"resources left -->\n {resources}")
            continue

        elif dollars > esp_cost:
            change = dollars - esp_cost
            print("\n"*20)
            print(f"here's your change 🙌 ${change}")
            resources['Money'] += esp_cost
            resources['water'] -= esp_water
            resources['coffee'] -= esp_coffee
            resources['milk'] -= esp_milk
            if resources['water']< 0 or resources['coffee'] < 0 or resources['milk']< 0:
                print("\n"*20)
                print("insufficient resources!")
                print("Money Refunded")
                resources['Money'] -= esp_cost
                resources['water'] += esp_water
                resources['coffee'] += esp_coffee
                resources['milk'] += esp_milk
                continue
            print("Your Latte is ready!☕")
            print(f"resources left -->\n {resources}")

        elif dollars < esp_cost:
            print("\n"*20)
            print(f"Insufficient funds for the type of drink. Money refunded💸: ${dollars}")
            continue
    elif user == 'cappuccino' or user == 'c':
        quarters = int(input("How many quarters?: "))

        dimes = int(input("How many dimes?: "))

        nickles = int(input("How many nickles?: "))

        pennies = int(input("How many pennies?: "))

        dollars = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
        esp = MENU['cappuccino']
        esp_cost = esp['cost']
        esp_ing = esp['ingredients']
        esp_water = esp_ing['water']
        esp_coffee = esp_ing['coffee']
        esp_milk = esp_ing['milk']
        if dollars == esp_cost:
            resources['Money'] += dollars
            resources['water'] -= esp_water
            resources['coffee'] -= esp_coffee
            resources['milk'] -= esp_milk
            if resources['water'] <  0 or resources['coffee'] <  0 or resources['milk'] <  0:
                print("\n"*20)
                print("insufficient resources!")
                print("Money Refunded")
                resources['Money'] -= dollars
                resources['water'] += esp_water
                resources['coffee'] += esp_coffee
                resources['milk'] += esp_milk
                continue
            print("\n"*20)
            print("Your cappuccino is ready!☕")
            print(f"resources left -->\n {resources}")
            continue

        elif dollars > esp_cost:
            change = dollars - esp_cost
            print("\n"*20)
            print(f"here's your change 🙌 ${change}")
            resources['Money'] += esp_cost
            resources['water'] -= esp_water
            resources['coffee'] -= esp_coffee
            resources['milk'] -= esp_milk
            if resources['water'] <= 0 or resources['coffee'] <= 0 or resources['milk'] <= 0:
                print("\n"*20)
                print("insufficient resources!")
                print("Money Refunded")
                resources['Money'] -= esp_cost
                resources['water'] += esp_water
                resources['coffee'] += esp_coffee
                resources['milk'] += esp_milk
                continue
            print("Your cappuccino is ready!☕")
            print(f"resources left -->\n {resources}")

        elif dollars < esp_cost:
            print("\n"*20)
            print(f"Insufficient funds for the type of drink. Money refunded💸: ${dollars}")
            continue
    elif user == 'resources' or user == 'r':
        print("\n"*20)
        print(f"Here are the resources left {resources}")
    elif user == 'refill':
        print("\n"*20)
        refill=input(f"Resources💰:\n {resources} \nWhat resource would you like to refill?: ").lower()
        if refill =='water':
            resources['water']+= 200
            print("Successfully refilled water!🚰")
            print(f"Resources left in the machine: {resources}")
            continue
        elif refill =='milk':
            resources['milk']+=200
            print("Successfully refilled milk!🥛")
            print(f"Resources left in the machine: {resources}")
            continue
        elif refill =='coffee':
            resources['coffee']+=100
            print("Successfully refilled coffee!☕")
            print(f"Resources left in the machine: {resources}")
            continue
        elif refill=='money':
            redeem_money= input("Would you like to redeem all the money available in the machine? y/n: ")
            if redeem_money =='y':
                password=input("Enter the password to redeem the money🔒: ")
                if password == PASSWORD:
                    print("Money redeemed!💵")
                    resources['Money'] -= resources['Money']
                    print(f"Resources left in the machine: {resources}")
                    continue
                else:
                    print("Wrong Password!❌")
                    continue
            else:
                print("Exiting refill mode!....")
                continue
        else:
            print("Wrong input!")
            continue


    else:
        print("\n"*20)
        print("Wrong input!")
        continue 

