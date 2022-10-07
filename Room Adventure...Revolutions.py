#######################################################
# Name: Jacob Craver
# Date: 04/15/20
# Decription: Room Adventure...Revolutions Program
# Python Version: 2.7.16
#######################################################

# Improvements:
#   - More rooms (3x3x2)
#   - Three dimensional mansion (stairs in room 5)
#   - More items with descriptions
#   - More grabbables
#   - Added puzzles to open doors with keys
#   - Added that some grabbables can be used as weapons
#   - Added that weapon grabbables are a one time use (except lasergun)
#   - Added enemies and combat with weapons
#   - Added item descriptions when grabbables are used as weapons
#   - Added score for defeating enemies
#   - Added 3 lives that are lost if you do not fight enemies
#   - Added map with basic layout of the mansion
#   - Added cheats
#   - Added GUI with individual pictures that change with each room

# Helpful Tips:
#   - Type "use 'item'/'grabbable'" to use items or weapons on things in the current room such as doors or enemies
#   - Not all doors open with a key specifically
#   - Any kind of key cannot be used as a weapon
#   - You can escape the mansion through the final door

# CHEATS:
#   - To activate CHEATS to explore more freely, type: "use cheats"

from Tkinter import *

score = 0 # score variable
lives = 3 # lives variable
  
class Room(object):
    def __init__(self, name, image):
        self.name = name
        self.image = image
        self.exits = {}
        self.items = {}
        self.grabbables = []
        self.enemies = []

    # accessors and mutators for everything
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    @property
    def enemies(self):
        return self._enemies

    @enemies.setter
    def enemies(self, value):
        self._enemies = value

    # end of accessors and mutators
    # some helper functions

    def addExit(self, exit, room):
        # append the exit and room to the appropriate lists
        self._exits[exit] = room

    def addItem(self, item, desc):
        # append the item and description to the appropriate lists
        self._items[item] = desc

    def addGrabbable(self, item):
        # append the item to the list
        self._grabbables.append(item)

    def delGrabbable(self, item):
        # remove the item from the list
        self._grabbables.remove(item)

    # adds an enemy to a room
    def addEnemy(self, enemy):
        self._enemies.append(enemy)
        
    # deletes an enenmy from a room
    def delEnemy(self, enemy):
        self._enemies.remove(enemy)

    # returns a string description of the room
    def __str__(self):

        # display game map
        s = "Floor 1"
        s += "\n################"
        s += "\n# 01 # 02 # 03 #"
        s += "\n################"
        s += "\n# 04 # ^^ # 06 #"
        s += "\n################"
        s += "\n# 07 # 08 # 09 #"
        s += "\n################"
        s += "\n\nFloor 2"
        s += "\n################"
        s += "\n# 10 # 11 # 12 #"
        s += "\n################"
        s += "\n# 13 # 14 # 15 #"
        s += "\n################"
        s += "\n# 16 # 17 # 18 #"
        s += "\n################"
        s += "\n\nHint: ^^ = stairs"
        
        # first, the room name
        s += "\n\nYou are in {}.\n".format(self.name)

        # next, the items in the room
        s += "You see: "
        for item in self.items.keys():
            s += item + ", "

        s += "\n\nEnemies: "
        for enemy in self.enemies:
            s += enemy + ", "
            
        s += "\nScore: {}".format(score)
        s += "\nLives: {}".format(lives)

        # next, the exits from the room
        s += "\n\nExits: "
        for exit in self.exits.keys():
            s += exit + ", "

        return s

#######################################################

