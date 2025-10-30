import random
num = ["stone",
       "paper",
       "scissor"]

print("Welcome to Stone-Paper-Scissor Game!")

def sps_game():
    random_choose = random.choice(num)

    your_input = input("Enter your choice (stone, paper, scissor or 'q' to quit): ").lower()

    if your_input == "q":
            print("Thanks for playing! Goodbye!")
            quit()
    elif your_input not in num:
        print("Invalid input! Please enter stone, paper, or scissor.")
        return sps_game()
    
    def main_game():
        if(your_input == random_choose):
            print(f"It's a tie! Both chose {your_input}.")
        elif(your_input == "paper" and random_choose == "stone" or your_input == "scissor" and random_choose == "paper" or your_input == "stone" and random_choose == "scissor"):
            print("You Win!")
        else:
            print("You Lose!")
    print(f"Computer chose: {random_choose}")
    main_game()
    return sps_game()

sps_game()
