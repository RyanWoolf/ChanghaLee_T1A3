"""import all the packages that needed. This module is the main frame of the app"""
import sys
import os
import random
from time import sleep
from art import tprint
import config_system as CS
import config_characters as CC


def clear_screen():
    """to clear the screen to keep the infos on top or else"""
    os.system('cls' if os.name == 'nt' else 'clear')


def enter_to_cont():
    """prevent too fast stream of the app. Wait until player check or read"""
    input("Please enter to continue ")


def show_logo():
    """Show the main logo at beginning"""
    tprint("\nLionWolf  Haus", font= "tarty1")
    tprint("\nRestaurant Tycoon\n\n", font= "tarty2")
    print(CS.color.BOLD + "Select one from the following\n" + CS.color.END)


def typing_animation(text, speed):
    """many time used in most of scripts. makes them look like typing. Check the Reference * """
    for letter in text:
        sleep(speed)
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("")


def input_check():
    """The reason I didn't use try/except is what i need for return is only 1 or 2"""
    select_right = False
    while select_right is False:
        select = input("Select : ")
        if select == "1" or select == "2":
            select_right = True
            return int(select)
        else:
            print(CS.color.RED + "Please enter the right number\n" + CS.color.END)


def checking_rules():
    """to decide that player passed or failed, used in System class and daily report"""
    if CC.venue.budgets < 5000 or CC.customers.happiness < 60 or CC.venue.wastage > 25:
        show_days()
        tprint("\n\nGAME OVER\n\n", font = "tarty1")
        print(f"Failed on Day {CC.venue.days}\n\n\n")
        if CC.venue.budgets < 5000:
            print(
                "I'm sorry, Our budget is now under $ " +
                CS.color.RED + "5000.\n" + CS.color.END)
        elif CC.customers.happiness < 60:
            print(
                "I'm sorry, Our customers happiness is now under " +
                CS.color.RED + "60" + CS.color.END + " %\n")
        elif CC.venue.wastage > 25:
            print(
                "I'm sorry, Our wastage is now more than " +
                CS.color.RED + "25" + CS.color.END + " %\n")
        print('''\nI guess it was our best.\n\n''')
        enter_to_cont()
        raise KeyboardInterrupt
    else:
        pass

def colour_balance(balance):
    """colour indicator for UI"""
    if balance >= 10000:
        colour_warning1 = CS.color.GREEN
    elif 7000 <= balance < 10000:
        colour_warning1 = CS.color.YELLOW
    else:
        colour_warning1 = CS.color.RED
    return colour_warning1

def colour_happiness(happiness):
    """colour indicator for UI"""
    if happiness >= 85:
        colour_warning2 = CS.color.GREEN
        max_happiness(happiness)
    elif 70 <= happiness < 85:
        colour_warning2 = CS.color.YELLOW
    else:
        colour_warning2 = CS.color.RED
    return colour_warning2

def colour_wastage(wastage):
    """colour indicator for UI"""
    if wastage >= 20:
        colour_warning3 = CS.color.RED
    elif 10 <= wastage < 20:
        colour_warning3 = CS.color.YELLOW
    else:
        colour_warning3 = CS.color.GREEN
    return colour_warning3

def max_happiness(num):
    """if happiness is over 100, make it back to max 100"""
    if num > 100:
        num = 100
    return num

def show_days():
    """Sub feature 1, for UI to display main variables to check"""
    clear_screen()
    tprint(f"\n         DAY {CC.venue.days}\n\n", font = "tarty3")
    balance = CC.venue.budgets_yesterday
    happiness = CC.customers.happiness_yesterday
    wastage = CC.venue.wastage
    print(
        "Current Balance : $ " + colour_balance(balance) +
        f"{balance:.2f}" + CS.color.END +
        "  |  Customers Happiness : " + colour_happiness(happiness) +
        f"{max_happiness(happiness):.2f}" + CS.color.END + " %"
        "  |  Stock Wastage : " + colour_wastage(wastage) +
        f"{wastage}" + CS.color.END + " %")
    print(
        "--------------------------------------" +
        "---------------------------------------------------\n\n")
    sleep(1)


