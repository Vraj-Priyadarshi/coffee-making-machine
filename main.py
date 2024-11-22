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
    "water": 1000,
    "milk": 1000,
    "coffee": 200,
}
cost = 0
something = True
while something == True:
    print("May i know your order please?")
    cof = input("What would you like to have: 'espresso' , 'latte' ,'cappuccino' : ")
    coffee = cof.lower()


    def coin_checker(quater, dime, nickle, penny, coffe):
        total = (0.25 * quater) + (0.10 * dime) + (0.05 * nickle) + (0.01 * penny)
        if total >= MENU[coffe]["cost"]:
            global cost
            cost += MENU[coffe]["cost"]
            print()
            print(f"Here is your {coffe} , ENJOY!!!!")
            print()
            return round(total - MENU[coffe]["cost"], 4)

        else:
            print("Sorry that's not enough money. Money refunded.")
            return total


    def resource_checking():
        if coffee == "espresso":
            if resources["water"] >= MENU["espresso"]["ingredients"]["water"]:
                if resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
                    print()
                    print("You have to enter coin below ")
                    print()
                    print("******************************************************************************")
                    x = True
                    return x
                else:
                    print("sorry there is not enough Coffee.")
            else:
                print("Sorry there is not enough Water.")
        if coffee == "latte":
            if resources["water"] >= MENU["latte"]["ingredients"]["water"]:
                if resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
                    if resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
                        print()
                        print("You have to enter coin below ")
                        print()
                        print("**************************************************************************************")
                        x = True
                        return x
                    else:
                        print("Sorry there is not enough milk.")
                else:
                    print("sorry there is not enough Coffee.")
            else:
                print("Sorry there is not enough Water.")
        if coffee == "cappuccino":
            if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"]:
                if resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
                    if resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"]:
                        print()
                        print("You have to enter coin below ")
                        print()
                        print("****************************************************************************")
                        x = True
                        return x
                    else:
                        print("Sorry there is not enough milk.")
                else:
                    print("sorry there is not enough Coffee.")
            else:
                print("Sorry there is not enough Water.")


    if coffee == "report":
        print(f"Water ==>{resources["water"]}ml \nMilk ==>{resources["milk"]}ml\n"
              f"Coffee ==>{resources["coffee"]}g \nMoney ==>${cost}")

    if coffee == "espresso":
        X = resource_checking()
        if X == True:
            resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] = resources["water"] - MENU["espresso"]["ingredients"]["coffee"]
            q = int(input("Enter how many quaters : "))
            d = int(input("Enter how many dimes : "))
            n = int(input("Enter how many nickles : "))
            p = int(input("Enter how many pennies : "))
            print(f"Your remaining change = {coin_checker(q, d, n, p, coffee)}")
    if coffee == "latte" or coffee == "cappuccino":
        X = resource_checking()
        if X == True:
            resources["water"] = resources["water"] - MENU[coffee]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU[coffee]["ingredients"]["coffee"]
            resources["milk"] = resources["milk"] - MENU[coffee]["ingredients"]["milk"]
            q = int(input("Enter how many quaters : "))
            d = int(input("Enter how many dimes : "))
            n = int(input("Enter how many nickles : "))
            p = int(input("Enter how many pennies : "))
            print(f"Your remaining change = {coin_checker(q, d, n, p, coffee)}")
    print("***********************************************************************")
    print()
    a = input("Would you like to purchase anything again if yes then press 'Y' "
              "or you want to off the machine the press 'off' : ")
    again = a.lower()
    if again == "off":
        something = False