
#Adventure - a simple text adventure game engine.

#####################################################################
# In progress simple text adventure game engine.
# Users create a character, explore a map, pick up items, solve puzzles, kill monsters, talk to NPCs, etc.
# Combat and conversation are works in-progress.
#
# The game world is read in from several text files:
#   Rooms on the map are described in roomsfile.txt
#   Items are described in itemsfile.txt
#   Random noises are described in randomnoisesfile.txt
#
# Current world described by roomsfile.txt, itemsfile.txt, and randomnoisesfile.txt is a simple Haunted House. There is no story line (yet).
#####################################################################


#####################################################################
# Import
import ast
from random import random, randrange
from collections import OrderedDict
#####################################################################

#####################################################################
# Room Construction
#
#Explanation of less obvious attributes:
#   exits are dictionary entries specifying the direction and what location you go to ({'w':4, 'west':4})
#   hiddenExitable means there is a hidden exit (1 or 0 for true or false)
#   hiddenExitFound means the hidden exit has been found or not (1 or 0 for true or false)

class Rooms:
    def __init__(self, roomNumber, name, longDescription, shortDescription, exitDescription, exits, hiddenExitable, hiddenExitFound, hiddenExitFindDescription, hiddenExitDescription, hiddenExits):
        self.roomNumber = roomNumber
        self.name = name
        self.longDescription = longDescription
        self.shortDescription = shortDescription
        self.exitDescription = exitDescription
        self.exits = exits
        self.hiddenExitable = hiddenExitable
        self.hiddenExitFound = hiddenExitFound
        self.hiddenExitFindDescription = hiddenExitFindDescription
        self.hiddenExitDescription = hiddenExitDescription
        self.hiddenExits = hiddenExits

def makeRooms(infoStr):
    roomNumber, name, longDescription, shortDescription, exitDescription, exits, hiddenExitable, hiddenExitFound, hiddenExitFindDescription, hiddenExitDescription, hiddenExits = infoStr.split("//")
    return Rooms(roomNumber, name, longDescription, shortDescription, exitDescription, exits, hiddenExitable, hiddenExitFound, hiddenExitFindDescription, hiddenExitDescription, hiddenExits)
    
def roomSetup():
    roomsfile = "roomsfile.txt"
    infile = open(roomsfile, 'r')
    roomsByName = []
    roomsByName = OrderedDict(roomsByName)
    for line in infile:
        newRoom = makeRooms(line)
        roomsByName[newRoom.name] = newRoom
    infile.close()
    roomsByIndex = list(roomsByName.values())
    return roomsByName, roomsByIndex

# End of Room Construction
#####################################################################

#####################################################################
# Item Construction
# Creates items and places them on the map.
# Explanation of less obvious attributes:
#       itemGettable means an item can be picked up (1 or 0 for true or false)
#       itemDoable means it is usable whether is in the user's inventory or not (1 or 0 for true or false)
#       itemLimited means it has limited number of uses, like a gun with bullets (1 or 0 for true or false)
#       itemUses is the number of times it can be used
#       itemRefillable means it can be re-loaded (1 or 0 for true or false)
#       itemHidden means it is hidden and must be found with a search (1 or 0 for true or false)
#       itemActionRequirements are inventory (has to be in user's inventory), location (item has to be used in particular location, specified by a dictionary entry
#           like {"location":4}), eitherInventoryLocation (item can be used either from inventory, or without picking it up)
#       itemActionTypes are unhideMap, unhideItems, message, changeStats, changeLocation.  These are the effects an item can have.
#       itemActions are verbs specified for that item; these can be anything (shoot for a gun, use, drink for a bottle)
#

