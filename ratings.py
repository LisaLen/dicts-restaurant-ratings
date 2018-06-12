"""Restaurant rating lister."""
import sys

from random import choice

def  dict_construct(file_name):
    restaurants_dict = {}
    for line in open(file_name):
        words = line.rstrip().split(':')
        restaurants_dict[words[0]] = words[1]
    return restaurants_dict

def print_restaurant_alph(dictionary):
    for key, values in sorted(dictionary.items()):
        print("{} is rated at {}.".format(key, values))

def add_new_restaurant(dictionary):

    rest_name = input("Enter new restaurant name: ")

    while True: 
        rest_score = int(input("Enter new restaurant score: "))
        if  rest_score > 5 or rest_score < 1:
            print('Please enter a score between 1 and 5')
        else: 
            break

    dictionary[rest_name] = rest_score
    return dictionary

def pick_random_restaurant(dictionary):
    keys_dict = list(dictionary.keys())
    random_rest = choice(keys_dict)

    return random_rest

def update_rest_rating(dictionary, random_rest):
    new_rating = int(input('What is the new rating for {}: '.format(random_rest)))
    dictionary[random_rest] = new_rating
    return dictionary


def user_choice():
    print("\n")
    print(' Here are the things you can do:')
    print('1 - to see all the ratings')
    print('2 - add new restaurant')
    print('3 - update random restaurant\'s rating')
    print ('q - quitting')

    choice = input('> ')
    return choice


file_name = sys.argv[1]

while True:

    choice = user_choice()
    restaurants_dict = dict_construct(file_name)
    lst = list(restaurants_dict.keys())
    print(lst)

    if choice == "1":
        print("\n")
        print_restaurant_alph(restaurants_dict)

    elif choice == "2":
        add_new_restaurant(restaurants_dict)
        print("\n")
        print_restaurant_alph(restaurants_dict)

    elif choice == '3':
        random_rest = pick_random_restaurant(restaurants_dict)
        print(type(random_rest))
        print('Your randomly chosen restaurant is {}'.format(random_rest))
        restaurants_dict = update_rest_rating(restaurants_dict, random_rest)
        print_restaurant_alph(restaurants_dict)

    elif choice == "q": break
    else: 
        print("\n")
        print('Please enter a valid choice')






# print(sorted(dict_construct(file_name).items()))


# put your code here
