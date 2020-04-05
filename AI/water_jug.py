class Node:
    def __init__(self,left,right,parent):
        self.left = left
        self.right = right
        self.parent = parent

    def get_value_str(self):
        return str([self.left,self.right])

    def get_value(self):
        return [int(self.left), int(self.right)]

class Graph:
    def __init__(self, root, initial, desired):
        self.root = root
        self.graph = {self.root: []}
        self.initial = initial
        self.desired = desired
        self.res = ''
        self.res_str = []
    
    def create_graph_bfs(self):
        nodes = [Node(self.initial[0], 0, self.root), Node(0, self.initial[1], self.root)]
        self.graph[self.root] = nodes
        self.graph[nodes[0]] = []
        self.graph[nodes[1]] = []
        bfs(self)
        return

    def create_graph_dfs(self):
        nodes = [Node(self.initial[0],0, self.root)]
        self.graph[self.root] = nodes
        self.graph[nodes[0]] = []

        if not dfs(nodes[0], self):
            nodes = [Node(0, self.initial[1], self.root)]
            self.graph[self.root] = nodes
            self.graph[nodes[1]] = []

            dfs(nodes[1], self)
        return

def create_res(node, g):
    g.res_str.append('(' + str(node.left) + ',' + str(node.right) + ')')
    if node and node.parent != 0:
        create_res(node.parent, g)
    return

def get_children(initial, nodes):
    children = []
    node = [nodes.left, nodes.right]
    children.append([0, node[1]])
    children.append([node[0],0])
    children.append([initial[0], node[1]])
    children.append([node[0], initial[1]])

    total = node[0] + node[1]
    left = max(total - initial[0], 0)
    children.append([total-left, left])

    left = max(total - initial[1], 0)
    children.append([left, total - left])
    return children

def bfs(g):
    temp_dict_keys = list(g.graph.keys()).copy()
    for parent in temp_dict_keys:
        if not g.graph[parent]:
            children = get_children(g.initial,parent)
            for i in children:
                if not exists(g.graph, i[0], i[1]):
                    n = Node(i[0], i[1], parent)
                    g.graph[parent].append(n)
                    g.graph[n] = []
                    goal = found_goal(g, i)
                    if goal:
                        g.res = n
                        return True

def dfs(node, g):
    for i in range(6):
        if i == 0:
            child = [0, node.right]
        elif i == 1:
            child = [node.left, 0]
        elif i == 2:
            child = [g.initial[0], node.right]
        elif i == 3:
            child = [node.left, g.initial[1]]
        elif i == 4:
            total = node.left + node.right
            left = max(total - g.initial[0], 0)
            child = [total - left, left]
        else:
            total = node.left + node.right
            left = max(total - g.initial[1], 0)
            child = [left, total - left]
        n = check_dfs(g, node, child)
        if found_goal(g, child):
            g.res = n
            return True
        if n:
            if dfs(n, g):
                return True
    return

def check_dfs(g, node, child):
    if not exists(g.graph, child[0], child[1]):
        n = Node(child[0], child[1], node)
        g.graph[node].append(n)
        g.graph[n] = []
        return n
    return None

def found_goal(g, node):
    return g.desired == node

def exists(g, left, right):
    for i in g.keys():
        if i.left == left and i.right == right:
            return True
    return False

def main():
    initial_a = int(input("Enter the initial capacity of Jug A (must be >0): "))
    initial_b = int(input("Enter the initial capacity of Jug B (must be >0): "))
    desired_a = int(input("Enter the desired capacity of water in Jug A (must be >1):"))
    desired_b = int(input("Enter the desired capacity of water in Jug B (must be >1):"))
    initial = [initial_a, initial_b]
    desired = [desired_a, desired_b]
    n = Node(0,0,0)
    while True:
        choice = int(input("Enter your choice:\n 1 for BFS\n 2 for DFS\n Other to exit\n"))
        if choice==1:
            print('Performing BFS operation................')
            g_bfs = Graph(n, initial, desired)
            g_bfs.create_graph_bfs()
            if g_bfs.res:
                create_res(g_bfs.res, g_bfs)
                print('->'.join(g_bfs.res_str[::-1]))
            else:
                print('Not Found')
        elif choice==2:
            print("Performing DFS operation.................")
            g_dfs = Graph(n, initial, desired)
            g_dfs.create_graph_dfs()
            if g_dfs.res:
                create_res(g_dfs.res, g_dfs)
                print('->'.join(g_dfs.res_str[::-1]))
            else:
                print('Not Found')
        else: 
            exit()
if __name__ == "__main__":
        main()