class Items:
    def __init__(self, itemID, itemName, itemLocation, itemLocationOriginal, itemFriendlyLocation, itemLongDescription, itemShortDescription, itemLocationOriginalDesc, itemDroppedDescription, itemGettable, itemDoable, itemLimited, itemUses, itemRefillable, itemHidden, itemActions, itemActionRequirements, itemActionType, itemActionUseSuccessDescription, itemActionUseFailDescription, itemActionOutcomeDescSuccess, itemActionOutcomeDescFailure):
        self.itemID = itemID
        self.itemName = itemName
        self.itemLocation = itemLocation
        self.itemLocationOriginal = itemLocationOriginal
        self.itemFriendlyLocation = itemFriendlyLocation
        self.itemLongDescription = itemLongDescription
        self.itemShortDescription = itemShortDescription
        self.itemLocationOriginalDesc = itemLocationOriginalDesc
        self.itemDroppedDescription = itemDroppedDescription
        self.itemGettable = itemGettable
        self.itemDoable = itemDoable
        self.itemLimited = itemLimited
        self.itemUses = itemUses
        self.itemRefillable = itemRefillable
        self.itemHidden = itemHidden
        self.itemActions = itemActions
        self.itemActionRequirements = itemActionRequirements
        self.itemActionType = itemActionType
        self.itemActionUseSuccessDescription = itemActionUseSuccessDescription
        self.itemActionUseFailDescription = itemActionUseFailDescription
        self.itemActionOutcomeDescSuccess = itemActionOutcomeDescSuccess
        self.itemActionOutcomeDescFailure = itemActionOutcomeDescFailure

def makeItems(infoStr):
    itemID, itemName, itemLocation, itemLocationOriginal, itemFriendlyLocation, itemLongDescription, itemShortDescription, itemLocationOriginalDesc, itemDroppedDescription, itemGettable, itemDoable, itemLimited, itemUses, itemRefillable, itemHidden, itemActions, itemActionRequirements, itemActionType, itemActionUseSuccessDescription, itemActionUseFailDescription, itemActionOutcomeDescSuccess, itemActionOutcomeDescFailure = infoStr.split("//")
    return Items(itemID, itemName, itemLocation, itemLocationOriginal, itemFriendlyLocation, itemLongDescription, itemShortDescription, itemLocationOriginalDesc, itemDroppedDescription, itemGettable, itemDoable, itemLimited, itemUses, itemRefillable, itemHidden, itemActions, itemActionRequirements, itemActionType, itemActionUseSuccessDescription, itemActionUseFailDescription, itemActionOutcomeDescSuccess, itemActionOutcomeDescFailure)
    
def itemsSetup():
    itemsfile = "itemsfile.txt"
    infile = open(itemsfile, 'r')
    itemsByName = []
    itemsByName = OrderedDict(itemsByName)
    for line in infile:
        newItem = makeItems(line)
        itemsByName[newItem.itemName] = newItem
    infile.close()
    itemsByIndex = list(itemsByName.values())
    return itemsByName, itemsByIndex

# End Item Construction
#####################################################################

#####################################################################
# NPC and Monster Construction
# Creates NPCs and monsters and places them on the map.
# Explanation of less obvious attributes:
#       
#

class NPCsMonsters:
    def __init__(self, npcmID, npcmName, npcmLocation, npcmStartingLocation, npcmFriendlyLocation, npcmLongDescription, npcmShortDescription, npcmStartingLocationDesc, npcmFightable, npcmAggression, npcmFlee, npcmAttack, npcmAttackSuccessDesc, npcmAttackFailDesc, npcmDamage, npcmArmor, npcmArmorSuccessDesc, npcmArmorFailDesc, npcmAlive, npcmHealth, npcmCurrentHealth, npcmOutlook, npcmTalkable, npcmConversation):
        self.npcmID = npcmID
        self.npcmName = npcmName
        self.npcmLocation = npcmLocation
        self.npcmStartingLocation = npcmStartingLocation
        self.npcmFriendlyLocation = npcmFriendlyLocation
        self.npcmLongDescription = npcmLongDescription
        self.npcmShortDescription = npcmShortDescription
        self.npcmStartingLocationDesc = npcmStartingLocationDesc
        self.npcmFightable = npcmFightable
        self.npcmAggression = npcmAggression
        self.npcmFlee = npcmFlee
        self.npcmAttack = npcmAttack
        self.npcmAttackSuccessDesc = npcmAttackSuccessDesc
        self.npcmAttackFailDesc = npcmAttackFailDesc
        self.npcmDamage = npcmDamage
        self.npcmArmor = npcmArmor
        self.npcmArmorSuccessDesc = npcmArmorSuccessDesc
        self.npcmArmorFailDesc = npcmArmorFailDesc
        self.npcmAlive = npcmAlive
        self.npcmHealth = npcmHealth
        self.npcmCurrentHealth = npcmCurrentHealth
        self.npcmOutlook = npcmOutlook
        self.npcmTalkable = npcmTalkable
        self.npcmConversation = npcmConversation

