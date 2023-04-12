def main():
    menu = {
        "espresso":{
            "ingredients":{
                "water":50,
                "coffee":18,
            },
            "cost":1.5,
        },
        "latte":{
            "ingredients":{
                "water":200,
                "coffee":24,
                "milk":150,
            },
            "cost":2.5,

        },
        "cappuccino":{
            "ingredients":{
                "water":250,
                "coffee":24,
                "milk":100
            },
            "cost":3.0,
        }
    }
    global profit
    profit = 0
    resources = {
        "water":300,
        "milk":200,
        "coffee":100
    }

    def sufficient_resources(ingredients):
        for i in ingredients:
            if ingredients[i] > resources[i]:
                print(f"Sorry there is not enough {i}")
                return False
        return True

    def process_coins():

        money = int(input('How many quarters?: ')) * 0.25
        money += int(input('How many dimes?: ')) * 0.10
        money += int(input('How many nickles?: ')) * 0.05
        money += int(input('How many pennies?: ')) * 0.01
        return money
    
    def is_transaction_successful(payment,cost):
        global profit
        if payment>=cost:
            change = round(payment - cost,2)
            print(f'Here is ${change} dollars in change')
            profit += cost
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")

    def make_coffee(drink, order_ingredients):
        for item in order_ingredients:
            resources[item] -= order_ingredients[item]
        print(f'Here is your {drink} ☕️. Enjoy!')




    taking_orders = True
    while taking_orders:
        logo = """

              Welcome to the Coffee Shop
                Today's Menu:
                
                 1. Espresso - $1.50
                 2. Latte - $2.50
                 3. Cappuccino - $3.00
                 
         Please enter your choice or type "off" to exit:
        
        
        """

        print(logo)
        choice = input("What would you like?(espresso/latte/cappuccino): ")
        if choice == 'off':
            is_on = False
            break
        elif choice == 'report':
            print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}")
        else:
            drink = menu[choice]
            if sufficient_resources(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment,drink["cost"]):
                    make_coffee(choice,drink["ingredients"])
main()
