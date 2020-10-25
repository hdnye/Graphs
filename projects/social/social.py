import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        return if the friendship has been added successfully
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True
    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(0, num_users):
            self.add_user(f'User {i}')

        # Create friendships:            
            # generate all possible friendship combinations, then
            # num_users * avg_friendships // 2 to generate the average of 2 friends per user
            # this produces O(n²) yikes
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append( (user_id, friend_id) )
        # randomize above array
        random.shuffle(possible_friendships)
       
        # pick out num_users * avg_friend from possible_friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def populate_graph_linear(self, num_users, avg_friendships):
        # corrects time complexity & randomization from above alg
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # add users
        for i in range(0, num_users):
            self.add_user(f'user {i}')
        # add friendships
        # radomnly sample friendships until total friendships met
        total_friendships = num_users * avg_friendships
        generated_friendships = 0
        collisions = 0
        while generated_friendships < total_friendships:
            # choose 2 random uers. randint() takes 2 parameters
            user_id = random.randint(1 , self.last_id)
            friend_id = random.randint(1, self.last_id)
            # uses the above f() to prevent redundancies
            if self.add_friendship(user_id, friend_id):
                generated_friendships += 2
            else:
                collisions += 1
        print(f'COLLISIONS: {collisions}')


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        queue = [ [ user_id] ] # tells us where to go next from starting point
        visited = {}  # Note that this is a dictionary, not a set 
        while len(queue) > 0:
            # check if queue still have vertices to visit
            path = queue.pop(0)
            cur_vert = path[-1]
            # add to visited if not seen before
            if cur_vert not in visited:
                # adds cur_vert as key & path as value
                visited[cur_vert] = path
                # find neighbors & add to queue
                for neighbor in self.friendships[cur_vert]:
                    # copy path array
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    queue.append(path_copy)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    sg.populate_graph_linear(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
