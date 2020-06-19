'''#Instructions to run the code:
#This algorithm is witten in python 2.7 version(spyder). run the file and enter the number of discs from (1 to 6 as 6 is the
#max number of discs handled in BFS*).'''


class Pegs(object):

    def __init__(self, disks=[], max_disks=0):
        if len(disks) > 0:
            self.disks = disks
        else:
            self.disks = [i for i in range(max_disks, 0, -1)]

    def __iter__(self):
        return iter(self.disks)

    def is_empty(self):
        return len(self.disks) == 0

    def get_top_disk(self):
        if self.is_empty():
            return 1000
        return self.disks[-1:].pop()

    def put_disk(self, ring):
        if not self.is_empty():
            if ring < self.disks[-1:].pop():
                self.disks.append(ring)
        else:
            self.disks.append(ring)

    def pop_disk(self):
        return self.disks.pop()

    def move_to(self, Pegs_dest):
        if not self.is_empty():
            if self.get_top_disk() < Pegs_dest.get_top_disk():
                Pegs_dest.put_disk(self.pop_disk())

    def get_state(self):
        return tuple(self.disks)


class State(object):
    def __init__(self, A, B, C, D, parent, end_goal=False):
        self.state = ([i for i in A],
                      [i for i in B],
                      [i for i in C],
                      [i for i in D])
        self.end_goal = end_goal
        self.value = None
        self.parent = parent

    def __eq__(self, other):
        if isinstance(other, State):
            try:
                for t_index in range(0, len(self.state)):
                    for r_index in range(0, len(self.state[t_index])):
                        if self.state[t_index][r_index] != other.state[t_index][r_index]:
                            return False
                for t_index in range(0, len(other.state)):
                    for r_index in range(0, len(other.state[t_index])):
                        if other.state[t_index][r_index] != self.state[t_index][r_index]:
                            return False
            except IndexError:
                return False
            return True

#Combined heuristics function. F = G(cost) + H(final state)
    def F(self, cost, final_state):
        self.value = self.G(cost) 
        return self.value

#Cost function. Equal cost for all legal moves
    def G(self, cost):
        if cost:
            return cost + 1
        else:
            return 1



class TowersOfHanoi(object):

    def __init__(self, initial_state, final_state):
        self.final_state = final_state
        self.initial_state = initial_state
        self.open_list = []
        self.closed_list = []

    def select_next_state(self, cost):
        minor_F = 1000000
        index = 0
        index_minor = 1000000
        for q in self.open_list:
            node_F = q.F(cost=q.value, final_state=self.final_state)
            if node_F < minor_F:
                minor_F = node_F
                index_minor = index
            index += 1

        print self.open_list[index_minor].state
        selected = self.open_list[index_minor]
        del self.open_list[index_minor]
        return selected