def makeNPCsMonsters(infoStr):
    npcmID, npcmName, npcmLocation, npcmStartingLocation, npcmFriendlyLocation, npcmLongDescription, npcmShortDescription, npcmStartingLocationDesc, npcmFightable, npcmAggression, npcmFlee, npcmAttack, npcmAttackSuccessDesc, npcmAttackFailDesc, npcmDamage, npcmArmor, npcmArmorSuccessDesc, npcmArmorFailDesc, npcmAlive, npcmHealth, npcmCurrentHealth, npcmOutlook, npcmTalkable, npcmConversation = infoStr.split("//")
    return NPCsMonsters(npcmID, npcmName, npcmLocation, npcmStartingLocation, npcmFriendlyLocation, npcmLongDescription, npcmShortDescription, npcmStartingLocationDesc, npcmFightable, npcmAggression, npcmFlee, npcmAttack, npcmAttackSuccessDesc, npcmAttackFailDesc, npcmDamage, npcmArmor, npcmArmorSuccessDesc, npcmArmorFailDesc, npcmAlive, npcmHealth, npcmCurrentHealth, npcmOutlook, npcmTalkable, npcmConversation)
    
def NPCsMonstersSetup():
    npcsmonstersfile = "npcsmonstersfile.txt"
    infile = open(npcsmonstersfile, 'r')
    NPCsMonstersByName = []
    NPCsMonstersByName = OrderedDict(NPCsMonstersByName)
    for line in infile:
        newNPCM = makeNPCsMonsters(line)
        NPCsMonstersByName[newNPCM.npcmName] = newNPCM
    infile.close()
    NPCsMonstersByIndex = list(NPCsMonstersByName.values())
    return NPCsMonstersByName, NPCsMonstersByIndex

# End NPC and Monster Construction
#####################################################################

#####################################################################
# Random Noises Construction and execution

def randomNoisesSetup():
    randomNoisesfile = "randomnoisesfile.txt"
    infile = open(randomNoisesfile, "r")
    randomNoises = []
    for line in infile:
        randomNoises.append(line)
    infile.close()
    return randomNoises

def randomEvents(randomNoises):
    numNoises = len(randomNoises)
    if random() < .1:
        randEvent = randrange(1, numNoises)
        print(randomNoises[randEvent])
    else:
        pass

# End Random Noises Construction and execution
#####################################################################

#####################################################################
# User Creation and Administration

class user():
    def __init__(self, userName, userStr, userDex, userHealth, userDamage, userAttack):
        self.userName = userName
        self.userStr = userStr
        self.userDex = userDex
        self.userHealth = userHealth
        self.userCurrentHealth = userHealth
        self.userDamage = userDamage
        self.userAttack = userAttack

def makeUser(userName, userStr, userDex, userHealth, userDamage, userAttack):
    return user(userName, userStr, userDex, userHealth, userDamage, userAttack)

def userCreation():
    userName = (input("What is your character's name? "))
    userStr = rollDice()
    userDex = rollDice()
    userHealth = rollDice()
    userDamage = int(userStr/3)
    userAttack = round((userDex/18), 2)
    userCharacter = makeUser(userName, userStr, userDex, userHealth, userDamage, userAttack)
    return userCharacter

def rollDice():
    dieOne = randrange(1,7)
    dieTwo = randrange(1,7)
    diceTotal = dieOne + dieTwo + 6
    return diceTotal

def viewUser(userCharacter):
    print("Character: ", userCharacter.userName)
    print("Strength: ", userCharacter.userStr)
    print("Dexterity: ", userCharacter.userDex)
    print("Base Damage: ", userCharacter.userDamage)
    print("Base Attack: ", userCharacter.userAttack)
    print("Health: {0}({1})".format(userCharacter.userCurrentHealth, userCharacter.userHealth))

# End User Creation
#####################################################################

#####################################################################
# Game Play

def gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, verb, randomNoises, userCharacter):
    location = 0
    while not gameOver(verb):
        randomEvents(randomNoises)
        inRoomMonsters = NPCsMonstersCheck(location, NPCsMonstersByName, NPCsMonstersByIndex, "notprint")
        NPCsMonstersAttackCheck(inRoomMonsters, roomsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, userCharacter)
        verb, noun = menuChoices2()
        location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsAndMonstersByName, NPCsAndMonstersByIndex, location, userCharacter)

