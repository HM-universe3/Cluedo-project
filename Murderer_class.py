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
        
characterList = ["Miss Peacock", "Colnel Mustard", "Professor Plum", "Reverand Green", "Mrs White", "Miss Scarlet"]
roomList = ["Garage", "Bathroom", "Bedroom", "Dining room", "Fountain", "Greenhouse", "Living room", "Office"]
weaponList = ["Lead pipe", "Rope", "Candlestick", "Revolver", "Spanner", "Dagger"]

murder = Murderer(characterList, roomList, weaponList)
