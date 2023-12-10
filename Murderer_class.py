import random

class Murderer:
    def __init__(self, characterList, roomList, weaponList):
        self.characterlist = characterList
        self.roomList = roomList
        self.weaponList = weaponList

    def chooseMurdererName(self):
        self.murdererName = random.choice(self.characterlist)
        return self.murdererName
    
    def chooseMurderRoom(self):
        self.murderRoom = random.choice(self.roomList)
    
    def chooseMurderWeapon(self):
        self.murderWeapon = random.choice(self.weaponList)
        