#####################################################################
# Generates next set of nodes or states
#####################################################################

    def generate_successive_states(self, q):
        P1 = Pegs(q.state[0])
        P2 = Pegs(q.state[1])
        P3 = Pegs(q.state[2])
        P4 = Pegs(q.state[3])
        successors = [] #initialise successive_states list

        #There are 6 possible moves
        #From Tower 1 to Tower 2

        PA1_1 = Pegs(disks=P1.disks[:])
        PA2_1 = Pegs(disks=P2.disks[:])
        PA3_1 = Pegs(disks=P3.disks[:])
        PA4_1 = Pegs(disks=P4.disks[:])
        PA1_1.move_to(PA2_1)
        successors.append(State(PA1_1, PA2_1, PA3_1, PA4_1, parent=q))

        #From tower1 to tower 3
        PA1_2 = Pegs(disks=P1.disks[:])
        PA2_2 = Pegs(disks=P2.disks[:])
        PA3_2 = Pegs(disks=P3.disks[:])
        PA4_2 = Pegs(disks=P4.disks[:])
        PA1_2.move_to(PA3_2)
        successors.append(State(PA1_2, PA2_2, PA3_2, PA4_2, parent=q))

        #From tower1 to tower4
        PA1_3 = Pegs(disks=P1.disks[:])
        PA2_3 = Pegs(disks=P2.disks[:])
        PA3_3 = Pegs(disks=P3.disks[:])
        PA4_3 = Pegs(disks=P4.disks[:])
        PA1_3.move_to(PA4_3)
        successors.append(State(PA1_3, PA2_3, PA3_3, PA4_3, parent=q))

        #from tower2 to tower1
        PB1_1 = Pegs(disks=P1.disks[:])
        PB2_1 = Pegs(disks=P2.disks[:])
        PB3_1 = Pegs(disks=P3.disks[:])
        PB4_1 = Pegs(disks=P4.disks[:])
        PB2_1.move_to(PB1_1)
        successors.append(State(PB1_1, PB2_1, PB3_1, PB4_1, parent=q))

        #from tower2 to tower3
        PB1_2 = Pegs(disks=P1.disks[:])
        PB2_2 = Pegs(disks=P2.disks[:])
        PB3_2 = Pegs(disks=P3.disks[:])
        PB4_2 = Pegs(disks=P4.disks[:])
        PB2_2.move_to(PB3_2)
        successors.append(State(PB1_2, PB2_2, PB3_2, PB4_2, parent=q))

        #from tower2 to tower4
        PB1_3 = Pegs(disks=P1.disks[:])
        PB2_3 = Pegs(disks=P2.disks[:])
        PB3_3 = Pegs(disks=P3.disks[:])
        PB4_3 = Pegs(disks=P4.disks[:])
        PB2_3.move_to(PB4_3)
        successors.append(State(PB1_3, PB2_3, PB3_3, PB4_3, parent=q))

        ##from tower3 to tower1
        PC1_1 = Pegs(disks=P1.disks[:])
        PC2_1 = Pegs(disks=P2.disks[:])
        PC3_1 = Pegs(disks=P3.disks[:])
        PC4_1 = Pegs(disks=P4.disks[:])
        PC3_1.move_to(PC1_1)
        successors.append(State(PC1_1, PC2_1, PC3_1, PC4_1, parent=q))

        #from tower3 to tower2
        PC1_2 = Pegs(disks=P1.disks[:])
        PC2_2 = Pegs(disks=P2.disks[:])
        PC3_2 = Pegs(disks=P3.disks[:])
        PC4_2 = Pegs(disks=P4.disks[:])
        PC3_2.move_to(PC2_2)
        successors.append(State(PC1_2, PC2_2, PC3_2, PC4_2, parent=q))

        #from tower3 to tower4
        PC1_3 = Pegs(disks=P1.disks[:])
        PC2_3 = Pegs(disks=P2.disks[:])
        PC3_3 = Pegs(disks=P3.disks[:])
        PC4_3 = Pegs(disks=P4.disks[:])
        PC3_3.move_to(PC4_3)
        successors.append(State(PC1_3, PC2_3, PC3_3, PC4_3, parent=q))


        #From fourth peg to first
        PD1_1 = Pegs(disks=P1.disks[:])
        PD2_1 = Pegs(disks=P2.disks[:])
        PD3_1 = Pegs(disks=P3.disks[:])
        PD4_1 = Pegs(disks=P4.disks[:])
        PD4_1.move_to(PD1_1)
        successors.append(State(PD1_1, PD2_1, PD3_1, PD4_1, parent=q))

        #from tower4 to tower2
        PD1_2 = Pegs(disks=P1.disks[:])
        PD2_2 = Pegs(disks=P2.disks[:])
        PD3_2 = Pegs(disks=P3.disks[:])
        PD4_2 = Pegs(disks=P4.disks[:])
        PD4_2.move_to(PD2_2)
        successors.append(State(PD1_2, PD2_2, PD3_2, PD4_2, parent=q))

        #from tower4 to tower3
        PD1_3 = Pegs(disks=P1.disks[:])
        PD2_3 = Pegs(disks=P2.disks[:])
        PD3_3 = Pegs(disks=P3.disks[:])
        PD4_3 = Pegs(disks=P4.disks[:])
        PD4_3.move_to(PD3_3)
        successors.append(State(PD1_3, PD2_3, PD3_3, PD4_3, parent=q))

        return successors


    #backtracks the solution path to give out the entire path 
    #Just keep following to the parent q
    def solution_path(self, q):
        path = []
        while q.parent != None:
            path.append(q)
            q = q.parent
        path.append(self.initial_state)
        return path

#####################################################################
#Solver Function with BFS Implementation
#####################################################################
    def Solve(self):
        cost = -1
        self.open_list.append(self.initial_state)
        while len(self.open_list) > 0:
            q = self.select_next_state(cost)
            cost += 1
            self.closed_list.append(q)
            if q == self.final_state:
                # Got to the final state, display and give the solution path
                print( "Total Number of States: %d" % len(self.closed_list))
                print( "Solution:")
                for n in reversed(self.solution_path(q)):
                    print n.state
                break
            else:
                #generate successive states for q
                successors = self.generate_successive_states(q)
                for s in successors:
                    new_state = True
                    #if state already in closed list, that is, visited, don't append it to open list
                    for c in self.closed_list:
                        if c == s:
                            new_state = False #initialise successive_states list

        #There are 12 possible moves
                    if new_state:
                        for o in self.open_list:
                            if o == s:
                                new_state = False
                                if o.value > s.value:
                                    self.open_list.remove(o)
                                    self.open_list.append(s)
                                    break
                        if new_state:
                            self.open_list.append(s)

#####################################################################
# Main Run
#####################################################################
import time

n = input('Enter number of disc')

# Starting state
PA1 = Pegs(max_disks=n)
PA2 = Pegs()
PA3 = Pegs()
PA4 = Pegs()
SS = State(PA1,PA2,PA3,PA4, parent=None)

# Goal state
PB1 = Pegs()
PB2 = Pegs()
PB3 = Pegs()
PB4 = Pegs(max_disks=n)
FS = State(PB1,PB2,PB3, PB4, parent=None, end_goal=True)

print "Starting State: %s" % str(SS.state)
print "Final State: %s" % str(FS.state)

#Start timer
start_time = time.time()

game = TowersOfHanoi(SS, FS)
game.Solve()

#End timer
end_time = time.time()

#Display the time it takes
print "Time Taken: %f seconds" % (end_time - start_time)                            