def gameOver(verb):
    return verb == "q"

def menuChoices2():
    action = input("What do you do? ")
    action = action.lower()
    try:
        verb, noun = action.split(" ")
        return verb, noun
    except:
        verb = action
        noun = " "
        return verb, noun

def verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, userCharacter):
    # Check for movements.
    # Check for built in commands: inventory, time
    # Check for gets and objects
    # Check for verbs specifc to objects
    moveVerbs = ["go", "walk", "run", "travel"]
    directionVerbs = ["north", "n", "south", "s", "west", "w", "east",  "e", "northwest", "nw", "northeast" ,"ne", "southwest", "sw", "southeast", "se"]
    getVerbs = ["get", "pickup", "grab", "take"]
    dropVerbs = ["drop", "ditch", "lose"]
    invVerbs = ["i", "inv", "inventory"]
    searchVerbs = ["search", "examine"]
    lookVerbs = ["look"]
    talkVerbs = ["talk", "speak", "communicate", "converse"]
    attackVerbs = ["attack", "kick", "punch"]
    gameActions = ["me", "self", "save", "quit"]
    pickup = ""
    inventory = inventoryCheck(itemsByIndex, "notprint")
    droppedItems = itemCheck(location, itemsByIndex, "notprint")
    inRoomMonsters = NPCsMonstersCheck(location, NPCsMonstersByName, NPCsMonstersByIndex, "notprint")
    if verb in gameActions:
        if verb == "me":
            viewUser(userCharacter)
        else:
            pass
    else:
        if verb in moveVerbs:
            location = moveCheck(roomsByIndex, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, noun, location)
        elif verb in directionVerbs:
            location = moveCheck(roomsByIndex, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, verb, location)
        elif verb in getVerbs and noun in droppedItems:
            getDropItems(itemsByName, location, "get", noun)
        elif verb in dropVerbs:
            getDropItems(itemsByName, location, "drop", noun)
        elif verb in invVerbs:
            inventoryCheck(itemsByIndex, "print")
        elif (verb in searchVerbs) and (noun == "room"):
            searchCheck(roomsByIndex, itemsByIndex, noun, location)
        elif (verb in lookVerbs) and (noun == "room"):
            roomDescription(location, roomsByIndex, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex)
        elif (verb in lookVerbs) and ((noun in inventory) or (noun in droppedItems)):
            print(itemsByName[noun].itemLongDescription)
        elif (noun in inventory) or (noun in droppedItems):
            location = useItems(itemsByName, itemsByIndex, roomsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, verb, noun)
        elif (verb in talkVerbs):
            conversation(roomsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, verb, noun)
        elif (verb in attackVerbs) and (noun in inRoomMonsters):
            userCharacter.currentHealth, NPCsMonstersByName[noun].npcmCurrentHealth = userAttackCheck(location, verb, noun, NPCsMonstersByName, userCharacter, "user")
        else:
            print("Huh?")
    return(location)

# End Game Play
#####################################################################

#####################################################################
# Basic movement, description, and getting and dropping items

def moveCheck(roomsByIndex, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, action, location):
    roomExitsStr = roomsByIndex[location].exits
    roomExits = ast.literal_eval(roomExitsStr)
    roomExitsHiddenStr = roomsByIndex[location].hiddenExits
    roomExitsHidden = ast.literal_eval(roomExitsHiddenStr)
    if action == ("" or "q"):
        pass
    elif action in roomExits:
        location = roomExits.get(action, 'unknown')
        roomDescription(location, roomsByIndex, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, userCharacter)
        return location
    elif (action in roomExitsHidden) and (roomsByIndex[location].hiddenExitFound == "1"):
        location = roomExitsHidden.get(action, 'unknown')
        roomDescription(location, roomsByIndex, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, userCharacter)
        return location
    else:
        print("You can't go in that direction!")
    return location

# changeLocation is used for non-normal movement around the map (by magic items, technology, whatever)
def changeLocation(location, locationSelection, locationChoices, roomsByIndex, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex):
    try:
        changeLocationTo = locationChoices[locationSelection]
        location = changeLocationTo
        validChoice = "true"
        return validChoice, location
    except:
        validChoice = "false"
        return validChoice, location