def rule_explain():
    """only used one time at the begging of game. rule explained"""
    tprint("Welcome", font= "tarty1")
    sleep(1)
    typing_animation(
        '''\n\nHi! My name is Ryan and I'm your assistant manager.
        ''', 0.02)
    sleep(0.5)
    typing_animation(
        '''\nAs you know, We have hired new staff recently.
    \nThey're working fine but it would be better if we have a good captain to lead.
        ''', 0.02)
    sleep(0.5)
    typing_animation(
        '''\nYour job is\n\n''' + CS.color.YELLOW +
        '''    to let me know what to order for the next day service and\n
    give orders to staff when situation happens.\n
        ''' + CS.color.END, 0.02)
    sleep(0.5)
    typing_animation(
        '''\nBut remember, You'll lose if you\n\n''' + CS.color.RED +
        '''    lose budget till $5000 or\n
    lose Customers Satisfaction till 60% or\n
    Wastage is over 25%\n''' + CS.color.END, 0.02)
    sleep(0.5)
    typing_animation(
        '''\nI'm always here to assist you, give you tips and my opinions.
        ''', 0.02)
    sleep(0.5)
    typing_animation(
        '''and remember, Whenever you hit ''' + CS.color.BLUE + "Ctrl + C" + CS.color.END +
        ''', You can exit the game.\n
        ''', 0.02)
    sleep(0.5)
    typing_animation("\nGood luck! :)\n\n", 0.02)
    sleep(1)
    enter_to_cont()


def good_morning():
    """good morning logo"""
    show_days()
    tprint("Good Morning", font = "tarty1")
    sleep(2)



def morning_briefing():
    """stock report before round"""
    if CC.venue.days == 1:
        typing_animation(
        '''Luckily We have received urgent delivery from the supplier early morning.
        ''', 0.02)
    CC.assist_m.bad_news = False
    CC.assist_m.tell_news()
    typing_animation("\nToday, We got \n\n", 0.02)
    print_current_stocks()
    sleep(0.5)
    typing_animation("\n\nWe're ready to open.\n\n", 0.02)
    enter_to_cont()



def good_night():
    """good night logo"""
    show_days()
    tprint("Good Night\n\n", font = "tarty1")
    sleep(1)
    enter_to_cont()


def copy_order_history():
    """used to compare last days order and now"""
    for item, stock in CC.venue.current_stocks.items():
        CC.venue.yesterday_stocks.update({item : stock})



def game_round():
    """part of Main feature 1."""
    customer = 0
    while customer < CC.customers.customers_number:
        food, drink = random.choice(CC.venue.list_foods), random.choice(CC.venue.list_drinks)
        CC.venue.current_stocks[food] -= 1
        CC.venue.current_stocks[drink] -= 1
        CC.venue.budgets += CC.venue.stock_prices[food] + CC.venue.stock_prices[drink]
        CC.customers.happiness += 0.2
        out_of_stock(food)
        out_of_stock(drink)
        CC.customers.happiness = max_happiness(CC.customers.happiness)
        customer += 1

def out_of_stock(item):
    """if out of stock, execute this"""
    difficulty = CC.venue.difficulty * 0.6
    if CC.venue.current_stocks[item] < 0:
        CC.customers.happiness -= (difficulty)
        CC.venue.current_stocks[item] = 0
        CC.venue.budgets -= CC.venue.stock_prices[item]

def count_hours():
    """setup to make it look like game_round function is excuting through time"""
    for time in range(9, 16):
        if time < 12:
            print(f"\n  {time} AM ...")
        elif time == 12:
            print(f"\n  {time} PM ...")
        else:
            print(f"\n  {time - 12} PM ...")
        sleep(1)
        accidents() # Unexpected accidents might happen
    sleep(1)
    typing_animation("\n\nWe're closed now!", 0.02)
    sleep(1)
    typing_animation("\n\nI'll go get the daily report.\n\n", 0.02)
    sleep(1)
    enter_to_cont()

def accidents():
    """part of Main feature 2. decide a chance that accident happens"""
    chance = random.randint(0, 100)
    if chance > 98:
        long_wait()
    elif 71 > chance > 68:
        broken_cups()
    elif 3 < chance < 5:
        food_inspector()

def food_inspector():
    """one of the unexpected accidents"""
    typing_animation(
        '''\n    Food & Safety inspector has visited. \n
    He looked around the restaurant and said that We have some problems over the kitchen.\n\n''' +
    CS.color.BLUE + "       1) Tell him they'll be fixed today." + CS.color.END + "or\n" +
    CS.color.BLUE + "       2) Bribe him! What else can be worse than now? \n" + CS.color.END, 0.02)
    sleep(1)
    selection = input_check()
    sleep(0.5)
    if selection == 1:
        print(
            '''\n   He went back after a warning. But I think our Customers heard what happened.\n
    We have lost''' + CS.color.RED + " 5 " + CS.color.END + "% Happiness. \n" )
        CC.customers.happiness -= 5
    elif selection == 2:
        bribe = random.randint(0, 10)
        if bribe > 7:
            print(
                '''\n    Oh no! He's going to fine us even harder! Darn! Shouldn't have tried!\n
    We have lost $''' + CS.color.RED + " 3000\n\n" + CS.color.END)
            CC.venue.budgets -= 3000
        elif bribe < 8:
            print(
                '''\n   We bribed him with $ ''' + CS.color.RED + "1000\n" + CS.color.END +
                "\n   Hope he doesn't come back again..\n\n")
            CC.venue.budgets -= 1000

