
#Adventure
# get, go, inventory, look, attack, punch, kick, kill, push, open, close, read, eat, search, shoot, climb, throw, north, n, south, s, east, e, west, w, northwest, nw, northeast, ne, southwest, se, southwest, sw
# Check if action pairs with object.  Check if location of object allows action (check inventory).  Return descript for action.  Update any properties/locations/inventories.

# Used items can open up the map, reveal hidden items, give messages, change stats, change location
# Properties of Items
# Gettable, Doable, Hidden, Actions, Action Requirements (in inventory, not in inventory, certain location, certain events complete), limited, number of uses
# ItemActionRequirementsFailureDescription
# Action Types: open up map (new exits), unhide items, give messages, change stats, change location
# ActionOutcomes
# ActionOutcomeDescriptionsSuccess
# ActionOutcomeDescriptionUnsuccessful

# Weapons
# Combat
# NPCs
# Conversation

#####################################################################
# Import
import ast
from random import random, randrange
from collections import OrderedDict
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
# Game Play

def gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises):
    location = 0
    while not gameOver(verb):
        randomEvents(randomNoises)
        verb, noun = menuChoices2()
        location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)

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

def verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location):
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
    pickup = ""
    inventory = inventoryCheck(itemsByIndex, "notprint")
    droppedItems = itemCheck(location, itemsByIndex, "notprint") 
    if verb in moveVerbs:
        location = moveCheck(roomsByIndex, itemsByIndex, noun, location)
    elif verb in directionVerbs:
        location = moveCheck(roomsByIndex, itemsByIndex, verb, location)
    elif verb in getVerbs and noun in droppedItems:
        getDropItems(itemsByName, location, "get", noun)
    elif verb in dropVerbs:
        getDropItems(itemsByName, location, "drop", noun)
    elif verb in invVerbs:
        inventoryCheck(itemsByIndex, "print")
    elif (verb in searchVerbs) and (noun == "room"):
        searchCheck(roomsByIndex, itemsByIndex, noun, location)
    elif (verb in lookVerbs) and (noun == "room"):
        roomDescription(location, roomsByIndex, itemsByIndex)
    elif (verb in lookVerbs) and ((noun in inventory) or (noun in droppedItems)):
        print(itemsByName[noun].itemLongDescription)
    elif (noun in inventory) or (noun in droppedItems):
        location = useItems(itemsByName, itemsByIndex, roomsByIndex, location, verb, noun)
    else:
        print("Huh?")
    return(location)

# End Game Play
#####################################################################

#####################################################################
# Basic movement, description, and getting and dropping items

def moveCheck(roomsByIndex, itemsByIndex, action, location):
    roomExitsStr = roomsByIndex[location].exits
    roomExits = ast.literal_eval(roomExitsStr)
    roomExitsHiddenStr = roomsByIndex[location].hiddenExits
    roomExitsHidden = ast.literal_eval(roomExitsHiddenStr)
    if action == ("" or "q"):
        pass
    elif action in roomExits:
        location = roomExits.get(action, 'unknown')
        roomDescription(location, roomsByIndex, itemsByIndex)
        return location
    elif (action in roomExitsHidden) and (roomsByIndex[location].hiddenExitFound == "1"):
        location = roomExitsHidden.get(action, 'unknown')
        roomDescription(location, roomsByIndex, itemsByIndex)
        return location
    else:
        print("You can't go in that direction!")
    return location

# changeLocation is used for non-normal movement around the map (by magic items, technology, whatever)
def changeLocation(location, locationSelection, locationChoices, roomsByIndex, itemsByIndex):
    try:
        changeLocationTo = locationChoices[locationSelection]
        location = changeLocationTo
        print(roomDescription(location, roomsByIndex, itemsByIndex))
        validChoice = "true"
        return validChoice, location
    except:
        validChoice = "true"
        return validChoice, location

def roomDescription(location, roomsByIndex, itemsByIndex):
    checkHiddenExit = int(roomsByIndex[location].hiddenExitable)
    checkHiddenExitFound = int(roomsByIndex[location].hiddenExitFound)
    print(roomsByIndex[location].longDescription)
    itemCheck(location, itemsByIndex, "print")
    print(roomsByIndex[location].exitDescription)
    if (checkHiddenExit == 1) and (checkHiddenExitFound == 1):
        print(roomsByIndex[location].hiddenExitDescription)
    else:
        pass

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

# Basic movement, description, and getting and dropping items
#####################################################################

#####################################################################
# Use Items

def useItems(itemsByName, itemsByIndex, roomsByIndex, location, verb, noun):
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
        location = useItemsSuccess(itemsByName, itemsByIndex, roomsByIndex, location, verb, noun)
    elif("inventory" in checkItemActionRequirements) and (checkLocation == "-1") and (verb in checkItemActions):
        location = useItemsSuccess(itemsByName, itemsByIndex, roomsByIndex, location, verb, noun)
    elif("notInventory" in checkItemActionRequirements) and ("location" in checkItemActionRequirements) and (location == itemReq.get("location", "unknown")) and (itemsByName[noun].itemLocation != "-1"):
        location = useItemsSuccess(itemsByName, itemsByIndex, roomsByIndex, location, verb, noun)
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

def useItemsSuccess(itemsByName, itemsByIndex, roomsByIndex, location, verb, noun):
    # Check to see if item has limited uses, and if item is re-usable.  If it's not re-usable and uses = 0, disappear the item.
    if itemsByName[noun].itemLimited == "1":
        itemUsesCheck = eval(itemsByName[noun].itemUses)
        itemUsesCheck = (itemUsesCheck - 1)
        itemsByName[noun].itemUses = itemUsesCheck
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
            locationSelection = eval(input("What is your selection?"))
            locationSelection = locationSelection - 1
            validChoice, location = changeLocation(location, locationSelection, locationChoices, roomsByIndex, itemsByIndex)
            if validChoice == "true":
                if (itemsByName[noun].itemActionOutcomeDescSuccess) == "none":
                    print(itemsByName[noun].itemActionOutcomeDescSuccess)
                else:
                    print
            elif validChoice == "false":
                if (itemsByName[noun].itemActionOutcomeDescFail) == "none":
                    pass
                else:
                    print(itemsByName[noun].itemActionOutcomeDescFail)
    else:
        print("Huh?")
    return location

# End Use Items
#####################################################################

#####################################################################
# Main

def main():
    #intro()
    #user()
    #inventory()
    roomsByName, roomsByIndex = roomSetup()
    itemsByName, itemsByIndex = itemsSetup()
    randomNoises = randomNoisesSetup()
    location = 0
    verb = ""
    roomDescription(location, roomsByIndex, itemsByIndex)
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)

if __name__=='__main__':
    main()

# End Main
#####################################################################
    
