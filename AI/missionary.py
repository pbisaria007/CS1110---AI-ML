author:@Pravesh Bisaria

class mission:

    def find_solution(self,state):                                                                               # find all possible states
        if state[2]==0:
            if state[0]>=2:                                                                                      # move two cannibals to right side
                j = (state[0] - 2, state[1], 1, state[3] + 2, state[4])
                if not ((j[0] > j[1] and j[1] >= 1) or (j[3] > j[4] and j[4] >= 1)):
                    if not visited_nodes.__contains__((state[0]-2,state[1],1,state[3]+2,state[4])):
                        j=(state[0]-2,state[1],1,state[3]+2,state[4])
                        visited_nodes.append((state[0]-2,state[1],1,state[3]+2,state[4]))
                        graph[state].append([state[0]-2,state[1],1,state[3]+2,state[4]])
                        graph[j]=[]
                        parents[j]=state
                        self.check_goal(j)


            if state[1]>=2:
                j = (state[0], state[1] - 2, 1, state[3], state[4] + 2)                                     # move two missionaries to right side
                if not ((j[0] > j[1] and j[1] >= 1) or (j[3] > j[4] and j[4] >= 1)):
                    if not visited_nodes.__contains__((state[0],state[1]-2,1,state[3],state[4]+2)):
                        j=(state[0],state[1]-2,1,state[3],state[4]+2)
                        visited_nodes.append(j)
                        graph[state].append([state[0],state[1]-2,1,state[3],state[4]+2])
                        graph[j]=[]
                        parents[j] = state
                        self.check_goal(j)


            if state[0]>0 and state[1]>0:                                                                   # move 1 missionary and 1 cannibal to right side
                j = (state[0] - 1, state[1] - 1, 1, state[3] + 1, state[4] + 1)
                if not ((j[0] > j[1] and j[1] >= 1) or (j[3] > j[4] and j[4] >= 1)):
                    if not visited_nodes.__contains__((state[0]-1,state[1]-1,1,state[3]+1,state[4]+1)):
                        j=(state[0]-1,state[1]-1,1,state[3]+1,state[4]+1)
                        visited_nodes.append(j)
                        graph[state].append([state[0]-1,state[1]-1,1,state[3]+1,state[4]+1])
                        graph[j]=[]
                        parents[j] = state
                        self.check_goal(j)



        else:

            if state[3]>=2:                                                                                       # move two cannibals to left side
                j = (state[0] + 2, state[1], 0, state[3] - 2, state[4])
                if not ((j[0] > j[1] and j[1] >= 1) or (j[3] > j[4] and j[4] >= 1)):
                    if not visited_nodes.__contains__((state[0] + 2, state[1], 0,state[3]-2,state[4])):
                        j = (state[0] + 2, state[1], 0,state[3]-2,state[4])
                        visited_nodes.append((state[0] + 2, state[1], 0,state[3]-2,state[4]))
                        graph[state].append([state[0] + 2, state[1], 0,state[3]-2,state[4]])
                        graph[j] = []
                        parents[j] = state
                        self.check_goal(j)


            if state[4] >= 2:                                                                                     # move two missionaries to left side
                j = (state[0], state[1] + 2, 0, state[3], state[4] - 2)
                if not ((j[0] > j[1] and j[1] >= 1) or (j[3] > j[4] and j[4] >= 1)):
                    if not visited_nodes.__contains__((state[0], state[1] + 2, 0,state[3],state[4]-2)):
                        j = (state[0], state[1] + 2, 0,state[3],state[4]-2)
                        visited_nodes.append(j)
                        graph[state].append([state[0], state[1] + 2, 0,state[3],state[4]-2])
                        graph[j] = []
                        parents[j] = state
                        self.check_goal(j)

            if state[3] > 0 and state[4] > 0:                                                                   # move 1 missionary and 1 cannibal to left side
                j = (state[0] + 1, state[1] + 1, 0,state[3]-1,state[4]-1)
                if not ((j[0] > j[1] and j[1] >= 1) or (j[3] > j[4] and j[4] >= 1)):
                    if not visited_nodes.__contains__((state[0] + 1, state[1] + 1, 0,state[3]-1,state[4]-1)):
                        j = (state[0] + 1, state[1] + 1, 0,state[3]-1,state[4]-1)
                        visited_nodes.append(j)
                        graph[state].append([state[0] + 1, state[1] + 1, 0,state[3]-1,state[4]-1])
                        graph[j] = []
                        parents[j] = state
                        self.check_goal(j)


            if state[3]>0:

                j=(state[0]+1,state[1],0,state[3]-1,state[4])                                                  # move 1 cannibal to left side

                if not ((j[0] > j[1] and j[1] >= 1) or (j[3] > j[4] and j[4] >= 1)):
                    if not visited_nodes.__contains__((state[0]+1,state[1],0,state[3]-1,state[4])):
                        j=(state[0]+1,state[1],0,state[3]-1,state[4])
                        visited_nodes.append(j)
                        graph[state].append([state[0]+1,state[1],0,state[3]-1,state[4]])
                        graph[j]=[]
                        parents[j] = state
                        self.check_goal(j)



            if state[4]>0:                                                                                     # move 1 missionary to left side

                j=(state[0],state[1]+1,0,state[3],state[4]-1)
                if not ((j[0] > j[1] and j[1] >= 1) or (j[3] > j[4] and j[4] >= 1)):
                    if not visited_nodes.__contains__((state[0],state[1]+1,0,state[3],state[4]-1)):
                        j=(state[0],state[1]+1,0,state[3],state[4]-1)
                        visited_nodes.append(j)
                        graph[state].append([state[0],state[1]+1,0,state[3],state[4]-1])
                        graph[j]=[]
                        parents[j] = state
                        self.check_goal(j)


        i = visited_nodes.index(state)
        k = visited_nodes[i + 1]
        self.find_solution(k)



    def check_goal(self,state):
        if state==goal_state:
            self.parent(state)

    def parent(self,j):

        while j!=start_state:
            path.append(j)
            self.parent(parents[j])
        path.append(start_state)

        for n in range(len(path)-1,0,-1):
            print(path[n])
        print(path[0])
        print("Graph: ", graph)
        exit(0)



m=mission()
graph={}
parents={}
path=[]
print("setting missionaries and cannibals...")
temp=int(input("Enter the number of missionaries or cannibels: "))
while not temp>0:
    temp=int(input("Enter the number of missionaries or cannibels, they should be equal in numbers!"))

start_state=(temp,temp,0,0,0)
visited_nodes=[]
bank=start_state[2]
print("setting goal state...")
print()
print("Solution:")
print("Cannibals Missionaries River_Bank Cannibals Missionaries")
goal_state=(0,0,1,temp,temp)
visited_nodes.append(start_state)
graph[start_state]=[]
m.find_solution(start_state)
