from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# You may find the commands `player.current_room.id`, `player.current_room.get_exits()` and `player.travel(direction)` useful.
backtrack = []
reverse = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
visited = set()

while len(visited) < len(world.rooms):
    next_room = None
    # find exits
    for exit in player.current_room.get_exits():
        # set exit as next room if not in visited
        if player.current_room.get_room_in_direction(exit) not in visited:
            next_room = exit
            # if multiple exits in 1 room 
            break
        
    if next_room != None: 
        traversal_path.append(next_room)
        # backtrack if no exit but room != None
        backtrack.append(reverse[next_room])
        # move player forward & add to visited
        player.travel(next_room)
        visited.add(player.current_room)
    # if next_room is none
    else: 
        next_room = backtrack.pop()
        traversal_path.append(next_room)
        # move player
        player.travel(next_room)

'''
# find every exit
# be able to backtrack from dead ends 
# find shortest path 
reverse = [ player.current_room: {d for d in room_graph if "'?'" else None}]
first pass solution
def get_path(self, direction):
    cur_room, path, exits = player.current_room.id, player.travel(direction), player.current_room.get_exits()
    # queue = [[cur_room]]
    visited = set()

    while len(queue) > 0:
        for room in room_graph: 
            path = traversal_path.pop(0)
            print(f'Path: {path}')
            cur_room = path[-1]
            if cur_room not in visited:
                visited.add(cur_room)
            for exits in room_graph[room][1]:
                new_path = path.copy()
                new_path.append(exits)
                traversal_path.append(new_path)
                if exits is None:
                    return new_path
    return None
'''




# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
