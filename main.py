#importing choice(). This allows us to 
#get a random selection of responses
from random import choice

def get_bot_response(user_response) :
    sweets = ['Ice Cream', 'Chocolate', 'Cake']
    salty = ['Chips', 'Popcorn', 'Cheese & Crackers']
    fruits = ['Bananas', 'Strawberries', 'Grapes']
    drinks = ['Water', 'Tea', 'Hot Chocolate']
    quick_meals = ['Mac & Cheese', 'Ramen', 'Salad']
    soups = ['Tomato Soup', 'Chicken Noodle Soup', 'Brocolli Cheddar Soup']

    if user_response == "sweet food":
        return choice(sweets)
    elif user_response == "salty food":
        return choice(salty)
    elif user_response == "healthy food":
        return choice(fruits)
    elif user_response == "beverage":
        return choice(drinks)
    elif user_response == "meals":
        return choice(quick_meals)
    elif user_response == "soup":
        return choice(soups)
    else:
        return "That's not an option we offer. Please try option or type 'done' to quit."
    

print("Welcome to the Mood Market Bot Assistant!")