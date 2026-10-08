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

answer2 = input("do you like a short game (A) a mediame length game (B) or along game (C)")
if answer2 == "A":
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
