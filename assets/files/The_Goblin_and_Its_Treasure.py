# ======================================================
# The Goblin and Its Treasure: A Text Adventure Game
#
# Author: Tristan Maloy
# SNHU CS499 Capstone
#
# Version History:
# v1.0 - Initial text adventure implementation
# - Basic room navigation
# - Inventory collection mechanics
# - Locked room progression
# - Goblin encounter and win/lose conditions
#
# v2.0 - Refactored and enhanced implementation
# - Rebuilt code structure for improved maintainability
# - Improved readability through cleaner organization
# - Refactored repeated logic to reduce redundancy
# - Improved modularity through reusable functions
# - Enhanced data structures for inventory handling
# - Added input validation and command normalization
# - Added dynamic room descriptions and flavor text
# - Added player choice consequences for equipment usage
# - Improved game scalability for future expansion
# ======================================================

DIRECTIONS = ["north", "south", "east", "west"]

def show_instructions():
    print('\033[1;4m' + "The Goblin and Its Treasure: A Text Adventure Game" + '\033[0m')
    print("Stories have spread across the land of a goblin lurking deep within an ancient dungeon.")
    print("The creature guards a treasure said to bring wealth, glory, and a life beyond hardship.")
    print("Many have entered seeking fortune. None have returned.")
    print("Armed with courage and determination, you step into the darkness to face the goblin and claim the treasure for yourself.\n")
    print("Find the keys needed to reach the goblin's lair.")
    print("Along the way, choose carefully what you carry. Some items may determine whether you survive.\n")
    print("Move commands: north, east, south, west")
    print("Add to Inventory: get 'item name'")

def show_status(current_room, inventory, visited_rooms):
    available_directions = [direction for direction in DIRECTIONS if direction in current_room]

    print("\n" + "*" * 120)
    print(f"You are in {current_room['name']}.")

    if current_room["name"] not in visited_rooms:
        if current_room["description"]:
            print(current_room["description"])
        visited_rooms.add(current_room["name"])

    print(f"Inventory: {sorted(inventory)}")

    if len(available_directions) == 1:
        exits = available_directions[0]
        print(f"There is a door to the {exits}.")
    elif len(available_directions) == 2:
        exits = " and ".join(available_directions)
        print(f"There are doors to the {exits}.")
    else:
        exits = ", ".join(available_directions[:-1]) + ", and " + available_directions[-1]
        print(f"There are doors to the {exits}.")

    item = current_room.get("item")

    if item and item not in inventory:
        print(f"You see a {item}.")
        print(f"Type \033[1;4mget {item}\033[0m to add it to your inventory.")
    elif item:
        print("Only dust and shadows remain.")
    else:
        print("You scan the room, but find nothing worth taking.")


def main():
    # Room definitions
    rooms = {
        'Room 1': {
            'name': 'Room 1',
            'locked': False,
            'east': 'Room 2',
            'item': 'Room 2 key',
            'description': 'The entrance chamber is cold and damp. Cracked stones line the walls and a rusty key glints near your feet.'
        },
        'Room 2': {
            'name': 'Room 2',
            'locked': True,
            'north': 'Room 3',
            'east': 'Room 5',
            'south': 'Room 6',
            'west': 'Room 1',
            'item': None,
            'description': 'This central chamber smells of dust and old smoke. Several dark doorways branch off into the dungeon.'
        },
        'Room 3': {
            'name': 'Room 3',
            'locked': False,
            'east': 'Room 4',
            'south': 'Room 2',
            'item': 'Sword',
            'description': 'Broken weapon racks cover the walls. Among the scraps of metal, one sword still looks sharp enough to use.'
        },
        'Room 4': {
            'name': 'Room 4',
            'locked': False,
            'west': 'Room 3',
            'item': 'Room 5 key',
            'description': 'A narrow storage room is packed with rotting crates. Something small and metallic rests atop one of the crates.'
        },
        'Room 5': {
            'name': 'Room 5',
            'locked': True,
            'north': 'Room 8',
            'west': 'Room 2',
            'item': 'Room 6 key',
            'description': 'The air grows warmer here. Scratch marks cover the floor, leading toward a heavy door to the north.'
        },
        'Room 6': {
            'name': 'Room 6',
            'locked': True,
            'north': 'Room 2',
            'east': 'Room 7',
            'item': 'Shield',
            'description': 'This room looks like an old guard post. A battered shield leans against the wall, dented but still usable.'
        },
        'Room 7': {
            'name': 'Room 7',
            'locked': False,
            'west': 'Room 6',
            'item': 'Room 8 key',
            'description': 'A quiet chamber sits at the edge of the dungeon. A single key hangs from a hook beside a burned-out torch.'
        },
        'Room 8': {
            'name': 'Room 8',
            'locked': True,
            'south': 'Room 5',
            'item': None,
            'description': None
        }
    }


    inventory = set()
    # Track visited rooms so descriptions only display the first time entered
    visited_rooms = set()
    current_room = rooms["Room 1"]

    show_instructions()

    # Main game loop
    while True:
        show_status(current_room, inventory, visited_rooms)

        command = input("\nWhat do you do? ").lower().strip()

        if command in DIRECTIONS:
            if command not in current_room:
                print("\n\033[1;4mYou cannot go that way.\033[0m")
                continue

            # Dynamically generate required room key to reduce hardcoded progression logic and improve scalability
            next_room_name = current_room[command]
            next_room = rooms[next_room_name]
            needed_key = f"{next_room_name} key"

            if next_room["locked"] and needed_key not in inventory:
                print("\n\033[1;4mThe room is locked.\033[0m")
            else:
                current_room = next_room

        elif command.startswith("get "):
            item_requested = command[4:].strip()
            room_item = current_room.get("item")

            if room_item and item_requested == room_item.lower():
                if room_item in inventory:
                    print("\nYou already picked up that item.")
                else:
                    inventory.add(room_item)
                    print(f"\nYou picked up the {room_item}.")
            else:
                print("\nThat item is not here.")

        else:
            print("\n\033[1;4mInvalid command\033[0m")

        # Final goblin encounter
        if current_room["name"] == "Room 8":

            has_sword = "Sword" in inventory
            has_shield = "Shield" in inventory

            print("\nThe goblin lair reeks of smoke and decay. Bones litter the stone floor beside piles of stolen treasure. You hear claws scraping against the stone floor.")
            print("\nSuddenly, the goblin rushes towards you.")

            if has_sword and has_shield:
                print("You raise the Shield just in time as the goblin lunges.")
                print("Steel crashes against iron.")
                print("The Sword feels heavy in your hands, but one opening is all you need.")
                print("With a swift strike, the goblin falls.")
                print("Silence fills the chamber.")
                print("The treasure is yours.")
                print("Congratulations! You win!")

            elif not has_sword and not has_shield:
                print("You reach instinctively for a weapon, but your hands are empty.")
                print("The goblin grins.")
                print("Without protection or a way to fight back, you never stood a chance. YOU LOSE!")

            elif not has_sword:
                print("You raise your Shield and block the goblin's first attack.")
                print("Each strike rattles your arms.")
                print("Without a weapon, you have no way to finish the fight.")
                print("Eventually, exhaustion wins. YOU LOSE!")

            elif not has_shield:
                print("You tighten your grip on the Sword and charge.")
                print("The goblin meets your attack head on.")
                print("Without protection, every strike forces you backward.")
                print("Eventually, one blow lands harder than the rest. YOU LOSE!")

            print("Thanks for playing!")
            input("Press ENTER to exit.")
            break


main()
