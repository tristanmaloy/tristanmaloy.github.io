# Tristan Maloy IT-140-J6285
def show_instructions():
    # print name, summary, and commands
    print('\033[1;4m' + "The Goblin and it's Treasure: A Text Adventure Game" + '\033[0m')
    print("You have heard tales of the Goblin in the dungeon.")
    print("The Goblin defends a treasure that will provide you wealth and fame.")
    print("You venture into the dungeon to face the Goblin and take the treasure for yourself.\n")
    print("Collect 4 keys, the sword, and the shield to beat the goblin and win the game.")
    print("Move commands: north, east, south, west")
    print("Add to Inventory: get 'item name'")

def show_status():
    print('\ninventory:', inventory, '\n----------'), #prints current inventory
    print('You are in {}.\n'.format(current_room['name'])) #prints current room
    if current_room['name'] == 'Room 1': #if loop for each room to display what directions have doors.
        print('There is a door to the east.')
    elif current_room['name'] == 'Room 2':
        print('There is a door to the north, east, south, and west.')
    elif current_room['name'] == 'Room 3':
        print('There is a door to the east, and the south.')
    elif current_room['name'] == 'Room 4':
        print('There is a door to the west.')
    elif current_room['name'] == 'Room 5':
        print('There is a door to the north, and the west.')
    elif current_room['name'] == 'Room 6':
        print('There is a door to the north, and to the east.')
    elif current_room['name'] == 'Room 7':
        print('There is a door to the west.')
    elif current_room['name'] == 'Room 8':
        print('I am not sure how you could possibly see this since you should win or lose the game when entering this room.')
    else:
        print('If you see this, the game is broken. Try again.')

# The dictionary links a room to other rooms.
rooms = {'Room 1': {'name': 'Room 1', 'locked': False, 'east': 'Room 2', 'item': 'Room 2 key'},
         'Room 2': {'name': 'Room 2', 'locked': True, 'north': 'Room 3', 'east': 'Room 5', 'south': 'Room 6',
                    'west': 'Room 1', 'item': 'no items'},
         'Room 3': {'name': 'Room 3', 'locked': False, 'east': 'Room 4', 'south': 'Room 2', 'item': 'sword'},
         'Room 4': {'name': 'Room 4', 'locked': False, 'west': 'Room 3', 'item': 'Room 5 key'},
         'Room 5': {'name': 'Room 5', 'locked': True, 'north': 'Room 8', 'west': 'Room 2', 'item': 'Room 6 key'},
         'Room 6': {'name': 'Room 6', 'locked': True, 'north': 'Room 2', 'east': 'Room 7', 'item': 'shield'},
         'Room 7': {'name': 'Room 7', 'locked': False, 'west': 'Room 6', 'item': 'Room 8 key'},
         'Room 8': {'name': 'Room 8', 'locked': True, 'south': 'Room 5', 'item': 'no items'}
         }

inventory = []
directions = ['north', 'south', 'east', 'west']  # establish our directions
current_room = rooms['Room 1']  # establish current room
show_instructions() #recall function initial

while True:
    show_status()

    if current_room['item'] in inventory: #if loop to print different messages if user picked up items already
        print('You have picked up all available items.') #print if already picked up

    else:
        if current_room['item'] == 'no items': #rooms with no items will print this
            print('There is nothing to pick up in this room.')

        else: #print to show what item is in the room as well as the command to add item to inventory
            print('In this room you see the {}.'.format(current_room['item']), 'Type \033[1;4m' + 'get {}' .format(current_room['item']) + '\033[0m to add to inventory.' )

    # user input
    command = input('Which direction do you go? north, south, east, west?\n')

    # if loop for direction, if true direction move to next room
    if command in directions:
        if command in current_room:
            new_room = rooms[current_room[command]] #establish new room to help determine which rooms are locked
            key_name = rooms[current_room[command]]['name'] + " key" #variable to attach each room to its own key.

            if new_room['locked'] and key_name in inventory: #if new room is locked and the room key is in inventory
                current_room = rooms[current_room[command]] #move to next room

            elif new_room['locked'] == False: #if room is not locked
                current_room = rooms[current_room[command]] #move to next room
            else: #if room is locked but the key is not in inventory
                print('\n\033[1;4m' + 'The room is locked.' + '\033[0m')

        else:
            #bad movement
            print('\n\033[1;4m' + 'You cannot go that way.' + '\033[0m\n')

    elif command == 'get {}' .format(current_room['item']): #establish input to add item to inventory
        inventory.append(current_room['item']) #adds to inventory list


    # invalid input
    else:
        print('\n\033[1;4m' + 'INVALID INPUT' + '\033[0m\n')  # bolds and underlines text

    if current_room['name'] == 'Room 8': #FINAL ROOM
        if len(inventory) == 6: #If inventory has all items, this is the winning route
            print("\nAs you enter the room, the goblin jumps at you. \nYou block with your shield and with a swift swipe of your sword, you take it's head off.")
            print('Congratulations! \nYou beat the goblin and have found the treasure at the end of the dungeon!')
            print('You head out of the dungeon with newfound wealth and glory while looking forward to a better life.')
            print('Thanks for playing!')
            input('press ENTER to exit')
        else: #must have 6 items in inventory in order to win. this is what prints if there isn't 6 items in inventory
            print('BONK! The goblin hits you over the head and prepares you as food for his children. YOU LOSE!')
            print('Thanks for playing!')
            input('Press ENTER to exit')
        break
