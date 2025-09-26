from character import Character
import random
import math
import os

os.system('cls' if os.name == 'nt' else 'clear')

while True:
    try:
        num_players = int(input("How many players will join the tournament? (Only powers of 2 | ex. 2, 4, 8, 16)\n> "))
        if num_players > 0 and math.log2(num_players) % 1 == 0:
            break
        else:
            print("The number of players must be a power of 2 | ex. 2, 4, 8, 16\n")
    except ValueError:
        print("Invalid input.\n")

availableCharacters = []
for i in range(num_players):
    name = input(f"Enter the name of the player {i+1}: ")
    strength = random.randint(1, 10)
    luck = random.randint(1, 6)
    availableCharacters.append(Character(name, strength, luck))

num_rounds = int(math.log2(len(availableCharacters)))

winners = []
losers = []
fighter1 = None
fighter2 = None

def fight():
        print("=============================================")
        print(f"  First up in our ring... we have {fighter1.name}!")
        print("=============================================\n")
        fighter1.introduce()
        print("=============================================")
        print(f"      Second up... we have {fighter2.name}!")
        print("=============================================\n")
        fighter2.introduce()
        print("=============================================")
        print(" Here are the stats of each of our players!")
        print("=============================================\n")
        fighter1.powerCheck()
        fighter2.powerCheck()
        fighter1Power = fighter1.strength * fighter1.luck
        fighter2Power = fighter2.strength * fighter2.luck

        print("=============================================")
        print("               Let's fight!!!")
        print("=============================================\n")
        if fighter2Power > fighter1Power:
            fighter2.declareWinner()
            winners.append(fighter2)
            losers.append(fighter1)
        elif fighter2Power < fighter1Power:
            fighter1.declareWinner()
            winners.append(fighter1)
            losers.append(fighter2)
        else:
            winner = random.choice([fighter1, fighter2])
            loser = fighter1 if winner == fighter2 else fighter2
            winners.append(winner)
            losers.append(loser)
            print(f"It looks like they tied! We're gonna go off of the audience vote!")
            print(f"The results are in... the people want {winner.name}!]")
            print(f"Congrats! Let's give them a HUGE round of applause.\n")
        ready = input("Press enter to continue the tournament")
        print()

def declareWinners():
    print("                  Results!")
    print("=============================================\n")
    print(f"Winner/s: {', '.join(i.name for i in winners)}\n")
    print(f"Loser/s: {', '.join(i.name for i in losers)}\n")

def cleanStart():
    for i in winners:
        availableCharacters.append(i)
    winners.clear()
    losers.clear()

def fightStart():
    global fighter1
    global fighter2
    while len(availableCharacters) > 1:
        fighter1 = random.choice(availableCharacters)
        availableCharacters.remove(fighter1)
        fighter2 = random.choice(availableCharacters)
        availableCharacters.remove(fighter2)
        fight()

print()
for i in range(1, num_rounds):
    fightStart()
    if len(availableCharacters) == 1:
        winners.append(availableCharacters.pop())
    print("=============================================")
    print(f"                   Round {i}")
    declareWinners()
    cleanStart()
    ready = input("Press enter to continue into the next round")
    print()

if len(availableCharacters) == 2:
    fighter1 = availableCharacters.pop()
    fighter2 = availableCharacters.pop()
    fight()
    print("=============================================")
    print("                 FINAL ROUND")
    declareWinners()
    final_winner = winners[0]
else:
    final_winner = availableCharacters[0]

print("=====================================================\n")
print(f"          And our winner is... {final_winner.name}")
print(f" Congratulations, and thank you everyone for coming!")
print("  That's all for today and we'll see you next time!\n")
print("=====================================================\n")