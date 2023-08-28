class Node():
    def __init__(self, state, movie, parent, action):
        self.state = state
        self.movie = movie
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []
        self.explored = []

    def is_explored(self, node):
        return node in self.explored
    
    def add(self, node):
        self.frontier.append(node)
    
    def add_explored(self, node):
        self.explored.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