def long_wait():
    """one of the unexpected accidents"""
    typing_animation(
        '''\n    There's some customers have complains because of long waits.\n
    You can give the staffs to look after by \n\n''' +
    CS.color.BLUE + "       1) offering them free extras, " + CS.color.END + "or\n" +
    CS.color.BLUE + "       2) telling them we're doing our best\n\n" + CS.color.END, 0.02)
    sleep(1)
    selection = input_check()
    sleep(0.5)
    if selection == 1:
        print(
            '''\n    We've offered them free extras. They're so much happy and grateful.\n
    We have ''' + CS.color.GREEN + " + 3 " + CS.color.END + "% Happiness and spent $" +
        CS.color.RED + " 150 " + CS.color.END + "from today's sales.\n\n")
        CC.venue.budgets -= 150
        CC.customers.happiness += 3
    elif selection == 2:
        print(
            '''\n    The customers didn't look mad but also happy.\n
    We have lost''' + CS.color.RED + " 4 " + CS.color.END + "% Happiness. \n\n" )
        CC.customers.happiness -= 4


def broken_cups():
    """one of the unexpected accidents"""
    typing_animation(
        '''\n    One of the staff has broken glasses.\n
    Thankfully nobody hurt but we need to order new glasswares.\n
    They're pretty luxury grade items. It'll cost $ ''' + CS.color.RED + "200" + CS.color.END +
    ", Paid directly to the store.\n\n", 0.02)
    CC.venue.budgets -= 200