class Game(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

    # function that creates the rooms
    def createRooms(self):
        
        # r1 through r18 are the 18 rooms in the mansion

        global currentRoom # currentRoom is the room the player is currently in

        # creates the rooms and gives them names
        r1 = Room("Room 1", "room1.gif")
        r2 = Room("Room 2", "room2.gif")
        r3 = Room("Room 3", "room3.gif")
        r4 = Room("Room 4", "room4.gif")
        global r5
        r5 = Room("Room 5", "room5.gif")
        r6 = Room("Room 6", "room6.gif")
        r7 = Room("Room 7", "room7.gif")
        r8 = Room("Room 8", "room8.gif")
        r9 = Room("Room 9", "room9.gif")
        r10 = Room("Room 10", "room10.gif")
        r11 = Room("Room 11", "room11.gif")
        global r12
        r12 = Room("Room 12", "room12.gif")
        r13 = Room("Room 13", "room13.gif")
        global r14
        r14 = Room("Room 14", "room14.gif")
        r15 = Room("Room 15", "room15.gif")
        r16 = Room("Room 16", "room16.gif")
        global r17
        r17 = Room("Room 17", "room17.gif")
        r18 = Room("Room 18", "room18.gif")
        
        # adds exits, items, item descriptions, enemies, and grabbables to the rooms
        # floor 1
        r1.addExit("south", r4)
        r1.addExit("east", r2)
        r1.addItem("chair", "It's made of wicker, and no one is sitting on it.")
        r1.addItem("table", "It's made of oak. A silver key rests on it, but it is broken and useless.")
        
        r2.addExit("south", r5)
        r2.addExit("east", r3)
        r2.addExit("west", r1)
        r2.addItem("rug", "It's nice and Indian. It also needs to be vaccuumed.")
        r2.addItem("fireplace", "It's full of 'ashes'.")
        r2.addEnemy("spider")
        r2.addGrabbable("ashes")

        r3.addExit("south", r6)
        r3.addExit("west", r2)
        r3.addItem("bookshelves", "They are empty. Go figure.")
        r3.addItem("statue", "There is nothing special about it, and it is too big to carry.")
        r3.addItem("desk", "The statue is resting on it. So is a 'book'.")
        r3.addGrabbable("book")

        r4.addExit("north", r1)
        r4.addExit("east", r5)
        r4.addExit("south", r7)
        r4.addItem("bed", "It's a water bed. How neat.")
        r4.addItem("chest", "It's metal and has a 'knife' in it.")
        r4.addEnemy("rat")
        r4.addGrabbable("knife")

        r5.addExit("north", r2)
        r5.addExit("south", r8)
        r5.addExit("east", r6)
        r5.addExit("west", r4)
        r5.addItem("door", "It's locked and has a silver keyhole.") # locked door to the second level

        r6.addExit("north", r3)
        r6.addExit("south", r9)
        r6.addExit("west", r5)
        r6.addItem("counter", "It's linoleum and has a nothing on it.")
        r6.addItem("fridge", "It's stainless steel and has an 'apple' in it.")
        r6.addEnemy("snake")
        r6.addGrabbable("apple")

        r7.addExit("north", r4)
        r7.addExit("east", r8)
        r7.addItem("television", "It's turned on. It's showing the News Channel.")
        r7.addItem("couch", "It's leather and it has a 'remote' on it.")
        r7.addGrabbable("remote")

        r8.addExit("north", r5)
        r8.addExit("south", None) # going south in room 8 will kill you
        r8.addExit("east", r9)
        r8.addExit("west", r7)
        r8.addItem("dresser", "It's old and has a 'lockpick' in it.")
        r8.addItem("mirror", "It's glass. Dang, you lookin' fly today.")
        r8.addItem("window", "If you went south through this window, the fall would kill you!")
        r8.addGrabbable("lockpick") # key to the first door

        r9.addExit("north", r6)
        r9.addExit("west", r8)
        r9.addItem("washer", "It's empty.")
        r9.addItem("dryer", "It's turned off. It has 'towel' in it.")
        r9.addGrabbable("towel")
        
        # floor 2
        r10.addExit("south", r13)
        r10.addExit("east", r11)
        r10.addItem("toolbox", "Surprisingly, it has no tools in it. How helpful...")
        r10.addItem("garden", "It's overgrown with weeds. It has a 'shovel' next to it.")
        r10.addEnemy("zombie")
        r10.addEnemy("scorpion")
        r10.addGrabbable("shovel")

        r11.addExit("south", r14)
        r11.addExit("east", r12)
        r11.addExit("west", r10)
        r11.addItem("chair", "It's a folding chair and is not very sturdy.")
        r11.addItem("balcony", "It's made of brick, and it has a 'stick' on it.")
        r11.addEnemy("gargoyle")
        r11.addEnemy("wraith")
        r11.addGrabbable("stick")

        r12.addExit("south", r15)
        r12.addExit("west", r11)
        r12.addItem("recliner", "It's made of cloth, and nothing is on it.")
        r12.addItem("safe", "It's made of steel, and it has a keypad on it. If only you had the code...") # locked safe contains the key to the second door

        r13.addExit("north", r10)
        r13.addExit("south", r16)
        r13.addExit("east", r14)
        r13.addItem("floor", "It's made of tile and is very clean.")
        r13.addItem("table", "It's made of spruce, and it has a small 'radio' on it.")
        r13.addEnemy("skeleton")
        r13.addEnemy("bat")
        r13.addGrabbable("radio")
        
        r14.addExit("north", r11)
        r14.addExit("south", r17)
        r14.addExit("east", r15)
        r14.addExit("west", r13)
        r14.addItem("door", "It's locked permanently. It does not appear that you can get back downstairs.") # permanently locked door to the first level

        r15.addExit("north", r12)
        r15.addExit("south", r18)
        r15.addExit("west", r14)
        r15.addItem("chair", "It's made of wicker, and no one is sitting on it.")
        r15.addItem("table", "It's made of oak. A 'spoon' rests on it.")
        r15.addEnemy("ghost")
        r15.addEnemy("centipede")
        r15.addGrabbable("spoon")

        r16.addExit("north", r13)
        r16.addExit("east", r17)
        r16.addItem("painting", "It's a painting of an old man. His eyes seem to follow you.")
        r16.addItem("crack", "There is a crack in the wall. There is a hidden compartment behind it with a secret 'code' in it.")
        r16.addGrabbable("code") # key to the safe

        r17.addExit("north", r14)
        r17.addExit("east", r18)
        r17.addExit("west", r16)
        r17.addItem("door", "It's locked and has a golden keyhole.") # locked door you must go through to complete the game
        
        r18.addExit("north", r15)
        r18.addExit("west", r17)
        r18.addItem("disco-floor", "It's made of flashing lights, and it makes you want to party.")
        r18.addItem("wall", "It's just a wall, but it has a 'lasergun' mounted on it!!!")
        r18.addEnemy("robot")
        r18.addEnemy("cyborg")
        r18.addEnemy("android")
        r18.addGrabbable("lasergun")

        # set room 1 as the current room at the beginning of the game
        Game.currentRoom = r1
        Game.inventory = []

    def setUpGui(self):
        self.pack(fill = BOTH, expand = 1)

        # set up entry widget for typing
        Game.player_input = Entry(self, bg = "white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side = BOTTOM, fill = X)
        Game.player_input.focus()

        # set up the image on the left
        img = None
        Game.image = Label(self, width = WIDTH/2, image = img)
        Game.image.image = img
        Game.image.pack(side = LEFT, fill = Y)
        Game.image.pack_propagate(False)

        #set up the text frame on the right
        text_frame = Frame(self, width = WIDTH/2)
        Game.text = Text(text_frame, bg = "lightgrey", state = DISABLED)
        Game.text.pack(fill = Y, expand = 1)
        text_frame.pack(side = RIGHT, fill = Y)
        text_frame.pack_propagate(False)
        

    def setRoomImage(self):
        global lives
        if (Game.currentRoom == None or lives == 0):
            Game.img = PhotoImage(file = "skull.gif")
        else:
            Game.img = PhotoImage(file = Game.currentRoom.image)

        Game.image.config(image = Game.img)
        Game.image.image = Game.img

    def setStatus(self, status):
        global lives
        Game.text.config(state = NORMAL)
        Game.text.delete("1.0", END)
        if (Game.currentRoom == None or lives == 0):
            Game.text.insert(END, "You are dead. All you can do is quit.")
        else:
            Game.text.insert(END, str(Game.currentRoom) + "\nYou are carrying: " + str(Game.inventory) + "\n\n" + status)                           
            Game.text.config(state = DISABLED)

    def play(self):
        #sete up the house
        self.createRooms()

        # sets up the GUI
        self.setUpGui()

        # sets up the image of the current room
        self.setRoomImage()

        # sets up the status
        self.setStatus("")

    def process(self, event):
        action = Game.player_input.get()
        action = action.lower()

        response = "I don't understand. Try verb noun. Valid verbs are go, look, and take."

        if (action in ["quit", "bye", "exit", "sionara"]):
            exit(0)
            return

        if (Game.currentRoom == None):
            Game.player_input.delete(0, END)
                                                                                                                         
        words = action.split()

        if (len(words) == 2):
            verb = words[0]
            noun = words[1]

            if (verb == "go"):
                global score
                global lives
                response = "Invalid Exit"
                # if you leave a room with an enemy still inside it you will lose a life
                if (len(Game.currentRoom.enemies) == 1):
                    lives -= 1
                # if you leave a room with 2 enemies still inside it you will lose 2 lives
                if (len(Game.currentRoom.enemies) == 2):
                    lives -= 2
                # if you leave a room with 3 enemies still inside it you will die instantly
                if (len(Game.currentRoom.enemies) == 3):
                    lives -= 3
                if (noun in Game.currentRoom.exits):
                    Game.currentRoom = Game.currentRoom.exits[noun]
                    response = "Room Changed"

            elif (verb == "look"):
                response = "I don't see that item."
                if (noun in Game.currentRoom.items):
                    response = Game.currentRoom.items[noun]

            elif (verb == "take"):
                response = "I don't see that item."
                for grabbable in Game.currentRoom.grabbables:
                    # a valid grabbable item is found
                    if (noun == grabbable):
                        # add the grabbable item to the player's inventory
                        Game.inventory.append(grabbable)
                        # remove the grabbable item from the room
                        Game.currentRoom.delGrabbable(grabbable)
                        # set the response (success)
                        response = "Item Grabbed"
                        # no need to check any more grabbable items
                        break

            # if the verb is use, the player will use the object indicated by the grabbable noun if the grabbable is in their inventory
            if (verb == "use"):
                global score
                response = "You cannot use that item here."
                if (noun == "lockpick" and Game.currentRoom == r5 and "lockpick" in Game.inventory):
                    Game.currentRoom = r14
                    status = "{}\nYou are carrying: {}\n".format(Game.currentRoom, Game.inventory)
                    response = "This doorway opened an exit upstairs, but the door locked permanently behind you!"
                    score += 100
                    
                if (noun == "code" and Game.currentRoom == r12 and "code" in Game.inventory):
                    Game.inventory.append("key")
                    response = "You got a golden key!"
                    score += 100

                if (noun == "key" and Game.currentRoom == r17 and "key" in Game.inventory):
                    response = "You walk through the door to find a ladder. You climb down and escape to safety...for now. YOU WIN!!! You can continue exploring or quit."
                    
                if (noun == "cheats"):
                    Game.inventory = []
                    Game.inventory.append("lasergun")
                    Game.inventory.append("lockpick")
                    Game.inventory.append("code")
                    Game.inventory.append("key")
                    lives = 1000
                    response = "*CHEATS ENABLED*"

                # if the player uses a grabbable on an enemy:
                # the enemy will die
                # the grbbable used will be removed from their inventory (broken)
                # the player will recieve 100 points
                # a unique response will be displayed for the use of each item
                for enemy in Game.currentRoom.enemies:
                    response = "You cannot use that item for combat."
                    for i in range(len(Game.inventory)):
                        if (noun in Game.inventory):
                                
                            if (noun == "ashes"):
                                Game.currentRoom.delEnemy(enemy)
                                Game.inventory.remove("ashes")
                                score += 100
                                response = "Another one bites the dust. Your ashes are gone!"
                                
                            if (noun == "book"):
                                Game.currentRoom.delEnemy(enemy)
                                Game.inventory.remove("book")
                                score += 100
                                response = "You just schooled your enemy, but your book tore to pieces!"
                                
                            if (noun == "knife"):
                                Game.currentRoom.delEnemy(enemy)
                                Game.inventory.remove("knife")
                                score += 100
                                response = "You stabbed your enemy to death, but your knife broke!"

                            if (noun == "apple"):
                                Game.currentRoom.delEnemy(enemy)
                                Game.inventory.remove("apple")
                                score += 100
                                response = "An apple a day keeps the monsters away...or something like that. Your apple got squashed!"

                            if (noun == "remote"):
                                Game.currentRoom.delEnemy(enemy)
                                Game.inventory.remove("remote")
                                score += 100
                                response = "The remote controls your enemy's mind, and you force your enemy to destroy itself. Your remote ran out of battery!"

                            if (noun == "towel"):
                                Game.currentRoom.delEnemy(enemy)
                                Game.inventory.remove("towel")
                                score += 100
                                response = "You choke your enemy to death with the towel, but it tore to shreds!"

                            if (noun == "shovel"):
                                Game.currentRoom.delEnemy(enemy)
                                Game.inventory.remove("shovel")
                                score += 100
                                response = "You really buried the competition. Your shovel broke!"

                            if (noun == "stick"):
                                Game.currentRoom.delEnemy(enemy)
                                Game.inventory.remove("stick")
                                score += 100
                                response = "You spoke softly and carried a big stick. Your stick broke!"

                            if (noun == "radio"):
                                Game.currentRoom.delEnemy(enemy)
                                Game.inventory.remove("radio")
                                score += 100
                                response = "You challenge your enemy to a dance off and showed it who's boss, but your radio ran out of battery!"

                            if (noun == "spoon"):
                                Game.currentRoom.delEnemy(enemy)
                                Game.inventory.remove("spoon")
                                score += 100
                                response = "Your enemy immediately faints out of fear of seeing the spoon. Weird. Your spoon mysteriously vanishes!"

                            if (noun == "lasergun"):
                                Game.currentRoom.delEnemy(enemy)
                                Game.inventory.remove("lasergun")
                                score += 100
                                response = "Dodge this. Your enemy incinerates with one shot of the lasergun. Your lasergun overheated and is destroyed!"


        # display the response on the right of the GUI
        # display the room's image on the left of the GUI
        # clear the player's input
        self.setStatus(response)
        self.setRoomImage()
        Game.player_input.delete(0, END)

#######################################################

# set defaults for the screen
WIDTH = 800
HEIGHT = 600

# create window
window = Tk()
window.title("Room Adventure...Revolutions")

# create the GUI as a canvas inside the window
g = Game(window)
# play the game
g.play()

# transfer control to the GUI indefinitely
window.mainloop()
