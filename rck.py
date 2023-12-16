import random
choice=("rock","paper","scissor")
running=True

while running:
    user=None
    cpu=random.choice(choice)

    while user not in choice:
        user=input("Enter rock/paper/scissor: ")
    print(f"User: {user}")
    print(f"Cpu: {cpu}")

    if user==cpu:
        print("It's a Tie! ")
    elif user=="rock" and cpu=="scissor":
       print("You win! ")
    elif user=="paper" and cpu=="rock":
        print("You win! ")
    elif user=="scissor" and cpu=="paper":
        print("You win!")
    else:
        print("You lose! ")
    if not input("Play again? Yes/No: ").lower()=="yes":
        running=False

print("The end!")
