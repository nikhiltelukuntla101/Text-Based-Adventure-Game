import time

def print_with_delay(message, delay=1.5):
    """Prints a message with a delay for better storytelling."""
    print(message)
    time.sleep(delay)

def start_game():
    print_with_delay("Welcome to the Mysterious Forest Adventure!")
    print_with_delay("You find yourself at the edge of a dark forest.")
    print_with_delay("There is a path leading into the forest and a small cabin nearby.")
    choice1()

def choice1():
    print("\nWhat would you like to do?")
    print("1. Enter the forest.")
    print("2. Explore the cabin.")
    choice = input("Enter 1 or 2: ").strip()
    
    if choice == "1":
        enter_forest()
    elif choice == "2":
        explore_cabin()
    else:
        print_with_delay("Invalid choice. Please try again.")
        choice1()

def enter_forest():
    print_with_delay("\nYou cautiously step into the forest.")
    print_with_delay("The trees are tall and the path is barely visible.")
    print("\nWhat would you like to do?")
    print("1. Follow the path deeper into the forest.")
    print("2. Look around for something unusual.")
    choice = input("Enter 1 or 2: ").strip()
    
    if choice == "1":
        deeper_forest()
    elif choice == "2":
        find_treasure()
    else:
        print_with_delay("Invalid choice. Please try again.")
        enter_forest()

def explore_cabin():
    print_with_delay("\nYou approach the small cabin.")
    print_with_delay("The door is slightly ajar. Inside, it’s dark and silent.")
    print("\nWhat would you like to do?")
    print("1. Enter the cabin.")
    print("2. Knock on the door.")
    choice = input("Enter 1 or 2: ").strip()
    
    if choice == "1":
        cabin_inside()
    elif choice == "2":
        knock_door()
    else:
        print_with_delay("Invalid choice. Please try again.")
        explore_cabin()

def deeper_forest():
    print_with_delay("\nYou follow the path deeper into the forest.")
    print_with_delay("Suddenly, you hear a growl behind you...")
    print_with_delay("A wolf appears!")
    print("\nWhat would you like to do?")
    print("1. Run!")
    print("2. Stand your ground.")
    choice = input("Enter 1 or 2: ").strip()
    
    if choice == "1":
        print_with_delay("\nYou run as fast as you can and escape the wolf. You survive!")
    elif choice == "2":
        print_with_delay("\nYou stand your ground and scare the wolf away. Brave choice!")
    else:
        print_with_delay("Invalid choice. Please try again.")
        deeper_forest()

def find_treasure():
    print_with_delay("\nYou look around and notice something shiny under a bush.")
    print_with_delay("It's a treasure chest!")
    print("\nWhat would you like to do?")
    print("1. Open the chest.")
    print("2. Leave it alone.")
    choice = input("Enter 1 or 2: ").strip()
    
    if choice == "1":
        print_with_delay("\nThe chest is full of gold and jewels! You’re rich!")
    elif choice == "2":
        print_with_delay("\nYou decide to leave the treasure for someone else. How noble!")
    else:
        print_with_delay("Invalid choice. Please try again.")
        find_treasure()

def cabin_inside():
    print_with_delay("\nYou enter the cabin and find a table with a mysterious map.")
    print_with_delay("The map leads to a hidden treasure in the forest.")
    print_with_delay("You take the map and begin your journey. Adventure awaits!")

def knock_door():
    print_with_delay("\nYou knock on the door, but no one answers.")
    print_with_delay("Suddenly, the wind blows the door open...")
    print_with_delay("Inside, you find an old diary with clues about the forest!")
    print_with_delay("You take the diary and start exploring. Exciting times ahead!")

# Start the game
start_game()