def roomDescription(location, roomsByIndex, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, userCharacter):
    checkHiddenExit = int(roomsByIndex[location].hiddenExitable)
    checkHiddenExitFound = int(roomsByIndex[location].hiddenExitFound)
    print(roomsByIndex[location].longDescription)
    itemCheck(location, itemsByIndex, "print")
    NPCsMonstersCheck(location, NPCsMonstersByName, NPCsMonstersByIndex, "print")
    print(roomsByIndex[location].exitDescription)
    if (checkHiddenExit == 1) and (checkHiddenExitFound == 1):
        print(roomsByIndex[location].hiddenExitDescription)
    else:
        pass
    #inRoomMonsters = NPCsMonstersCheck(location, NPCsMonstersByName, NPCsMonstersByIndex, "notprint")
    #NPCsMonstersAttackCheck(inRoomMonsters, roomsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, userCharacter)

def NPCsMonstersCheck(location, NPCsMonstersByName, NPCsMonstersByIndex, action):
    numMonsters = len(NPCsMonstersByIndex)
    inRoomMonsters = []
    inRoomMonstersDescription = []
    for n in range(numMonsters):
        checkLocation = int(NPCsMonstersByIndex[n].npcmLocation)
        checkStartingLocation = int(NPCsMonstersByIndex[n].npcmStartingLocation)
        if (checkLocation == location) and (checkLocation != checkStartingLocation):
            inRoomMonsters.append(NPCsMonstersByIndex[n].npcmName)
            inRoomMonstersDescription.append(NPCsMonstersByIndex[n].npcmStartingLocationDescription)
        elif (checkLocation == location) and (checkLocation == checkStartingLocation):
            inRoomMonsters.append(NPCsMonstersByIndex[n].npcmName)
            inRoomMonstersDescription.append(NPCsMonstersByIndex[n].npcmShortDescription)
        else:
            pass
    numInRoomMonsters = (len(inRoomMonsters))
    if action == "print" and (numInRoomMonsters == 0):
        pass
    elif action == "print" and (numInRoomMonsters > 0):
        for n in range(numInRoomMonsters):
            print(inRoomMonstersDescription[n])
    else:
        return(inRoomMonsters)

def NPCsMonstersAttackCheck(inRoomMonsters, roomsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, userCharacter):
    numMonsters = len(inRoomMonsters)
    userCurrentHealth = int(userCharacter.userCurrentHealth)
    for n in range (numMonsters):
        noun = inRoomMonsters[n]
        monsterCurrentHealth = int(NPCsMonstersByName[noun].npcmCurrentHealth)
        monsterAggression = float(NPCsMonstersByName[noun].npcmAggression)
        monsterAttack = float(NPCsMonstersByName[noun].npcmAttack)
        if (monsterAttack == "1") or (random() < monsterAggression):
            # Monster wants to attack
            NPCsMonstersByName[noun].npcmAttack = "1"
            userCurrentHealth, monsterCurrentHealth = combat("", noun, NPCsMonstersByName, userCharacter, "monster")
        else:
            pass
    return userCurrentHealth, monsterCurrentHealth
        #self.npcmFlee = npcmFlee

def itemCheck(location, itemsByIndex, action):
    numItems = len(itemsByIndex)
    droppedItems = []
    droppedItemsDescription = []
    for n in range(numItems):
        checkLocation = int(itemsByIndex[n].itemLocation)
        checkHidden = int(itemsByIndex[n].itemHidden)
        checkLocationOriginal = int(itemsByIndex[n].itemLocationOriginal)
        if (checkLocation == location) and (checkHidden == 0) and (checkLocation != checkLocationOriginal):
            droppedItems.append(itemsByIndex[n].itemName)
            droppedItemsDescription.append(itemsByIndex[n].itemDroppedDescription)
        elif (checkLocation == location) and (checkHidden == 0) and (checkLocation == checkLocationOriginal):
            droppedItems.append(itemsByIndex[n].itemName)
            droppedItemsDescription.append(itemsByIndex[n].itemLocationOriginalDesc)
        else:
            pass
    numDroppedItems = (len(droppedItems))
    if action == "print" and (numDroppedItems == 0):
        pass
    elif action == "print" and (numDroppedItems > 0):
        for n in range(numDroppedItems):
            print(droppedItemsDescription[n])
    else:
        return(droppedItems)
        
