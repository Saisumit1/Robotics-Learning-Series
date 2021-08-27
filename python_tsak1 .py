import random as r

# user input
over = int(input("Enter number of overs : "))
comp_score = r.randint(1,over*36)
print(f"Computer has scored {comp_score} runs. Your target {comp_score+1} runs")

# playing with user
def find_user_score(over,comp_score):
    user_score = 0
    for i in range(over):
        for j in range(6):
            if user_score <= comp_score:
                print(f"\nOver {i+1} Ball {j+1}")
                bat = int(input("Enter number to bat : "))
                while bat not in range(1,7):
                    bat = int(input("Enter number to bat(1-6) : "))
                comp_no = r.randint(1,6)
                print(f"Computer’s number : {comp_no}")
                if bat == comp_no:
                    print(f"Total Runs : {user_score}\nYou are Out")
                    break
                else:
                    user_score += bat
                    print(f"Total Runs : {user_score}")
            else:
                break
        if bat == comp_no or user_score > comp_score:
            break
    return user_score

user_score = find_user_score(over,comp_score)

# printing the winner
if user_score > comp_score:
    print("\nYou Won the game")
elif user_score < comp_score:
    print("\nComputer Won the game")
else:
    print("\nMatch draw...")                      