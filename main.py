#importing choice(). This allows us to get a random selection of responses
from random import choice

#Description of Mood Bot
print("Welcome to the Mood Market!")
print('The Mood Bot Assistant 🤖 is here to help you pick you food depending on what type of food your mood is craving today!')
print("Here are your options of food types today: ") 
#Food options to choose from. Enter without emojis
print("🍰 sweet food 🍰")
print("🍿 salty food 🍿")
print("🍓 healthy food 🍓")
print("🍵 beverage 🍵")
print("🍜 warm meal 🍜")
print("🍲 hot soup 🍲")

#Created function get_bot_response()
def get_bot_response(user_response) :

    #List of different food options
    sweets = ['🍦 Ice Cream 🍦', '🍫 Chocolate 🍫', '🍰 Cake 🍰']
    salty = ['🥨 Pretzels 🥨', '🍿 Popcorn 🍿', '🧀 Cheese & Crackers 🧀']
    fruits = ['🍌 Bananas 🍌', '🍓 Strawberries 🍓', '🍇 Grapes 🍇']
    drinks = ['💧 Water 💧', '🍵 Tea 🍵', '☕️ Hot Chocolate ☕️']
    quick_meals = ['🧈 Mac & Cheese 🧈 ', '🍜 Ramen 🍜', '🥪Grilled Cheese🥪']
    soups = ['🍅 Tomato Soup 🍅', '🍗 Chicken Noodle Soup 🍗', '🍲 Brocolli Cheddar Soup 🍲']

    #conditionals for user response which then retrives a random food from their selected food choice
    if user_response == "sweet food":
        return f'You should have {choice(sweets)}'
    elif user_response == "salty food":
        return f'You should have {choice(salty)}'
    elif user_response == "healthy food":
        return f'You should have {choice(fruits)}'
    elif user_response == "beverage":
        return f'You should have {choice(drinks)}'
    elif user_response == "warm meal":
        return f'You should have {choice(quick_meals)}'
    elif user_response == "hot soup":
        return f'You should have {choice(soups)}'
    else:
        return ('Please enter one of the options listed above or enter "done" to exit')
    
#Stores user input
user_response =''
while True:
    user_response = input("Please choose the food your mood is craving: ")
    #Breaks the code when user types done
    if user_response == 'done':
        break
    
    print(get_bot_response(user_response))