def inventoryCheck(itemsByIndex, action):
    numItems = len(itemsByIndex)
    inv = -1
    inventory = []
    for n in range(numItems):
        checkLocation = int(itemsByIndex[n].itemLocation)
        if checkLocation == inv:
            inventory.append(itemsByIndex[n].itemName)
        else:
            pass
    numInventoryItems = len(inventory)
    if (action == "print") and (numInventoryItems == 0):
        print("You're not carrying anything!")
    elif (action == "print") and (numInventoryItems > 0):
        print("In your inventory you have:")
        for n in range(numInventoryItems):
            print(inventory[n])
    else:
        return inventory

def searchCheck(roomsByIndex, itemsByIndex, noun, location):
    FindSuccess = "false"
    numItems = len(itemsByIndex)
    checkHiddenExit = int(roomsByIndex[location].hiddenExitable)
    checkHiddenExitFound = int(roomsByIndex[location].hiddenExitFound)
    for n in range(numItems):
        checkLocation = int(itemsByIndex[n].itemLocation)
        checkHidden = int(itemsByIndex[n].itemHidden)
        if (checkLocation == location) and (checkHidden == 1) and (random() < .9):
            itemsByIndex[n].itemHidden = "0"
            print("You're search has found a concealed item!")
            print(itemsByIndex[n].itemDroppedDescription)
            break
        else:
            pass
    if (checkHiddenExit == 1) and (checkHiddenExitFound == 0) and (random() < .9):
        roomsByIndex[location].hiddenExitFound = "1"
        FindSuccess = "true"
        print("You're search has found", roomsByIndex[location].hiddenExitFindDescription)
    elif FindSuccess == "false":
        print("Your search reveals nothing!")
    return(location)

def getDropItems(itemsByName, location, action, noun):
    checkLocation = int(itemsByName[noun].itemLocation)
    checkGettable = int(itemsByName[noun].itemGettable)
    checkHidden = int(itemsByName[noun].itemHidden)
    if action == "get":
        if (checkLocation == location) and (checkGettable == 1) and (checkHidden == 0):
            itemsByName[noun].itemLocation = "-1"
            print
            print("You pick up the {0}.".format(noun))
        elif (checkLocation == location) and (checkGettable == 0) and (checkHidden == 0):
            print
            print("You can't pick up the {0}.".format(noun))
        else:
            print
            print("There is no {0} to get!".format(noun))
    elif action =="drop":
        if checkLocation == -1:
            itemsByName[noun].itemLocation = location
            print
            print("You drop the {0}.".format(noun))
        else:
            print("You don't have the", noun, "to drop!")
    return(location)

# End Basic movement, description, and getting and dropping items
#####################################################################

#####################################################################
# Combat

def userAttackCheck(location, verb, noun, NPCsMonstersByName, userCharacter, attacker):
    checkLocation = int(NPCsMonstersByName[noun].npcmLocation)
    checkFightable = int(NPCsMonstersByName[noun].npcmFightable)
    checkAlive = int(NPCsMonstersByName[noun].npcmAlive)
    userCurrentHealth = int(userCharacter.userCurrentHealth)
    monsterCurrentHealth = int(NPCsMonstersByName[noun].npcmCurrentHealth)
    if (checkLocation == location) and (checkFightable == 1) and (checkAlive == 1):
        userCurrentHealth, monsterCurrentHealth = combat(verb, noun, NPCsMonstersByName, userCharacter, "user")
    elif (checkLocation == location) and (checkFightable == 1) and (checkAlive == 0):
        print("You {0} the dead {1}, which is kind of gross.".format(verb, noun))
    else:
        print("Uh, why're you fighting with yourself?")
    return userCurrentHealth, monsterCurrentHealth

