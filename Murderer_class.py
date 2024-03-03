import random

class Murderer:
    def __init__(self, characterList, roomList, weaponList):
        self.characterlist = characterList
        self.roomList = roomList
        self.weaponList = weaponList

    def chooseMurdererName(self):
        self.murdererName = random.choice(self.characterlist)
        
    
    def chooseMurderRoom(self):
        self.murderRoom = random.choice(self.roomList)
    
    def chooseMurderWeapon(self):
        self.murderWeapon = random.choice(self.weaponList)
    
    def revealMurderer(self):
        print(f"It was {self.murdererName} in the {self.murderRoom} with the {self.murderWeapon}")

characterList = ["Mrs White", "Miss Scarlet", "Miss Peacock", "Professor Plum", "Colnel Mustard", "Reverand Green"]
roomList = ["Garage", "Dining Room", "Bathroom", "Conservatory", "Bedroom", "Study", "Fountain", "Living Room"]
weaponList = ["Lead Pipe", "Rope", "Candlestick", "Revolver", "Spanner", "Dagger"]

murder = Murderer(characterList, roomList, weaponList)
murder.chooseMurdererName()
murder.chooseMurderRoom()
murder.chooseMurderWeapon()
murder.revealMurderer()