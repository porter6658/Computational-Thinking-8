football_points = 0
baseball_points = 0
soccer_points = 0

answer1 = input("do you perfer a slow paced game (A) fast paced game (B) or medium paced game (C)")
if answer1 == "A":
    football_points += 1
elif answer1 == "B":
    soccer_points += 1
elif answer1 == "c":
    baseball_points += 1

answer2 = input("do you like a short game (A) a mediame length game (B) or a long game (C)")
if answer2 == "A" or "a":
    football_points += 1
elif answer2 == "B":
    soccer_points += 1
elif answer2 == "c":
    baseball_points += 1
    
answer3 = input("do you like a game with alot of players (A) a game with not alot of players (B) or a game with a normal amount of players (C)")
if answer3 == "A":
    football_points += 1
elif answer3 == "B":
    soccer_points += 1
elif answer3 == "c":
    baseball_points += 1

answer4 = input("do you like a medieam hard game to learn (A) an easy game to learn (B) or a hard game to lear (C)")
if answer4 == "A":
    football_points += 1
elif answer4 == "B":
    soccer_points += 1
elif answer4 == "c":
    baseball_points += 1 

answer5 = input(" do you like a physical game (A) a meadiam physical game (B) or a not physical gaem (C)")
if answer5 == "A":
    football_points += 1
elif answer5 == "B":
    soccer_points += 1
elif answer5 == "c":
    baseball_points += 1 
    
if football_points > soccer_points and football_points > baseball_points:
    print("you are a football person") 
elif soccer_points > football_points and soccer_points > baseball_points:
    print("You are soccer person") 
elif baseball_points > football_points and baseball_points > soccer_points:
    print("you are a baseball person")
