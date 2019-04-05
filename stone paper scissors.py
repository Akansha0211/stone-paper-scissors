import random
print("Winning rules for Stone ,paper and scissors game are as followe:\n "+"Stone Vs Paper-> Paper wins\n"+ "Paper Vs Scissors ->Scissors win\n"+"Stone Vs Scissors->Stone wins")
while True:
    print("your choice")
    print("i.e Enter \n"+"1 for  Stone \n"+"2 for Paper\n"+"3 for Scissors")
    n=int(input("Enter 1,2 or 3"))
    if n==1:
        your_choice="Stone"
    if n==2:
        your_choice="Paper"
    if n==3:
        your_choice="Scissors"
    print("now computer chance")
    p=random.choice([1,2,3])
    print(p)
    if p==1:
        computer_choice="Stone"
    elif p==2:
        computer_choice="Paper"
    elif p==3:
        computer_choice="Scissors"
    if n==1 and p==1 or n==2 and p==2 or n==3 and p==3:
        print("Match tie")
    elif n==1 and p==2:
        print("You chose:",your_choice)
        print("Computer choose:",computer_choice)
        print("Computer win")
    elif n==1 and p==3:
        print("You choose:",your_choice)
        print("computer choice:",computer_choice)       
        print("You win")
    elif n==2 and p==1:
        print("You choose:",your_choice)
        print("Computer choose:",computer_choice)
        print("You win")
    elif  n==2  and p==3:
        print("You choose:",your_choice)
        print("Computer choose",computer_choice)
        print("Computer win")
    elif n==3 and p==1:
        print("You choose:",your_choice)
        print("computer choose:",computer_choice)
        print("Computer win")
    elif n==3 and p==2:
        print("You choose:",your_choice)
        print("Computer choose:",compute_choice)
        print("Computer  win")
    print("want to play again")
    print("If so enter Yes or No")
    i=int(input("Enter  1 for Yes\n"+ "2 for No"))
    if i==2:
        break
print("Thanks for playing")


        
