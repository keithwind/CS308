class Node:
    def __init__(self,data):
        self.data = data
        self.children = []

    def addnode(self,node):
        self.children.append(node)

class Stack:
    def __init__(self,top):
        self.top = top
    
    def Pop(self):
        print(self.top)
        top = top+1
    
    def push(self,data):
        self.top = data

class Tree:
    def __init__(self,root):
        self.root = root

    def bfs(self):
        explore = [self.root]
        while(explore != []):
            next = explore.pop(0)
            print(next.data)
            for child in next.children:
                explore.append(child)
    
    def dfs(self):

a = Node(1)
b = Node(2)
c = Node(12)
d = Node(4)
e = Node(10)
f = Node(12)
g = Node(13)
a.addnode(b)
a.addnode(c)
a.addnode(d)
b.addnode(e)
b.addnode(f)
c.addnode(g)

T1 = Tree(a)
T1.bfs()




