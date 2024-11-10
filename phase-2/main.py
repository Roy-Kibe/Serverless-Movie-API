import requests
from functions import menu, search_by_title, search_by_year


while True:
    menu()
    console = input("Please choose a number from the menu: ")
    if console == '1':
        search_by_title()
    elif console == '2':
        search_by_year()
    elif console == '4':
        print("Exiting")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