def daily_report_scripts():
    """part of Main feature 3"""
    print("Daily Report : ")
    sleep(1)
    if CC.customers.happiness > 90:
        typing_animation("\n\nIt was great day!\n", 0.02)
        sleep(0.5)
        typing_animation("I think our customers were super happy today!\n", 0.02)
    elif 80 < CC.customers.happiness < 91:
        typing_animation("\n\nIt was good day!\n", 0.02)
        sleep(0.5)
        typing_animation("We did good job generally.\n", 0.02)
    else:
        typing_animation("\n\nIt wasn't bad day.\n", 0.02)
        sleep(0.5)
        typing_animation("But it seems like we need to do something to make it better.\n", 0.02)
    sleep(1)
    gross_sales = CC.venue.budgets - CC.venue.budgets_yesterday
    actual_number = int(CC.customers.customers_number // 1)
    print(
        "\nWe served " +
        CS.color.YELLOW + f"{actual_number}" + CS.color.END +
        ''' pax customers through the service. Pretty big number.\n''')
    print(
        "We earned $ " + CS.color.YELLOW + f"{gross_sales}" + CS.color.END + " today, " +
        "Current balance is $ " + CS.color.YELLOW + f"{CC.venue.budgets}" + CS.color.END)
    CC.venue.budgets_yesterday = CC.venue.budgets
    sleep(1)
    happiness = CC.customers.happiness
    print(
        "\nAnd, Todays our customers happiness is " +
        colour_happiness(happiness) + f"{max_happiness(happiness):.2f}" + CS.color.END + " %\n")
    CC.customers.happiness_yesterday = CC.customers.happiness
    sleep(2)




def wastage_check():
    """tell how many left from yesterdays stock order"""
    typing_animation("\n\nChecking the stocks left ...\n\n", 0.02)
    sleep(1)
    print_current_stocks()
    sleep(1)
    num_wastage = 0
    price_wastage = 0
    price_stocks = 0
    for menu, stock in CC.venue.current_stocks.items():
        num_wastage += stock
        price_stocks += CC.venue.stock_prices[menu] * CC.venue.yesterday_stocks[menu]
        price_wastage += CC.venue.stock_prices[menu] * stock
    percent_wastage = round(price_wastage / price_stocks * 100, 2)
    CC.venue.wastage = percent_wastage
    typing_animation(
        "\nWe have " + colour_wastage(percent_wastage) + f"{percent_wastage}" + CS.color.END +
        "% wastage today. That was $ " + CS.color.BLUE + f"{price_wastage:.2f}" + CS.color.END +
        " worths.", 0.02)
    typing_animation(
        "\nWe don't use the stock again. We'll dicard them and replace to fresh ones.\n", 0.02)
    sleep(1)
    enter_to_cont()



def print_current_stocks():
    """show what we currently have"""
    for name, stock in CC.venue.current_stocks.items():
        print(f"    {name} : {stock} ea\n")
        sleep(0.2)



def closing_venue():
    """end of a round."""
    show_days()
    typing_animation("\nThe orders have been placed. They'll be deliverd over the night.", 0.02)
    sleep(0.5)
    typing_animation("\n\nI'll see you tomorrow. :) \n\n", 0.02)
    sleep(0.5)
    enter_to_cont()

def bad_news():
    """price adjustment chance setup."""
    chance = random.randint(0, 100)
    if chance > 86:
        CC.assist_m.bad_news = True
        CC.assist_m.tell_news()
        percentage = CC.assist_m.percent_priceup * 100
        typing_animation(
            '''\n\n    I have a bad new from the supplier. Due to the bad weather condition,\n
    their cargo truck couldn't arrive yet.\n
    They said they can't help but increase the supplier price for ''' +
            CS.color.RED + f"{percentage}" + CS.color.END + " % today.\n\n", 0.02)
        sleep(1)
        enter_to_cont()
        print("\n")

def percentage_priceup():
    """pick up the percentage"""
    percentage = round(random.uniform(0.10, 0.25), 2)
    return percentage


def place_order():
    """part of main feature 3."""
    typing_animation("\nPlease let me know the stock orders for tomorrow service.\n\n", 0.02)
    sleep(0.5)
    payments_due = 0
    adj = CC.venue.price_adj
    if CC.venue.days % 7 == 0: # paying rent fee setup
        print('''\n    Every 7 days, We have to pay the rent to the realestate agent.\n
    We have paid $''' + CS.color.RED + "8500" + CS.color.END +
    ". It'lle be added to the payment due.\n\n")
        payments_due += 8500
    print("Order list : \n\n")
    sleep(0.5)
    for name in CC.venue.current_stocks.keys():
        while True: # Order amount compare with last one
            num_taken = input(
                name + " is $ " +
                CS.color.BLUE + f"{adj * CC.venue.supplier_prices[name]:.2f}" + CS.color.END +
                ". How many units to order? Yeseterday : " +
                f"{CC.venue.yesterday_stocks[name]} ea / Today : ")
            try:        # doesn't need certain numbers. any numbers but letters or negative numbers
                units = int(num_taken)
                if units < 0:       # negative numbers
                    raise ValueError
                CC.venue.current_stocks.update({name : int(units)})
                payments_due += int(units) * CC.venue.supplier_prices[name] * adj
            except ValueError:
                print(CS.color.RED + "Please enter the right number\n" + CS.color.END)
                continue # pass the below and go back to ask again
            finally:
                print("")
            break
    sleep(0.5)
    print(
        "\n\nThe total payments due is $ " +
        CS.color.YELLOW + f"{payments_due:.2f}" + CS.color.END +
        " and the daily wage for staffs is $ " +
        CS.color.YELLOW + f"{CC.venue.daily_staffs_wage:.2f}\n\n" + CS.color.END)
    if payments_due+CC.venue.daily_staffs_wage > CC.venue.budgets:
        print(CS.color.RED +
        "It's over your current balance. Please change the amount of order.\n\n" + CS.color.END)
        sleep(1)
        enter_to_cont()
        CC.assist_m.place_orders()
    print("Is it correct?\n\n   1) Yes\n   2) No\n")
    selection = input_check()
    if selection == 1:
        print(
            "\n\nYou have paid $ " +
            CS.color.BLUE + f"{payments_due + CC.venue.daily_staffs_wage:.2f}" + CS.color.END +
            " altogether.\n\n")
        CC.venue.budgets -= (payments_due+CC.venue.daily_staffs_wage)
        sleep(1)
        enter_to_cont()
    elif selection == 2:
        CC.assist_m.place_orders()


def lose_customers():
    """number of customer control setup"""
    if CC.venue.days % 5 == 0:
        CC.customers.customers_number *= (90 - CC.venue.days)/100

def game_over():
    """the page that player will see if they lose or exit via ctrl + c"""
    clear_screen()
    tprint("\n\nGood bye\n\n", font= "tarty1")
    print("Sorry to see you go. Hope to meet you soon again!\n\n")
