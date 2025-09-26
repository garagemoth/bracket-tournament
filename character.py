import random

introductions = [
    "I'm ready to win this!",
    "You're gonna bite the dust!",
    "Let's get ready to rumble!",
    "Oh, get ready to bite the ground!",
    "Let's do our best!"
]

class Character:
    def __init__(self, name, strength, luck):
        self.name = name
        self.strength = strength
        self.luck = luck

    def introduce(self):
        introList = introductions.copy()
        chosenIntro = random.choice(introList)
        introList.remove(chosenIntro)
        print(f"\"{chosenIntro}\"\n")

    def powerCheck(self):
        print(f"{self.name}'s strength: {self.strength}")
        print(f"{self.name}'s luck: {self.luck}\n")

    def declareWinner(self):
        print(f"And... the winner is... {self.name}!")
        print(f"Let's give them a HUGE round of applause.\n")