def combat(verb, noun, NPCsMonstersByName, userCharacter, attacker):
    #checkLocation = int(NPCsMonstersByName[noun].npcmLocation)
    #checkFightable = int(NPCsMonstersByName[noun].npcmFightable)
    #checkAlive = int(NPCsMonstersByName[noun].npcmAlive)
    userCurrentHealth = int(userCharacter.userCurrentHealth)
    monsterCurrentHealth = int(NPCsMonstersByName[noun].npcmCurrentHealth)
    userAttack = userCharacter.userAttack
    monsterAttack = float(NPCsMonstersByName[noun].npcmAttack)
    userDamage = userCharacter.userDamage
    monsterDamage = int(NPCsMonstersByName[noun].npcmDamage)
    userHit = ""
    monsterHit = ""
    # User Attack
    if attacker == "user":
        if random() < userAttack:
            print("Your {0} connects! The {1} reels!".format(verb, noun))
            userHit = "true"
        else:
            print("Your {0} misses!".format(verb))
    elif attacker == "monster":
        if random() < monsterAttack:
            print("The {0} hits you!".format(noun))
            monsterHit = "true"
        else:
            print("The {0} misses you!".format(noun))
    else:
        pass
    # Damage by User
    if userHit == "true":
        damage = randrange(1,userDamage)
        monsterCurrentHealth = (monsterCurrentHealth - damage)
        NPCsMonstersByName[noun].npcmCurrentHealth = monsterCurrentHealth
        print("You do {0} points of damage to the {1}!".format(damage, noun))
    if monsterHit == "true":
        damage = randrange(1,monsterDamage)
        userCurrentHealth = (userCurrentHealth - damage)
        userCharacter.userCurrentHealth = userCurrentHealth
        print("The {0} does {1} points of damage to you!".format(noun, damage))
    else:
        pass
        # Monster Health Check
    if monsterCurrentHealth < 1:
        NPCsMonstersByName[noun].npcmAlive = 0
        print("The {0} is dead!".format(noun))
    else:
        pass
    return userCurrentHealth, monsterCurrentHealth

# End Combat
#####################################################################

#####################################################################
# Converation

def conversation(roomsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, verb, noun):
    checkLocation = int(NPCsMonstersByName[noun].npcmLocation)
    checkTalkable = int(NPCsMonstersByName[noun].npcmTalkable)
    endConversation = "false"
    if (checkLocation == location) and (checkTalkable == 1):
        npcmConversation = ast.literal_eval(NPCsMonstersByName[noun].npcmConversation)
        while endConversation == "false":
            question = input("What do you say to the {0} [Press 'q' to quit your conversation]? ".format(noun))
            question.replace("'", "")
            questionSplit = question.split()
            match = "false"
            while match == "false":
                for word in questionSplit:
                    if word == "q":
                        print(npcmConversation.get("exit", "That's an odd thing to say!"))
                        match = "true"
                        endConversation = "true"
                        break
                    elif word in npcmConversation:
                        print(npcmConversation.get(word, "That's an odd thing to say!"))
                        match = "true"
                        break
                    else:
                        pass
                else:
                    if match == "false":
                        print("That's an odd thing to say!")
                        match = "true"
    else:
        print("Uh, why're you talking to yourself?")

# End Conversation
#####################################################################

#####################################################################
# Use Items

def useItems(itemsByName, itemsByIndex, roomsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, verb, noun):
    checkItemActions = itemsByName[noun].itemActions
    checkLocation = itemsByName[noun].itemLocation
    checkGettable = itemsByName[noun].itemGettable
    checkDoable = itemsByName[noun].itemDoable
    # Item Action Requirements: inventory, location, eitherInventoryLocation
    checkItemActionRequirements = itemsByName[noun].itemActionRequirements
    checkItemActionType = ast.literal_eval(itemsByName[noun].itemActionType)
    itemReq = ast.literal_eval(itemsByName[noun].itemActionRequirements)
    # Successes
    if ("eitherInventoryLocation" in checkItemActionRequirements) and (verb in checkItemActions):
        location = useItemsSuccess(itemsByName, itemsByIndex, roomsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, verb, noun)
    elif("inventory" in checkItemActionRequirements) and (checkLocation == "-1") and (verb in checkItemActions):
        location = useItemsSuccess(itemsByName, itemsByIndex, roomsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, verb, noun)
    elif("notInventory" in checkItemActionRequirements) and ("location" in checkItemActionRequirements) and (location == itemReq.get("location", "unknown")) and (itemsByName[noun].itemLocation != "-1"):
        location = useItemsSuccess(itemsByName, itemsByIndex, roomsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, verb, noun)
    # Failures
    elif ("notInventory" in checkItemActionRequirements) and (checkLocation == "-1"):
        print(itemReq.get("notInventory", "unknown"))
    elif ("notInventory" in checkItemActionRequirements) and (checkLocation != "-1") and (location != itemReq.get("location", "unknown")):
        print("You can't use the", noun, "here!")
    elif("inventory" in checkItemActionRequirements) and (checkLocation != "-1") and (verb in checkItemActions):
        print(itemReq.get("inventory", "unknown"))
    else:
        print("Do what with the {0}?".format(noun))
    return location

