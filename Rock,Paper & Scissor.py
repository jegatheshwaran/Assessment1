user1_input = int(input("user1_input:"))
user2_input = int(input("user2_input:"))
game = ['Rock','Paper','Scissors']
3
if user1_input >=3 or user1_input <0:
    print("Enter valid from input1,Enter values between 0,1,2")
if user2_input >=3 or user2_input <0:
    print("Enter valid input2,Enter values between 0,1,2")

else:
    if user1_input == 0 and user2_input == 2:
        print("user1 wins the game")
    elif user2_input == 0 and user1_input == 2:
        print("user2 wins the game")
    elif user1_input > user2_input:
        print("user1 wins the game")
    elif user2_input > user1_input:
        print("user2 wins the game")
    elif user1_input == user2_input:
        print("Match tie in-between both users")


