# simply displays game title
def game_title():
    print("MADLIBS: HERO EDITION")



# game logic 
# we import count from main so it does not reset to 0 when function calls each time
def play_story(count):
    username = input(" What is your name: ")
    choice = input(f"Hello {username}, pick a story: \na) spy mission \nb) dragonball  \nyour choice:  ")

    print("Tell me a little about yourself")

    # story details
    character = input("pick a name: ")
    friend = input("pick a friend's name: ")
    adjective = input("pick an adjective: ")
    verb = input("pick a verb ending with -ing.. ")
    animal = input("Pick an animal...")
    species = input("pick a species: ")
    rival = input("pick a rival's name: ")
    country = input("pick a country: ")
    weapons = input("pick a weapon: ")
    
    # choice that triggers story with user's chosen details

    # option 1
    if choice == "a" or choice == "spy" or choice == "spy mission":
        print(f"\n \nWelcome {character}. \nhow are you brave soldier? \na fire has broken out near {rival}'s headquarters. You have been hired by the {country} special unit to inspect a mission critical situation. \nWe have equipped you with magic {weapons}. \nYour guide for this journey is a rare mindreading {species} breed named {friend}. \nUnfortunately only one of you can come back.\n")
        count += 1 # increments count if chosen
    # option 2
    elif choice == "b" or choice == "dragonball":
        print(f"Breaking News! Freeza's broken out of hell again and Goku and Vegeta are busy fighting a universe-level threat. {character}, you are Earth's last hope. King Kai says you're the next best {adjective} {verb} {animal} warrior! I provided you with a senzu bean so you can start off fully recovered. Goodbye!")
        count += 1 # increments count if chosen
    # error handling
    else:
        print("invalid option. try again")
        return count # returns current count
    
    # outside of the if statement
    # tells us amount of stories created with count
    print(f"You've created {count} stories so far!")
    return count # returns total count

# runs our "global" logic
def main():
    game_title()
    count = 0 # memory storage for count

    playing = input("Would you like to play? y/n: ")

    # if y or yes for play again, 
    # count goes from 0 to whatever increments in play_story function logic?
    while playing == "y" or playing == "yes":
        count = play_story(count) # updates count
        playing = input("Do you want to play again? y/n: ") # this is how the loop runs again if we type in y or yes or terminates if that is untrue
    
    print(f"Thanks for playing! You created {count} stories")

if __name__ == "__main__":
    main()