Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 02:56:36) 
[GCC 4.2.1 (Apple Inc. build 5577)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 72, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 66, in main
    rooms = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 40, in roomSetup
    rooms.append(makeRooms(line))
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 33, in makeRooms
    return Rooms(roomNumber, name, longDescription, shortDescription, exits, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 8, in __init__
    self.longDescription = longDescription
NameError: global name 'longDescription' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 72, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 67, in main
    location = rooms.getRoomNumber[1]
AttributeError: 'list' object has no attribute 'getRoomNumber'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 72, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 68, in main
    move = menuChoices()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 45, in menuChoices
    while action !="q":
UnboundLocalError: local variable 'action' referenced before assignment
>>> ================================ RESTART ================================
>>> 
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 72, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 68, in main
    move = menuChoices()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 47, in menuChoices
    action = action([0]).lower
TypeError: 'str' object is not callable
>>> ================================ RESTART ================================
>>> 
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 72, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 68, in main
    move = menuChoices()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 47, in menuChoices
    action = action([0]).lower()
TypeError: 'str' object is not callable
>>> ================================ RESTART ================================
>>> 
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 72, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 68, in main
    move = menuChoices()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 47, in menuChoices
    action = (action([0])).lower()
TypeError: 'str' object is not callable
>>> ================================ RESTART ================================
>>> 
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 72, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 68, in main
    move = menuChoices()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 47, in menuChoices
    action = (action[0]).lower()
KeyboardInterrupt
>>> ================================ RESTART ================================
>>> 
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 72, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 68, in main
    move = menuChoices()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 46, in menuChoices
    while action !="q":
KeyboardInterrupt
>>> ================================ RESTART ================================
>>> 
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 71, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 68, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 50, in moveCheck
    roomExits = room.getExits[location]
NameError: global name 'room' is not defined
>>> ================================ RESTART ================================
>>> 
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 71, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 68, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 50, in moveCheck
    roomExits = rooms.getExits[location]
AttributeError: 'list' object has no attribute 'getExits'
>>> ================================ RESTART ================================
>>> 
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 71, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 68, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 50, in moveCheck
    roomExits = rooms[location].getExits()
AttributeError: 'Rooms' object has no attribute 'getExits'
>>> ================================ RESTART ================================
>>> 
What do you do? w
test1
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 72, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 69, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 50, in moveCheck
    roomExits = rooms[location].getExits()
AttributeError: 'Rooms' object has no attribute 'getExits'
>>> ================================ RESTART ================================
>>> 
What do you do? w
test1
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 72, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 69, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 50, in moveCheck
    roomExits = rooms[location].getExits()
AttributeError: 'Rooms' object has no attribute 'getExits'
>>> ================================ RESTART ================================
>>> 
What do you do? w
test1
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 72, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 69, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 50, in moveCheck
    roomExits = brooms[location].getExits()
NameError: global name 'brooms' is not defined
>>> ================================ RESTART ================================
>>> 
What do you do? w
test1
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 72, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 69, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 50, in moveCheck
    roomExits = rooms[location].getRoomNumber()
AttributeError: 'Rooms' object has no attribute 'getRoomNumber'
>>> ================================ RESTART ================================
>>> 
What do you do? 
>>> ================================ RESTART ================================
>>> 
W
What do you do? w
test1
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 72, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 69, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 50, in moveCheck
    roomExits = rooms([location].getRoomNumber())
AttributeError: 'list' object has no attribute 'getRoomNumber'
>>> ================================ RESTART ================================
>>> 
What do you do? w
test1
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 72, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 69, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 50, in moveCheck
    roomExits = (rooms[location].getRoomNumber())
AttributeError: 'Rooms' object has no attribute 'getRoomNumber'
>>> ================================ RESTART ================================
>>> 
What do you do? w
test1
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 73, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 70, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 51, in moveCheck
    roomExits = rooms[location].getRoomNumber()
AttributeError: 'Rooms' object has no attribute 'getRoomNumber'
>>> ================================ RESTART ================================
>>> 
What do you do? w
test1
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 73, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 70, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 51, in moveCheck
    roomEx = rooms[location].getRoomNumber()
AttributeError: 'Rooms' object has no attribute 'getRoomNumber'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 73, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 70, in main
    print(rooms[location].getName())
AttributeError: 'Rooms' object has no attribute 'getName'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 73, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 70, in main
    print(rooms[0].getName())
AttributeError: 'Rooms' object has no attribute 'getName'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 73, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 70, in main
    print(xrooms[0].getName())
AttributeError: 'Rooms' object has no attribute 'getName'
>>> ================================ RESTART ================================
>>> 
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 72, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 69, in main
    moveCheck(rooms, move, location)
NameError: global name 'rooms' is not defined
>>> ================================ RESTART ================================
>>> 
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 72, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 69, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 52, in moveCheck
    if move in roomsExits:
NameError: global name 'roomsExits' is not defined
>>> ================================ RESTART ================================
>>> 
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 72, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 69, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 52, in moveCheck
    if move in roomsExits:
NameError: global name 'roomsExits' is not defined
>>> ================================ RESTART ================================
>>> 
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 72, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 69, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 52, in moveCheck
    if move in roomsExits:
NameError: global name 'roomsExits' is not defined
>>> ================================ RESTART ================================
>>> 
What do you do? w
That's not a valid direction!
>>> ================================ RESTART ================================
>>> 
What do you do? W
That's not a valid direction!
>>> ================================ RESTART ================================
>>> 
What do you do? w
2
That's not a valid direction!
>>> ================================ RESTART ================================
>>> 
What do you do? w
2
That's not a valid direction!
>>> ================================ RESTART ================================
>>> 
What do you do? w
2
That's not a valid direction!
>>> ================================ RESTART ================================
>>> 
What do you do? e
2
That's not a valid direction!
>>> ================================ RESTART ================================
>>> 
What do you do? g
2
That's not a valid direction!
>>> ================================ RESTART ================================
>>> 
What do you do? e
That's not a valid direction!
>>> ================================ RESTART ================================
>>> 
What do you do? e
That's not a valid direction!
>>> ================================ RESTART ================================
>>> 
What do you do? e
'w':'1'
That's not a valid direction!
>>> ================================ RESTART ================================
>>> 
What do you do? n
'w':'1'
That's not a valid direction!
>>> ================================ RESTART ================================
>>> 
What do you do? e
'e':'1'
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 71, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 55, in moveCheck
    location = roomExits.get(move)
AttributeError: 'str' object has no attribute 'get'
>>> ================================ RESTART ================================
>>> 
What do you do? e
'w':'1'
That's not a valid direction!
>>> ================================ RESTART ================================
>>> 
What do you do? e
'w':'1'
That's not a valid direction!
>>> ================================ RESTART ================================
>>> 
What do you do? e
'w':'1'
That's not a valid direction!
>>> ================================ RESTART ================================
>>> 
What do you do? e
'w':'1'
That's not a valid direction!
>>> ================================ RESTART ================================
>>> 
What do you do? s
'w':'1'
That's not a valid direction!
>>> ================================ RESTART ================================
>>> 
What do you do? s
'e':'2', 'n':'3', 'w':'4'
That's not a valid direction!
>>> ================================ RESTART ================================
>>> 
What do you do? e
'e':'2', 'n':'3', 'w':'4'
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 71, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 54, in moveCheck
    location = roomExits.get(move)
AttributeError: 'str' object has no attribute 'get'
>>> ================================ RESTART ================================
>>> 
What do you do? e
'e':'2', 'n':'3', 'w':'4'
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 71, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 54, in moveCheck
    location = roomExits.get(move)
AttributeError: 'str' object has no attribute 'get'
>>> ================================ RESTART ================================
>>> 
What do you do? e
'e':'2', 'n':'3', 'w':'4'
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 71, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 54, in moveCheck
    location = (roomExits).get('move', 'unknown')
AttributeError: 'str' object has no attribute 'get'
>>> ================================ RESTART ================================
>>> 
What do you do? e
'e':'2', 'n':'3', 'w':'4'
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 71, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 54, in moveCheck
    location = roomExits.get('move', 'unknown')
AttributeError: 'str' object has no attribute 'get'
>>> ================================ RESTART ================================
>>> 
What do you do? eAttributeError: 'str' object has no attribute 'get'
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 70, in main
    move = menuChoices()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 45, in menuChoices
    action = input("What do you do? ")
KeyboardInterrupt
>>> ================================ RESTART ================================
>>> 
What do you do? e
'e':'2', 'n':'3', 'w':'4'
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 71, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 54, in moveCheck
    location = roomExits.get(move, 'unknown')
AttributeError: 'str' object has no attribute 'get'
>>> roomExits = {}
>>> roomExits['e'] = '2'
>>> roomExits
{'e': '2'}
>>> roomExits.get('2', 'unknown')
'unknown'
>>> roomExits.get(('e', 'unnown')

	      
KeyboardInterrupt
>>> roomExits.get('e', 'unknown')
'2'
>>> move = 'e'
>>> roomExits.get(move, 'unknown')
'2'
>>> ================================ RESTART ================================
>>> 
What do you do? e
'e':'2', 'n':'3', 'w':'4'
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 71, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 54, in moveCheck
    location = roomExits.get(move, 'unknown')
AttributeError: 'str' object has no attribute 'get'
>>> 
>>> 
>>> 
>>> roome = ['e':'2', 'n':'3']
SyntaxError: invalid syntax
>>> roome = ["'e':'2', 'n':'3'"]
>>> roomExits = {}
>>> roomExits = roome
>>> roomExits
["'e':'2', 'n':'3'"]
>>> ================================ RESTART ================================
>>> 
What do you do? e
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 71, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 51, in moveCheck
    roomExits = dict(rooms[location].getExits())
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? eValueError: dictionary update sequence element #0 has length 1; 2 is requiredTraceback (most recent call last):
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 71, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 51, in moveCheck
    roomExits = dict(rooms[location].getExits())
ValueError: dictionary update sequence element #0 has length 1; 2 is required

>>> roome = ["'e':'2'"]
>>> dict(roome)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict(roome)
ValueError: dictionary update sequence element #0 has length 7; 2 is required
>>> roome = ['e', 2]
>>> dict(roome)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    dict(roome)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> roome = ['e', '2']
>>> dict(roome)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    dict(roome)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 71, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 51, in moveCheck
    roomExits = dict(rooms[location].getExits())
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> 
>>> 
>>> 
>>> 
>>> roome = ['e', 2]
>>> a = {}
>>> a.update(roome)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a.update(roome)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> roome = [0, '2', 2]
>>> a = {}
>>> a.update(roome)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.update(roome)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> 
>>> 
>>> zip
<class 'zip'>
>>> lst = ['e', 1]
>>> dict(lst)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    dict(lst)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> lst = [('e', 1)]
>>> dict(lst)
{'e': 1}
>>> lst
[('e', 1)]
>>> a = dict(lst)
>>> a
{'e': 1}
>>> ================================ RESTART ================================
>>> 
What do you do? e
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 71, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 51, in moveCheck
    roomExits = dict(rooms[location].getExits())
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 76, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 73, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 53, in moveCheck
    dict(roomExits)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
('e', 2), ('n', 3), ('w', 4)
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 76, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 73, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 54, in moveCheck
    dict(roomExits)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
('e', 2), ('n', 3), ('w', 4)
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 76, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 73, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 54, in moveCheck
    a = dict(roomExits)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> 
>>> 
>>> lst = [('e', 2)]
>>> lst
[('e', 2)]
>>> a = dict(lst)
>>> a
{'e': 2}
>>> ================================ RESTART ================================
>>> 
What do you do? e
[('e', 2), ('n', 3), ('w', 4)]
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 76, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 73, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 54, in moveCheck
    a = dict(roomExits)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
[('e', 2), ('n', 3), ('w', 4)]
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 77, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 55, in moveCheck
    a = dict(roomExits)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/room.py", line 8, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/room.py", line 4, in main
    dict(rooms)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> ================================ RESTART ================================
>>> 
[('e', 2), ('n', 1)]
>>> ================================ RESTART ================================
>>> 
What do you do? e
('e', 2), ('n', 3), ('w', 4)
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 77, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 55, in moveCheck
    a = dict(roomExits)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
["('e', 2), ('n', 3), ('w', 4)"]
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 77, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 54, in moveCheck
    eval(roomExits)
TypeError: eval() arg 1 must be a string, bytes or code object
>>> ================================ RESTART ================================
>>> 
What do you do? e
["('e', 2), ('n', 3), ('w', 4)"]
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 76, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 73, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 54, in moveCheck
    a = dict(roomExits)
ValueError: dictionary update sequence element #0 has length 28; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 75, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 72, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 52, in moveCheck
    roomExitslist = append(roomExits.split("),"))
NameError: global name 'append' is not defined
>>> ================================ RESTART ================================
>>> 
What do you do? e
[["('e', 2", " ('n', 3", " ('w', 4)"]]
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 75, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 72, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 54, in moveCheck
    roomExitsdict = dict(roomExitslist)
ValueError: dictionary update sequence element #0 has length 3; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
[["('e', 2)  ('n', 3)  ('w', 4)"]]
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 75, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 72, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 54, in moveCheck
    roomExitsdict = dict(roomExitslist)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
[["('e', 2)", "('n', 3)", "('w', 4)"]]
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 75, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 72, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 54, in moveCheck
    roomExitsdict = dict(roomExitslist)
ValueError: dictionary update sequence element #0 has length 3; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
('e', 2)  ('n', 3)  ('w', 4)
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 73, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 70, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 52, in moveCheck
    dict(roomExits)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e["('e', 2), ('n', 3), ('w', 4)"e
('e', 2), ('n', 3), ('w', 4)
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 72, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 69, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 53, in moveCheck
    location = roomsExits.get(move, 'unknown')
NameError: global name 'roomsExits' is not defined
>>> ================================ RESTART ================================
>>> 
What do you do? e
('e', 2), ('n', 3), ('w', 4)
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 72, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 69, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 53, in moveCheck
    location = roomExits.get(move, 'unknown')
AttributeError: 'str' object has no attribute 'get'
>>> ================================ RESTART ================================
>>> 
What do you do? e
('e', 2), ('n', 3), ('w', 4)
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 73, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 70, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 52, in moveCheck
    dict(roomExits)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
(
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 73, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 70, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 52, in moveCheck
    dict(roomExits)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
'
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 73, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 70, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 52, in moveCheck
    dict(roomExits)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
('e', 2)
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 73, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 70, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 52, in moveCheck
    dict(roomExits)
ValueError: dictionary update sequence element #0 has length 8; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
["('e', 2)", "('n', 3)", "('w', 4)"]
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 73, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 70, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 52, in moveCheck
    dict(roomExits)
ValueError: dictionary update sequence element #0 has length 8; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
('n', 3)
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 73, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 70, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 52, in moveCheck
    dict(roomExits)
ValueError: dictionary update sequence element #0 has length 8; 2 is required
>>> 
>>> 
>>> 
>>> lst = [('e', 2), ('n', 1)]
>>> lst
[('e', 2), ('n', 1)]
>>> a = dict(lst)
>>> a
{'n': 1, 'e': 2}
>>> ================================ RESTART ================================
>>> 
What do you do? e
["('e', 2)", "('n', 3)", "('w', 4)"]
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 73, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 70, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 52, in moveCheck
    dict(roomExits)
ValueError: dictionary update sequence element #0 has length 8; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 73, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 70, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 50, in moveCheck
    roomExits.append(rooms[location].getExits().split("  "))
NameError: global name 'roomExits' is not defined
>>> ================================ RESTART ================================
>>> 
What do you do? e
[["('e', 2)", "('n', 3)", "('w', 4)"]]
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 71, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 53, in moveCheck
    dict(roomExits)
ValueError: dictionary update sequence element #0 has length 3; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 71, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 51, in moveCheck
    roomExits.append(rooms[location].getExits().split("  "))
NameError: global name 'roomExits' is not defined
>>> ================================ RESTART ================================
>>> 
What do you do? e
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 71, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 51, in moveCheck
    roomExits = dict(rooms[location].getExits().split("  "))
ValueError: dictionary update sequence element #0 has length 8; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 71, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 51, in moveCheck
    roomExits = dict(rooms[location].getExits().split("  "))
ValueError: dictionary update sequence element #0 has length 11; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
[['e', '2', 'n', '3', 'w', '4']]
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 71, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 53, in moveCheck
    dict(roomExits)
ValueError: dictionary update sequence element #0 has length 6; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 75, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 72, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 52, in moveCheck
    eval(roomExits)
TypeError: eval() arg 1 must be a string, bytes or code object
>>> 
>>> 
>>> 
>>> literal_eval
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    literal_eval
NameError: name 'literal_eval' is not defined
>>> import ast
>>> ast.literal_eval
<function literal_eval at 0x23f2c00>
>>> ================================ RESTART ================================
>>> 
What do you do? e
{'e': 2, 'n': 3, 'w': 4}
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 75, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 72, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 56, in moveCheck
    location = roomExits.get(move, 'unknown')
AttributeError: 'str' object has no attribute 'get'
>>> ================================ RESTART ================================
>>> 
What do you do? e
{'e': 2, 'n': 3, 'w': 4}
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 75, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 72, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 56, in moveCheck
    location = roomExits.get(move, 'unknown')
AttributeError: 'str' object has no attribute 'get'
>>> ================================ RESTART ================================
>>> 
What do you do? e
{'e': 2, 'n': 3, 'w': 4}
{'e': 2, 'n': 3, 'w': 4}
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 76, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 73, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 57, in moveCheck
    location = roomExits.get(move, 'unknown')
AttributeError: 'str' object has no attribute 'get'
>>> ================================ RESTART ================================
>>> 
What do you do? e
{'e': 2, 'n': 3, 'w': 4}
{
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 76, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 73, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 57, in moveCheck
    location = roomExits.get(move, 'unknown')
AttributeError: 'str' object has no attribute 'get'
>>> ================================ RESTART ================================
>>> 
What do you do? e
{'e': 2, 'n': 3, 'w': 4}
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 77, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 54, in moveCheck
    ast.literal_eval("roomExits")
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 86, in literal_eval
    return _convert(node_or_string)
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 85, in _convert
    raise ValueError('malformed node or string: ' + repr(node))
ValueError: malformed node or string: <_ast.Name object at 0x24112d0>
>>> ================================ RESTART ================================
>>> 
What do you do? e
{'e': 2, 'n': 3, 'w': 4}
{'e': 2, 'n': 3, 'w': 4}
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 77, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 56, in moveCheck
    print(roomExits.keys)
AttributeError: 'str' object has no attribute 'keys'
>>> ================================ RESTART ================================
>>> 
What do you do? e
{'e': 2, 'n': 3, 'w': 4}
{'e': 2, 'n': 3, 'w': 4}
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 77, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 56, in moveCheck
    print(roomExits.keys())
AttributeError: 'str' object has no attribute 'keys'
>>> ================================ RESTART ================================
>>> 
What do you do? e
{'e': 2, 'n': 3, 'w': 4}
{'e': 2, 'n': 3, 'w': 4}
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 78, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 75, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 57, in moveCheck
    print(roomExits.keys())
AttributeError: 'str' object has no attribute 'keys'
>>> ================================ RESTART ================================
>>> 
What do you do? e
{'e': 2, 'n': 3, 'w': 4}
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 79, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 76, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 56, in moveCheck
    dict(roomExits)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
{'e': 2, 'n': 3, 'w': 4}
{'e': 2, 'n': 3, 'w': 4}
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 79, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 76, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 60, in moveCheck
    location = roomExits.get(move, 'unknown')
AttributeError: 'str' object has no attribute 'get'
>>> ================================ RESTART ================================
>>> 
What do you do? e
{'e': 2, 'n': 3, 'w': 4}
{'e': 2, 'n': 3, 'w': 4}
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 80, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 77, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 61, in moveCheck
    location = roomExits.get(move, 'unknown')
AttributeError: 'str' object has no attribute 'get'
>>> ================================ RESTART ================================
>>> 
What do you do? e
{'e': 2, 'n': 3, 'w': 4}
{'e': 2, 'n': 3, 'w': 4}
<class 'str'>
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 80, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 77, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 61, in moveCheck
    location = roomExits.get(move, 'unknown')
AttributeError: 'str' object has no attribute 'get'
>>> ================================ RESTART ================================
>>> 
What do you do? e
{'e': 2, 'n': 3, 'w': 4}
{'e': 2, 'n': 3, 'w': 4}
<class 'str'>
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 80, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 77, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 61, in moveCheck
    location = roomExits.get(move, 'unknown')
AttributeError: 'str' object has no attribute 'get'
>>> ================================ RESTART ================================
>>> 
What do you do? e
{'e': 2, 'n': 3, 'w': 4}
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 81, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 78, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 55, in moveCheck
    roomExits = dict([roomExits.strip('{}').split(":"),])
ValueError: dictionary update sequence element #0 has length 4; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
{'e': 2, 'n': 3, 'w': 4}
{'e': 2, 'n': 3, 'w': 4}
<class 'str'>
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 81, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 78, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 62, in moveCheck
    location = roomExits.get(move, 'unknown')
AttributeError: 'str' object has no attribute 'get'
>>> ================================ RESTART ================================
>>> 
What do you do? e
{'e': 2, 'n': 3, 'w': 4}
{'e': 2, 'n': 3, 'w': 4}
<class 'str'>
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 81, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 78, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 62, in moveCheck
    location = roomExits.get(move, 'unknown')
AttributeError: 'str' object has no attribute 'get'
>>> ================================ RESTART ================================
>>> 
What do you do? e
{'e': 2, 'n': 3, 'w': 4}
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 82, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 79, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 57, in moveCheck
    dict(roomExits)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
('e', 2), ('n', 3), ('w', 4)
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 82, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 79, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 57, in moveCheck
    dict(roomExits)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
('e', 2), ('n', 3), ('w', 4)
<class 'str'>
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 83, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 80, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 58, in moveCheck
    dict(roomExits)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
e=2 n=3 w=4
<class 'str'>
e=2 n=3 w=4
<class 'str'>
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 77, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 58, in moveCheck
    location = roomExits.get(move, 'unknown')
AttributeError: 'str' object has no attribute 'get'
>>> ================================ RESTART ================================
>>> 
What do you do? e
('e':2. 'n':3, 'w':4)
<class 'str'>
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 77, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 54, in moveCheck
    dict(roomExits)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
('e':2. 'n':3, 'w':4)
<class 'str'>
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 77, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 54, in moveCheck
    dict(ast.literal_eval(roomExits))
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 47, in literal_eval
    node_or_string = parse(node_or_string, mode='eval')
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 35, in parse
    return compile(source, filename, mode, PyCF_ONLY_AST)
  File "<unknown>", line 1
    ('e':2. 'n':3, 'w':4)
        ^
SyntaxError: invalid syntax
>>> ================================ RESTART ================================
>>> 
What do you do? e
('e':2, 'n':3, 'w':4)
<class 'str'>
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 77, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 54, in moveCheck
    dict(ast.literal_eval(roomExits))
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 47, in literal_eval
    node_or_string = parse(node_or_string, mode='eval')
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 35, in parse
    return compile(source, filename, mode, PyCF_ONLY_AST)
  File "<unknown>", line 1
    ('e':2, 'n':3, 'w':4)
        ^
SyntaxError: invalid syntax
>>> ================================ RESTART ================================
>>> 
What do you do? e
('e:2', 'n:3', 'w:4')
<class 'str'>
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 77, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 54, in moveCheck
    dict(ast.literal_eval(roomExits))
ValueError: dictionary update sequence element #0 has length 3; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
('e', 2, 'n', 3, 'w', 4)
<class 'str'>
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 77, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 54, in moveCheck
    dict(ast.literal_eval(roomExits))
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
('e', 2, 'n', 3, 'w', 4)
<class 'str'>
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 77, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 54, in moveCheck
    dict(roomExits)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
('e', 2, 'n', 3, 'w', 4)
<class 'str'>
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 77, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 54, in moveCheck
    dict([ast,literal_eval(roomExits)])
NameError: global name 'literal_eval' is not defined
>>> ================================ RESTART ================================
>>> 
What do you do? e
('e', 2, 'n', 3, 'w', 4)
<class 'str'>
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 77, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 54, in moveCheck
    dict([ast.literal_eval(roomExits)])
ValueError: dictionary update sequence element #0 has length 6; 2 is required
>>> 
>>> 
>>> 
>>> s = ["'e', 2. 'n', 3"]
>>> s
["'e', 2. 'n', 3"]
>>> dist(s)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    dist(s)
NameError: name 'dist' is not defined
>>> dict(s)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 14; 2 is required
>>> import ast
>>> ast.literal_eval(s)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    ast.literal_eval(s)
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 86, in literal_eval
    return _convert(node_or_string)
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 85, in _convert
    raise ValueError('malformed node or string: ' + repr(node))
ValueError: malformed node or string: ["'e', 2. 'n', 3"]
>>> s = ["'e', 2, 'n', 3"]
>>> dict(s)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 14; 2 is required
>>> ast.literal_eval(s)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    ast.literal_eval(s)
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 86, in literal_eval
    return _convert(node_or_string)
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 85, in _convert
    raise ValueError('malformed node or string: ' + repr(node))
ValueError: malformed node or string: ["'e', 2, 'n', 3"]
>>> ================================ RESTART ================================
>>> 
What do you do? e
('e', 2), ('n', 3), ('w', 4)
<class 'str'>
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 77, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 54, in moveCheck
    dict([ast.literal_eval(roomExits)])
ValueError: dictionary update sequence element #0 has length 3; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
["('e', 2), ('n', 3), ('w', 4)"]
<class 'list'>
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 78, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 75, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 55, in moveCheck
    dict([ast.literal_eval(roomExits)])
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 86, in literal_eval
    return _convert(node_or_string)
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 85, in _convert
    raise ValueError('malformed node or string: ' + repr(node))
ValueError: malformed node or string: ["('e', 2), ('n', 3), ('w', 4)"]
>>> ================================ RESTART ================================
>>> 
What do you do? e
[(('e', 2), ('n', 3), ('w', 4))]
<class 'list'>
[(('e', 2), ('n', 3), ('w', 4))]
<class 'list'>
That's not a valid direction!
>>> ================================ RESTART ================================
>>> 
What do you do? e
[(('e', 2), ('n', 3), ('w', 4))]
<class 'list'>
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 79, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 76, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 55, in moveCheck
    dict(roomExits)
ValueError: dictionary update sequence element #0 has length 3; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 79, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 76, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 52, in moveCheck
    roomExits.append(rooms[location].getExits()).split
AttributeError: 'NoneType' object has no attribute 'split'
>>> ================================ RESTART ================================
>>> 
What do you do? e
('e', 2), ('n', 3), ('w', 4)
<class 'str'>
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 79, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 76, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 55, in moveCheck
    dict(roomExits)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> ================================ RESTART ================================
>>> 
What do you do? e
{'e':2, 'n':3, 'w':4}
<class 'str'>
{'e':2, 'n':3, 'w':4}
<class 'str'>
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 77, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 58, in moveCheck
    location = roomExits.get(move, 'unknown')
AttributeError: 'str' object has no attribute 'get'
>>> ================================ RESTART ================================
>>> 
What do you do? e
<class 'dict'>
{'e':2, 'n':3, 'w':4}
<class 'str'>
{'e':2, 'n':3, 'w':4}
<class 'str'>
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 79, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 76, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 60, in moveCheck
    location = roomExits.get(move, 'unknown')
AttributeError: 'str' object has no attribute 'get'
>>> ================================ RESTART ================================
>>> 
What do you do? e
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 77, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 74, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 52, in moveCheck
    print(roomExits)
UnboundLocalError: local variable 'roomExits' referenced before assignment
>>> ================================ RESTART ================================
>>> 
What do you do? e
{'e':2, 'n':3, 'w':4}
<class 'str'>
{'n': 3, 'w': 4, 'e': 2}
<class 'dict'>
2
>>> ================================ RESTART ================================
>>> 
What do you do? e
{'e':2, 'n':3, 'w':4}
<class 'str'>
{'n': 3, 'w': 4, 'e': 2}
<class 'dict'>
2
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 78, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 75, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 60, in moveCheck
    print(roomExits.getName(location))
AttributeError: 'dict' object has no attribute 'getName'
>>> ================================ RESTART ================================
>>> 
What do you do? e
{'e':2, 'n':3, 'w':4}
<class 'str'>
{'e': 2, 'w': 4, 'n': 3}
<class 'dict'>
2
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 78, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 75, in main
    moveCheck(rooms, move, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 60, in moveCheck
    print(rooms.getName(location))
AttributeError: 'list' object has no attribute 'getName'
>>> ================================ RESTART ================================
>>> 
What do you do? e
{'e':2, 'n':3, 'w':4}
<class 'str'>
{'e': 2, 'w': 4, 'n': 3}
<class 'dict'>
2
Sitting Room
>>> ================================ RESTART ================================
>>> 
What do you do? e
2
Sitting Room
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 90, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 87, in main
    action = gamePlay(rooms, action, location)
UnboundLocalError: local variable 'action' referenced before assignment
>>> ================================ RESTART ================================
>>> 
What do you do? e
2
Sitting Room
What do you do? e
2
Sitting Room
What do you do? w
4
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 91, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 88, in main
    play = gamePlay(rooms, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 53, in gamePlay
    moveCheck(rooms, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 69, in moveCheck
    print(rooms[location].getName())
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
What do you do? e
2
Sitting Room
What do you do? w
4
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 91, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 88, in main
    play = gamePlay(rooms, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 53, in gamePlay
    moveCheck(rooms, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 69, in moveCheck
    print(rooms[location].getName())
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
What do you do? w
4
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 91, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 88, in main
    play = gamePlay(rooms, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 53, in gamePlay
    moveCheck(rooms, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 69, in moveCheck
    print(rooms[location].getName())
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
What do you do? e
2
Sitting Room
What do you do? w
4
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 91, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 88, in main
    play = gamePlay(rooms, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 53, in gamePlay
    moveCheck(rooms, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 69, in moveCheck
    print(rooms[location].getName())
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
What do you do? e
2
Sitting Room
What do you do? w
4
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 91, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 88, in main
    play = gamePlay(rooms, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 53, in gamePlay
    moveCheck(rooms, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 69, in moveCheck
    print(rooms[location].getName())
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
What do you do? e
2
Sitting Room
What do you do? w
4
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 91, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 88, in main
    play = gamePlay(rooms, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 53, in gamePlay
    lcoation = moveCheck(rooms, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 69, in moveCheck
    print(rooms[location].getName())
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
What do you do? e
2
Sitting Room
What do you do? w
1
Parlor Room
What do you do? e
1
Parlor Room
What do you do? w
That's not a valid direction!
What do you do? e
1
Parlor Room
What do you do? e
1
Parlor Room
What do you do? e
1
Parlor Room
What do you do? n
That's not a valid direction!
What do you do? s
That's not a valid direction!
What do you do? w
That's not a valid direction!
What do you do? e
1
Parlor Room
What do you do? e
1
Parlor Room
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? e
1
Parlor Room
What do you do? w
0
Entryway
What do you do? w
2
Sitting Room
What do you do? n
5
The kitchen
What do you do? s
3
Hallway
What do you do? e
4
Stairs up
What do you do? w
3
Hallway
What do you do? s
0
Entryway
What do you do? n
3
Hallway
What do you do? n
5
The kitchen
What do you do? e
6
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 91, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 88, in main
    play = gamePlay(rooms, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 53, in gamePlay
    location = moveCheck(rooms, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 69, in moveCheck
    print(rooms[location].getName())
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
What do you do? w
2
Sitting Room
What do you do? e
0
Entryway
What do you do? w
2
Sitting Room
What do you do? e
0
Entryway
What do you do? w
2
Sitting Room
What do you do? e
0
Entryway
What do you do? e
1
Parlor Room
What do you do? w
0
Entryway
What do you do? e
1
Parlor Room
What do you do? n
6
Dining room
What do you do? w
5
The kitchen
What do you do? s
3
Hallway
What do you do? s
0
Entryway
What do you do? n
3
Hallway
What do you do? e
4
Stairs up
What do you do? w
3
Hallway
What do you do? s
0
Entryway
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? e
1
The parlor room.
What do you do? w
0
The entryway to the haunted house.
What do you do? w
2
The sitting room.
What do you do? n
5
The kitchen.
What do you do? w
That's not a valid direction!
What do you do? e
6
The Dining room.
What do you do? s
1
The parlor room.
What do you do? s
That's not a valid direction!
What do you do? e
That's not a valid direction!
What do you do? w
0
The entryway to the haunted house.
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? e
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 99, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 96, in main
    play = gamePlay(rooms, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 52, in gamePlay
    action1, action2 = menuChoices()
ValueError: need more than 1 value to unpack
>>> ================================ RESTART ================================
>>> 
What do you do?e
I'm not sure what you're trying to do!
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 99, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 96, in main
    play = gamePlay(rooms, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 52, in gamePlay
    action1, action2 = menuChoices2()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 69, in menuChoices2
    return action1, action2
UnboundLocalError: local variable 'action1' referenced before assignment
>>> ================================ RESTART ================================
>>> 
What do you do?go north
That's not a valid direction!
What do you do?
>>> ================================ RESTART ================================
>>> 

What do you do? go north
That's not a valid direction!
What do you do? e
I'm not sure what you're trying to do!
1
Parlor Room
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? go north
That's not a valid direction!
What do you do? n
3
Hallway
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? e
1
Parlor Room
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? e
1
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
What do you do? w
0
You are in the entryway to the haunted house. You see a hallway to the north, and doors to the east and west.
What do you do? 
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 112, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 104, in main
    rooms = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 51, in roomSetup
    rooms.append(makeRooms(line))
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 43, in makeRooms
    roomNumber, name, longDescription, shortDescription, exitDescription, exits, items = infoStr.split("\t")
ValueError: need more than 6 values to unpack
>>> ================================ RESTART ================================
>>> 
What do you do? e
1
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 112, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 109, in main
    play = gamePlay(rooms, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 62, in gamePlay
    location = moveCheck(rooms, action1, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 90, in moveCheck
    print(rooms[location].getExitDescription())
AttributeError: 'Rooms' object has no attribute 'getExitDescription'
>>> ================================ RESTART ================================
>>> 
What do you do? e
1
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
What do you do? w
0
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? n
3
You enter a long, dark hallway.
There are stairs to the east, and a doorway to the north.
What do you do? n
5
The kitchen.
There are doors to the south, and east.
What do you do? e
6
The Dining room.
There are doors to the south, and west.
What do you do? q
That's not a valid direction!
What do you do? q
That's not a valid direction!
What do you do? 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 112, in <module>
    location = roomExits.get(move, 'unknown')
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 109, in main
    roomExitsStr = rooms[location].getExits()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 61, in gamePlay
    def getExitDescription(self):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 73, in menuChoices2
    infile = open(roomsfile, 'r')
KeyboardInterrupt
>>> 
>>> 
>>> 
>>> lst = [(1, 3, 4), (2, 4)]
>>> lst
[(1, 3, 4), (2, 4)]
>>> 2 in lst
False
>>> 2 in lst[1]
True
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 155, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 145, in main
    rooms = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 76, in roomSetup
    rooms.append(makeRooms(line))
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 68, in makeRooms
    roomNumber, name, longDescription, shortDescription, exitDescription, exits, items = infoStr.split("\t")
ValueError: need more than 6 values to unpack
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 155, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 147, in main
    items = itemsSetup()
NameError: global name 'itemsSetup' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 155, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 147, in main
    items = itemsSetup()
NameError: global name 'itemsSetup' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 155, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 147, in main
    items = itemsSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 33, in itemsSetup
    items.append(makeItems(line))
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 25, in makeItems
    itemID, name, itemLocation, friendlyLocation, longDescription, shortDescription, actions, gettable, doable, hidden = infoStr.split("\t")
ValueError: need more than 1 value to unpack
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 155, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 147, in main
    items = itemsSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 33, in itemsSetup
    items.append(makeItems(line))
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 25, in makeItems
    itemID, name, itemLocation, friendlyLocation, longDescription, shortDescription, actions, gettable, doable, hidden = infoStr.split("\t")
ValueError: need more than 1 value to unpack
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 155, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 147, in main
    items = itemsSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 33, in itemsSetup
    items.append(makeItems(line))
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 25, in makeItems
    itemID, name, itemLocation, friendlyLocation, longDescription, shortDescription, actions, gettable, doable, hidden = infoStr.split("\t")
ValueError: too many values to unpack (expected 10)
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 155, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 147, in main
    items = itemsSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 33, in itemsSetup
    items.append(makeItems(line))
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 25, in makeItems
    itemID, name, itemLocation, friendlyLocation, longDescription, shortDescription, actions, gettable, doable, hidden = infoStr.split("\t")
ValueError: too many values to unpack (expected 10)
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 155, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 147, in main
    items = itemsSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 33, in itemsSetup
    items.append(makeItems(line))
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 25, in makeItems
    self, itemID, name, itemLocation, friendlyLocation, longDescription, shortDescription, actions, gettable, doable, hidden = infoStr.split("\t")
ValueError: need more than 10 values to unpack
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 156, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 148, in main
    items = itemsSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 34, in itemsSetup
    items.append(makeItems(line))
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 26, in makeItems
    self, itemID, name, itemLocation, friendlyLocation, longDescription, shortDescription, actions, gettable, doable, hidden = infoStr.split("\t")
ValueError: need more than 10 values to unpack
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 156, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 148, in main
    items = itemsSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 34, in itemsSetup
    items.append(makeItems(line))
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 27, in makeItems
    return Items(self, itemID, name, itemLocation, friendlyLocation, longDescription, shortDescription, actions, gettable, doable, hidden)
NameError: global name 'self' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 156, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 148, in main
    items = itemsSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 34, in itemsSetup
    items.append(makeItems(line))
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 26, in makeItems
    itemID, name, itemLocation, friendlyLocation, longDescription, shortDescription, actions, gettable, doable, hidden = infoStr.split("\t")
ValueError: too many values to unpack (expected 10)
>>> ================================ RESTART ================================
>>> 
What do you do? eValueError: too many values to unpack (expected
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 156, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 153, in main
    play = gamePlay(rooms, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 87, in gamePlay
    action1, action2 = menuChoices2()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 99, in menuChoices2
    action = input("What do you do? ")
KeyboardInterrupt
>>> ================================ RESTART ================================
>>> 
What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 156, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 153, in main
    play = gamePlay(rooms, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 88, in gamePlay
    location = moveCheck(rooms, action1, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 117, in moveCheck
    stuff = stuffInTheRoom(location, items)
NameError: global name 'stuffInTheRoom' is not defined
>>> ================================ RESTART ================================
>>> 
What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 156, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 153, in main
    play = gamePlay(rooms, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 88, in gamePlay
    location = moveCheck(rooms, action1, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 117, in moveCheck
    stuff = itemCheck(location, items)
NameError: global name 'items' is not defined
>>> ================================ RESTART ================================
>>> 
What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 156, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 153, in main
    play = gamePlay(rooms, items, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 88, in gamePlay
    location = moveCheck(rooms, items, action1, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 117, in moveCheck
    stuff = itemCheck(location, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 125, in itemCheck
    for n in numItems:
TypeError: 'int' object is not iterable
>>> ================================ RESTART ================================
>>> 
What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 156, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 153, in main
    play = gamePlay(rooms, items, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 88, in gamePlay
    location = moveCheck(rooms, items, action1, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 117, in moveCheck
    stuff = itemCheck(location, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 125, in itemCheck
    for n in numItems():
TypeError: 'int' object is not callable
>>> ================================ RESTART ================================
>>> 
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 156, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 153, in main
    play = gamePlay(rooms, items, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 87, in gamePlay
    verb, noun = menuChoices2()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 107, in menuChoices2
    return verb, noun
UnboundLocalError: local variable 'noun' referenced before assignment
>>> ================================ RESTART ================================
>>> 
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 157, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 154, in main
    play = gamePlay(rooms, items, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 87, in gamePlay
    verb, noun = menuChoices2()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 108, in menuChoices2
    return verb, noun
UnboundLocalError: local variable 'noun' referenced before assignment
>>> ================================ RESTART ================================
>>> 
What do you do? go west
That's not a valid direction!
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 157, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 154, in main
    play = gamePlay(rooms, items, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 88, in gamePlay
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 118, in moveCheck
    stuff = itemCheck(location, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 126, in itemCheck
    for n in numItems:
TypeError: 'int' object is not iterable
>>> ================================ RESTART ================================
>>> 
What do you do? wTypeError: 'int' object is not iterable
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 157, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 154, in main
    play = gamePlay(rooms, items, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 87, in gamePlay
    verb, noun = menuChoices2()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 99, in menuChoices2
    action = input("What do you do? ")
KeyboardInterrupt
>>> ================================ RESTART ================================
>>> 
What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.


There's nothing in the room!
What do you do? e
0
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.


There's nothing in the room!
What do you do? e
1
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.


There's nothing in the room!
What do you do? w
0
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.


There's nothing in the room!
What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.


There's nothing in the room!
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
2


There's nothing in the room!
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
2
1

2

There's nothing in the room!
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
2
1

2

There's nothing in the room!
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
2
1

2

There's nothing in the room!
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
2
1
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 162, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 159, in main
    play = gamePlay(rooms, items, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 88, in gamePlay
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 118, in moveCheck
    stuff = itemCheck(location, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 130, in itemCheck
    print(items[n].ItemName())
AttributeError: 'Items' object has no attribute 'ItemName'
>>> ================================ RESTART ================================
>>> 
What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
2
1
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 162, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 159, in main
    play = gamePlay(rooms, items, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 88, in gamePlay
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 118, in moveCheck
    stuff = itemCheck(location, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 130, in itemCheck
    print(items[n].itemName())
AttributeError: 'Items' object has no attribute 'itemName'
>>> ================================ RESTART ================================
>>> 
What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
2
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 192, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 189, in main
    play = gamePlay(rooms, items, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 118, in gamePlay
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 148, in moveCheck
    stuff = itemCheck(location, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 158, in itemCheck
    print(items[n].getItemLocation())
AttributeError: 'Items' object has no attribute 'getItemLocation'
>>> ================================ RESTART ================================
>>> 
What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
2
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 192, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 189, in main
    play = gamePlay(rooms, items, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 118, in gamePlay
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 148, in moveCheck
    stuff = itemCheck(location, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 158, in itemCheck
    print(items[n].getItemLocation())
AttributeError: 'Items' object has no attribute 'getItemLocation'
>>> ================================ RESTART ================================
>>> 
What do you do? wAttributeError: 'Items' object has no attribute 'getItemLocation'
That's not a valid direction!
What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
2
1
gun

2
comb

There's nothing in the room!
What do you do? 
>>> ================================ RESTART ================================
>>> 
w
What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
1
gun

2
comb

There's nothing in the room!
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
2
1
gun

2
2
comb

There's nothing in the room!
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
<class 'int'>
<class 'str'>
gun

<class 'int'>
<class 'str'>
comb

There's nothing in the room!
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
<class 'int'>
<class 'int'>
gun

<class 'int'>
<class 'int'>
comb
comb
There is a  ['comb'] .
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.

comb
There is a  ['comb'] .
What do you do? e
0
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.


There's nothing in the room!
What do you do? e
1
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
gun

There is a  ['gun'] .
What do you do? n
6
The Dining room.
There are doors to the south, and west.


There's nothing in the room!
What do you do? s
1
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
gun

There is a  ['gun'] .
What do you do? 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 189, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 186, in main
    play = gamePlay(rooms, items, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 117, in gamePlay
    verb, noun = menuChoices2()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 129, in menuChoices2
    action = input("What do you do? ")
KeyboardInterrupt
>>> 
>>> 
>>> 
>>> lst = ["gun", "comb"]
>>> lst
['gun', 'comb']
>>> ================================ RESTART ================================
>>> 
What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.

comb
There is a  comb .
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.

comb
There is a comb .
What do you do? e
0
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.


There's nothing in the room!
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.

comb
There is a comb .
What do you do? e
0
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.


What do you do? e
1
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
gun

There is a gun .
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 194, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 191, in main
    play = gamePlay(rooms, items, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 122, in gamePlay
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 152, in moveCheck
    stuff = itemCheck(location, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 173, in itemCheck
    print("There are ", (stuffInTheRoom), ".")
NameError: global name 'stuffInTheRoom' is not defined
>>> ================================ RESTART ================================
>>> 
What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 194, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 191, in main
    play = gamePlay(rooms, items, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 122, in gamePlay
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 152, in moveCheck
    stuff = itemCheck(location, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure.py", line 163, in itemCheck
    print(items[n].getDroppedItemDescription())
AttributeError: 'Items' object has no attribute 'getDroppedItemDescription'
>>> ================================ RESTART ================================
>>> 
What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
There is a comb among the wreckage.
What do you do? e
0
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
1
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
You can see a gun on the floor.
What do you do? go north
That's not a valid direction!
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? go west
That's not a valid direction!
What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
There is a comb among the wreckage.
What do you do? q
That's not a valid direction!
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
There is a comb among the wreckage.
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
That's not a valid direction!
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 180, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 177, in main
    play = gamePlay(rooms, items, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 123, in gamePlay
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 149, in moveCheck
    print("That's not a valid direction!")
KeyboardInterrupt
>>> ================================ RESTART ================================
>>> 
What do you do? w
What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
There is a comb among the wreckage.
What do you do? e
0
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
1
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
You can see a gun on the floor.
What do you do? w
0
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
There is a comb among the wreckage.
What do you do? q
That's not a valid direction!
>>> q
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    q
NameError: name 'q' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 180, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 177, in main
    play = gamePlay(rooms, items, action, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 121, in gamePlay
    while not gameOver(verb):
UnboundLocalError: local variable 'verb' referenced before assignment
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 180, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 177, in main
    play = gamePlay(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 121, in gamePlay
    while not gameOver(verb):
UnboundLocalError: local variable 'verb' referenced before assignment
>>> ================================ RESTART ================================
>>> 
What do you do? e
1
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
You can see a gun on the floor.
What do you do? e
That's not a valid direction!
What do you do? w
0
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
There is a comb among the wreckage.
What do you do? e
0
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? q
That's not a valid direction!
>>> q
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    q
NameError: name 'q' is not defined
>>> ================================ RESTART ================================
>>> 
That's not a valid direction!
What do you do? e
1
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
You can see a gun on the floor.
What do you do? w
0
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? q
>>> ================================ RESTART ================================
>>> 
That's not a valid direction!
What do you do? e
1
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
You can see a gun on the floor.
What do you do? q
>>> ================================ RESTART ================================
>>> 
What do you do? w
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
There is a comb among the wreckage.
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 189, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 186, in main
    play = gamePlay(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 123, in gamePlay
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 151, in moveCheck
    print(roomDescription(location))
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 166, in roomDescription
    print(rooms[location].getLongDescription())
NameError: global name 'rooms' is not defined
>>> ================================ RESTART ================================
>>> 
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 189, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 186, in main
    play = gamePlay(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 123, in gamePlay
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 151, in moveCheck
    print(roomDescription(location, rooms))
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 168, in roomDescription
    stuff = itemCheck(location, items)
NameError: global name 'items' is not defined
>>> ================================ RESTART ================================
>>> 
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
There is a comb among the wreckage.
None
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
None
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
You can see a gun on the floor.
None
What do you do? e
That's not a valid direction!
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
None
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
There is a comb among the wreckage.
None
What do you do? n
The kitchen.
There are doors to the south, and east.
None
What do you do? e
The Dining room.
There are doors to the south, and west.
None
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
None
There are doors to the east and north.
None
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There are doors to the east and north.
None
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
None
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? w
There is a comb among the wreckage.
None
What do you do? e
None
What do you do? e
You can see a gun on the floor.
None
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
None
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
None
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
None
There are doors to the east and north.
None
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
None
There are doors to the east and north.
What do you do? e
You are in the entryway to the haunted house.
None
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
None
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
None
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
None
There are doors to the east and north.
What do you do? n
The kitchen.
None
There are doors to the south, and east.
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There are doors to the east and north.
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? n
The Dining room.
There are doors to the south, and west.
What do you do? n
That's not a valid direction!
What do you do? 
>>> ================================ RESTART ================================
>>> 

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There are doors to the east and north.
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There are doors to the east and north.
What do you do? n
The kitchen.
There are doors to the south, and east.
What do you do? s
You enter a long, dark hallway.
There are stairs to the east, and a doorway to the north.
What do you do? s
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? n
The Dining room.
There are doors to the south, and west.
What do you do? w
The kitchen.
There are doors to the south, and east.
What do you do? s
You enter a long, dark hallway.
There are stairs to the east, and doorways to the north and south.
What do you do? s
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? q
That's not a valid direction!
>>> 
>>> 
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
What do you do? e
What do you do? e
What do you do? q
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There are doors to the east and north.
What do you do? q
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 196, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 193, in main
    gamePlay(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 123, in gamePlay
    verbAndNounCheck(verb, noun)
TypeError: verbAndNounCheck() missing 3 required positional arguments: 'rooms', 'items', and 'location'
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 196, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 193, in main
    gamePlay(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 123, in gamePlay
    verbAndNounCheck(verb, noun, rooms, items, locations)
NameError: global name 'locations' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
Huh?
What do you do? go north
That's not a valid direction!
What do you do? west
Huh?
What do you do? go
That's not a valid direction!
What do you do? walk north
Huh?
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
Huh?
What do you do? go west
That's not a valid direction!
What do you do? q
Huh?
>>> 
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There are doors to the east and north.
What do you do? go east
That's not a valid direction!
What do you do? walk east
That's not a valid direction!
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? go west
go west
That's not a valid direction!
What do you do? go w
go w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? go west
go west
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There are doors to the east and north.
What do you do? run north
run north
You enter a long, dark hallway.
There are stairs to the east, and doorways to the north and south.
What do you do? s
s  
That's not a valid direction!
What do you do? n
n  
You enter a long, dark hallway.
There are stairs to the east, and doorways to the north and south.
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? w
w  
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
w  
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There are doors to the east and north.
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? west
west  
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There are doors to the east and north.
What do you do? east
east  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? w
w  
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There are doors to the east and north.
What do you do? w
w  
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There are doors to the east and north.
What do you do? w
w  
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There are doors to the east and north.
What do you do? go west
go west
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? go east
go east
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? go west
go west
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There are doors to the east and north.
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? w
w  
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There are doors to the east and north.
What do you do? n
n  
You enter a long, dark hallway.
There are stairs to the east, and doorways to the north and south.
What do you do? s
s  
That's not a valid direction!
What do you do? n
n  
You enter a long, dark hallway.
There are stairs to the east, and doorways to the north and south.
What do you do? n
n  
You enter a long, dark hallway.
There are stairs to the east, and doorways to the north and south.
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? w
w  
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There are doors to the east and north.
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? w
w  
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There are doors to the east and north.
What do you do? w
w  
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There are doors to the east and north.
What do you do? n
n  
You enter a long, dark hallway.
There are stairs to the east, and doorways to the north and south.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
1
What do you do? w
w  
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There are doors to the east and north.
2
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
1
What do you do? w
w  
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There are doors to the east and north.
2
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
0
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
1
0
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
0
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
1
0
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
0
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
1
0
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
0
What do you do? 
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 205, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 201, in main
    roomDescription(location, rooms, items)
NameError: global name 'location' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
0
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
1
0
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
0
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
1
0
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
0
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
1
0
0
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
0
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
1
dir 0
0
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
gamep 0
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
1
dir 0
gamep 0
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
gamep 0
What do you do? e
e  
mc1 0
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
mc2 1
mc3 1
dir 0
gamep 0
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
gamep 0
What do you do? e
e  
mc1 0
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
mc2 1
dir 0
gamep 0
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
gamep 0
What do you do? e
e  
mc1 0
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
mc2 1
dir 1
gamep 1
What do you do? w
w  
mc1 1
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
mc2 0
dir 0
gamep 0
What do you do? w
w  
mc1 0
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There are doors to the east and north.
mc2 2
dir 2
gamep 2
What do you do? n
n  
mc1 2
The kitchen.
There are doors to the south, and east.
mc2 5
dir 5
gamep 5
What do you do? e
e  
mc1 5
The Dining room.
There are doors to the south, and west.
mc2 6
dir 6
gamep 6
What do you do? s
s  
mc1 6
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
mc2 1
dir 1
gamep 1
What do you do? go west
go west
mc1 1
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
mc2 0
verb 1
gamep 1
What do you do? walk north
walk north
mc1 1
The Dining room.
There are doors to the south, and west.
mc2 6
verb 1
gamep 1
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
gamep 0
What do you do? walk east
walk east
mc1 0
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
mc2 1
verb 1
gamep 1
What do you do? go west
go west
mc1 1
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
mc2 0
verb 0
gamep 0
What do you do? n
n  
mc1 0
You enter a long, dark hallway.
There are stairs to the east, and doorways to the north and south.
mc2 3
dir 3
gamep 3
What do you do? n
n  
mc1 3
The kitchen.
There are doors to the south, and east.
mc2 5
dir 5
gamep 5
What do you do? s
s  
mc1 5
You enter a long, dark hallway.
There are stairs to the east, and doorways to the north and south.
mc2 3
dir 3
gamep 3
What do you do? s
s  
mc1 3
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
mc2 0
dir 0
gamep 0
What do you do? e
e  
mc1 0
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
mc2 1
dir 1
gamep 1
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
gamep 0
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
gamep None
What do you do? w
w  
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 204, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 201, in main
    gamePlay(rooms, items, verb)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 125, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 153, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 160, in moveCheck
    roomExitsStr = rooms[location].getExits()
TypeError: list indices must be integers, not NoneType
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? w
w  
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? n
n  
You enter a long, dark hallway.
There are stairs to the east, and doorways to the north and south.
What do you do? go south
go south
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? run north
run north
You enter a long, dark hallway.
There are stairs to the east, and doorways to the north and south.
What do you do? run north
run north
The kitchen.
There are doors to the south, and east.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? w
w  
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
w  
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
get gun
You pick up the  gun
There is no  gun to get!
There is no  gun to get!
What do you do? w
w  
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 213, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 210, in main
    gamePlay(rooms, items, verb)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 124, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 153, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 169, in moveCheck
    roomExitsStr = rooms[location].getExits()
TypeError: list indices must be integers, not NoneType
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
get gun
You pick up the gun .
There is no  gun to get!
There is no  gun to get!
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? e
e  
That's not a valid direction!
What do you do? get gun
get gun
You pick up the gun .
What do you do? w
w  
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
w  
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? take comb
take comb
There is no  comb to get!
You pick up the comb .
What do you do? get kjhkjh
get kjhkjh
There is no  kjhkjh to get!
There is no  kjhkjh to get!
There is no  kjhkjh to get!
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
get gun
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 222, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 219, in main
    gamePlay(rooms, items, verb)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 124, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 162, in verbAndNounCheck
    pickup = true
NameError: global name 'true' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
get gun
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 222, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 219, in main
    gamePlay(rooms, items, verb)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 124, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 162, in verbAndNounCheck
    pickup = a
NameError: global name 'a' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
get gun
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 223, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 220, in main
    gamePlay(rooms, items, verb)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 124, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 163, in verbAndNounCheck
    pickup = true
NameError: global name 'true' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
get gun
There is no gun to get!
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
get gun
You pick up the gun .
What do you do? w
w  
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
w  
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? take bomb
take bomb
You pick up the bomb .
What do you do? get gjg
get gjg
There is no gjg to get!
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
e  
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
get gun
You pick up the gun .
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
What do you do? w
You are in the entryway to the haunted house.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 221, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 218, in main
    gamePlay(rooms, items, verb)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 124, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 154, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 183, in moveCheck
    roomDescription(location, rooms, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 200, in roomDescription
    itemCheck(location, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 192, in itemCheck
    checkLocation = eval(items[n].getItemLocation())
  File "<string>", line 1, in <module>
NameError: name 'i' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
What do you do? w
You are in the entryway to the haunted house.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 221, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 218, in main
    gamePlay(rooms, items, verb)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 124, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 154, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 183, in moveCheck
    roomDescription(location, rooms, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 200, in roomDescription
    itemCheck(location, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 192, in itemCheck
    checkLocation = eval(items[n].getItemLocation())
TypeError: eval() arg 1 must be a string, bytes or code object
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
What do you do? w
You are in the entryway to the haunted house.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 221, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 218, in main
    gamePlay(rooms, items, verb)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 124, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 154, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 183, in moveCheck
    roomDescription(location, rooms, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 200, in roomDescription
    itemCheck(location, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 192, in itemCheck
    checkLocation = eval(items[n].getItemLocation())
TypeError: eval() arg 1 must be a string, bytes or code object
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
What do you do? w
You are in the entryway to the haunted house.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 221, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 218, in main
    gamePlay(rooms, items, verb)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 124, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 154, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 183, in moveCheck
    roomDescription(location, rooms, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 200, in roomDescription
    itemCheck(location, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 192, in itemCheck
    checkLocation = eval(items[n].getItemLocation())
TypeError: eval() arg 1 must be a string, bytes or code object
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
What do you do? get khjsdf
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 225, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 222, in main
    gamePlay(rooms, items, verb)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 124, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 159, in verbAndNounCheck
    checkLocation = eval(items[n].getItemLocation())
TypeError: eval() arg 1 must be a string, bytes or code object
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
1
9
You pick up the gun .
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
1
9
You pick up the gun .
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
<class 'str'>
1
<class 'int'>
9
You pick up the gun .
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
<class 'str'>
1
<class 'str'>
9
You pick up the gun .
What do you do? get gun
There is no gun to get!
There is no gun to get!
There is no gun to get!
What do you do? get gsfh
There is no gsfh to get!
There is no gsfh to get!
There is no gsfh to get!
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
<class 'str'>
1
<class 'str'>
i
You pick up the gun .
What do you do? get shaskdfjh
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 229, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 226, in main
    gamePlay(rooms, items, verb)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 124, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 159, in verbAndNounCheck
    checkLocation = eval(items[n].getItemLocation())
  File "<string>", line 1, in <module>
NameError: name 'i' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
<class 'str'>
1
<class 'str'>
-1
You pick up the gun .
What do you do? get gun
There is no gun to get!
There is no gun to get!
There is no gun to get!
What do you do? get glkjsdf
There is no glkjsdf to get!
There is no glkjsdf to get!
There is no glkjsdf to get!
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? get bomb
There is no bomb to get!
There is no bomb to get!
<class 'str'>
2
<class 'str'>
-1
You pick up the bomb .
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
What do you do? get gun
There is no gun to get!
There is no gun to get!
There is no gun to get!
There is no gun to get!
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
What do you do? get gun
There is no gun to get!
What do you do? get gun
There is no gun to get!
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? get bomb
There is no bomb to get!
What do you do? get sdfhakhdf
There is no sdfhakhdf to get!
What do you do? get comb
You pick up the comb .
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
What do you do? inv
gun
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
What do you do? inv
In your inventory you have:
gun
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
Rats scurry across the floor.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
Rats scurry across the floor.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
Somewhere upstairs, you hear a piercing scream.
What do you do? n
The kitchen.
There are doors to the south, and east.
Somewhere upstairs, you hear a piercing scream.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
Rats scurry across the floor.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a comb among the wreckage.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 258, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 251, in main
    randomNoises = randomNoisesSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 126, in randomNoisesSetup
    randomNoise.append(line)
NameError: global name 'randomNoise' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear footsteps.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? 
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 257, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 249, in main
    items = itemsSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 70, in itemsSetup
    items.append(makeItems(line))
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 62, in makeItems
    itemID, itemName, itemLocation, itemFriendlyLocation, itemLongDescription, itemShortDescription,itemDroppedDescription, itemActions, itemGettable, itemDoable, itemHidden = infoStr.split("\\")
ValueError: need more than 1 value to unpack
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
Rats scurry across the floor.

What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
Rats scurry across the floor.

What do you do? get gun
You pick up the gun .
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? inv
In your inventory you have:
gun
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
Rats scurry across the floor.

What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
You hear footsteps.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
You hear faint laughter.

What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear footsteps.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 258, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 255, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 169, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 201, in moveCheck
    roomDescription(location, rooms, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 219, in roomDescription
    itemCheck(location, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 212, in itemCheck
    if (checkLocation == location) and (items[n].itemHidden() == "false"):
TypeError: 'str' object is not callable
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear footsteps.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 258, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 254, in main
    roomDescription(location, rooms, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 219, in roomDescription
    itemCheck(location, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 211, in itemCheck
    print(items[n].itemHidden())
TypeError: 'str' object is not callable
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
false

false

false
You see a hallway to the north, and doors to the east and west.
You hear footsteps.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
false

false

false
There are doors to the west and north.
Rats scurry across the floor.

What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
<class 'str'>
<class 'str'>
<class 'str'>
You see a hallway to the north, and doors to the east and west.
Rats scurry across the floor.

What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
<class 'str'>
<class 'str'>
<class 'str'>
There are doors to the west and north.
Rats scurry across the floor.

What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
<class 'str'>
<class 'str'>
<class 'str'>
You see a hallway to the north, and doors to the east and west.
Rats scurry across the floor.

What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
<class 'str'>
<class 'str'>
<class 'str'>
There are doors to the west and north.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
Rats scurry across the floor.

What do you do? e
That's not a valid direction!
Rats scurry across the floor.

What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
You hear faint laughter.

What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
false

false

false
You see a hallway to the north, and doors to the east and west.
You hear footsteps.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
false

false

false
There are doors to the west and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear faint laughter.

What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 258, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 255, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 169, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 201, in moveCheck
    roomDescription(location, rooms, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 219, in roomDescription
    itemCheck(location, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 212, in itemCheck
    if (checkLocation == location) and (checkHidden == false):
NameError: global name 'false' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear faint laughter.

What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
You hear footsteps.
What do you do? e
That's not a valid direction!
You hear faint laughter.

What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
Rats scurry across the floor.

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a bomb among the wreckage.
There are doors to the east and north.
You hear faint laughter.

What do you do? get bomb
You pick up the bomb .
Rats scurry across the floor.

What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
Rats scurry across the floor.

What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? get gun
You pick up the gun .
You hear faint laughter.

What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
Rats scurry across the floor.

What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
You hear faint laughter.

What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear footsteps.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
You hear faint laughter.

What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a bomb among the wreckage.
There are doors to the east and north.
Rats scurry across the floor.

What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
Rats scurry across the floor.

What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear footsteps.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear faint laughter.

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
Rats scurry across the floor.

What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a bomb among the wreckage.
There are doors to the east and north.
You hear faint laughter.

What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
Rats scurry across the floor.

What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
You hear footsteps.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear footsteps.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a bomb among the wreckage.
There are doors to the east and north.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear footsteps.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
You hear footsteps.
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear faint laughter.

What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear faint laughter.

What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
Rats scurry across the floor.

What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
Rats scurry across the floor.

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a bomb among the wreckage.
There are doors to the east and north.
You hear footsteps.
What do you do? w
That's not a valid direction!
You hear footsteps.
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear footsteps.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
You hear footsteps.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear faint laughter.

What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a bomb among the wreckage.
There are doors to the east and north.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a bomb among the wreckage.

There are doors to the east and north.
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear faint laughter.

What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? w
That's not a valid direction!
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
gun
comb
bomb
You see a hallway to the north, and doors to the east and west.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
gun
comb
bomb
There are doors to the west and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
gun
comb
bomb
End
You see a hallway to the north, and doors to the east and west.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
gun
comb
bomb
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
gun
comb
bomb
There are doors to the west and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear footsteps.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
What do you do? e
That's not a valid direction!
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
1
0
2
0
2
0
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
1
1
2
1
2
1
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
1
0
2
0
2
0
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
1
2
2
2
2
2
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
1
0
2
0
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
1
2
2
2
There is an ivory comb among the wreckage.
There are doors to the east and north.
What do you do? e
You are in the entryway to the haunted house.
1
0
2
0
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
1
1
2
1
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
1
0
2
0
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
1
2
2
2
There is an ivory comb among the wreckage.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
1
0
2
0
2
0
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
1
1
2
1
2
1
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
1
0
2
0
2
0
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
1
2
2
2
2
2
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
1
0
2
0
2
0
2
0
You see a hallway to the north, and doors to the east and west.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
1
2
2
2
2
2
2
2
There is a bowl on the floor.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
1
0
2
0
2
0
2
0
You see a hallway to the north, and doors to the east and west.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
1
2
2
2
2
2
2
2
There are doors to the east and north.
What do you do? e
You are in the entryway to the haunted house.
1
0
2
0
2
0
2
0
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
1
1
2
1
2
1
2
1
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
1
0
2
0
2
0
2
0
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
1
2
2
2
2
2
2
2
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
1
0
2
0
2
0
2
0
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
1
1
2
1
2
1
2
1
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
1
0
2
0
2
0
2
0
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
1
2
2
2
2
2
2
2
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
1
0
2
0
2
0
2
0
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
1
2
2
2
2
2
2
2
There is a bowl on the floor.
There are doors to the east and north.
What do you do? e
You are in the entryway to the haunted house.
1
0
2
0
2
0
2
0
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
1
1
2
1
2
1
2
1
There are doors to the west and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
1
0
false

2
0
false

2
0
false

2
0
false
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
1
1
false

2
1
false

2
1
false

2
1
false
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
1
0
false

2
0
false

2
0
false

2
0
false
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
1
2
false

2
2
false

2
2
false

2
2
false
There is a bowl on the floor.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
1
0
false

2
0
false

2
0
false

2
0
false
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
1
1
false

2
1
false

2
1
false

2
1
false
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
1
0
false

2
0
false

2
0
false

2
0
false
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
1
2
false

2
2
false

2
2
false

2
2
false
There is a bowl on the floor.
There are doors to the east and north.
You hear faint laughter.

What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
1
0
false

2
0
false

2
0
false

2
0
false
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
1
1
false

2
1
false

2
1
false

2
1
false
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
1
0
false

2
0
false

2
0
false

2
0
false
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
1
2
false

2
2
false

2
2
false

2
2
false
There is a bowl on the floor.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
1
0
false

2
0
false

2
0
false

2
0
false
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
1
1
false

2
1
false

2
1
false

2
1
false
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
1
0
false

2
0
false

2
0
false

2
0
false
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
1
2
false

2
2
false

2
2
false

2
2
false
There is a bowl on the floor.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a bowl on the floor.
There are doors to the east and north.
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear faint laughter.

What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a bowl on the floor.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a bowl on the floor.
There are doors to the east and north.
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
You hear footsteps.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a bowl on the floor.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
Rats scurry across the floor.

What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a bowl on the floor.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a bowl on the floor.
There are doors to the east and north.
What do you do? w
That's not a valid direction!
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a bowl on the floor.
There are doors to the east and north.
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
There is a bowl on the floor.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 258, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 255, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 169, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 201, in moveCheck
    roomDescription(location, rooms, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 219, in roomDescription
    itemCheck(location, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 213, in itemCheck
    print(items[n].getItemDroppedDescription())
KeyboardInterrupt
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There is a bowl on the floor.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There is a bowl on the floor.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There is a bowl on the floor.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There is a bowl on the floor.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear footsteps.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 258, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 255, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 169, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 201, in moveCheck
    roomDescription(location, rooms, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 219, in roomDescription
    itemCheck(location, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 212, in itemCheck
    if (checkLocation == location) and (checkHidden == false):
NameError: global name 'false' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? n
You enter a long, dark hallway.
There's an elephant in the corner.
There are stairs to the east, and doorways to the north and south.
You hear footsteps.
What do you do? get elephant
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 264, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 261, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 176, in verbAndNounCheck
    checkGettable = eval(items[n].getItemGettable())
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 53, in getItemGettable
    return self.itemGetabble
AttributeError: 'Items' object has no attribute 'itemGetabble'
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? n
You enter a long, dark hallway.
There's an elephant in the corner.
There are stairs to the east, and doorways to the north and south.
What do you do? get elephant
You can't pick up elephant .
What do you do? q
Huh?
>>> lst = [(name = "gun"), (location = 1)]
SyntaxError: invalid syntax
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 296, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 293, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 190, in verbAndNounCheck
    print(items.index(noun))
ValueError: 'gun' is not in list
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 296, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 293, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 190, in verbAndNounCheck
    print(items.index("name"))
ValueError: 'name' is not in list
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 296, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 293, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 190, in verbAndNounCheck
    print(items.index("itemName"))
ValueError: 'itemName' is not in list
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 296, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 293, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 190, in verbAndNounCheck
    print(items.index())
TypeError: index() takes at least 1 argument (0 given)
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 296, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 293, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 190, in verbAndNounCheck
    print(items.index(getItemName()))
NameError: global name 'getItemName' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 296, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 293, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 190, in verbAndNounCheck
    print(items.index(getItemName))
NameError: global name 'getItemName' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
[<__main__.Items object at 0x2c0e210>, <__main__.Items object at 0x2c0e290>, <__main__.Items object at 0x2c0e350>, <__main__.Items object at 0x2c0e410>, <__main__.Items object at 0x2c0e470>]
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 296, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 293, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 190, in verbAndNounCheck
    print(items())
TypeError: 'list' object is not callable
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear faint laughter.

What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
<__main__.Items object at 0x2c0f210>
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 296, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 293, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 190, in verbAndNounCheck
    print(items(n))
TypeError: 'list' object is not callable
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
<built-in method index of list object at 0x2bf7698>
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
Rats scurry across the floor.

What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 296, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 293, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 190, in verbAndNounCheck
    print(items.index())
TypeError: index() takes at least 1 argument (0 given)
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? get gun
You pick up the gun .
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 296, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 293, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 190, in verbAndNounCheck
    print([y[0] for y in items.index('gun')])
ValueError: 'gun' is not in list
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? 
Huh?
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 296, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 293, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 190, in verbAndNounCheck
    print([y[1] for y in items.index('gun')])
ValueError: 'gun' is not in list
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 296, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 293, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 190, in verbAndNounCheck
    print([y[1] for y in items.index(noun)])
ValueError: 'gun' is not in list
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
Rats scurry across the floor.

What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? get gun
You pick up the gun .
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
You hear footsteps.
What do you do? inv
In your inventory you have:
gun
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
What do you do? drop gun
You drop the gun .
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 310, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 307, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 170, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 205, in moveCheck
    roomExitsStr = rooms[location].getExits()
TypeError: list indices must be integers, not NoneType
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear footsteps.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 311, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 308, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 170, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 205, in moveCheck
    roomExitsStr = rooms[location].getExits()
TypeError: list indices must be integers, not NoneType
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? n
The kitchen.
There are doors to the south, and east.
What do you do? e
The Dining room.
There are doors to the south, and west.
What do you do? s
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
Rats scurry across the floor.

What do you do? e
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 311, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 308, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 170, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 205, in moveCheck
    roomExitsStr = rooms[location].getExits()
TypeError: list indices must be integers, not NoneType
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 311, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 308, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 170, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 205, in moveCheck
    roomExitsStr = rooms[location].getExits()
TypeError: list indices must be integers, not NoneType
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear footsteps.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 311, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 308, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 170, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 205, in moveCheck
    roomExitsStr = rooms[location].getExits()
TypeError: list indices must be integers, not NoneType
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 310, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 307, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 170, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 205, in moveCheck
    roomExitsStr = rooms[location].getExits()
TypeError: list indices must be integers, not NoneType
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
You hear footsteps.
What do you do? get gun
You pick up the gun .
1
What do you do? e
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 311, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 308, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 170, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 205, in moveCheck
    roomExitsStr = rooms[location].getExits()
TypeError: list indices must be integers, not NoneType
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
0
<class 'int'>
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
Rats scurry across the floor.

What do you do? get gun
You pick up the gun .
1
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? e
0
<class 'int'>
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
1
<class 'int'>
What do you do? get gun
You pick up the gun .
1
<class 'int'>
What do you do? w
None
<class 'NoneType'>
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 316, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 313, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 170, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 207, in moveCheck
    roomExitsStr = rooms[location].getExits()
TypeError: list indices must be integers, not NoneType
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
0
<class 'int'>
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
1
<class 'int'>
What do you do? get gun
You pick up the gun .
1
<class 'int'>
You hear footsteps.
What do you do? w
1
<class 'int'>
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
0
<class 'int'>
What do you do? drop gun
You drop the gun .
0
<class 'int'>
What do you do? n
None
<class 'NoneType'>
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 317, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 314, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 170, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 208, in moveCheck
    roomExitsStr = rooms[location].getExits()
TypeError: list indices must be integers, not NoneType
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? 
Huh?
What do you do? e
0
<class 'int'>
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
1
<class 'int'>
What do you do? get gun
You pick up the gun .
1
<class 'int'>
What do you do? w
1
<class 'int'>
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
0
<class 'int'>
What do you do? drop gun
You drop the gun .
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? e
None
<class 'NoneType'>
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 318, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 315, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 170, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 208, in moveCheck
    roomExitsStr = rooms[location].getExits()
TypeError: list indices must be integers, not NoneType
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
0
<class 'int'>
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
1
<class 'int'>
What do you do? get gun
You pick up the gun .
1
<class 'int'>
What do you do? w
1
<class 'int'>
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
0
<class 'int'>
What do you do? drop gun
You drop the gun .
0
<class 'int'>
What do you do? w
0
<class 'int'>
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 318, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 315, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 170, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 215, in moveCheck
    roomDescription(location, rooms, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 235, in roomDescription
    itemCheck(location, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 226, in itemCheck
    checkLocation = eval(items[n].getItemLocation())
TypeError: eval() arg 1 must be a string, bytes or code object
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
0
<class 'int'>
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
1
<class 'int'>
What do you do? get gun
You pick up the gun .
1
<class 'int'>
What do you do? w
1
<class 'int'>
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
0
<class 'int'>
What do you do? drop gun
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 318, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 315, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 198, in verbAndNounCheck
    getDropItems(items, location, "drop", noun)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 285, in getDropItems
    items[n].itemLocation = eval(location)
TypeError: eval() arg 1 must be a string, bytes or code object
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
0
<class 'int'>
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
1
<class 'int'>
What do you do? get gun
You pick up the gun .
1
<class 'int'>
What do you do? w
1
<class 'int'>
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
0
<class 'int'>
What do you do? drop gun
You drop the gun .
0
<class 'int'>
What do you do? n
0
<class 'int'>
You enter a long, dark hallway.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 318, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 315, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 170, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 215, in moveCheck
    roomDescription(location, rooms, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 235, in roomDescription
    itemCheck(location, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 226, in itemCheck
    checkLocation = eval(items[n].getItemLocation())
TypeError: eval() arg 1 must be a string, bytes or code object
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
1
<class 'str'>
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
What do you do? e
0
<class 'int'>
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
1
<class 'str'>
You can see a gun on the floor.
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
There are doors to the west and north.
1
<class 'int'>
What do you do? get gun
You pick up the gun .
1
<class 'int'>
What do you do? w
1
<class 'int'>
You are in the entryway to the haunted house.
-1
<class 'str'>
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
0
<class 'int'>
What do you do? drop gun
You drop the gun .
0
<class 'int'>
You hear faint laughter.

What do you do? w
0
<class 'int'>
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
0
<class 'int'>
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 321, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 318, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 170, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 215, in moveCheck
    roomDescription(location, rooms, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 238, in roomDescription
    itemCheck(location, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 229, in itemCheck
    checkLocation = eval(items[n].getItemLocation())
TypeError: eval() arg 1 must be a string, bytes or code object
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
1
<class 'str'>
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
What do you do? e
0
<class 'int'>
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
1
<class 'str'>
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
There are doors to the west and north.
1
<class 'int'>
What do you do? get gun
You pick up the gun .
1
<class 'int'>
Rats scurry across the floor.

What do you do? w
1
<class 'int'>
You are in the entryway to the haunted house.
-1
<class 'str'>
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
0
<class 'int'>
What do you do? drop gun
You drop the gun .
0
<class 'int'>
What do you do? w
0
<class 'int'>
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
0
<class 'int'>
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
There are doors to the east and north.
2
<class 'int'>
What do you do? e
2
<class 'int'>
You are in the entryway to the haunted house.
0
<class 'int'>
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
0
<class 'int'>
What do you do? w
0
<class 'int'>
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
0
<class 'int'>
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
There are doors to the east and north.
2
<class 'int'>
What do you do? e
2
<class 'int'>
You are in the entryway to the haunted house.
0
<class 'int'>
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
0
<class 'int'>
What do you do? w
0
<class 'int'>
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
0
<class 'int'>
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
There are doors to the east and north.
2
<class 'int'>
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
1
<class 'str'>
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
What do you do? e
0
<class 'int'>
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
1
<class 'str'>
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
There are doors to the west and north.
1
<class 'int'>
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
1
<class 'str'>
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
What do you do? e
0
<class 'int'>
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
1
<class 'str'>
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
There are doors to the west and north.
1
<class 'int'>
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
1
<class 'str'>
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
What do you do? e
0
<class 'int'>
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
1
<class 'str'>
You can see a gun on the floor.
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
There are doors to the west and north.
1
<class 'int'>
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
1
<class 'str'>
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
What do you do? e
0
<class 'int'>
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
1
<class 'str'>
You can see a gun on the floor.
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
There are doors to the west and north.
1
<class 'int'>
What do you do? get gun
You pick up the gun .
1
<class 'int'>
What do you do? w
1
<class 'int'>
You are in the entryway to the haunted house.
-1
<class 'str'>
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
0
<class 'int'>
What do you do? drop gun
You drop the gun .
0
<class 'int'>
What do you do? w
0
<class 'int'>
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
0
<class 'int'>
2
<class 'str'>
There is an ivory comb among the wreckage.
2
<class 'str'>
There is a bomb among the wreckage.
2
<class 'str'>
3
<class 'str'>
There are doors to the east and north.
2
<class 'int'>
What do you do? e
2
<class 'int'>
You are in the entryway to the haunted house.
0
<class 'int'>
You can see a gun on the floor.
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
0
<class 'int'>
What do you do? get gun
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 321, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 318, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 173, in verbAndNounCheck
    getDropItems(items, location, "get", noun)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 258, in getDropItems
    checkLocation = eval(items[n].getItemLocation())
TypeError: eval() arg 1 must be a string, bytes or code object
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
1
<class 'str'>
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
What do you do? e
0
<class 'int'>
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
1
<class 'str'>
You can see a gun on the floor.
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
There are doors to the west and north.
1
<class 'int'>
What do you do? get gun
You pick up the gun .
1
<class 'int'>
What do you do? w
1
<class 'int'>
You are in the entryway to the haunted house.
-1
<class 'str'>
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
0
<class 'int'>
What do you do? w
0
<class 'int'>
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
-1
<class 'str'>
2
<class 'str'>
There is an ivory comb among the wreckage.
2
<class 'str'>
There is a bomb among the wreckage.
2
<class 'str'>
3
<class 'str'>
There are doors to the east and north.
2
<class 'int'>
What do you do? get comb
You pick up the comb .
2
<class 'int'>
What do you do? e
2
<class 'int'>
You are in the entryway to the haunted house.
-1
<class 'str'>
-1
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
0
<class 'int'>
What do you do? drop comb
You drop the comb .
0
<class 'int'>
What do you do? w
0
<class 'int'>
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
-1
<class 'str'>
0
<class 'int'>
2
<class 'str'>
There is a bomb among the wreckage.
2
<class 'str'>
3
<class 'str'>
There are doors to the east and north.
2
<class 'int'>
What do you do? e
2
<class 'int'>
You are in the entryway to the haunted house.
-1
<class 'str'>
0
<class 'int'>
There is an ivory comb among the wreckage.
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
0
<class 'int'>
What do you do? drop gun
You drop the gun .
0
<class 'int'>
What do you do? w
0
<class 'int'>
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
0
<class 'int'>
0
<class 'int'>
2
<class 'str'>
There is a bomb among the wreckage.
2
<class 'str'>
3
<class 'str'>
There are doors to the east and north.
2
<class 'int'>
What do you do? e
2
<class 'int'>
You are in the entryway to the haunted house.
0
<class 'int'>
You can see a gun on the floor.
0
<class 'int'>
There is an ivory comb among the wreckage.
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
0
<class 'int'>
What do you do? get gun
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 321, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 318, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 139, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 173, in verbAndNounCheck
    getDropItems(items, location, "get", noun)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 258, in getDropItems
    checkLocation = eval(items[n].getItemLocation())
TypeError: eval() arg 1 must be a string, bytes or code object
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
1
<class 'str'>
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
What do you do? e
0
<class 'int'>
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
1
<class 'str'>
You can see a gun on the floor.
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
There are doors to the west and north.
1
<class 'int'>
What do you do? get gun
You pick up the gun .
1
<class 'int'>
What do you do? w
1
<class 'int'>
You are in the entryway to the haunted house.
-1
<class 'str'>
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
0
<class 'int'>
What do you do? drop gun
You drop the gun .
0
<class 'int'>
What do you do? e
0
<class 'int'>
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
0
<class 'int'>
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
There are doors to the west and north.
1
<class 'int'>
What do you do? w
1
<class 'int'>
You are in the entryway to the haunted house.
0
<class 'int'>
You can see a gun on the floor.
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
0
<class 'int'>
What do you do? get gun
You pick up the gun .
0
<class 'int'>
What do you do? w
0
<class 'int'>
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
-1
<class 'str'>
2
<class 'str'>
There is an ivory comb among the wreckage.
2
<class 'str'>
There is a bomb among the wreckage.
2
<class 'str'>
3
<class 'str'>
There are doors to the east and north.
2
<class 'int'>
What do you do? e
2
<class 'int'>
You are in the entryway to the haunted house.
-1
<class 'str'>
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
0
<class 'int'>
What do you do? w
0
<class 'int'>
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
-1
<class 'str'>
2
<class 'str'>
There is an ivory comb among the wreckage.
2
<class 'str'>
There is a bomb among the wreckage.
2
<class 'str'>
3
<class 'str'>
There are doors to the east and north.
2
<class 'int'>
What do you do? e
2
<class 'int'>
You are in the entryway to the haunted house.
-1
<class 'str'>
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
0
<class 'int'>
What do you do? n
0
<class 'int'>
You enter a long, dark hallway.
-1
<class 'str'>
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
There's an elephant in the corner.
There are stairs to the east, and doorways to the north and south.
3
<class 'int'>
What do you do? get elephant
There is no elephant to get!
3
<class 'int'>
What do you do? e
3
<class 'int'>
Stairs leading up.
-1
<class 'str'>
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
You can go back down the stairs to the west.
4
<class 'int'>
What do you do? w
4
<class 'int'>
You enter a long, dark hallway.
-1
<class 'str'>
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
There's an elephant in the corner.
There are stairs to the east, and doorways to the north and south.
3
<class 'int'>
What do you do? e
3
<class 'int'>
Stairs leading up.
-1
<class 'str'>
2
<class 'str'>
2
<class 'str'>
2
<class 'str'>
3
<class 'str'>
You can go back down the stairs to the west.
4
<class 'int'>
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
icheck before ic 1
<class 'str'>
icheck before ic 2
<class 'str'>
icheck before ic 2
<class 'str'>
icheck before ic 2
<class 'str'>
icheck before ic 3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
icheck before ic, location of items 1
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
What do you do? e
0
<class 'int'>
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
icheck before ic, location of items 1
<class 'str'>
You can see a gun on the floor.
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 3
<class 'str'>
There are doors to the west and north.
mvcheck after move 1
<class 'int'>
What do you do? w
1
<class 'int'>
You are in the entryway to the haunted house.
icheck before ic, location of items 1
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
mvcheck after move 0
<class 'int'>
What do you do? n
0
<class 'int'>
You enter a long, dark hallway.
icheck before ic, location of items 1
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 3
<class 'str'>
There's an elephant in the corner.
There are stairs to the east, and doorways to the north and south.
mvcheck after move 3
<class 'int'>
What do you do? get elephant
There is no elephant to get!
getditems 3
<class 'int'>
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
icheck before ic, location of items 1
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
What do you do? n
0
<class 'int'>
You enter a long, dark hallway.
icheck before ic, location of items 1
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 3
<class 'str'>
There's an elephant in the corner.
There are stairs to the east, and doorways to the north and south.
mvcheck after move 3
<class 'int'>
What do you do? get elephant
check location 1
<class 'int'>
check name gun
<class 'str'>
1
<class 'int'>
0
<class 'int'>
check location 2
<class 'int'>
check name comb
<class 'str'>
1
<class 'int'>
0
<class 'int'>
check location 2
<class 'int'>
check name bomb
<class 'str'>
1
<class 'int'>
0
<class 'int'>
check location 2
<class 'int'>
check name bowl
<class 'str'>
1
<class 'int'>
1
<class 'int'>
check location 3
<class 'int'>
check name an elephant
<class 'str'>
0
<class 'int'>
0
<class 'int'>
There is no elephant to get!
getditems 3
<class 'int'>
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
icheck before ic, location of items 1
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
What do you do? n
0
<class 'int'>
You enter a long, dark hallway.
icheck before ic, location of items 1
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 3
<class 'str'>
There's an elephant in the corner.
There are stairs to the east, and doorways to the north and south.
mvcheck after move 3
<class 'int'>
You hear footsteps.
What do you do? s
3
<class 'int'>
You are in the entryway to the haunted house.
icheck before ic, location of items 1
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
mvcheck after move 0
<class 'int'>
What do you do? w
0
<class 'int'>
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
icheck before ic, location of items 1
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
There is an ivory comb among the wreckage.
icheck before ic, location of items 2
<class 'str'>
There is a bomb among the wreckage.
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 3
<class 'str'>
There are doors to the east and north.
mvcheck after move 2
<class 'int'>
What do you do? get comb
check location 1
<class 'int'>
check name gun
<class 'str'>
1
<class 'int'>
0
<class 'int'>
check location 2
<class 'int'>
check name comb
<class 'str'>
1
<class 'int'>
0
<class 'int'>
You pick up the comb .
getditems 2
<class 'int'>
What do you do? get bomb
check location 1
<class 'int'>
check name gun
<class 'str'>
1
<class 'int'>
0
<class 'int'>
check location -1
<class 'int'>
check name comb
<class 'str'>
1
<class 'int'>
0
<class 'int'>
check location 2
<class 'int'>
check name bomb
<class 'str'>
1
<class 'int'>
0
<class 'int'>
You pick up the bomb .
getditems 2
<class 'int'>
What do you do? e
2
<class 'int'>
You are in the entryway to the haunted house.
icheck before ic, location of items 1
<class 'str'>
icheck before ic, location of items -1
<class 'str'>
icheck before ic, location of items -1
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 3
<class 'str'>
You see a hallway to the north, and doors to the east and west.
mvcheck after move 0
<class 'int'>
What do you do? n
0
<class 'int'>
You enter a long, dark hallway.
icheck before ic, location of items 1
<class 'str'>
icheck before ic, location of items -1
<class 'str'>
icheck before ic, location of items -1
<class 'str'>
icheck before ic, location of items 2
<class 'str'>
icheck before ic, location of items 3
<class 'str'>
There's an elephant in the corner.
There are stairs to the east, and doorways to the north and south.
mvcheck after move 3
<class 'int'>
What do you do? get elephant
check location 1
<class 'int'>
check name gun
<class 'str'>
1
<class 'int'>
0
<class 'int'>
check location -1
<class 'int'>
check name comb
<class 'str'>
1
<class 'int'>
0
<class 'int'>
check location -1
<class 'int'>
check name bomb
<class 'str'>
1
<class 'int'>
0
<class 'int'>
check location 2
<class 'int'>
check name bowl
<class 'str'>
1
<class 'int'>
1
<class 'int'>
check location 3
<class 'int'>
check name elephant
<class 'str'>
0
<class 'int'>
0
<class 'int'>
You can't pick up elephant .
getditems 3
<class 'int'>
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
0
<class 'int'>
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? drop gun
You drop the gun .
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? e
You are in the entryway to the haunted house.
You can see a gun on the floor.
You see a hallway to the north, and doors to the east and west.
What do you do? n
You enter a long, dark hallway.
There's an elephant in the corner.
There are stairs to the east, and doorways to the north and south.
What do you do? get gun
There is no gun to get!
What do you do? get elephant
You can't pick up elephant .
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get couch
There is no couch to get!
What do you do? 
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 294, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 285, in main
    rooms = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 113, in roomSetup
    rooms.append(makeRooms(line))
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 105, in makeRooms
    rroomNumber, name, longDescription, shortDescription, exitDescription, exits, hiddenExitable, hiddenExitFound, hiddenExitFindDescription, hiddenExitsDescription, hiddenExits = infoStr.split("\\")
ValueError: too many values to unpack (expected 11)
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 294, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 285, in main
    rooms = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 113, in roomSetup
    rooms.append(makeRooms(line))
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 105, in makeRooms
    rroomNumber, name, longDescription, shortDescription, exitDescription, exits, hiddenExitable, hiddenExitFound, hiddenExitFindDescription, hiddenExitsDescription, hiddenExits = infoStr.split("\\")
ValueError: too many values to unpack (expected 11)
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 294, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 285, in main
    rooms = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 113, in roomSetup
    rooms.append(makeRooms(line))
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 105, in makeRooms
    rroomNumber, name, longDescription, shortDescription, exitDescription, exits, hiddenExitable, hiddenExitFound, hiddenExitFindDescription, hiddenExitsDescription, hiddenExits = infoStr.split("\\")
ValueError: too many values to unpack (expected 11)
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 294, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 285, in main
    rooms = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 113, in roomSetup
    rooms.append(makeRooms(line))
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 105, in makeRooms
    rroomNumber, name, longDescription, shortDescription, exitDescription, exits, hiddenExitable, hiddenExitFound, hiddenExitFindDescription, hiddenExitsDescription, hiddenExits = infoStr.split("\\")
ValueError: too many values to unpack (expected 11)
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 294, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 285, in main
    rooms = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 113, in roomSetup
    rooms.append(makeRooms(line))
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 105, in makeRooms
    rroomNumber, name, longDescription, shortDescription, exitDescription, exits, hiddenExitable, hiddenExitFound, hiddenExitFindDescription, hiddenExitsDescription, hiddenExits = infoStr.split("\\")
ValueError: too many values to unpack (expected 11)
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 294, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 285, in main
    rooms = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 113, in roomSetup
    rooms.append(makeRooms(line))
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 105, in makeRooms
    rroomNumber, name, longDescription, shortDescription, exitDescription, exits, hiddenExitable, hiddenExitFound, hiddenExitFindDescription, hiddenExitsDescription, hiddenExits = infoStr.split("\\")
ValueError: too many values to unpack (expected 11)
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 294, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 285, in main
    rooms = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 113, in roomSetup
    rooms.append(makeRooms(line))
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 105, in makeRooms
    rroomNumber, name, longDescription, shortDescription, exitDescription, exits, hiddenExitable, hiddenExitFound, hiddenExitFindDescription, hiddenExitsDescription, hiddenExits = infoStr.split("\\")
ValueError: too many values to unpack (expected 11)
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 294, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 285, in main
    rooms = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 113, in roomSetup
    rooms.append(makeRooms(line))
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 105, in makeRooms
    rroomNumber, name, longDescription, shortDescription, exitDescription, exits, hiddenExitable, hiddenExitFound, hiddenExitFindDescription, hiddenExitsDescription, hiddenExits = infoStr.split("\\")
ValueError: too many values to unpack (expected 11)
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 294, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 285, in main
    rooms = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 113, in roomSetup
    rooms.append(makeRooms(line))
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 105, in makeRooms
    rroomNumber, name, longDescription, shortDescription, exitDescription, exits, hiddenExitable, hiddenExitFound, hiddenExitFindDescription, hiddenExitsDescription, hiddenExits = infoStr.split("\\")
ValueError: too many values to unpack (expected 11)
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 294, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 285, in main
    rooms = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 113, in roomSetup
    rooms.append(makeRooms(line))
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 105, in makeRooms
    roomNumber, name, longDescription, shortDescription, exitDescription, exits, hiddenExitable, hiddenExitFound, hiddenExitFindDescription, hiddenExitsDescription, hiddenExits = infoStr.split("\\")
ValueError: too many values to unpack (expected 11)
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 294, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 285, in main
    rooms = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 113, in roomSetup
    rooms.append(makeRooms(line))
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 105, in makeRooms
    roomNumber, name, longDescription, shortDescription, exitDescription, exits, hiddenExitable, hiddenExitFound, hiddenExitFindDescription, hiddenExitsDescription, hiddenExits = infoStr.split("\\")
ValueError: too many values to unpack (expected 11)
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 317, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 308, in main
    rooms = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 136, in roomSetup
    rooms.append(makeRooms(line))
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 128, in makeRooms
    roomNumber, name, longDescription, shortDescription, exitDescription, exits, hiddenExitable, hiddenExitFound, hiddenExitFindDescription, hiddenExitsDescription, hiddenExits = infoStr.split("\\")
ValueError: too many values to unpack (expected 11)
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? eValueError: too many values to unpack (expected 11)
Huh?
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? drop gun
You drop the gun .
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
You can see a gun on the floor.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? w
That's not a valid direction!
What do you do? e
You are in the entryway to the haunted house.
You can see a gun on the floor.
You see a hallway to the north, and doors to the east and west.
What do you do? n
You enter a long, dark hallway.
There's an elephant in the corner.
There are stairs to the east, and doorways to the north and south.
What do you do? get elephant
You can't pick up elephant .
What do you do? get sadfjkl
There is no sadfjkl to get!
What do you do? w
That's not a valid direction!
What do you do? e
Stairs leading up.
You can go back down the stairs to the west.
What do you do? s
That's not a valid direction!
What do you do? 
Huh?
What do you do? e
That's not a valid direction!
What do you do? w
You enter a long, dark hallway.
There's an elephant in the corner.
There are stairs to the east, and doorways to the north and south.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? s
You are in the entryway to the haunted house.
You can see a gun on the floor.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? search room
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 314, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 311, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 159, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 202, in verbAndNounCheck
    location = searchCheck(rooms, items, noun, location)
NameError: global name 'searchCheck' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? search room
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? search room
You hear footsteps.
What do you do? search room
What do you do? search room
Your search reveals nothing!
Your search reveals nothing!
Your search reveals nothing!
Your search reveals nothing!
Your search reveals nothing!
What do you do? search room
What do you do? search room
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? search room
What do you do? search room
Your search reveals nothing!
You hear footsteps.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? search room
What do you do? search room
What do you do? search room
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 337, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 334, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 159, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 191, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 208, in moveCheck
    roomExitsStr = rooms[location].getExits()
TypeError: list indices must be integers, not NoneType
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? search room
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 339, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 336, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 159, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 191, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 209, in moveCheck
    roomExitsStr = rooms[location].getExits()
TypeError: list indices must be integers, not NoneType
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? search room
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 341, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 338, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 159, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 191, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 209, in moveCheck
    roomExitsStr = rooms[location].getExits()
TypeError: list indices must be integers, not NoneType
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? search room
What do you do? search room
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 340, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 337, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 159, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 191, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 208, in moveCheck
    roomExitsStr = rooms[location].getExits()
TypeError: list indices must be integers, not NoneType
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? search room
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 340, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 337, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 159, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 191, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 208, in moveCheck
    roomExitsStr = rooms[location].getExits()
TypeError: list indices must be integers, not NoneType
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? search room
What do you do? search room
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 340, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 337, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 159, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 191, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 208, in moveCheck
    roomExitsStr = rooms[location].getExits()
TypeError: list indices must be integers, not NoneType
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
You hear footsteps.
What do you do? search room
There is a bowl on the floor.
2
<class 'int'>
You hear footsteps.
What do you do? 
Huh?
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 342, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 339, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 159, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 191, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 210, in moveCheck
    roomExitsStr = rooms[location].getExits()
TypeError: list indices must be integers, not NoneType
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? search room
There is a bowl on the floor.
2
<class 'int'>
What do you do? w
That's not a valid direction!
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? search room
What do you do? search room
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? search room
There is a bowl on the floor.
What do you do? w
That's not a valid direction!
What do you do? n
The kitchen.
There are doors to the south, and east.
What do you do? s
You enter a long, dark hallway.
There's an elephant in the corner.
There are stairs to the east, and doorways to the north and south.
What do you do? e
Stairs leading up.
You can go back down the stairs to the west.
What do you do? w
You enter a long, dark hallway.
There's an elephant in the corner.
There are stairs to the east, and doorways to the north and south.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? search room
There is a bowl on the floor.
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? n
You enter a long, dark hallway.
There's an elephant in the corner.
There are stairs to the east, and doorways to the north and south.
What do you do? w
That's not a valid direction!
What do you do? s
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There is a bowl on the floor.
There are doors to the east and north.
What do you do? get bowl
You pick up the bowl .
What do you do? get bomb
You pick up the bomb .
You hear footsteps.
What do you do? w
That's not a valid direction!
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? n
You enter a long, dark hallway.
There's an elephant in the corner.
There are stairs to the east, and doorways to the north and south.
What do you do? n
The kitchen.
There are doors to the south, and east.
What do you do? e
The Dining room.
There are doors to the south, and west.
What do you do? s
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? s
Huh?
What do you do? kljsdflaskjdf
Huh?
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? search room
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? search room
Rats scurry across the floor.

What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? search room
Your search reveals nothing!
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? search room
You're search has found a concealed item!
There is a bowl on the floor.
a secret door in the bookcase.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear footsteps.
What do you do? search room
Your search reveals nothing!
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? search room
You're search has found a concealed item!
There is a bowl on the floor.
You're search has found  a secret door in the bookcase.
What do you do? w
That's not a valid direction!
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? s
That's not a valid direction!
What do you do? n
You enter a long, dark hallway.
There's an elephant in the corner.
There are stairs to the east, and doorways to the north and south.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
You hear footsteps.
What do you do? search room
Your search reveals nothing!
What do you do? search room
You're search has found a secret door in the bookcase.
What do you do? look room
Huh?
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
What do you do? search room
You're search has found a concealed item!
There is a bowl on the floor.
You're search has found a secret door in the bookcase.
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There is a bowl on the floor.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
{'n': 3, 'east': 1, 'west': 2, 'e': 1, 'w': 2, 'north': 3}
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
You hear footsteps.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 347, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 344, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 159, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 191, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 213, in moveCheck
    roomExitsHidden = ast.literal_eval(roomExitsHiddenStr)
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 86, in literal_eval
    return _convert(node_or_string)
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 85, in _convert
    raise ValueError('malformed node or string: ' + repr(node))
ValueError: malformed node or string: <_ast.Name object at 0x3419470>
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
{}
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? search room
Your search reveals nothing!
What do you do? search room
You're search has found a concealed item!
There is a bowl on the floor.
You're search has found a secret door in the bookcase.
What do you do? e
{'w': 7}
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
{}
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There is a bowl on the floor.
There are doors to the east and north.
What do you do? w
{'w': 7}
That's not a valid direction!
What do you do? e
{'w': 7}
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
{}
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There is a bowl on the floor.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
{}
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? w
{}
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
{}
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
{}
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? search room
Your search reveals nothing!
What do you do? search room
You're search has found a concealed item!
There is a bowl on the floor.
You're search has found a secret door in the bookcase.
What do you do? w
{'w': 7}
That's not a valid direction!
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? e
{'w': 7}
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
{}
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There is a bowl on the floor.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
{}
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase.
You hear footsteps.
What do you do? e
{'w': 7}
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
{}
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
What do you do? go west
{'w': 7}
That's not a valid direction!
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
{}
0
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
{}
0
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? w
{}
0
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
{}
0
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? search room
You're search has found a concealed item!
There is a bowl on the floor.
You're search has found a secret door in the bookcase.
What do you do? go west
{'w': 7}
1
That's not a valid direction!
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
{}
0
<class 'str'>
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? w
{}
0
<class 'str'>
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
{}
0
<class 'str'>
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? search room
You're search has found a concealed item!
There is a bowl on the floor.
You're search has found a secret door in the bookcase.
What do you do? go west
{'w': 7}
1
<class 'str'>
That's not a valid direction!
What do you do? n
{'w': 7}
1
<class 'str'>
The kitchen.
There are doors to the south, and east.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? s
{}
0
<class 'str'>
You enter a long, dark hallway.
There's an elephant in the corner.
There are stairs to the east, and doorways to the north and south.
What do you do? s
{}
0
<class 'str'>
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
{}
0
<class 'str'>
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There is a bowl on the floor.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
What do you do? west
{'w': 7}
1
<class 'str'>
That's not a valid direction!
Rats scurry across the floor.

What do you do? w
{'w': 7}
1
<class 'str'>
The hidden room
There is a door to the east.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
{}
0
<class 'str'>
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? w
{}
0
<class 'str'>
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
You hear footsteps.
What do you do? w
{}
0
<class 'str'>
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? search room
You're search has found a concealed item!
There is a bowl on the floor.
You're search has found a secret door in the bookcase.
What do you do? w
{'west': 7, 'w': 7}
1
<class 'str'>
The hidden room
There is a door to the east.
What do you do? e
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 355, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 352, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 159, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 191, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 213, in moveCheck
    roomExitsHidden = ast.literal_eval(roomExitsHiddenStr)
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 86, in literal_eval
    return _convert(node_or_string)
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 85, in _convert
    raise ValueError('malformed node or string: ' + repr(node))
ValueError: malformed node or string: <_ast.Name object at 0x241a510>
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
{}
0
<class 'str'>
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
Rats scurry across the floor.

What do you do? search room
You're search has found a concealed item!
There is a bowl on the floor.
You're search has found a secret door in the bookcase.
What do you do? go west
{'w': 7, 'west': 7}
1
<class 'str'>
The hidden room
There is a door to the east.
What do you do? e
{}
0
<class 'str'>
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There is a bowl on the floor.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? search room
You're search has found a concealed item!
There is a bowl on the floor.
You're search has found a secret door in the bookcase.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? search room
Your search reveals nothing!
What do you do? search room
You're search has found a secret door in the bookcase.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? look room
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
What do you do? get comb
You pick up the comb .
What do you do? w
The hidden room
There is a door to the east.
What do you do? drop comb
You drop the comb .
What do you do? look room
The hidden room
There is an ivory comb among the wreckage.
There is a door to the east.
What do you do? e
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is a bomb among the wreckage.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? n
You enter a long, dark hallway.
There's an elephant in the corner.
There are stairs to the east, and doorways to the north and south.
What do you do? get elephant
You can't pick up elephant .
What do you do? n
The kitchen.
There are doors to the south, and east.
What do you do? 
Huh?
Rats scurry across the floor.

What do you do? 
Huh?
You hear faint laughter.

What do you do? 
Huh?
What do you do? 
Huh?
What do you do? 
Huh?
What do you do? 
Huh?
What do you do? 
Huh?
What do you do? 
Huh?
What do you do? 
Huh?
What do you do? 
Huh?
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? 
Huh?
What do you do? 
Huh?
What do you do? 
Huh?
What do you do? 
Huh?
What do you do? 
Huh?
What do you do? 
Huh?
What do you do? inv
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 349, in <module>
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 346, in main
    if __name__=='__main__':
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 159, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 197, in verbAndNounCheck
    inventoryCheck(items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 240, in inventoryCheck
    checkLocation = eval(items[n].getItemLocation())
TypeError: eval() arg 1 must be a string, bytes or code object
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
What do you do? i
Huh?
What do you do? inv
In your inventory you have:
gun
What do you do? look room
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
There are doors to the west and north.
What do you do? search room
Your search reveals nothing!
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? 
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 368, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 360, in main
    items = itemsSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 87, in itemsSetup
    items.append(makeItems(line))
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 79, in makeItems
    itemID, itemName, itemLocation, itemFriendlyLocation, itemLongDescription, itemShortDescription, itemDroppedDescription, itemGettable, itemDoable, itemHidden, itemAction, itemActionRequirements, itemActionType, itemActionOutcome, itemActionOutcomeDescription = infoStr.split("//")
ValueError: need more than 14 values to unpack
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 367, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 359, in main
    items = itemsSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 86, in itemsSetup
    items.append(makeItems(line))
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 79, in makeItems
    return Items(itemID, itemName, itemLocation, itemFriendlyLocation, itemLongDescription, itemShortDescription, itemDroppedDescription, itemGettable, itemDoable, itemHidden, itemAction, itemActionRequirements, itemActionType, itemActionOutcome, itemActionOutcomeDescription)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 26, in __init__
    self.itemActions = itemActions
NameError: global name 'itemActions' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 367, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 359, in main
    items = itemsSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 86, in itemsSetup
    items.append(makeItems(line))
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 78, in makeItems
    itemID, itemName, itemLocation, itemFriendlyLocation, itemLongDescription, itemShortDescription, itemDroppedDescription, itemGettable, itemDoable, itemHidden, itemActions, itemActionRequirements, itemActionType, itemActionOutcome, itemActionOutcomeDescription = infoStr.split("//")
ValueError: need more than 14 values to unpack
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? search room
Your search reveals nothing!
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear faint laughter.

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? search room
You're search has found a concealed item!
There is a bowl on the floor.
Your search reveals nothing!
What do you do? get bowl
You pick up the bowl .
You hear footsteps.
What do you do? look room
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? drop bomb
You drop the bomb .
What do you do? use bomb
Huh?
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? inv
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 379, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 376, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 175, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 213, in verbAndNounCheck
    inventoryCheck(items, "print")
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 263, in inventoryCheck
    for n in range(numitems):
NameError: global name 'numitems' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? inv
In your inventory you have:
[]
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? inv
In your inventory you have:
['bomb']
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? inv
You're not carrying anything!
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
You hear faint laughter.

What do you do? inv
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? inv
You're not carrying anything!
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? inv
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? inv
You're not carrying anything!
What do you do? 
Huh?
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? inv
['bomb']
1
What do you do? inv
['bomb']
1
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? inv
You're not carrying anything!
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? inv
['bomb']
1
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? inv
You're not carrying anything!
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
You hear footsteps.
What do you do? get bomb
You pick up the bomb .
What do you do? inv
['bomb']
1
You hear footsteps.
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
What do you do? inv
['gun']
1
['gun', 'bomb']
2
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? inv
[]
0
<class 'int'>
You're not carrying anything!
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? inv
['bomb']
1
<class 'int'>
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? inv
[]
0
<class 'int'>
You're not carrying anything!
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? inv
['bomb']
1
<class 'int'>
You're not carrying anything!
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? inv
[]
0
<class 'int'>
You're not carrying anything!
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? inv
['bomb']
0
<class 'int'>
You're not carrying anything!
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? inv
[]
0
<class 'int'>
You're not carrying anything!
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
Rats scurry across the floor.

What do you do? get bomb
You pick up the bomb .
What do you do? inv
['bomb']
1
<class 'int'>
In your inventory you have:
bomb
What do you do? drop bomb
You drop the bomb .
What do you do? inv
[]
0
<class 'int'>
You're not carrying anything!
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You can see a gun on the floor.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There is a bowl on the floor.
There's an elephant in the corner.
You see a hallway to the north, and doors to the east and west.
What do you do? get bowk
There is no bowk to get!
What do you do? get bowl
There is no bowl to get!
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There is an ivory comb among the wreckage.
There is a bomb among the wreckage.
There are doors to the east and north.
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You can see a gun on the floor.
There are doors to the west and north.
What do you do? get gun
You pick up the gun .
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? drop gun
You drop the gun .
What do you do? look room
You are in the entryway to the haunted house.
You can see a gun on the floor.
You see a hallway to the north, and doors to the east and west.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
You see an ivory comb tossed carelessly on the the floor.
There is a disarmed bomb on the floor.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? drop bomb
You drop the bomb .
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 428, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 425, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 204, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 238, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 264, in moveCheck
    roomDescription(location, rooms, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 352, in roomDescription
    itemCheck(location, items, "print")
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 288, in itemCheck
    droppedItems.append(items[n].getItemLocationOriginalDesc())
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 68, in getItemLocationOriginalDesc
    return itemLocationOriginalDesc
NameError: global name 'itemLocationOriginalDesc' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? 
Huh?
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 428, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 425, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 204, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 238, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 264, in moveCheck
    roomDescription(location, rooms, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 352, in roomDescription
    itemCheck(location, items, "print")
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 288, in itemCheck
    droppedItems.append(items[n].getItemLocationOriginalDesc())
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 68, in getItemLocationOriginalDesc
    return itemLocationOriginalDesc
NameError: global name 'itemLocationOriginalDesc' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 428, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 425, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 204, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 238, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 264, in moveCheck
    roomDescription(location, rooms, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 352, in roomDescription
    itemCheck(location, items, "print")
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 296, in itemCheck
    print(droppedItemsDescription[n])
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
Rats scurry across the floor.

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
4
[]
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 430, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 427, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 204, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 238, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 264, in moveCheck
    roomDescription(location, rooms, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 354, in roomDescription
    itemCheck(location, items, "print")
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 298, in itemCheck
    print(droppedItemsDescription[n])
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
4
[]
['ivory comb', 'Sitting on an end-table is a beautiful ivory comb.', 'bomb', 'There is a bomb among the wreckage. It is disarmed.']
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 431, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 428, in main
    gamePlay(rooms, items, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 204, in gamePlay
    location = verbAndNounCheck(verb, noun, rooms, items, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 238, in verbAndNounCheck
    location = moveCheck(rooms, items, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 264, in moveCheck
    roomDescription(location, rooms, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 355, in roomDescription
    itemCheck(location, items, "print")
  File "/Users/cwinter/Documents/Python Stuff/adventure1.py", line 299, in itemCheck
    print(droppedItemsDescription[n])
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
2
['Sitting on an end-table is a beautiful ivory comb.', 'There is a bomb among the wreckage. It is disarmed.']
['ivory comb', 'bomb']
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get comb
There is no comb to get!
What do you do? get bomb
You pick up the bomb .
You hear faint laughter.

What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? get comb
You pick up the comb .
What do you do? get bomb
You pick up the bomb .
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? drop cob
You don't have cob to drop!
What do you do? drop comb
You drop the comb .
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
Rats scurry across the floor.

What do you do? e
You are in the entryway to the haunted house.
Sitting on an end-table is a beautiful ivory comb.
You see a hallway to the north, and doors to the east and west.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
Loc: 1
Orig Loc: 1
Loc: 2
Orig Loc: 2
Loc: 2
Orig Loc: 2
Loc: 3
Orig Loc: 3
You see a hallway to the north, and doors to the east and west.
What do you do? w
Loc: 1
Orig Loc: 1
Loc: 2
Orig Loc: 2
Loc: 2
Orig Loc: 2
Loc: 3
Orig Loc: 3
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Loc: 1
Orig Loc: 1
Loc: 2
Orig Loc: 2
Loc: 2
Orig Loc: 2
Loc: 3
Orig Loc: 3
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get comb
Loc: 1
Orig Loc: 1
Loc: 2
Orig Loc: 2
Loc: 2
Orig Loc: 2
Loc: 3
Orig Loc: 3
You pick up the comb .
What do you do? look room
Loc: 1
Orig Loc: 1
Loc: -1
Orig Loc: -1
Loc: 2
Orig Loc: 2
Loc: 3
Orig Loc: 3
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Loc: 1
Orig Loc: 1
Loc: -1
Orig Loc: -1
Loc: 2
Orig Loc: 2
Loc: 3
Orig Loc: 3
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? e
Loc: 1
Orig Loc: 1
Loc: -1
Orig Loc: -1
Loc: 2
Orig Loc: 2
Loc: 3
Orig Loc: 3
You are in the entryway to the haunted house.
Loc: 1
Orig Loc: 1
Loc: -1
Orig Loc: -1
Loc: 2
Orig Loc: 2
Loc: 3
Orig Loc: 3
You see a hallway to the north, and doors to the east and west.
What do you do? drop comb
Loc: 1
Orig Loc: 1
Loc: -1
Orig Loc: -1
Loc: 2
Orig Loc: 2
Loc: 3
Orig Loc: 3
You drop the comb .
What do you do? look room
Loc: 1
Orig Loc: 1
Loc: 0
Orig Loc: 0
Loc: 2
Orig Loc: 2
Loc: 3
Orig Loc: 3
You are in the entryway to the haunted house.
Loc: 1
Orig Loc: 1
Loc: 0
Orig Loc: 0
Loc: 2
Orig Loc: 2
Loc: 3
Orig Loc: 3
Sitting on an end-table is a beautiful ivory comb.
You see a hallway to the north, and doors to the east and west.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
Loc: 1
Orig Loc: 1
Loc: 2
Orig Loc: 2
Loc: 2
Orig Loc: 2
Loc: 3
Orig Loc: 3
You see a hallway to the north, and doors to the east and west.
What do you do? w
Loc: 1
Orig Loc: 1
Loc: 2
Orig Loc: 2
Loc: 2
Orig Loc: 2
Loc: 3
Orig Loc: 3
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Loc: 1
Orig Loc: 1
Loc: 2
Orig Loc: 2
Loc: 2
Orig Loc: 2
Loc: 3
Orig Loc: 3
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get comb
Loc: 1
Orig Loc: 1
Loc: 2
Orig Loc: 2
Loc: 2
Orig Loc: 2
Loc: 3
Orig Loc: 3
You pick up the comb .
What do you do? look room
Loc: 1
Orig Loc: 1
Loc: -1
Orig Loc: -1
Loc: 2
Orig Loc: 2
Loc: 3
Orig Loc: 3
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Loc: 1
Orig Loc: 1
Loc: -1
Orig Loc: -1
Loc: 2
Orig Loc: 2
Loc: 3
Orig Loc: 3
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
Loc: 1
Orig Loc: 1
Loc: 2
Orig Loc: 2
Loc: 2
Orig Loc: 2
Loc: 3
Orig Loc: 3
You see a hallway to the north, and doors to the east and west.
What do you do? w
Loc: 1
Orig Loc: 1
Loc: 2
Orig Loc: 2
Loc: 2
Orig Loc: 2
Loc: 3
Orig Loc: 3
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Loc: 1
Orig Loc: 1
Loc: 2
Orig Loc: 2
Loc: 2
Orig Loc: 2
Loc: 3
Orig Loc: 3
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get comb
Loc: 1
Orig Loc: 1
Loc: 2
Orig Loc: 2
Loc: 2
Orig Loc: 2
Loc: 3
Orig Loc: 3
You pick up the comb .
What do you do? e
Loc: 1
Orig Loc: 1
Loc: -1
Orig Loc: 2
Loc: 2
Orig Loc: 2
Loc: 3
Orig Loc: 3
You are in the entryway to the haunted house.
Loc: 1
Orig Loc: 1
Loc: -1
Orig Loc: 2
Loc: 2
Orig Loc: 2
Loc: 3
Orig Loc: 3
You see a hallway to the north, and doors to the east and west.
What do you do? drop comb
Loc: 1
Orig Loc: 1
Loc: -1
Orig Loc: 2
Loc: 2
Orig Loc: 2
Loc: 3
Orig Loc: 3
You drop the comb .
You hear faint laughter.

What do you do? look room
Loc: 1
Orig Loc: 1
Loc: 0
Orig Loc: 2
Loc: 2
Orig Loc: 2
Loc: 3
Orig Loc: 3
You are in the entryway to the haunted house.
Loc: 1
Orig Loc: 1
Loc: 0
Orig Loc: 2
Loc: 2
Orig Loc: 2
Loc: 3
Orig Loc: 3
You see an ivory comb tossed carelessly on the the floor.
You see a hallway to the north, and doors to the east and west.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get comb
You pick up the comb .
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? drop comb
You drop the comb .
What do you do? use comb
Huh?
What do you do? get comb
You pick up the comb .
What do you do? use comb
What do you do? inv
In your inventory you have:
comb
What do you do? 
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 73, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 69, in main
    eval(roomName = rooms[n])
TypeError: eval() takes no keyword arguments
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 73, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 69, in main
    eval("roomName = rooms[n]")
  File "<string>", line 1
    roomName = rooms[n]
             ^
SyntaxError: invalid syntax
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 75, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 71, in main
    ast.literal_eval(roomName = rooms[n])
TypeError: literal_eval() got an unexpected keyword argument 'roomName'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 75, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 71, in main
    ast.literal_eval("roomName = rooms[n]")
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 47, in literal_eval
    node_or_string = parse(node_or_string, mode='eval')
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 35, in parse
    return compile(source, filename, mode, PyCF_ONLY_AST)
  File "<unknown>", line 1
    roomName = rooms[n]
             ^
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> lst = ["bob", "george"]
>>> list.split
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    list.split
AttributeError: type object 'list' has no attribute 'split'
>>> lst.split
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    lst.split
AttributeError: 'list' object has no attribute 'split'
>>> lst.split()
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    lst.split()
AttributeError: 'list' object has no attribute 'split'
>>> lst
['bob', 'george']
>>> lst = "bob//george"
>>> lst
'bob//george'
>>> lst.split("\\")
['bob//george']
>>> lst
'bob//george'
>>> lst = "bob\\george\\"
>>> lst
'bob\\george\\'
>>> lst.split("\\")
['bob', 'george', '']
>>> lst
'bob\\george\\'
>>> lst.split(0)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    lst.split(0)
TypeError: Can't convert 'int' object to str implicitly
>>> splitlist = lst.split("\\")
>>> splitlist
['bob', 'george', '']
>>> splitlist(0)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    splitlist(0)
TypeError: 'list' object is not callable
>>> splitlist[0]
'bob'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 77, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 72, in main
    rooms = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 61, in roomSetup
    name = splitline[1]
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
["0//Entryway//You are in the entryway to the haunted house.//You are in the entryway.//You see a hallway to the north, and doors to the east and west.//{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}//0//0//none//none//{}\n"]
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 78, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 73, in main
    rooms = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 62, in roomSetup
    name = splitline[1]
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
['0', 'Entryway', 'You are in the entryway to the haunted house.', 'You are in the entryway.', 'You see a hallway to the north, and doors to the east and west.', "{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}", '0', '0', 'none', 'none', '{}\n']
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 78, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 73, in main
    rooms = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 64, in roomSetup
    roomsByName.append(name)
AttributeError: 'dict' object has no attribute 'append'
>>> ================================ RESTART ================================
>>> 
['0', 'Entryway', 'You are in the entryway to the haunted house.', 'You are in the entryway.', 'You see a hallway to the north, and doors to the east and west.', "{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}", '0', '0', 'none', 'none', '{}\n']
['1', 'ParlorRoom', 'You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.', 'You are in the parlor room.', 'There are doors to the west and north.', "{'w': 0, 'west':0, 'n':6, 'north':6}", '0', '0', 'none', 'none', '{}\n']
['2', 'SittingRoom', 'You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.', 'You are in the sitting room.', 'There are doors to the east and north.', "{'e':0, 'east':0, 'n':5, 'north':5}", '1', '0', 'a secret door in the bookcase, to the west.', 'There is a secret door in the bookcase, to the west.', "{'w':7, 'west':7}\n"]
['3', 'Hallway', 'You enter a long, dark hallway.', 'You are in the hallway.', 'There are stairs to the east, and doorways to the north and south.', "{'s':0, 'south':0, 'e':4, 'east':4, 'n':5, 'north':5}", '0', '0', 'none', 'none', '{}\n']
['4', 'StairsUp', 'Stairs leading up.', 'Stairs leading up.', 'At the top of the stairs is a locked door. You can go back down the stairs to the west.', "{'w':3, 'west':3}", '0', '0', 'none', 'none', '{}\n']
['5', 'Kitchen', 'The kitchen.', 'The kitchen.', 'There are doors to the south, and east.', "{'s':3, 'south':3, 'e':6, 'east':6}", '0', '0', 'none', 'none', '{}\n']
['6', 'DiningRoom', 'The Dining room.', 'The dining room.', 'There are doors to the south, and west.', "{'s':1, 'south':1, 'w':5, 'west':5}", '0', '0', 'none', 'none', '{}\n']
['7', 'HiddenRoom', 'The hidden room', 'The hidden room.', 'There is a door to the east.', "{'e':2}", '0', '0', 'none', 'none', '{}\n']
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 80, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 77, in main
    print(Entryway.longDescription)
NameError: global name 'Entryway' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 79, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 76, in main
    print(Entryway.longDescription)
NameError: global name 'Entryway' is not defined
>>> ================================ RESTART ================================
>>> 
{'Entryway': <__main__.Rooms object at 0x240fb50>, 'StairsUp': <__main__.Rooms object at 0x240fd30>, 'ParlorRoom': <__main__.Rooms object at 0x240fbd0>, 'SittingRoom': <__main__.Rooms object at 0x240fb70>, 'DiningRoom': <__main__.Rooms object at 0x240fe70>, 'Hallway': <__main__.Rooms object at 0x240fcb0>, 'Kitchen': <__main__.Rooms object at 0x240fdf0>, 'HiddenRoom': <__main__.Rooms object at 0x240ff30>}
>>> ================================ RESTART ================================
>>> 
{'ParlorRoom': <__main__.Rooms object at 0x2c0bbd0>, 'DiningRoom': <__main__.Rooms object at 0x2c0be70>, 'HiddenRoom': <__main__.Rooms object at 0x2c0bf30>, 'Hallway': <__main__.Rooms object at 0x2c0bcb0>, 'Kitchen': <__main__.Rooms object at 0x2c0bdf0>, 'Entryway': <__main__.Rooms object at 0x2c0bb50>, 'SittingRoom': <__main__.Rooms object at 0x2c0bb70>, 'StairsUp': <__main__.Rooms object at 0x2c0bd30>}
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 79, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 76, in main
    print(Entryway.name)
NameError: global name 'Entryway' is not defined
>>> ================================ RESTART ================================
>>> 
{'DiningRoom': <__main__.Rooms object at 0x240ae70>, 'ParlorRoom': <__main__.Rooms object at 0x240abd0>, 'StairsUp': <__main__.Rooms object at 0x240ad30>, 'Hallway': <__main__.Rooms object at 0x240acb0>, 'Kitchen': <__main__.Rooms object at 0x240adf0>, 'HiddenRoom': <__main__.Rooms object at 0x240af30>, 'Entryway': <__main__.Rooms object at 0x240ab50>, 'SittingRoom': <__main__.Rooms object at 0x240ab70>}
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 79, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 76, in main
    print(roomsByName[Entryway.name])
NameError: global name 'Entryway' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 78, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 75, in main
    print(roomsByName[0])
KeyError: 0
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 78, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 74, in main
    rooms, roomsByName = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 64, in roomSetup
    roomsByName[name] = makeRooms(line)
TypeError: 'tuple' object does not support item assignment
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 78, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 74, in main
    rooms, roomsByName = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 64, in roomSetup
    name = roomsByName.append(makeRooms(line))
AttributeError: 'tuple' object has no attribute 'append'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 79, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 75, in main
    rooms, roomsByName = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 65, in roomSetup
    roomsByName.append(name)
AttributeError: 'tuple' object has no attribute 'append'
>>> ================================ RESTART ================================
>>> 
<__main__.Rooms object at 0x2c0ab30>
>>> ================================ RESTART ================================
>>> 
[<__main__.Rooms object at 0x2c0ab50>, <__main__.Rooms object at 0x2c0abd0>, <__main__.Rooms object at 0x2c0ab70>, <__main__.Rooms object at 0x2c0acb0>, <__main__.Rooms object at 0x2c0ac10>, <__main__.Rooms object at 0x2c0add0>, <__main__.Rooms object at 0x2c0ad90>, <__main__.Rooms object at 0x2c0aef0>]
>>> ================================ RESTART ================================
>>> 
[<__main__.Rooms object at 0x240ab50>, <__main__.Rooms object at 0x240abd0>, <__main__.Rooms object at 0x240ab70>, <__main__.Rooms object at 0x240acb0>, <__main__.Rooms object at 0x240ac10>, <__main__.Rooms object at 0x240add0>, <__main__.Rooms object at 0x240ad90>, <__main__.Rooms object at 0x240aef0>]
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 80, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 77, in main
    Entryway.name
NameError: global name 'Entryway' is not defined
>>> ================================ RESTART ================================
>>> 
[<__main__.Rooms object at 0x2c0ab50>, <__main__.Rooms object at 0x2c0abd0>, <__main__.Rooms object at 0x2c0ab70>, <__main__.Rooms object at 0x2c0acb0>, <__main__.Rooms object at 0x2c0ac10>, <__main__.Rooms object at 0x2c0add0>, <__main__.Rooms object at 0x2c0ad90>, <__main__.Rooms object at 0x2c0aef0>]
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 80, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 77, in main
    Entryway.name()
NameError: global name 'Entryway' is not defined
>>> name = "bob"
>>> name
'bob'
>>> print(name)
bob
>>> eval(name)
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    eval(name)
  File "<string>", line 1, in <module>
NameError: name 'bob' is not defined
>>> name(1)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    name(1)
TypeError: 'str' object is not callable
>>> ================================ RESTART ================================
>>> 
{'DiningRoom': <__main__.Rooms object at 0x2c0ae70>, 'StairsUp': <__main__.Rooms object at 0x2c0ad30>, 'ParlorRoom': <__main__.Rooms object at 0x2c0abd0>, 'Kitchen': <__main__.Rooms object at 0x2c0adf0>, 'Hallway': <__main__.Rooms object at 0x2c0acb0>, 'SittingRoom': <__main__.Rooms object at 0x2c0ab70>, 'Entryway': <__main__.Rooms object at 0x2c0ab50>, 'HiddenRoom': <__main__.Rooms object at 0x2c0af30>}
>>> ================================ RESTART ================================
>>> 
{'HiddenRoom': <__main__.Rooms object at 0x2c0af30>, 'Entryway': <__main__.Rooms object at 0x2c0ab50>, 'SittingRoom': <__main__.Rooms object at 0x2c0ab70>, 'Hallway': <__main__.Rooms object at 0x2c0acb0>, 'Kitchen': <__main__.Rooms object at 0x2c0adf0>, 'ParlorRoom': <__main__.Rooms object at 0x2c0abd0>, 'StairsUp': <__main__.Rooms object at 0x2c0ad30>, 'DiningRoom': <__main__.Rooms object at 0x2c0ae70>}
>>> ================================ RESTART ================================
>>> 
{'DiningRoom': <__main__.Rooms object at 0x2c0ae90>, 'HiddenRoom': <__main__.Rooms object at 0x2c0af50>, 'StairsUp': <__main__.Rooms object at 0x2c0ad50>, 'Hallway': <__main__.Rooms object at 0x2c0acd0>, 'Kitchen': <__main__.Rooms object at 0x2c0ae10>, 'ParlorRoom': <__main__.Rooms object at 0x2c0abf0>, 'Entryway': <__main__.Rooms object at 0x2c0ab70>, 'SittingRoom': <__main__.Rooms object at 0x2c0ab90>}
>>> ================================ RESTART ================================
>>> 
{'StairsUp': <__main__.Rooms object at 0x2c0ad30>, 'HiddenRoom': <__main__.Rooms object at 0x2c0af30>, 'DiningRoom': <__main__.Rooms object at 0x2c0ae70>, 'SittingRoom': <__main__.Rooms object at 0x2c0ab70>, 'Entryway': <__main__.Rooms object at 0x2c0ab50>, 'ParlorRoom': <__main__.Rooms object at 0x2c0abd0>, 'Kitchen': <__main__.Rooms object at 0x2c0adf0>, 'Hallway': <__main__.Rooms object at 0x2c0acb0>}
>>> ================================ RESTART ================================
>>> 
{'ParlorRoom': <__main__.Rooms object at 0x2c0abd0>, 'DiningRoom': <__main__.Rooms object at 0x2c0ae70>, 'HiddenRoom': <__main__.Rooms object at 0x2c0af30>, 'Kitchen': <__main__.Rooms object at 0x2c0adf0>, 'Hallway': <__main__.Rooms object at 0x2c0acb0>, 'SittingRoom': <__main__.Rooms object at 0x2c0ab70>, 'Entryway': <__main__.Rooms object at 0x2c0ab50>, 'StairsUp': <__main__.Rooms object at 0x2c0ad30>}
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 79, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 76, in main
    roomsByName.get(Entryway, unknown)
NameError: global name 'Entryway' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 80, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 76, in main
    roomsByName.get(Entryway, unknown)
NameError: global name 'Entryway' is not defined
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
{'HiddenRoom': <__main__.Rooms object at 0x240af30>, 'Kitchen': <__main__.Rooms object at 0x240adf0>, 'Hallway': <__main__.Rooms object at 0x240acb0>, 'ParlorRoom': <__main__.Rooms object at 0x240abd0>, 'SittingRoom': <__main__.Rooms object at 0x240ab70>, 'Entryway': <__main__.Rooms object at 0x240ab50>, 'StairsUp': <__main__.Rooms object at 0x240ad30>, 'DiningRoom': <__main__.Rooms object at 0x240ae70>}
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 71, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 65, in main
    rooms = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 60, in roomSetup
    rooms[newroom.roomName] = newroom
AttributeError: 'Rooms' object has no attribute 'roomName'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 71, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 67, in main
    exits = rooms[roomCheck].roomExits
KeyError: 'entryway'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 71, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 67, in main
    exits = rooms[roomCheck].roomExits
AttributeError: 'Rooms' object has no attribute 'roomExits'
>>> ================================ RESTART ================================
>>> 
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
>>> ================================ RESTART ================================
>>> 
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 449, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 441, in main
    items = itemsSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 116, in itemsSetup
    items[newItem.name] = newItem
AttributeError: 'Items' object has no attribute 'name'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 449, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 445, in main
    roomDescription(location, rooms, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 346, in roomDescription
    checkHiddenExit = int(rooms[location].hiddenExitable)
KeyError: 0
>>> ================================ RESTART ================================
>>> 
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 72, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 69, in main
    print(rooms[0].exits)
KeyError: 0
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 452, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 443, in main
    rooms = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 182, in roomSetup
    rooms[newRoom.name] = newRoom
TypeError: list indices must be integers, not str
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 452, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 443, in main
    rooms = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 180, in roomSetup
    rooms = collections.OrderedDict(rooms)
NameError: global name 'collections' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 452, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 444, in main
    items = itemsSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 117, in itemsSetup
    items[newItem.itemName] = newItem
TypeError: list indices must be integers, not str
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 453, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 445, in main
    items = itemsSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 120, in itemsSetup
    items = collections.OrderedDict(items)
NameError: global name 'collections' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 452, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 448, in main
    roomDescription(location, rooms, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 349, in roomDescription
    checkHiddenExit = int(rooms[location].hiddenExitable)
KeyError: 0
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 452, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 448, in main
    roomDescription(location, rooms, items)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 349, in roomDescription
    checkHiddenExit = int(rooms.items()[location].hiddenExitable)
TypeError: 'ItemsView' object does not support indexing
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 75, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 67, in main
    rooms = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 64, in roomSetup
    return rooms
NameError: global name 'rooms' is not defined
>>> ================================ RESTART ================================
>>> 
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
>>> ================================ RESTART ================================
>>> 
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
{'up': 9}
>>> ================================ RESTART ================================
>>> 
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
{'up': 9}
<built-in method items of dict object at 0x23ed710>
>>> ================================ RESTART ================================
>>> 
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
{'up': 9}
dict_items([('DiningRoom', <__main__.Rooms object at 0x240b970>), ('ParlorRoom', <__main__.Rooms object at 0x240b710>), ('SittingRoom', <__main__.Rooms object at 0x240b730>), ('Entryway', <__main__.Rooms object at 0x240b690>), ('Kitchen', <__main__.Rooms object at 0x240b8f0>), ('HiddenRoom', <__main__.Rooms object at 0x240ba10>), ('Hallway', <__main__.Rooms object at 0x240b7d0>), ('StairsUp', <__main__.Rooms object at 0x240b850>)])
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 79, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 68, in main
    roomsDict, roomsList = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 63, in roomSetup
    roomsList.append((newroom.name), (newroom))
TypeError: append() takes exactly one argument (2 given)
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 80, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 71, in main
    exits = roomsDict[roomCheck].exits
KeyError: 'Entryway'
>>> ================================ RESTART ================================
>>> 
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
>>> ================================ RESTART ================================
>>> 
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 81, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 73, in main
    print(rooms.items()[0])
TypeError: 'ItemsView' object does not support indexing
>>> ================================ RESTART ================================
>>> 
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 81, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 73, in main
    print(rooms.items()[0].exits)
TypeError: 'ItemsView' object does not support indexing
>>> ================================ RESTART ================================
>>> 
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
ItemsView(OrderedDict([('Entryway', <__main__.Rooms object at 0x240b6d0>), ('ParlorRoom', <__main__.Rooms object at 0x240b750>), ('SittingRoom', <__main__.Rooms object at 0x240b770>), ('Hallway', <__main__.Rooms object at 0x240b810>), ('StairsUp', <__main__.Rooms object at 0x240b890>), ('Kitchen', <__main__.Rooms object at 0x240b930>), ('DiningRoom', <__main__.Rooms object at 0x240b9b0>), ('HiddenRoom', <__main__.Rooms object at 0x240ba50>)]))
>>> TypeError: 'ItemsView' object does not support indexing
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> import collections
>>> d = collections.OrderedDict()
>>> d['foo'] = 'python'
>>> d['bar'] = 'spam'
>>> d.items()
ItemsView(OrderedDict([('foo', 'python'), ('bar', 'spam')]))
>>> d.items()[0]
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    d.items()[0]
TypeError: 'ItemsView' object does not support indexing
>>> ================================ RESTART ================================
>>> 
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
ItemsView(OrderedDict([('Entryway', <__main__.Rooms object at 0x240b6b0>), ('ParlorRoom', <__main__.Rooms object at 0x240b730>), ('SittingRoom', <__main__.Rooms object at 0x240b750>), ('Hallway', <__main__.Rooms object at 0x240b7f0>), ('StairsUp', <__main__.Rooms object at 0x240b870>), ('Kitchen', <__main__.Rooms object at 0x240b910>), ('DiningRoom', <__main__.Rooms object at 0x240b990>), ('HiddenRoom', <__main__.Rooms object at 0x240ba30>)]))
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 82, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 74, in main
    print(list(rooms.values()[0].exits))
TypeError: 'ValuesView' object does not support indexing
>>> ================================ RESTART ================================
>>> 
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
ItemsView(OrderedDict([('Entryway', <__main__.Rooms object at 0x2c0b6b0>), ('ParlorRoom', <__main__.Rooms object at 0x2c0b730>), ('SittingRoom', <__main__.Rooms object at 0x2c0b750>), ('Hallway', <__main__.Rooms object at 0x2c0b7f0>), ('StairsUp', <__main__.Rooms object at 0x2c0b870>), ('Kitchen', <__main__.Rooms object at 0x2c0b910>), ('DiningRoom', <__main__.Rooms object at 0x2c0b990>), ('HiddenRoom', <__main__.Rooms object at 0x2c0ba30>)]))
[<__main__.Rooms object at 0x2c0b6b0>, <__main__.Rooms object at 0x2c0b730>, <__main__.Rooms object at 0x2c0b750>, <__main__.Rooms object at 0x2c0b7f0>, <__main__.Rooms object at 0x2c0b870>, <__main__.Rooms object at 0x2c0b910>, <__main__.Rooms object at 0x2c0b990>, <__main__.Rooms object at 0x2c0ba30>]
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 81, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 68, in main
    rooms, roomsByIndex = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 61, in roomSetup
    roomsDict[newroom.name] = newroom
NameError: global name 'roomsDict' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 81, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 68, in main
    rooms, roomsByIndex = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 61, in roomSetup
    rooms[newroom.name] = newroom
TypeError: list indices must be integers, not str
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 82, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 69, in main
    rooms, roomsByIndex = roomSetup()
ValueError: too many values to unpack (expected 2)
>>> ================================ RESTART ================================
>>> 
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
ItemsView(OrderedDict([('Entryway', <__main__.Rooms object at 0x240b730>), ('ParlorRoom', <__main__.Rooms object at 0x240b810>), ('SittingRoom', <__main__.Rooms object at 0x240b830>), ('Hallway', <__main__.Rooms object at 0x240b8d0>), ('StairsUp', <__main__.Rooms object at 0x240b950>), ('Kitchen', <__main__.Rooms object at 0x240b9f0>), ('DiningRoom', <__main__.Rooms object at 0x240ba70>), ('HiddenRoom', <__main__.Rooms object at 0x240bb10>)]))
>>> ================================ RESTART ================================
>>> 
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
ItemsView(OrderedDict([('Entryway', <__main__.Rooms object at 0x240b730>), ('ParlorRoom', <__main__.Rooms object at 0x240b810>), ('SittingRoom', <__main__.Rooms object at 0x240b830>), ('Hallway', <__main__.Rooms object at 0x240b8d0>), ('StairsUp', <__main__.Rooms object at 0x240b950>), ('Kitchen', <__main__.Rooms object at 0x240b9f0>), ('DiningRoom', <__main__.Rooms object at 0x240ba70>), ('HiddenRoom', <__main__.Rooms object at 0x240bb10>)]))
>>> ================================ RESTART ================================
>>> 
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
ItemsView(OrderedDict([('Entryway', <__main__.Rooms object at 0x2c0b730>), ('ParlorRoom', <__main__.Rooms object at 0x2c0b810>), ('SittingRoom', <__main__.Rooms object at 0x2c0b830>), ('Hallway', <__main__.Rooms object at 0x2c0b8d0>), ('StairsUp', <__main__.Rooms object at 0x2c0b950>), ('Kitchen', <__main__.Rooms object at 0x2c0b9f0>), ('DiningRoom', <__main__.Rooms object at 0x2c0ba70>), ('HiddenRoom', <__main__.Rooms object at 0x2c0bb10>)]))
<__main__.Rooms object at 0x2c0b730>
>>> ================================ RESTART ================================
>>> 
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
ItemsView(OrderedDict([('Entryway', <__main__.Rooms object at 0x240b730>), ('ParlorRoom', <__main__.Rooms object at 0x240b810>), ('SittingRoom', <__main__.Rooms object at 0x240b830>), ('Hallway', <__main__.Rooms object at 0x240b8d0>), ('StairsUp', <__main__.Rooms object at 0x240b950>), ('Kitchen', <__main__.Rooms object at 0x240b9f0>), ('DiningRoom', <__main__.Rooms object at 0x240ba70>), ('HiddenRoom', <__main__.Rooms object at 0x240bb10>)]))
Entryway
>>> ================================ RESTART ================================
>>> 
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
ItemsView(OrderedDict([('Entryway', <__main__.Rooms object at 0x240b750>), ('ParlorRoom', <__main__.Rooms object at 0x240b830>), ('SittingRoom', <__main__.Rooms object at 0x240b850>), ('Hallway', <__main__.Rooms object at 0x240b8f0>), ('StairsUp', <__main__.Rooms object at 0x240b970>), ('Kitchen', <__main__.Rooms object at 0x240ba10>), ('DiningRoom', <__main__.Rooms object at 0x240ba90>), ('HiddenRoom', <__main__.Rooms object at 0x240bb30>)]))
Entryway
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 82, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 78, in main
    print(room.items())
NameError: global name 'room' is not defined
>>> ================================ RESTART ================================
>>> 
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
ItemsView(OrderedDict([('Entryway', <__main__.Rooms object at 0x2c0b730>), ('ParlorRoom', <__main__.Rooms object at 0x2c0b810>), ('SittingRoom', <__main__.Rooms object at 0x2c0b830>), ('Hallway', <__main__.Rooms object at 0x2c0b8d0>), ('StairsUp', <__main__.Rooms object at 0x2c0b950>), ('Kitchen', <__main__.Rooms object at 0x2c0b9f0>), ('DiningRoom', <__main__.Rooms object at 0x2c0ba70>), ('HiddenRoom', <__main__.Rooms object at 0x2c0bb10>)]))
Entryway
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
ItemsView(OrderedDict([('Entryway', <__main__.Rooms object at 0x2c0b730>), ('ParlorRoom', <__main__.Rooms object at 0x2c0b810>), ('SittingRoom', <__main__.Rooms object at 0x2c0b830>), ('Hallway', <__main__.Rooms object at 0x2c0b8d0>), ('StairsUp', <__main__.Rooms object at 0x2c0b950>), ('Kitchen', <__main__.Rooms object at 0x2c0b9f0>), ('DiningRoom', <__main__.Rooms object at 0x2c0ba70>), ('HiddenRoom', <__main__.Rooms object at 0x2c0bb10>)]))
{'up': 9}
>>> ================================ RESTART ================================
>>> 
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
{'up': 9}
{'up': 9}
>>> ================================ RESTART ================================
>>> 
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
{'up': 9}
{'up': 9}
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 90, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 82, in main
    roomsByName[1].name = "ParlorRoom2"
NameError: global name 'roomsByName' is not defined
>>> ================================ RESTART ================================
>>> 
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
{'up': 9}
{'up': 9}
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 90, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 82, in main
    rooms[1].name = "ParlorRoom2"
KeyError: 1
>>> ================================ RESTART ================================
>>> 
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
{'up': 9}
{'up': 9}
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 90, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 83, in main
    print(rooms["ParlorRoom2"].name)
KeyError: 'ParlorRoom2'
>>> ================================ RESTART ================================
>>> 
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
{'up': 9}
{'up': 9}
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 91, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/roomtest.py", line 84, in main
    print(rooms[roomCheck].name)
KeyError: 'ParlorRoom2'
>>> ================================ RESTART ================================
>>> 
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
{'e':1, 'east':1, 'n':3, 'north':3, 'w':2, 'west':2}
{'up': 9}
{'up': 9}
ParlorRoom2
ParlorRoom2
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 454, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 445, in main
    roomsByName, roomsByIndex = roomSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 186, in roomSetup
    roomsByIndex = list(roomsByName(values()))
NameError: global name 'values' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 454, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 450, in main
    roomDescription(location, roomsByIndex, items)
NameError: global name 'items' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 454, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 450, in main
    roomDescription(location, roomsByIndex, itemsByIndex)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 351, in roomDescription
    checkHiddenExit = int(rooms.items()[location].hiddenExitable)
AttributeError: 'list' object has no attribute 'items'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 454, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 450, in main
    roomDescription(location, roomsByIndex, itemsByIndex)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 351, in roomDescription
    checkHiddenExit = int(roomsByIndex[location].hiddenExitable)
NameError: global name 'roomsByIndex' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? eTypeError: 'ValuesView' object does not support indexing
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 454, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 451, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 211, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByindex, location)
NameError: global name 'itemsByindex' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 454, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 451, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 211, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 240, in verbAndNounCheck
    inventory = inventoryCheck(itemsByIndex, "notprint")
NameError: global name 'itemsByIndex' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
What do you do? get note
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 454, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 451, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 211, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 247, in verbAndNounCheck
    getDropItems(itemsByName, location, "get", noun)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 362, in getDropItems
    checkLocation = itemsByName[noun].itemLocation
KeyError: 'note'
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear faint laughter.

What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
What do you do? get note
There is no note to get!
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
What do you do? get note
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 454, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 451, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 211, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 247, in verbAndNounCheck
    getDropItems(itemsByName, location, "get", noun)
TypeError: getDropItems() missing 1 required positional argument: 'noun'
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? get note
There is no note to get!
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
What do you do? get note
1
1
1
0
There is no note to get!
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
What do you do? get note
1
1
1
0
<class 'int'>
<class 'str'>
<class 'str'>
<class 'str'>
There is no note to get!
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear footsteps.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
What do you do? get note
1
1
1
0
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
You pick up the note .
What do you do? drop note
1
-1
1
0
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
You drop the note .
Rats scurry across the floor.

What do you do? get note
1
1
1
0
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
You pick up the note .
What do you do? inv
In your inventory you have:
note
What do you do? e
You can't go in that direction!
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? drop note
0
-1
1
0
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
You drop the note .
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
What do you do? get note
You pick up the note .
What do you do? look note
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 454, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 451, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 211, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 257, in verbAndNounCheck
    useItems(itemsByName, location, verb, noun)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 428, in useItems
    inventory = inventoryCheck(items, "notprint")
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 311, in inventoryCheck
    checkLocation = int(itemsByIndex[n].itemLocation)
KeyError: 0
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
What do you do? get note
You pick up the note .
What do you do? look note
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 456, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 453, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 211, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 257, in verbAndNounCheck
    print(itemsByName[name].itemLongDescription)
NameError: global name 'name' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
What do you do? get note
You pick up the note .
What do you do? look note
a handwritten note, written in beautiful cursive.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? search room
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 456, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 453, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 211, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 253, in verbAndNounCheck
    searchCheck(roomsByIndex, itemsByIndex, noun, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 330, in searchCheck
    numItems = len(items)
NameError: global name 'items' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? search room
Your search reveals nothing!
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? search room
Your search reveals nothing!
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? look room
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 456, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 453, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 211, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 245, in verbAndNounCheck
    location = moveCheck(roomsByIndex, itemsByIndex, verb, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 277, in moveCheck
    roomDescription(location, roomsByIndex, itemsByName)
NameError: global name 'itemsByName' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? get comb
You pick up the comb .
What do you do? inv
In your inventory you have:
comb
In your inventory you have:
bomb
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
Rats scurry across the floor.

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? get comb
You pick up the comb .
What do you do? inv
In your inventory you have:
comb
bomb
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
There is a door to the east.
What do you do? look room
The hidden room
There is a door to the east.
What do you do? search room
Your search reveals nothing!
What do you do? w
You can't go in that direction!
What do you do? n
You can't go in that direction!
What do you do? e
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
What do you do? n
The kitchen.
There are doors to the south, and east.
What do you do? look room
The kitchen.
There are doors to the south, and east.
What do you do? drop bomb
You drop the bomb .
What do you do? drop comb
You drop the comb .
What do you do? lookroom
Huh?
What do you do? look room
The kitchen.
You see an ivory comb tossed carelessly on the the floor.
There is a disarmed bomb on the floor.
There are doors to the south, and east.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? look room
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? search room
Your search reveals nothing!
What do you do? n
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
What do you do? get elephant
You can't pick up the elephant .
What do you do? n
The kitchen.
There are doors to the south, and east.
What do you do? look elephant
Huh?
What do you do? s
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
What do you do? look elephant
an elephant
What do you do? e
Stairs leading up.
At the top of the stairs is a locked door. You can go back down the stairs to the west.
What do you do? w
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
What do you do? e
Stairs leading up.
At the top of the stairs is a locked door. You can go back down the stairs to the west.
What do you do? w
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
What do you do? e
Stairs leading up.
At the top of the stairs is a locked door. You can go back down the stairs to the west.
What do you do? e
You can't go in that direction!
What do you do? n
You can't go in that direction!
What do you do? s
You can't go in that direction!
What do you do? search room
Your search reveals nothing!
You hear footsteps.
What do you do? 
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 343, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 335, in main
    itemsByName, itemsByIndex = itemsSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 57, in itemsSetup
    newItem = makeItems(line)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 48, in makeItems
    itemID, itemName, itemLocation, itemLocationOriginal, itemFriendlyLocation, itemLongDescription, itemShortDescription, itemLocationOriginalDesc, itemDroppedDescription, itemGettable, itemDoable, itemLimited, itemUses, itemHidden, itemActions, itemActionRequirements, itemActionReqFailureDesc, itemActionType, itemActionOutcomeDescSuccess, itemActionOutcomeDescFailure = infoStr.split("//")
ValueError: need more than 1 value to unpack
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
What do you do? get note
You pick up the note .
What do you do? read note
The note says, "I'm not afraid to die. Are you?"
What do you do? drop note
You drop the note .
What do you do? e
You can't go in that direction!
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? read note
Huh?
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
What do you do? read note
The note says, "I'm not afraid to die. Are you?"
What do you do? look note
It's a handwritten note, written in beautiful cursive.
What do you do? use note
The note says, "I'm not afraid to die. Are you?"
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
What do you do? read note
The note says, "I'm not afraid to die. Are you?"
You hear footsteps.
What do you do? use note
Do what with the note ?
You hear footsteps.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
You hear footsteps.
What do you do? use note
Do what with the note ?
What do you do? n
The Dining room.
There are doors to the south, and west.
What do you do? look room
The Dining room.
There are doors to the south, and west.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? go east
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
What do you do? read note
The note says, "I'm not afraid to die. Are you?"
You hear faint laughter.

What do you do? look room
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? drop bomb
You drop the bomb .
What do you do? i
You're not carrying anything!
What do you do? get bomb
You pick up the bomb .
What do you do? i
In your inventory you have:
bomb
What do you do? look
Huh?
What do you do? look room
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? n
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
What do you do? get elephant
You can't pick up the elephant .
What do you do? go north
The kitchen.
There are doors to the south, and east.
What do you do? walk east
The Dining room.
There are doors to the south, and west.
What do you do? s
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
What do you do? get note
You pick up the note .
What do you do? read note
The note says, "I'm not afraid to die. Are you?"
What do you do? inv
In your inventory you have:
note
bomb
What do you do? drop note
You drop the note .
What do you do? inv
In your inventory you have:
bomb
What do you do? 
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 346, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 338, in main
    itemsByName, itemsByIndex = itemsSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 56, in itemsSetup
    newItem = makeItems(line)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 47, in makeItems
    itemID, itemName, itemLocation, itemLocationOriginal, itemFriendlyLocation, itemLongDescription, itemShortDescription, itemLocationOriginalDesc, itemDroppedDescription, itemGettable, itemDoable, itemLimited, itemUses, itemHidden, itemActions, itemActionRequirements, itemActionType, itemActionOutcomeDescSuccess, itemActionOutcomeDescFailure = infoStr.split("//")
ValueError: too many values to unpack (expected 19)
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? use bomb
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 346, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 343, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 117, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 165, in verbAndNounCheck
    useItems(itemsByName, location, verb, noun)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 309, in useItems
    print(itemActionReqFailureDesc.get("notInventory", "unknown"))
NameError: global name 'itemActionReqFailureDesc' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
Rats scurry across the floor.

What do you do? use bomb
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 346, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 343, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 117, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 165, in verbAndNounCheck
    useItems(itemsByName, location, verb, noun)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 309, in useItems
    print(itemActionRequirements.get("notInventory", "unknown"))
NameError: global name 'itemActionRequirements' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? use bomb
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 348, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 345, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 117, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 165, in verbAndNounCheck
    useItems(itemsByName, location, verb, noun)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 307, in useItems
    itemReq = ast.literal_eval(itemReqStr)
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 47, in literal_eval
    node_or_string = parse(node_or_string, mode='eval')
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 35, in parse
    return compile(source, filename, mode, PyCF_ONLY_AST)
  File "<unknown>", line 1
    {'notInventory':'You can't use the bomb while you're holding it!', 'location':'You can't use the bomb here!'}
                             ^
SyntaxError: invalid syntax
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? wSyntaxError: invalid syntax
Huh?
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
What do you do? get note
You pick up the note .
What do you do? read note
The note says, "I'm not afraid to die. Are you?"
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? use bomb
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 349, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 346, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 117, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 165, in verbAndNounCheck
    useItems(itemsByName, location, verb, noun)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 307, in useItems
    itemReq = ast.literal_eval(itemReqStr)
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 47, in literal_eval
    node_or_string = parse(node_or_string, mode='eval')
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 35, in parse
    return compile(source, filename, mode, PyCF_ONLY_AST)
  File "<unknown>", line 1
    {'notInventory':'You can't use the bomb while you're holding it!', 'location':'You can't use the bomb here!'}
                             ^
SyntaxError: invalid syntax
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
Rats scurry across the floor.

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? use bomb
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 349, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 346, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 117, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 165, in verbAndNounCheck
    useItems(itemsByName, location, verb, noun)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 307, in useItems
    itemReq = ast.literal_eval(itemReqStr)
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 47, in literal_eval
    node_or_string = parse(node_or_string, mode='eval')
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 35, in parse
    return compile(source, filename, mode, PyCF_ONLY_AST)
  File "<unknown>", line 1
    {'notInventory':'You can't use the bomb while you're holding it!', 'location':'You can't use the bomb here!'}
                             ^
SyntaxError: invalid syntax
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? use bomb
<class 'dict'>
Do what with the bomb ?
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? use bob
Huh?
What do you do? use bomb
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 349, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 346, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 117, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 165, in verbAndNounCheck
    useItems(itemsByName, location, verb, noun)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 307, in useItems
    itemReq = ast.literal_eval(itemReqStr)
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 47, in literal_eval
    node_or_string = parse(node_or_string, mode='eval')
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 35, in parse
    return compile(source, filename, mode, PyCF_ONLY_AST)
  File "<unknown>", line 1
    {'notInventory':You can't use the bomb while you're holding it!, 'location':You can't use the bomb here!}
                          ^
SyntaxError: invalid syntax
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? 
Huh?
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? use bomb
<class 'dict'>
4
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? use bomb
<class 'dict'>
4
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? use bomb
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 349, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 346, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 117, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 165, in verbAndNounCheck
    useItems(itemsByName, location, verb, noun)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 307, in useItems
    itemReq = ast.literal_eval(itemReqStr)
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 47, in literal_eval
    node_or_string = parse(node_or_string, mode='eval')
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 35, in parse
    return compile(source, filename, mode, PyCF_ONLY_AST)
  File "<unknown>", line 1
    {'notInventory':'You can't use the bomb while you're holding it!'}
                             ^
SyntaxError: invalid syntax
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear faint laughter.

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? use bomb
<class 'dict'>
You can't use the bomb while you're holding it!
You hear footsteps.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
Rats scurry across the floor.

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? use bomb
<class 'dict'>
You can't use the bomb while you're holding it!
You hear footsteps.
What do you do? drop bomb
You drop the bomb .
What do you do? use bomb
<class 'dict'>
You can't use the bomb here!
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? use bomb
You can't use the bomb while you're holding it!
Rats scurry across the floor.

What do you do? drop bomb
You drop the bomb .
You hear faint laughter.

What do you do? use bomb
You can't use the bomb here!
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? use bomb
Huh?
What do you do? use note
Huh?
What do you do? read note
Huh?
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? use comb
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 351, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 348, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 117, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 165, in verbAndNounCheck
    useItems(itemsByName, location, verb, noun)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 306, in useItems
    itemReq = ast.literal_eval(itemsByName[noun].itemActionRequirements)
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 47, in literal_eval
    node_or_string = parse(node_or_string, mode='eval')
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 35, in parse
    return compile(source, filename, mode, PyCF_ONLY_AST)
  File "<unknown>", line 1
    {'inventory':'How can you comb your hair? You don't have the comb in your inventory'}
                                                      ^
SyntaxError: invalid syntax
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? use comb
Do what with the comb ?
What do you do? get comb
You pick up the comb .
What do you do? use comb
none
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? use comb
Do what with the comb ?
What do you do? get comb
You pick up the comb .
What do you do? use comb
none
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? ue comb
Huh?
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? use comb
How can you comb your hair? You don't have the comb in your inventory.
What do you do? get comb
You pick up the comb .
Rats scurry across the floor.

What do you do? use comb
none
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? use comb
How can you comb your hair? You don't have the comb in your inventory.
What do you do? get comb
You pick up the comb .
What do you do? use comb
"You comb your hair/"
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get comb
You pick up the comb .
What do you do? get bomb
You pick up the bomb .
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? inv
In your inventory you have:
comb
bomb
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? n
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
What do you do? use elephant
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 355, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 352, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 117, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 165, in verbAndNounCheck
    useItems(itemsByName, location, verb, noun)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 305, in useItems
    checkItemActionType = ast.literal_eval(itemsByName[noun].itemActionType)
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 86, in literal_eval
    return _convert(node_or_string)
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 85, in _convert
    raise ValueError('malformed node or string: ' + repr(node))
ValueError: malformed node or string: <_ast.Name object at 0x2c13d30>
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
You hear footsteps.
What do you do? get bomb
You pick up the bomb .
You hear footsteps.
What do you do? get comb
You pick up the comb .
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? n
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
What do you do? get elephant
You can't pick up the elephant .
What do you do? use elephant
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 355, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 352, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 117, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 165, in verbAndNounCheck
    useItems(itemsByName, location, verb, noun)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 306, in useItems
    itemReq = ast.literal_eval(itemsByName[noun].itemActionRequirements)
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 47, in literal_eval
    node_or_string = parse(node_or_string, mode='eval')
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 35, in parse
    return compile(source, filename, mode, PyCF_ONLY_AST)
  File "<unknown>", line 1
    {'none':'You can't use the elephant!'}
                     ^
SyntaxError: invalid syntax
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get comb
You pick up the comb .
What do you do? get bomb
You pick up the bomb .
What do you do? use comb
"You comb your hair."
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
You hear faint laughter.

What do you do? use comb
How can you comb your hair? You don't have the comb in your inventory.
What do you do? get comb
You pick up the comb .
What do you do? use comb
'You comb your hair.'
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get comb
You pick up the comb .
What do you do? use comb
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 355, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 352, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 117, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 165, in verbAndNounCheck
    useItems(itemsByName, location, verb, noun)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 305, in useItems
    checkItemActionType = ast.literal_eval(itemsByName[noun].itemActionType)
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 47, in literal_eval
    node_or_string = parse(node_or_string, mode='eval')
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 35, in parse
    return compile(source, filename, mode, PyCF_ONLY_AST)
  File "<unknown>", line 1
    {'message':You comb your hair.}
                      ^
SyntaxError: invalid syntax
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get comb
You pick up the comb .
What do you do? use comb
'You comb your hair.'
What do you do? get bomb
You pick up the bomb .
What do you do? use bomb
You can't use the bomb while you're holding it!
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
What do you do? read note
The note says, "I'm not afraid to die. Are you?"
What do you do? use bomb
You can't use the bomb while you're holding it!
What do you do? use comb
'You comb your hair.'
What do you do? use note
Do what with the note ?
What do you do? read note
The note says, "I'm not afraid to die. Are you?"
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get comb
You pick up the comb .
What do you do? use comb
You comb your hair.
What do you do? get bomb
You pick up the bomb .
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? w
You can't go in that direction!
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? n
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
You hear faint laughter.

What do you do? get elephant
You can't pick up the elephant .
What do you do? use elephant
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 355, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 352, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 117, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 165, in verbAndNounCheck
    useItems(itemsByName, location, verb, noun)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 306, in useItems
    itemReq = ast.literal_eval(itemsByName[noun].itemActionRequirements)
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 47, in literal_eval
    node_or_string = parse(node_or_string, mode='eval')
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 35, in parse
    return compile(source, filename, mode, PyCF_ONLY_AST)
  File "<unknown>", line 1
    {'none':'You can't use the elephant!'}
                     ^
SyntaxError: invalid syntax
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
Rats scurry across the floor.

What do you do? get bomb
You pick up the bomb .
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
Rats scurry across the floor.

What do you do? n
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
What do you do? use elephant
Do what with the elephant ?
What do you do? look room
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
What do you do? e
Stairs leading up.
At the top of the stairs is a locked door. You can go back down the stairs to the west.
What do you do? use bomb
You can't use the bomb while you're holding it!
What do you do? drop bomb
You drop the bomb .
What do you do? use bomb
Do what with the bomb ?
What do you do? get bomb
You pick up the bomb .
What do you do? w
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
What do you do? drop bomb
You drop the bomb .
What do you do? use bomb
You can't use the bomb here!
What do you do? get bomb
You pick up the bomb .
What do you do? e
Stairs leading up.
At the top of the stairs is a locked door. You can go back down the stairs to the west.
What do you do? drop bomb
You drop the bomb .
What do you do? use bomb
Do what with the bomb ?
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear faint laughter.

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? n
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
What do you do? e
Stairs leading up.
At the top of the stairs is a locked door. You can go back down the stairs to the west.
What do you do? drop bomb
You drop the bomb .
What do you do? use bomb
Huh?
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? n
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
What do you do? e
Stairs leading up.
At the top of the stairs is a locked door. You can go back down the stairs to the west.
What do you do? drop bomb
You drop the bomb .
What do you do? use bomb
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 361, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 358, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 117, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 165, in verbAndNounCheck
    useItems(itemsByName, roomsByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 313, in useItems
    useItemsSuccess(itemsByName, location, verb, noun)
TypeError: useItemsSuccess() missing 1 required positional argument: 'noun'
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? n
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
What do you do? e
Stairs leading up.
At the top of the stairs is a locked door. You can go back down the stairs to the west.
What do you do? drop bomb
You drop the bomb .
What do you do? use bomb
Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 361, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 358, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 117, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 165, in verbAndNounCheck
    useItems(itemsByName, roomsByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 313, in useItems
    useItemsSuccess(itemsByName, roomsByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 329, in useItemsSuccess
    if "unhideLocation" in checkActionType:
NameError: global name 'checkActionType' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? n
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
What do you do? e
Stairs leading up.
At the top of the stairs is a locked door. You can go back down the stairs to the west.
What do you do? drop bomb
You drop the bomb .
What do you do? use bomb
The bomb explodes with a thundering bang, and a shockwave washes over you.
The bomb has revealed none
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? n
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
What do you do? e
Stairs leading up.
At the top of the stairs is a locked door. You can go back down the stairs to the west.
What do you do? drop bomb
You drop the bomb .
What do you do? use bomb
The bomb explodes with a thundering bang, and a shockwave washes over you.
The locked door has been blown off its hinges!
What do you do? look room
Stairs leading up.
There is a disarmed bomb on the floor.
At the top of the stairs is a locked door. You can go back down the stairs to the west.
What do you do? e
The upstairs hallway
You can go east along the hallway, or west back down the stairs.
You hear faint laughter.

What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? n
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
What do you do? e
Stairs leading up.
At the top of the stairs is a locked door. You can go back down the stairs to the west.
What do you do? drop bomb
You drop the bomb .
What do you do? use bomb
The bomb explodes with a thundering bang, and a shockwave washes over you.
The locked door has been blown off its hinges!
What do you do? look room
Stairs leading up.
There is a disarmed bomb on the floor.
At the top of the stairs is a locked door. You can go back down the stairs to the west.
What do you do? 
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 372, in <module>
    main()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 364, in main
    itemsByName, itemsByIndex = itemsSetup()
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 57, in itemsSetup
    newItem = makeItems(line)
  File "/Users/cwinter/Documents/Python Stuff/adventure2.py", line 48, in makeItems
    itemID, itemName, itemLocation, itemLocationOriginal, itemFriendlyLocation, itemLongDescription, itemShortDescription, itemLocationOriginalDesc, itemDroppedDescription, itemGettable, itemDoable, itemLimited, itemUses, itemRefillable, itemHidden, itemActions, itemActionRequirements, itemActionType, itemActionOutcomeDescSuccess, itemActionOutcomeDescFailure = infoStr.split("//")
ValueError: need more than 1 value to unpack
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? n
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
What do you do? e
Stairs leading up.
At the top of the stairs is a locked door. You can go back down the stairs to the west.
What do you do? drop bomb
You drop the bomb .
What do you do? use bomb
The bomb explodes with a thundering bang, and a shockwave washes over you.
The locked door has been blown off its hinges!
What do you do? look room
Stairs leading up.
At the top of the stairs is a locked door. You can go back down the stairs to the west.
What do you do? inv
You're not carrying anything!
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear footsteps.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? n
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
What do you do? e
Stairs leading up.
At the top of the stairs is a locked door. You can go back down the stairs to the west.
What do you do? drop bomb
You drop the bomb .
What do you do? use bomb
The bomb explodes with a thundering bang, and a shockwave washes over you.
The locked door has been blown off its hinges!
What do you do? look room
Stairs leading up.
You can go back down the stairs to the west. To the east, a door hangs from its hinges.
What do you do? e
The upstairs hallway
You can go east along the hallway, or west back down the stairs.
What do you do? 
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/cwinter/Documents/Adventure/adventure2.py", line 375, in <module>
    main()
  File "/Users/cwinter/Documents/Adventure/adventure2.py", line 366, in main
    roomsByName, roomsByIndex = roomSetup()
  File "/Users/cwinter/Documents/Adventure/adventure2.py", line 86, in roomSetup
    infile = open(roomsfile, 'r')
FileNotFoundError: [Errno 2] No such file or directory: 'roomsfile.txt'
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb .
What do you do? get comb
You pick up the comb .
What do you do? inb
Huh?
What do you do? inv
In your inventory you have:
comb
bomb
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? n
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
What do you do? use elephant
Do what with the elephant ?
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? n
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
What do you do? get elephant
You can't pick up the elephant.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear footsteps.
What do you do? n
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
What do you do? get elephant
You can't pick up the elephant.
What do you do? s
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get comb
You pick up thecomb.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get comb
You pick up the comb.
What do you do? get bomb
You pick up the bomb.
What do you do? inv
In your inventory you have:
comb
bomb
What do you do? i
In your inventory you have:
comb
bomb
What do you do? look comb
It's an ivory comb.
What do you do? look bomb
a disarmed bomb.
What do you do? arm bomb
You can't use the bomb while you're holding it!
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? search room
Your search reveals nothing!
What do you do? w
You can't go in that direction!
What do you do? s
You can't go in that direction!
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
What do you do? look room
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb.
What do you do? inv
In your inventory you have:
bomb
What do you do? 
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.

>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 396, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 388, in main
    itemsByName, itemsByIndex = itemsSetup()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 61, in itemsSetup
    newItem = makeItems(line)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 52, in makeItems
    itemID, itemName, itemLocation, itemLocationOriginal, itemFriendlyLocation, itemLongDescription, itemShortDescription, itemLocationOriginalDesc, itemDroppedDescription, itemGettable, itemDoable, itemLimited, itemUses, itemRefillable, itemHidden, itemActions, itemActionRequirements, itemActionType, itemActionOutcomeDescSuccess, itemActionOutcomeDescFailure = infoStr.split("//")
ValueError: need more than 1 value to unpack
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
What do you do? e
You can't go in that direction!
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
What do you do? search roo
Huh?m
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
What do you do? look room
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 396, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 393, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 122, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 158, in verbAndNounCheck
    getDropItems(itemsByName, location, "get", noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 274, in getDropItems
    checkLocation = int(itemsByName[noun].itemLocation)
KeyError: 'ring'
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? get ring
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 396, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 393, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 122, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 158, in verbAndNounCheck
    getDropItems(itemsByName, location, "get", noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 274, in getDropItems
    checkLocation = int(itemsByName[noun].itemLocation)
KeyError: 'ring'
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? get ring
Huh?
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
What do you do? search room
Your search reveals nothing!
What do you do? search room
Your search reveals nothing!
What do you do? w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear faint laughter.

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
Rats scurry across the floor.

What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
Huh?
What do you do? get magic ring
Huh?
You hear footsteps.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
You hear footsteps.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
You hear footsteps.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 396, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 393, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 122, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 170, in verbAndNounCheck
    useItems(itemsByName, roomsByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 306, in useItems
    checkItemActionType = ast.literal_eval(itemsByName[noun].itemActionType)
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 47, in literal_eval
    node_or_string = parse(node_or_string, mode='eval')
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 35, in parse
    return compile(source, filename, mode, PyCF_ONLY_AST)
  File "<unknown>", line 1
    {'changeLocation':1,2,3}
                         ^
SyntaxError: invalid syntax
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 396, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 393, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 122, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 170, in verbAndNounCheck
    useItems(itemsByName, roomsByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 312, in useItems
    useItemsSuccess(itemsByName, location, verb, noun)
TypeError: useItemsSuccess() missing 1 required positional argument: 'noun'
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
Where do you want to go to?
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 396, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 393, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 122, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 170, in verbAndNounCheck
    useItems(itemsByName, roomsByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 312, in useItems
    useItemsSuccess(itemsByName, roomsByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 354, in useItemsSuccess
    print(n, " - ", roomsByIndex[n].shortDescription)
TypeError: list indices must be integers, not str
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?1
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 396, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 393, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 122, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 170, in verbAndNounCheck
    useItems(itemsByName, roomsByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 312, in useItems
    useItemsSuccess(itemsByName, roomsByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 356, in useItemsSuccess
    validChoice = changeLocation(location, locationSelection, locationChoices, roomsByIndex, itemsByIndex)
NameError: global name 'itemsByIndex' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 396, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 393, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 122, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 170, in verbAndNounCheck
    useItems(itemsByName, roomsByIndex, location, verb, noun)
TypeError: useItems() missing 1 required positional argument: 'noun'
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?1
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?2
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?3
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?4
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?5
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?1
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?1
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?1
What do you do? look room
The hidden room
There is a door to the east.
What do you do? 
>>> ================================ RESTART ================================
>>> 
w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? usering
Huh?
What do you do? use ring
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?1
Rats scurry across the floor.

What do you do? look room
The hidden room
There is a door to the east.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?1
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 398, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 395, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 122, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 170, in verbAndNounCheck
    useItems(itemsByName, itemsByIndex, roomsByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 312, in useItems
    useItemsSuccess(itemsByName, itemsByIndex, roomsByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 356, in useItemsSuccess
    validChoice = changeLocation(location, locationSelection, locationChoices, roomsByIndex, itemsByIndex)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 362, in changeLocation
    changeLocationTo = locationChoices(locationSelection)
TypeError: 'tuple' object is not callable
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?1
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 398, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 395, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 122, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 170, in verbAndNounCheck
    useItems(itemsByName, itemsByIndex, roomsByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 312, in useItems
    useItemsSuccess(itemsByName, itemsByIndex, roomsByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 356, in useItemsSuccess
    validChoice = changeLocation(location, locationSelection, locationChoices, roomsByIndex, itemsByIndex)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 362, in changeLocation
    changeLocationTo = locationChoices[locationSelection]
TypeError: tuple indices must be integers, not str
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use rin
Huh?
What do you do? use ring
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?1
2
2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
None
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
There is a flash of light!
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?2
3
3
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
None
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
There is a flash of light!
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?3
What do you do? use ring
There is a flash of light!
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?0
1
1
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
None
What do you do? n
You can't go in that direction!
What do you do? look room
The hidden room
There is a door to the east.
What do you do? e
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
What do you do? n
The kitchen.
There are doors to the south, and east.
What do you do? use ring
There is a flash of light!
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?0
1
1
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
None
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
There is a flash of light!
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?1
1
1
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
None
What do you do? use ring
There is a flash of light!
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?1
1
1
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
None
What do you do? use ring
There is a flash of light!
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?3
3
3
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
None
What do you do? 
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 402, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 394, in main
    itemsByName, itemsByIndex = itemsSetup()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 63, in itemsSetup
    newItem = makeItems(line)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 54, in makeItems
    itemID, itemName, itemLocation, itemLocationOriginal, itemFriendlyLocation, itemLongDescription, itemShortDescription, itemLocationOriginalDesc, itemDroppedDescription, itemGettable, itemDoable, itemLimited, itemUses, itemRefillable, itemHidden, itemActions, itemActionRequirements, itemActionType, itemActionUseSuccessDescription, itemActionUseFailDescription, itemActionOutcomeDescSuccess, itemActionOutcomeDescFailure = infoStr.split("//")
ValueError: need more than 1 value to unpack
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? use ring
There is a flash of light!
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?1
1
1
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
None
Rats scurry across the floor.

What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
There is a flash of light!
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?1
1
1
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
None
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
You hear faint laughter.

What do you do? get bomb
You pick up the bomb.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? use bomb
You can't use the bomb while you're holding it!
What do you do? drop bomb
You drop the bomb.
What do you do? use bomb
You can't use the bomb here!
What do you do? get bomb
You pick up the bomb.
What do you do? get comb
You pick up the comb.
What do you do? use comb
You comb your hair.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use rig
Huh?
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?3
3
3
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
None
What do you do? e
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? e
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
You hear faint laughter.

What do you do? get bomb
You pick up the bomb.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?3
3
3
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
None
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?3
3
3
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
None
What do you do? e
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?3
3
3
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
None
What do you do? e
Stairs leading up.
At the top of the stairs is a locked door. You can go back down the stairs to the west.
What do you do? use bomb
You arm the bomb, and then step back around the corner, shielded from the blast.
The bomb explodes with a thundering bang, and a shockwave washes over you.
The locked door has been blown off its hinges!
What do you do? inv
In your inventory you have:
ring
What do you do? 
>>> ================================ RESTART ================================
>>> 
w
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb.
What do you do? use bomb
You can't use the bomb while you're holding it!
What do you do? drop bomb
You drop the bomb.
You hear footsteps.
What do you do? use bomb
You can't use the bomb here!
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb.
What do you do? use bomb
You can't use the bomb while you're holding it!
What do you do? drop bomb
You drop the bomb.
What do you do? use bomb
You can't use the bomb here!
What do you do? get bomb
You pick up the bomb.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? look room
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?3
3
3
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
None
What do you do? e
Stairs leading up.
At the top of the stairs is a locked door. You can go back down the stairs to the west.
What do you do? use bomb
You can't use the bomb while you're holding it!
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? drop bomb
You drop the bomb.
What do you do? use bomb
You arm the bomb, and then step back around the corner, shielded from the blast.
The bomb explodes with a thundering bang, and a shockwave washes over you.
The locked door has been blown off its hinges!
You hear faint laughter.

What do you do? look room
Stairs leading up.
You can go back down the stairs to the west. To the east, a door hangs from its hinges.
What do you do? e
The upstairs hallway
You can go east along the hallway, or west back down the stairs.
What do you do? e
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 471, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 468, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 159, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 193, in verbAndNounCheck
    location = moveCheck(roomsByIndex, itemsByIndex, verb, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 227, in moveCheck
    roomDescription(location, roomsByIndex, itemsByIndex)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 252, in roomDescription
    checkHiddenExit = int(roomsByIndex[location].hiddenExitable)
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? get comb
You pick up the comb.
What do you do? use comb
You comb your hair.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? e
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
Rats scurry across the floor.

What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? e
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
What do you do? read note
The note says, "I'm not afraid to die. Are you?"
What do you do? get note
You pick up the note.
What do you do? inb
Huh?
What do you do? inv
In your inventory you have:
note
comb
bomb
ring
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?3
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
None
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?3
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
None
What do you do? get elephat
Huh?
What do you do? get elephant
You can't pick up the elephant.
What do you do? use elephant
Do what with the elephant?
What do you do? e
Stairs leading up.
At the top of the stairs is a locked door. You can go back down the stairs to the west.
What do you do? use bomb
You can't use the bomb while you're holding it!
Rats scurry across the floor.

What do you do? drop bomb
You drop the bomb.
What do you do? use bomb
You arm the bomb, and then step back around the corner, shielded from the blast.
The bomb explodes with a thundering bang, and a shockwave washes over you.
The locked door has been blown off its hinges!
What do you do? e
The upstairs hallway
You can go east along the hallway, or west back down the stairs.
What do you do? w
You can't go in that direction!
What do you do? n
You can't go in that direction!
What do you do? s
You can't go in that direction!
What do you do? e
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 471, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 468, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 159, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 193, in verbAndNounCheck
    location = moveCheck(roomsByIndex, itemsByIndex, verb, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 227, in moveCheck
    roomDescription(location, roomsByIndex, itemsByIndex)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 250, in roomDescription
    checkHiddenExit = int(roomsByIndex[location].hiddenExitable)
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get bomb
You pick up the bomb.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?3
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
None
What do you do? e
Stairs leading up.
At the top of the stairs is a locked door. You can go back down the stairs to the west.
What do you do? drop bomb
You drop the bomb.
What do you do? use bomb
You arm the bomb, and then step back around the corner, shielded from the blast.
The bomb explodes with a thundering bang, and a shockwave washes over you.
The locked door has been blown off its hinges!
What do you do? e
The upstairs hallway
You can go east along the hallway, or west back down the stairs.
What do you do? w
Stairs leading up.
You can go back down the stairs to the west. To the east, a door hangs from its hinges.
What do you do? w
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
What do you do? n
The kitchen.
There are doors to the south, and east.
What do you do? e
The Dining room.
There are doors to the south, and west.
What do you do? w
The kitchen.
There are doors to the south, and east.
What do you do? s
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
What do you do? s
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? look room
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? search room
Your search reveals nothing!
What do you do? 
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 523, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 516, in main
    NPCsAndMonstersByName, NPCsAndMonstersByIndex = NPCsAndMonstersSetup()
NameError: global name 'NPCsAndMonstersSetup' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 523, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 516, in main
    NPCsAndMonstersByName, NPCsAndMonstersByIndex = NPCsAndMonstersSetup()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 166, in NPCsAndMonstersSetup
    infile = open(npcsandmonstersfile, 'r')
NameError: global name 'npcsandmonstersfile' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 523, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 516, in main
    NPCsAndMonstersByName, NPCsAndMonstersByIndex = NPCsAndMonstersSetup()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 170, in NPCsAndMonstersSetup
    newNPC = makeNPCsAndMonsters(line)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 161, in makeNPCsAndMonsters
    npcmID, npcmName, npcmLocation, npcmStartingLocation, npcmFriendlyLocation, npcmLongDescription, npcmShortDescription, npcmStartingLocationDesc, npcmFightable, npcmAggression, npcmFlee, npcmAttack, npcmAttackSuccessDesc, npcmAttackFailDesc, npcmDamage, npcmArmor, npcmArmorSuccessDesc, npcmArmorFailDesc, npcmStartingHealth, npcmHealth, npcmOutlook, npcmConversation = infoStr.split("//")
ValueError: need more than 21 values to unpack
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? e
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? q
Huh?
>>> 
>>> 
>>> 
>>> lkj
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    lkj
NameError: name 'lkj' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 548, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 544, in main
    roomDescription(location, roomsByIndex, itemsByIndex)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 305, in roomDescription
    NPCsAndMonstersCheck(location, NPCsAndMonstersByIndex, "print")
NameError: global name 'NPCsAndMonstersCheck' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 548, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 544, in main
    roomDescription(location, roomsByIndex, itemsByIndex)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 305, in roomDescription
    NPCsAndMonstersCheck(location, NPCsAndMonstersByIndex, "print")
NameError: global name 'NPCsAndMonstersByIndex' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 548, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 541, in main
    NPCsMonstersByName, NPCsMonstersByIndex = NPCsMonstersSetup()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 166, in NPCsMonstersSetup
    infile = open(npcsmonstersfile, 'r')
FileNotFoundError: [Errno 2] No such file or directory: 'npcsmonstersfile.txt'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 548, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 541, in main
    NPCsMonstersByName, NPCsMonstersByIndex = NPCsMonstersSetup()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 170, in NPCsMonstersSetup
    newNPCM = makeNPCsMonsters(line)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 162, in makeNPCsMonsters
    return NPCsAndMonsters(npcmID, npcmName, npcmLocation, npcmStartingLocation, npcmFriendlyLocation, npcmLongDescription, npcmShortDescription, npcmStartingLocationDesc, npcmFightable, npcmAggression, npcmFlee, npcmAttack, npcmAttackSuccessDesc, npcmAttackFailDesc, npcmDamage, npcmArmor, npcmArmorSuccessDesc, npcmArmorFailDesc, npcmStartingHealth, npcmHealth, npcmOutlook, npcmConversation)
NameError: global name 'NPCsAndMonsters' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 548, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 541, in main
    NPCsMonstersByName, NPCsMonstersByIndex = NPCsMonstersSetup()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 171, in NPCsMonstersSetup
    NPCsMonstersByName[newNPCM.npcmName] = newNPC
NameError: global name 'newNPC' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 548, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 544, in main
    roomDescription(location, roomsByIndex, itemsByIndex)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 305, in roomDescription
    NPCsMonstersCheck(location, NPCsAndMonstersByIndex, "print")
NameError: global name 'NPCsAndMonstersByIndex' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 548, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 544, in main
    roomDescription(location, roomsByIndex, itemsByIndex)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 305, in roomDescription
    NPCsMonstersCheck(location, NPCsMonstersByIndex, "print")
NameError: global name 'NPCsMonstersByIndex' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 548, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 544, in main
    roomDescription(location, roomsByIndex, itemsByIndex)
TypeError: roomDescription() missing 2 required positional arguments: 'NPCsMonstersByName' and 'NPCsMonstersByIndex'
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 548, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 544, in main
    roomDescription(location, roomsByIndex, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 305, in roomDescription
    NPCsMonstersCheck(location, NPCsMonstersByIndex, "print")
TypeError: NPCsMonstersCheck() missing 1 required positional argument: 'action'
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 548, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 544, in main
    roomDescription(location, roomsByIndex, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 305, in roomDescription
    NPCsMonstersCheck(ocation, NPCsMonstersByName, NPCsMonstersByIndex, "print")
NameError: global name 'ocation' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 548, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 544, in main
    roomDescription(location, roomsByIndex, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 305, in roomDescription
    NPCsMonstersCheck(location, NPCsMonstersByName, NPCsMonstersByIndex, "print")
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 313, in NPCsMonstersCheck
    numMonsters = len(NPCsAndMonstersByIndex)
NameError: global name 'NPCsAndMonstersByIndex' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 548, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 544, in main
    roomDescription(location, roomsByIndex, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 305, in roomDescription
    NPCsMonstersCheck(location, NPCsMonstersByName, NPCsMonstersByIndex, "print")
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 318, in NPCsMonstersCheck
    checkStartingLocation = int(NPCsAndMonstersByIndex[n].npcmStartingLocation)
NameError: global name 'NPCsAndMonstersByIndex' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 548, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 544, in main
    roomDescription(location, roomsByIndex, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 305, in roomDescription
    NPCsMonstersCheck(location, NPCsMonstersByName, NPCsMonstersByIndex, "print")
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 323, in NPCsMonstersCheck
    inRoomMonsters.append(NPCsMonstersByIndex[n].itemName)
AttributeError: 'NPCsMonsters' object has no attribute 'itemName'
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? look ratNPCsMonstersByIndex
Huh?
What do you do? look rat
Huh?
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 548, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 545, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 210, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsAndMonstersByName, NPCsAndMonstersByIndex, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 244, in verbAndNounCheck
    location = moveCheck(roomsByIndex, itemsByIndex, verb, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 278, in moveCheck
    roomDescription(location, roomsByIndex, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex)
NameError: global name 'NPCsMonstersByName' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? look rat
Huh?
What do you do? w
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 548, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 545, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 210, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsAndMonstersByName, NPCsAndMonstersByIndex, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 244, in verbAndNounCheck
    location = moveCheck(roomsByIndex, itemsByIndex, verb, location)
TypeError: moveCheck() missing 2 required positional arguments: 'action' and 'location'
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? e
You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? look rat
Huh?
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get comb
You pick up the comb.
What do you do? use comb
You comb your hair.
What do you do? drop comb
You drop the comb.
What do you do? get comb
You pick up the comb.
What do you do? inv
In your inventory you have:
comb
Rats scurry across the floor.

What do you do? search room
You're search has found a secret door in the bookcase, to the west.
Rats scurry across the floor.

What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?3
What do you do? look room
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 548, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 545, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 210, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsAndMonstersByName, NPCsAndMonstersByIndex, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 254, in verbAndNounCheck
    roomDescription(location, roomsByIndex, itemsByIndex)
TypeError: roomDescription() missing 2 required positional arguments: 'NPCsMonstersByName' and 'NPCsMonstersByIndex'
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?3
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 548, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 545, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 210, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsAndMonstersByName, NPCsAndMonstersByIndex, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 258, in verbAndNounCheck
    location = useItems(itemsByName, itemsByIndex, roomsByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 447, in useItems
    location = useItemsSuccess(itemsByName, itemsByIndex, roomsByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 513, in useItemsSuccess
    validChoice, location = changeLocation(location, locationSelection, locationChoices, roomsByIndex, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex)
NameError: global name 'NPCsMonstersByName' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?3
Rats scurry across the floor.

What do you do? look room
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?1
Rats scurry across the floor.

What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
Rats scurry across the floor.

What do you do? search room
Your search reveals nothing!
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
You hear faint laughter.

What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?3
There is a flash of light!
What do you do? look room
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?3
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
None
There is a flash of light!
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
Rats scurry across the floor.

What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?3
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
None
There is a flash of light!
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?3
There is a flash of light!
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
None
What do you do? s
You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? n
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?3
There is a flash of light!
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
None
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?1
There is a flash of light!
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
None
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?2
There is a flash of light!
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
None
What do you do? e
You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?1
There is a flash of light!
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
None
Rats scurry across the floor.

What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?2
There is a flash of light!
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
None
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
You hear footsteps.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?1
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
None
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?1
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
None
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?2
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
None
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?3
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
None
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
You hear footsteps.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?2
There is a flash of light!
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
None
What do you do? w
The hidden room
There is a door to the east.
What do you do? e
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?2
There is a flash of light!
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
None
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?4
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 548, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 545, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 210, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsAndMonstersByName, NPCsAndMonstersByIndex, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 258, in verbAndNounCheck
    location = useItems(itemsByName, itemsByIndex, roomsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 446, in useItems
    location = useItemsSuccess(itemsByName, itemsByIndex, roomsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 520, in useItemsSuccess
    if (itemsByName[noun].itemActionOutcomeDescFail) == "none":
AttributeError: 'Items' object has no attribute 'itemActionOutcomeDescFail'
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
You hear faint laughter.

What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? use ring
You can't use the ring if you don't have it!
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?5
There is a small pop and then nothing happens!
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection?2
There is a flash of light!
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
None
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection? 2
There is a flash of light!
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
None
What do you do? use ring
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 548, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 545, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 210, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsAndMonstersByName, NPCsAndMonstersByIndex, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 258, in verbAndNounCheck
    location = useItems(itemsByName, itemsByIndex, roomsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 446, in useItems
    location = useItemsSuccess(itemsByName, itemsByIndex, roomsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 463, in useItemsSuccess
    itemUsesCheck = eval(itemsByName[noun].itemUses)
TypeError: eval() arg 1 must be a string, bytes or code object
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? use ring
You can't use the ring if you don't have it!
What do you do? get ring
You pick up the ring.
What do you do? use ring
2
<class 'int'>
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection? 2
There is a flash of light!
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
None
Rats scurry across the floor.

What do you do? use ring
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 550, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 547, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 210, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsAndMonstersByName, NPCsAndMonstersByIndex, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 258, in verbAndNounCheck
    location = useItems(itemsByName, itemsByIndex, roomsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 446, in useItems
    location = useItemsSuccess(itemsByName, itemsByIndex, roomsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 463, in useItemsSuccess
    itemUsesCheck = eval(itemsByName[noun].itemUses)
TypeError: eval() arg 1 must be a string, bytes or code object
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
2
<class 'str'>
2
<class 'int'>
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection? 2
There is a flash of light!
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
None
Rats scurry across the floor.

What do you do? use ring
1
<class 'int'>
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 552, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 549, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 210, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsAndMonstersByName, NPCsAndMonstersByIndex, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 258, in verbAndNounCheck
    location = useItems(itemsByName, itemsByIndex, roomsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 446, in useItems
    location = useItemsSuccess(itemsByName, itemsByIndex, roomsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 465, in useItemsSuccess
    itemUsesCheck = eval(itemsByName[noun].itemUses)
TypeError: eval() arg 1 must be a string, bytes or code object
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
You hear footsteps.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
2
<class 'str'>
2
<class 'int'>
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection? 2
There is a flash of light!
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
None
What do you do? use ring
1
<class 'str'>
1
<class 'int'>
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection? 2
There is a flash of light!
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
None
What do you do? use ring
Huh?
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection? 3
There is a flash of light!
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
None
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection? f
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 548, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 545, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 210, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsAndMonstersByName, NPCsAndMonstersByIndex, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 258, in verbAndNounCheck
    location = useItems(itemsByName, itemsByIndex, roomsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 446, in useItems
    location = useItemsSuccess(itemsByName, itemsByIndex, roomsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 510, in useItemsSuccess
    locationSelection = eval(input("What is your selection? "))
  File "<string>", line 1, in <module>
NameError: name 'f' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection? f
Uh, what?
What is your selection? 2
There is a flash of light!
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
None
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection? 6
There is a small pop and then nothing happens!
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection? 2
There is a flash of light!
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
None
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection? 3
There is a flash of light!
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
None
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection? 1
There is a flash of light!
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
None
What do you do? look room
You are in the parlor room. Peeling wallpaper clings feebly to the walls. A dank odor hangs in the room. There is a couch in the center of the room.
You see a handwritten note, tacked to the wall. The note is written in beautiful cursive handwriting.
There are doors to the west and north.
What do you do? 
>>> ================================ RESTART ================================
>>> 

gg You are in the entryway to the haunted house.
jj You see a huge rat.
hh You see a hallway to the north, and doors to the east and west.
What do you do? w
gg You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
kk Sitting on an end-table is a beautiful ivory comb.
kk There is a bomb among the wreckage. It is disarmed.
hh There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
ee You hear footsteps.
What do you do? w
gg The hidden room
kk A magic ring stands on a pedestal.
hh There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
aa 1  -  You are in the parlor room.
aa 2  -  You are in the sitting room.
aa 3  -  You are in the hallway.
What is your selection? 2
bb There is a flash of light!
gg You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
kk Sitting on an end-table is a beautiful ivory comb.
kk There is a bomb among the wreckage. It is disarmed.
hh There are doors to the east and north.
ii There is a secret door in the bookcase, to the west.
cc None
What do you do? 
>>> ================================ RESTART ================================
>>> 

gg You are in the entryway to the haunted house.
jj You see a huge rat.
hh You see a hallway to the north, and doors to the east and west.
What do you do? w
gg You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
kk Sitting on an end-table is a beautiful ivory comb.
kk There is a bomb among the wreckage. It is disarmed.
hh There are doors to the east and north.
ee From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? search room
You're search has found a secret door in the bookcase, to the west.
ee Rats scurry across the floor.

What do you do? w
gg The hidden room
kk A magic ring stands on a pedestal.
hh There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection? 3
There is a flash of light!
gg You enter a long, dark hallway.
kk An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
hh There are stairs to the east, and doorways to the north and south.
cc None
What do you do? 
>>> ================================ RESTART ================================
>>> 

gg You are in the entryway to the haunted house.
jj You see a huge rat.
hh You see a hallway to the north, and doors to the east and west.
ee Rats scurry across the floor.

What do you do? w
gg You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
kk Sitting on an end-table is a beautiful ivory comb.
kk There is a bomb among the wreckage. It is disarmed.
hh There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
gg The hidden room
kk A magic ring stands on a pedestal.
hh There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection? 3
There is a flash of light!
gg You enter a long, dark hallway.
kk An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
hh There are stairs to the east, and doorways to the north and south.
None
What do you do? look room
gg You enter a long, dark hallway.
kk An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
hh There are stairs to the east, and doorways to the north and south.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
jj You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
kk Sitting on an end-table is a beautiful ivory comb.
kk There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
kk A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection? 2
There is a flash of light!
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
kk Sitting on an end-table is a beautiful ivory comb.
kk There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
None
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
jj You see a huge rat.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
kk Sitting on an end-table is a beautiful ivory comb.
kk There is a bomb among the wreckage. It is disarmed.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
kk A magic ring stands on a pedestal.
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection? 3
There is a flash of light!
You enter a long, dark hallway.
kk An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
None
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
jj You see a huge rat.
You see a hallway to the north, and doors to the east and west.
NotNone!
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
kk Sitting on an end-table is a beautiful ivory comb.
kk There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
NotNone!
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
kk A magic ring stands on a pedestal.
There is a door to the east.
NotNone!
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection? 3
There is a flash of light!
You enter a long, dark hallway.
kk An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
NotNone!
None
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
jj You see a huge rat.
You see a hallway to the north, and doors to the east and west.
ee From somewhere upstairs, you hear a piercing scream. Your heart pounds.

What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
kk Sitting on an end-table is a beautiful ivory comb.
kk There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
ee You hear faint laughter.

What do you do? search room
Your search reveals nothing!
ee You hear footsteps.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
kk A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection? 3
There is a flash of light!
You enter a long, dark hallway.
kk An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection? 2
There is a flash of light!
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
kk Sitting on an end-table is a beautiful ivory comb.
kk There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
What do you do? 
>>> ================================ RESTART ================================
>>> 

>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
You hear footsteps.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection? f
Uh, what?
What is your selection? 2
There is a flash of light!
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
What do you do? 
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 564, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 557, in main
    NPCsMonstersByName, NPCsMonstersByIndex = NPCsMonstersSetup()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 171, in NPCsMonstersSetup
    newNPCM = makeNPCsMonsters(line)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 162, in makeNPCsMonsters
    npcmID, npcmName, npcmLocation, npcmStartingLocation, npcmFriendlyLocation, npcmLongDescription, npcmShortDescription, npcmStartingLocationDesc, npcmFightable, npcmAggression, npcmFlee, npcmAttack, npcmAttackSuccessDesc, npcmAttackFailDesc, npcmDamage, npcmArmor, npcmArmorSuccessDesc, npcmArmorFailDesc, npcmStartingHealth, npcmHealth, npcmOutlook, npcmConversation = infoStr.split("//")
ValueError: too many values to unpack (expected 22)
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 564, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 557, in main
    NPCsMonstersByName, NPCsMonstersByIndex = NPCsMonstersSetup()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 171, in NPCsMonstersSetup
    newNPCM = makeNPCsMonsters(line)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 163, in makeNPCsMonsters
    return NPCsMonsters(npcmID, npcmName, npcmLocation, npcmStartingLocation, npcmFriendlyLocation, npcmLongDescription, npcmShortDescription, npcmStartingLocationDesc, npcmFightable, npcmAggression, npcmFlee, npcmAttack, npcmAttackSuccessDesc, npcmAttackFailDesc, npcmDamage, npcmArmor, npcmArmorSuccessDesc, npcmArmorFailDesc, npcmStartingHealth, npcmHealth, npcmOutlook, npcmTalkable, npcmConversation)
NameError: global name 'npcmTalkable' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? talk rat
Huh?
What do you do? e
You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? talk rat
Huh?
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? go west
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? e
You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? get comb
You pick up the comb.
Rats scurry across the floor.

What do you do? inv
In your inventory you have:
comb
What do you do? get bomb
You pick up the bomb.
What do you do? search room
You're search has found a secret door in the bookcase, to the west.
What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? e
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
There are doors to the east and north.
There is a secret door in the bookcase, to the west.
You hear faint laughter.

What do you do? w
The hidden room
A magic ring stands on a pedestal.
There is a door to the east.
What do you do? get ring
You pick up the ring.
What do you do? use ring
The world seems to fade away.
Where do you want to go to?
1  -  You are in the parlor room.
2  -  You are in the sitting room.
3  -  You are in the hallway.
What is your selection? 3
There is a flash of light!
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
What do you do? e
Stairs leading up.
At the top of the stairs is a locked door. You can go back down the stairs to the west.
What do you do? use bomb
You can't use the bomb while you're holding it!
What do you do? drop bomb
You drop the bomb.
What do you do? use bomb
You arm the bomb, and then step back around the corner, shielded from the blast.
The bomb explodes with a thundering bang, and a shockwave washes over you.
The locked door has been blown off its hinges!
What do you do? look room
Stairs leading up.
You can go back down the stairs to the west. To the east, a door hangs from its hinges.
What do you do? e
The upstairs hallway
You can go east along the hallway, or west back down the stairs.
What do you do? w
Stairs leading up.
You can go back down the stairs to the west. To the east, a door hangs from its hinges.
You hear footsteps.
What do you do? n
You can't go in that direction!
What do you do? s
You can't go in that direction!
Rats scurry across the floor.

What do you do? look room
Stairs leading up.
You can go back down the stairs to the west. To the east, a door hangs from its hinges.
What do you do? w
You enter a long, dark hallway.
An elephant stands majestically in a corner, slowly blinking its eyes and happily swishing its tail.
There are stairs to the east, and doorways to the north and south.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? w
You are in the sitting room. The furniture is smashed - broken into large and small pieces. There is a fireplace in the west wall. The embers of a fire smoke.
Sitting on an end-table is a beautiful ivory comb.
There is a bomb among the wreckage. It is disarmed.
There are doors to the east and north.
What do you do? talk rat
Uh, why're you talking to yourself?
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
You hear footsteps.
What do you do? talk rat
What do you say to the rat?name
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 585, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 582, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 211, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsAndMonstersByName, NPCsAndMonstersByIndex, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 263, in verbAndNounCheck
    conversation(roomsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 446, in conversation
    questionSplit = words.split()
NameError: global name 'words' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? talk rat
What do you say to the rat ?name
squeek
What do you say to the rat ?
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? talk rat
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 585, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 582, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 211, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsAndMonstersByName, NPCsAndMonstersByIndex, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 263, in verbAndNounCheck
    conversation(roomsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 443, in conversation
    npcmConversation = ast.literal_eval(NPCsMonstersByName[noun].npcmConversation)
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 47, in literal_eval
    node_or_string = parse(node_or_string, mode='eval')
  File "/Library/Frameworks/Python.framework/Versions/3.3/lib/python3.3/ast.py", line 35, in parse
    return compile(source, filename, mode, PyCF_ONLY_AST)
  File "<unknown>", line 1
    {"name", "job":"squeek"}
                  ^
SyntaxError: invalid syntax
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? talk rat
What do you say to the rat? name
squeek
What do you say to the rat? job
Eating cheese!
What do you say to the rat? what's your job?
unknown
unknown
unknown
What do you say to the rat? job
Eating cheese!
What do you say to the rat? what job
unknown
Eating cheese!
What do you say to the rat? whats your job
unknown
unknown
Eating cheese!
What do you say to the rat? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? talk rat
What do you say to the rat? job
Eating cheese!
What do you say to the rat? name
squeek
What do you say to the rat? kjhkj
That's an odd thing to say!
What do you say to the rat? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? talk rat
What do you say to the rat? q
That's an odd thing to say!
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? talk rat
What do you say to the rat? q
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? talk rat
What do you say to the rat? q
The rat shrugs, and turns away.
What do you do? talk rat
What do you say to the rat? name
The rat shrugs, and turns away.
What do you do? talk rat
What do you say to the rat? job
The rat shrugs, and turns away.
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
You hear footsteps.
What do you do? talk rat
What do you say to the rat? q
The rat shrugs, and turns away.
What do you do? talk rat
What do you say to the rat? job
Eating cheese!
What do you say to the rat? name
squeek
What do you say to the rat? ksjdf
That's an odd thing to say!
What do you say to the rat? q
The rat shrugs, and turns away.
What do you do? what's your job?
Huh?
What do you do? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? talk rat
What do you say to the rat? what's your job?
That's an odd thing to say!
That's an odd thing to say!
That's an odd thing to say!
What do you say to the rat? 
>>> ================================ RESTART ================================
>>> 

You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? talk rat
What do you say to the rat? name
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 595, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 592, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 211, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsAndMonstersByName, NPCsAndMonstersByIndex, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 263, in verbAndNounCheck
    conversation(roomsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 448, in conversation
    match = false
NameError: global name 'false' is not defined
>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? talk rat
What do you say to the rat? name
squeek
What do you say to the rat? job
Eating cheese!
What do you say to the rat? whats ur job
Eating cheese!
What do you say to the rat? q
The rat shrugs, and turns away.
What do you do? talk rat
What do you say to the rat? askdfh
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 595, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 592, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 211, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsAndMonstersByName, NPCsAndMonstersByIndex, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 263, in verbAndNounCheck
    conversation(roomsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 450, in conversation
    for word in questionSplit:
KeyboardInterrupt





>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? talk rat
What do you say to the rat? jjj
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 595, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 592, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 211, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsAndMonstersByName, NPCsAndMonstersByIndex, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 263, in verbAndNounCheck
    conversation(roomsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 461, in conversation
    print("That's a weird thing to say!")
KeyboardInterrupt



>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? talk rat
What do you say to the rat? who

>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? talk rat
What do you say to the rat? asdf
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 596, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 593, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 211, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsAndMonstersByName, NPCsAndMonstersByIndex, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 263, in verbAndNounCheck
    conversation(roomsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 459, in conversation
    match = "true"
KeyboardInterrupt


>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? talk rat
What do you say to the rat? sfasfd
Traceback (most recent call last):
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 594, in <module>
    main()
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 591, in main
    gamePlay(roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, verb, randomNoises)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 211, in gamePlay
    location = verbAndNounCheck(verb, noun, roomsByName, roomsByIndex, itemsByName, itemsByIndex, NPCsAndMonstersByName, NPCsAndMonstersByIndex, location)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 263, in verbAndNounCheck
    conversation(roomsByIndex, NPCsMonstersByName, NPCsMonstersByIndex, location, verb, noun)
  File "/Users/cwinter/Documents/adventure/adventure2.py", line 456, in conversation
    if word in npcmConversation:
KeyboardInterrupt





>>> ================================ RESTART ================================
>>> 
You are in the entryway to the haunted house.
You see a huge rat.
You see a hallway to the north, and doors to the east and west.
What do you do? talk rat
What do you say to the rat? what job
Eating cheese!
What do you say to the rat? q
The rat shrugs, and turns away.
What do you do? 
