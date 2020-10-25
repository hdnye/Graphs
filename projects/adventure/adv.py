from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

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

# find every exit
# be able to backtrack from dead ends 
# find shortest path 
# DFT to find all paths
def find_all_paths(room_graph, row, col):
    room_graph.update(row, col) 
    
    # check base case if no exit
    if room_graph[row][col] != exit:
        return False
    if room_graph[row][col] not in visited_rooms:
        visited_rooms.add([row][col])
    if room_graph.get_exits[row][col] == True:
        path = room_graph.update(row, col)
        
# BFS to find shortest path



'''
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