def useItemsSuccess(itemsByName, itemsByIndex, roomsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, verb, noun):
    # Check to see if item has limited uses, and if item is re-usable.  If it's not re-usable and uses = 0, disappear the item.
    if itemsByName[noun].itemLimited == "1":
        itemUsesCheck = eval(itemsByName[noun].itemUses)
        itemUsesCheck = (itemUsesCheck - 1)
        itemsByName[noun].itemUses = str(itemUsesCheck)
        if itemUsesCheck == 0 and itemsByName[noun].itemRefillable == "0":
            itemsByName[noun].itemLocation = "-2"
        else:
            pass
    else:
        pass
    # Action Types are: unhideMap, unhideItems, message, changeStats, changeLocation
    checkItemActionType = itemsByName[noun].itemActionType
    # Check to see if any of the Descriptions contain "none" - if so, do not print them.  If not, print them.  This allows for more or less description of the item and its uses,
    #   depending on the situation and the needs of the story.
    if "message" in checkItemActionType:
        if itemsByName[noun].itemActionUseSuccessDescription == "none":
            pass
        else:
            print(itemsByName[noun].itemActionUseSuccessDescription)
        if (itemsByName[noun].itemActionOutcomeDescSuccess) == "none":
            pass
        else:
            print(itemsByName[noun].itemActionOutcomeDescSuccess)
    elif "unhideLocation" in checkItemActionType:
        if itemsByName[noun].itemActionUseSuccessDescription == "none":
            pass
        else:
            print(itemsByName[noun].itemActionUseSuccessDescription)
        if (itemsByName[noun].itemActionOutcomeDescSuccess) == "none":
            pass
        else:
            print(itemsByName[noun].itemActionOutcomeDescSuccess)
        roomsByIndex[location].hiddenExitFound = "1"
        print(roomsByIndex[location].hiddenExitFindDescription)
        # Update Exits description
        roomsByIndex[location].exitDescription = roomsByIndex[location].hiddenExitDescription
    elif "changeLocation" in checkItemActionType:
        if itemsByName[noun].itemActionUseSuccessDescription == "none":
            pass
        else:
            print(itemsByName[noun].itemActionUseSuccessDescription)
        itemActionTypeCheck = ast.literal_eval(itemsByName[noun].itemActionType)
        locationChoices = eval(itemActionTypeCheck.get("changeLocation", "unknown"))
        validChoice = "false"
        while validChoice == "false":
            print("Where do you want to go to?")
            for n in locationChoices:
                print(n, " - ", roomsByIndex[n].shortDescription)
            locationSelection = "false"
            while locationSelection == "false":
                try:
                    locationSelection = eval(input("What is your selection? "))
                except:
                    print("Uh, what?")
                    locationSelection = "false"
            locationSelection = locationSelection - 1
            validChoice, location = changeLocation(location, locationSelection, locationChoices, roomsByIndex, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex)
            if validChoice == "true":
                if (itemsByName[noun].itemActionOutcomeDescSuccess) == "none":
                    pass
                else:
                    print(itemsByName[noun].itemActionOutcomeDescSuccess)
                roomDescription(location, roomsByIndex, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex)
            elif validChoice == "false":
                if (itemsByName[noun].itemActionOutcomeDescFailure) == "none":
                    pass
                else:
                    print(itemsByName[noun].itemActionOutcomeDescFailure)
    else:
        print("Huh?")
    return location

# End Use Items
#####################################################################

#####################################################################
# Main

def main():
    #intro()
    roomsByName, roomsByIndex = roomSetup()
    itemsByName, itemsByIndex = itemsSetup()
    randomNoises = randomNoisesSetup()
    NPCsMonstersByName, NPCsMonstersByIndex = NPCsMonstersSetup()
    userCharacter = userCreation()
    location = 0
    verb = ""
    roomDescription(location, roomsByIndex, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, userCharacter)
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, verb, randomNoises, userCharacter)

if __name__=='__main__':
    main()

# End Main
#####################################################################
    
