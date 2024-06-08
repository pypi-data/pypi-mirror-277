import math
import numpy as np

import random


class Random:
    def __repr__(self):
        return 'Random strategy'

    @staticmethod
    def select(fringe):
        random.shuffle(fringe)
        node = fringe.pop(0)
        return fringe, node


class BreadthFirst:
    def __repr__(self):
        return 'Breadth First strategy'

    @staticmethod
    def select(fringe):
        node = fringe.pop(0)
        return fringe, node


class DepthFirst:
    def __repr__(self):
        return 'Depth First strategy'

    @staticmethod
    def select(fringe):
        node = fringe.pop()
        return fringe, node


class UniformCost:
    def __repr__(self):
        return 'Uniform Cost strategy'

    @staticmethod
    def select(fringe):
        fringe = sorted(fringe, key=lambda x: x.cost)
        node = fringe.pop(0)
        return fringe, node


class DepthLimitedSearch:
    def __init__(self, limit):
        self.limit = limit

    def __repr__(self):
        return 'Depth First Limited strategy'

    def select(self, fringe):
        fringe = [n for n in fringe if n.depth <= self.limit]
        try:
            node = fringe.pop()
        except IndexError:
            return [], None
        return fringe, node


class Greedy:
    def __init__(self, problem):
        self.problem = problem

    def __repr__(self):
        return 'Greedy strategy'

    def select(self, fringe):
        # sort fringe following the evaluation function
        fringe = sorted(fringe, key=lambda x: self.problem.h(x.state))
        node = fringe.pop(0)
        return fringe, node


class AStar:
    def __init__(self, problem):
        self.problem = problem

    def __repr__(self):
        return 'AStar strategy'

    def select(self, fringe):
        # sort fringe following the evaluation function
        fringe = sorted(fringe, key=lambda x: (self.problem.h(x.state)+x.cost))
        node = fringe.pop(0)
        return fringe, node





class Roads:
    def __init__(self, streets, coordinates):
        self.streets = streets
        self.coordinates = coordinates

    def distance(self, start, end):
        lat_a, long_a = self.coordinates[start]
        lat_b, long_b = self.coordinates[end]
        lat_diff = abs(lat_a - lat_b)*111
        long_diff = abs(long_a - long_b)*111
        return math.sqrt(lat_diff**2 + long_diff**2)


class Maze:
    def __init__(self, M, N, K, V):
        self.width = N
        self.height = M
        self.n_walls = K
        self.p_walls = V

    def create_environment(self):
        maze = np.ones((self.height, self.width), dtype=int)
        for i in range(self.n_walls):
            maze[self.p_walls[i][0]][self.p_walls[i][1]] = 2
        return maze


class TreeSearch:

    def __init__(self, problem, strategy=None):
        self.problem = problem
        self.strategy = strategy
        self.fringe = []

    def __repr__(self):
        return 'Tree Search'

    def run(self):

        node = Node(state=self.problem.initial_state,
                    parent=None,
                    action=None,
                    cost=0,
                    depth=0)
        while True:
            if self.problem.goal_test(node.state):
                return 'Ok', node
            new_states = self.problem.successors(node.state)
            new_nodes = [node.expand(state=s,
                                     action=a,
                                     cost=self.problem.cost(node.state, a)) for s, a in new_states]
            self.fringe = self.fringe + new_nodes
            if len(self.fringe) != 0:
                self.fringe, node = self.strategy.select(self.fringe)
                if node is None:
                    return 'Fail', []
            else:
                if self.problem.goal_test(node.state):
                    return 'Ok', node
                else:
                    return 'Fail', []

class GraphSearch:
    def __init__(self, problem, strategy=None):
        self.problem = problem
        self.strategy = strategy
        self.fringe = []
        self.visited = []

    def __repr__(self):
        return 'Graph Search'

    def run(self):

        node = Node(state=self.problem.initial_state,
                    parent=None,
                    action=None,
                    cost=0,
                    depth=0)

        while True:
            if self.problem.goal_test(node.state):
                return 'Ok', node
            self.visited.append(node.state)
            new_states = self.problem.successors(node.state)
            new_nodes = [node.expand(state=s,
                                     action=a,
                                     cost=self.problem.cost(node.state, a)) for s, a in new_states]
            new_nodes = [n for n in new_nodes if n.state not in self.visited]
            self.fringe = [n for n in self.fringe if n.state not in self.visited]

            self.fringe = self.fringe + new_nodes

            if len(self.fringe) != 0:
                self.fringe, node = self.strategy.select(self.fringe)
                if node is None:
                    return 'Fail', []
            else:
                if self.problem.goal_test(node.state):
                    return 'Ok', node
                else:
                    return 'Fail', []



import math
import random


class HillClimbing:

    def __init__(self, problem):
        self.problem = problem

    def __repr__(self):
        return 'Hill Climbing'

    def run(self):
        node = Node(state=self.problem.initial_state,
                    parent=None,
                    action=None,
                    cost=0,
                    depth=0)

        while True:
            new_states = self.problem.successors(node.state)
            if not new_states:
                return 'Stop', node.state
            best_neighbor, best_action = max(new_states, key=lambda x: self.problem.value(x[0]))

            if self.problem.value(node.state) >= self.problem.value(best_neighbor):
                return 'Ok', node.state

            node = node.expand(state=best_neighbor,
                               action=best_action,
                               cost=1)


class SimulatedAnnealing:

    def __init__(self, problem, min_temp=0, max_time=100, lam=0.001):
        self.problem = problem
        self.min_temp = min_temp
        self.max_time = max_time
        self.lam = lam

    def __repr__(self):
        return 'Simulated Annealing'

    def linear_schedule(self, temp):
        return temp - self.lam

    def proportional_schedule(self, temp):
        return temp - self.lam * temp

    def exponential_schedule(self, temp, time):
        return temp * math.exp(-self.lam * time)

    def run(self, initial_temp=100):
        time = 0
        temp = initial_temp

        node = Node(state=self.problem.initial_state,
                    parent=None,
                    action=None,
                    cost=0,
                    depth=0)

        while temp > self.min_temp and time < self.max_time:
            new_states = self.problem.successors(node.state)

            if not new_states:
                return 'Stop', node

            selected_neighbour, selected_action = random.choice(new_states)

            score_diff = self.problem.value(selected_neighbour) - self.problem.value(node.state)

            if score_diff > 0 or random.uniform(0, 1) < math.exp(score_diff / temp):
                node = node.expand(state=selected_neighbour,
                                   action=selected_action,
                                   cost=1)
            temp = self.exponential_schedule(temp, time)
            time += 1

        print(f'temp: {temp}, time: {time}')
        return 'Ok', node.state


class Genetic:

    def __init__(self, problem, population=1000, generations=100, p_mutation=0.1, gene_pool=None):
        self.problem = problem
        self.population = population
        self.generations = generations
        self.couples = int(self.population / 2)
        self.p_mutation = p_mutation
        self.gene_pool = gene_pool

    def __repr__(self):
        return 'Genetic'

    def select(self, population):
        fitnesses = list(map(self.problem.value, population))
        return random.choices(population=population, weights=fitnesses, k=2)

    def crossover(self, couple):
        parent_a, parent_b = couple
        split = random.randrange(0, len(parent_a))
        return tuple(list(parent_a[:split]) + list(parent_b[split:]))

    def mutation(self, state):
        if random.uniform(0, 1) > self.p_mutation or self.gene_pool is None:
            return state
        new_state = list(state)
        new_state[random.randrange(len(state))] = random.choice(self.gene_pool)
        return tuple(new_state)

    def run(self):
        population = [self.problem.random() for _ in range(self.population)]
        for e in range(self.generations):
            best = max(population, key=lambda x: self.problem.value(x))
            print(f'Generation: {e} - max score: {self.problem.value(best)}')
            new_generation = [
                self.mutation(
                    self.crossover(
                        self.select(population)
                    )
                )
                for _ in range(self.population)]
            population = new_generation
        return 'ok', max(population, key=lambda x: self.problem.value(x))


class Node:
    def __init__(self, state, parent, action, cost, depth):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.depth = depth

    def __repr__(self):
        return f'({self.state})'

    def expand(self, state, action, cost=1):
        return Node(state=state,
                    parent=self,
                    action=action,
                    cost=self.cost+cost,
                    depth=self.depth+1)

    def path(self):
        path = []
        node = self
        while node.parent:
            path.append(node.action)
            node = node.parent
        path = list(reversed(path))
        return path


import math
import random


class StreetProblem:

    def __init__(self, initial_state, goal_state, environment):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.environment = environment

    def successors(self, state):
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def actions(self, state):
        return self.environment.streets[state]

    def result(self, state=None, action=None):
        return action

    def goal_test(self, state):
        return state == self.goal_state

    def cost(self, state, action):
        reached_state = self.result(state, action)
        return self.environment.distance(state, reached_state)

    def h(self, state):
        lat_a, long_a = self.environment.coordinates[state]
        lat_b, long_b = self.environment.coordinates[self.goal_state]
        lat_diff = abs(lat_a - lat_b) * 111  # <- *111 to just convert the latitude distance in KM.
        long_diff = abs(long_a - long_b) * 111  # <- *111 to just convert the longitude distance in KM.
        return math.sqrt(lat_diff ** 2 + long_diff ** 2)


class MazeProblem:

    def __init__(self, initial_state, goal_state, environment):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.environment = environment

    def successors(self, state):
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def actions(self, state):
        actionList = ['up', 'down', 'left', 'right']

        if state[0] == 0:
            actionList.remove("up")

        if state[0] == self.environment.height - 1:
            actionList.remove("down")

        if state[1] == 0:
            actionList.remove("left")

        if state[1] == self.environment.width - 1:
            actionList.remove("right")

        for i in range(self.environment.n_walls):
            if (state[0] - 1, state[1]) == self.environment.p_walls[i]:
                actionList.remove("up")
            if (state[0] + 1, state[1]) == self.environment.p_walls[i]:
                actionList.remove("down")
            if (state[0], state[1] - 1) == self.environment.p_walls[i]:
                actionList.remove("left")
            if (state[0], state[1] + 1) == self.environment.p_walls[i]:
                actionList.remove("right")

        return actionList

    def result(self, state=None, action=None):
        if action == 'up':
            reached_state = (state[0] - 1, state[1])
        if action == 'down':
            reached_state = (state[0] + 1, state[1])
        if action == 'left':
            reached_state = (state[0], state[1] - 1)
        if action == 'right':
            reached_state = (state[0], state[1] + 1)
        return reached_state

    def goal_test(self, state):
        return state == self.goal_state

    def cost(self, state, action):
        return 1

    def h(self, state):
        return abs(self.goal_state[0] - state[0]) + abs(self.goal_state[1] - state[1])


class HanoiTower:
    def __init__(self, n, initial_state=None, goal_state=None):
        self.n = n
        if initial_state is None:
            initial_state = [list(range(1, self.n + 1)), [], []]
        if goal_state is None:
            goal_state = [[], [], list(range(1, self.n + 1))]
        self.initial_state = initial_state
        self.goal_state = goal_state

    def successors(self, state):
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def actions(self, state):
        possible_actions = ['Move from A to B', 'Move from A to C',
                            'Move from B to A', 'Move from B to C',
                            'Move from C to A', 'Move from C to B']
        if len(state[0]) == 0:
            possible_actions.remove('Move from A to B')
            possible_actions.remove('Move from A to C')
        else:
            top_disk = state[0][0]
            for i in range(0, len(state)):
                if i != 0 and len(state[i]) != 0:
                    if top_disk > state[i][0]:
                        if i == 1:
                            possible_actions.remove('Move from A to B')
                        else:
                            possible_actions.remove('Move from A to C')

        if len(state[1]) == 0:
            possible_actions.remove('Move from B to A')
            possible_actions.remove('Move from B to C')
        else:
            top_disk = state[1][0]
            for i in range(0, len(state)):
                if i != 1 and len(state[i]) != 0:
                    if top_disk > state[i][0]:
                        if i == 0:
                            possible_actions.remove('Move from B to A')
                        else:
                            possible_actions.remove('Move from B to C')

        if len(state[2]) == 0:
            possible_actions.remove('Move from C to B')
            possible_actions.remove('Move from C to A')
        else:
            top_disk = state[2][0]
            for i in range(0, len(state)):
                if i != 2 and len(state[i]) != 0:
                    if top_disk > state[i][0]:
                        if i == 0:
                            possible_actions.remove('Move from C to A')
                        else:
                            possible_actions.remove('Move from C to B')

        return possible_actions

    def result(self, state=None, action=None):
        rod_1 = state[0].copy()
        rod_2 = state[1].copy()
        rod_3 = state[2].copy()
        if action == 'Move from A to B':
            disk = rod_1.pop(0)
            rod_2.insert(0, disk)
        if action == 'Move from A to C':
            disk = rod_1.pop(0)
            rod_3.insert(0, disk)
        if action == 'Move from B to A':
            disk = rod_2.pop(0)
            rod_1.insert(0, disk)
        if action == 'Move from B to C':
            disk = rod_2.pop(0)
            rod_3.insert(0, disk)
        if action == 'Move from C to A':
            disk = rod_3.pop(0)
            rod_1.insert(0, disk)
        if action == 'Move from C to B':
            disk = rod_3.pop(0)
            rod_2.insert(0, disk)

        return [rod_1, rod_2, rod_3]

    def goal_test(self, state):
        return state == self.goal_state

    def cost(self, state, action):
        return 1

    def h(self, state):
        return len(state[0]) + len(state[1])


class EightQueensProblem:

    def __init__(self, initial_state=None):
        if initial_state is None:
            initial_state = self.random()
        self.initial_state = initial_state
        self.max_conflicts = sum([i for i in range(1, 8)])

    def successors(self, state):
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def actions(self, state):
        actions = []
        for col, queen in enumerate(state):
            squares = list(range(0, 8))
            squares.remove(queen)
            # new_actions = list(zip(squares, [col]*len(squares)))
            new_actions = list(zip([col] * len(squares), squares))
            actions.extend(new_actions)
        return actions

    def result(self, state=None, action=None):
        new_state = list(state)
        col, new_row = action
        new_state[col] = new_row
        return tuple(new_state)

    def conflicts(self, state):
        conflicts = 0
        for col in range(8):
            queen = state[col]
            for col1 in range(col+1, 8):
                queen1 = state[col1]
                if queen == queen1:
                    conflicts += 1
                if queen - col == queen1 - col1 or queen + col == queen1 + col1:
                    conflicts += 1
        return conflicts

    def goal_test(self, state):
        return self.conflicts(state) == 0

    def cost(self, state, action):
        return 1

    def value(self, state):
        return self.max_conflicts - self.conflicts(state)

    @staticmethod
    def random():
        chess = [random.randrange(0, 8) for _ in range(8)]
        return tuple(chess)

    @staticmethod
    def print_chess(state):
        print('\t', end='')
        for number in [1, 2, 3, 4, 5, 6, 7, 8]:
            print(f"|  {number}  ", end='')
        print('|', end='')
        print('\n\t_________________________________________________')

        for row, letter in zip(range(8), ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']):
            print(letter + '\t', end='')
            print('|', end='')

            for queen in state:
                if queen == row:
                    print('  Q  ', end='')
                else:
                    print('     ', end='')
                print('|', end='')
            print('\n', end='')
            print('\t_________________________________________________')


class AC3:
    def __init__(self, csp):
        self.csp = csp

    def all_arcs(self):
        queue = []
        for cons in self.csp.constraints:
            if cons.degree == 2:
                queue.append(cons)
        return queue

    def add_neighbours(self, queue, arc):
        var, _ = arc.variables
        neighbours = [arc for arc in self.all_arcs() if arc.variables[1] == var]
        queue.extend(neighbours)

    def run(self, state):
        queue = self.all_arcs()
        while queue:
            arc = queue.pop()
            if 0 in [len(v) for k, v in self.csp.domains.items()]:
                return False
            if self.csp.remove_inconsistent_values(arc=arc, actual_state=state):
                self.add_neighbours(queue, arc)
        return True



import random


def random_variable(problem, state):
    assignable_vars = problem.assignable_variables(state)
    if assignable_vars:
        random.shuffle(assignable_vars)
        return assignable_vars.pop()
    return None


def minimum_remaining_values(problem, state):
    return min(problem.assignable_variables(state), key=lambda v: len(problem.legal_moves(state, v)))


def degree_heuristic(problem, state):
    return max(problem.assignable_variables(state), key=lambda v: problem.remaining_constraints(state, v))


def random_assignment(problem, state, variable, domains):
    possible_values = domains[variable]
    random.shuffle(possible_values)
    return possible_values


def least_constraining_value(problem, state, variable, domains):
    assignable_values = domains[variable]
    return sorted(assignable_values,
                  key=lambda v: -sum([len(problem.legal_moves(problem.assign(state, variable, v), var))
                                      for var in problem.assignable_variables(problem.assign(state, variable, v))]))


class BackTracking:

    def __init__(self, problem, var_criterion=None, value_criterion=None):
        self.problem = problem
        if var_criterion is None:
            var_criterion = random_variable
        self.var_criterion = var_criterion
        if value_criterion is None:
            value_criterion = random_assignment
        self.value_criterion = value_criterion

    def __repr__(self):
        return 'Backtracking'

    def run(self, state):
        if self.problem.goal_test(state):
            return state

        variable = self.var_criterion(self.problem, state)
        if variable is None:
            return False

        values = self.value_criterion(self.problem, state, variable, self.problem.domains)

        for value in values:
            new_state = self.problem.assign(state=state,
                                            variable=variable,
                                            value=value)
            if self.problem.consistent(new_state):
                state = dict(new_state)

                result = self.run(dict(state))

                if result:
                    return result
                else:

                    state = self.problem.rollback(state, variable)

        return False

    def forward_checking(self, state, domains):
        new_domains = dict(domains)
        for var in self.problem.variables:
            new_domains[var] = self.problem.legal_moves(state, var)
        return new_domains

    def run_with_forward_checking(self, state, domains):

        if self.problem.goal_test(state):
            return state

        if [] in domains.values():
            return False

        variable = self.var_criterion(self.problem, state)
        if variable is None:
            return False

        values = self.value_criterion(self.problem, state, variable, domains)

        for value in values:

            new_state = self.problem.assign(state=state,
                                            variable=variable,
                                            value=value)

            if self.problem.consistent(new_state):
                state = dict(new_state)

                new_domains = self.forward_checking(state, domains)
                del(new_domains[variable])

                result = self.run_with_forward_checking(dict(state), new_domains)

                if result:
                    return result
                else:

                    state = self.problem.rollback(state, variable)

        return False


class Constraint:
    def __init__(self, variables):
        self.variables = variables
        self.degree = len(variables)

    def check(self, state):
        return True


class UnaryConstraint(Constraint):
    def __init__(self, variable):
        self.variable = variable
        super(UnaryConstraint, self).__init__(variables=variable)

    def check(self, state):
        return True


class ValueConstraint(UnaryConstraint):

    def __init__(self, variable, accepted_values):
        super(ValueConstraint, self).__init__(variable)
        self.accepted_values = accepted_values

    def check(self, state):
        if self.variable in state:
            return state[self.variable] in self.accepted_values
        return True


class DifferentValues(Constraint):

    def check(self, state):
        values = [state[var] for var in self.variables if var in state]
        return len(values) == len(set(values))


class EqualValues(Constraint):

    def check(self, state):
        values = [state[var] for var in self.variables if var in state]
        if values:
            return len(set(values)) == 1
        else:
            return True


class MaximumCapacity(UnaryConstraint):
    def __init__(self, variable, max_capacity):
        super(MaximumCapacity, self).__init__(variable)
        self.maxCapacity = max_capacity

    def check(self, state):
        values = [state[var] for var in self.variables if var in state]
        return all([values.count(x) <= self.maxCapacity for x in values])


'''
class MaximumCapacity(UnaryConstraint):
    def __init__(self, variable, max_capacity):
        super(MaximumCapacity, self).__init__(variable)
        self.maxCapacity = max_capacity

    def check(self, state):
        if self.variable in state:
            return len(state[self.variable]) <= self.maxCapacity
        return True


class UniqueValue(UnaryConstraint):
    def __init__(self, variable, values):
        super(UniqueValue, self).__init__(variable)
        self.values = values

    def check(self, state):
        if self.variable in state:
            in_list = [state[var] for var in self.variables if state[var] in self.values]
            return len(in_list) < 2
        return True

class NotInSame(Constraint):
'''


class CSP:

    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.initial_state = dict()

    def consistent(self, state):
        return all([c.check(state) for c in self.constraints])

    def complete(self, state):
        return len(state) == len(self.variables)

    def goal_test(self, state):
        return self.complete(state) and self.consistent(state)

    def assign(self, state, variable, value):
        if variable in self.variables and value in self.domains[variable]:
            new_state = dict(state)
            new_state[variable] = value
            return new_state
        raise ValueError

    def rollback(self, state, variable):

        if variable in self.variables:
            new_state = dict(state)
            del new_state[variable]
            return new_state
        raise ValueError

    def legal_moves(self, state, variable):

        possible_values = self.domains[variable]
        return [value for value in possible_values
                if self.consistent(self.assign(state, variable, value))]

    def count_constraints(self, first_variable, second_variable):

        return sum([1 for c in self.constraints
                    if first_variable in c.variables
                    and second_variable in c.variables])

    def remaining_constraints(self, state, variable):

        remaining_variables = [var for var in self.variables if var not in state and var != variable]
        if remaining_variables:
            return sum([self.count_constraints(variable, rem_var) for rem_var in remaining_variables])
        else:
            return 0

    def assignable_variables(self, state):
        return [variable for variable in self.variables if variable not in state]

    def remove_inconsistent_values(self, arc, actual_state):

        x_i, x_j = arc.variables

        removed = False
        for value_i in self.domains[x_i]:
            state = self.assign(state=actual_state,
                                variable=x_i,
                                value=value_i)
            assignments = [arc.check(self.assign(state=state,
                                                 variable=x_j,
                                                 value=value_j)) for value_j in self.domains[x_j]]
            if not any(assignments):
                self.domains[x_i].remove(value_i)
                print(f'removing {value_i} from {x_i}')
                removed = True
        return removed


class MapColors(CSP):
    def __init__(self):
        self.variables = ['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T']
        self.domains = {var: ['green', 'red', 'blue'] for var in self.variables}
        self.constraints = [DifferentValues(['WA', 'NT']),
                            DifferentValues(['NT', 'WA']),
                            DifferentValues(['WA', 'SA']),
                            DifferentValues(['SA', 'WA']),
                            DifferentValues(['SA', 'NT']),
                            DifferentValues(['NT', 'SA']),
                            DifferentValues(['SA', 'Q']),
                            DifferentValues(['Q', 'SA']),
                            DifferentValues(['SA', 'NSW']),
                            DifferentValues(['NSW', 'SA']),
                            DifferentValues(['SA', 'V']),
                            DifferentValues(['V', 'SA']),
                            DifferentValues(['Q', 'NT']),
                            DifferentValues(['NT', 'Q']),
                            DifferentValues(['NSW', 'Q']),
                            DifferentValues(['Q', 'NSW']),
                            DifferentValues(['V', 'NSW']),
                            DifferentValues(['NSW', 'V'])
                            ]


class Containers(CSP):
    def __init__(self):
        self.variables = ['t1', 't2', 't3', 't4', 't5', 'f1', 'f2', 'f3', 'e1', 'e2', 'fz1', 'fz2', 'fz3', 'fs1']
        self.domains = {var: ['C1', 'C2', 'C3', 'C4'] for var in self.variables}
        self.constraints = [DifferentValues(['e1', 'e2']),
                            DifferentValues(['e2', 'e1']),
                            DifferentValues(['t1', 'f1']),
                            DifferentValues(['f1', 't1']),
                            DifferentValues(['t1', 'f2']),
                            DifferentValues(['f2', 't1']),
                            DifferentValues(['t1', 'f3']),
                            DifferentValues(['f3', 't1']),
                            DifferentValues(['t2', 'f1']),
                            DifferentValues(['f1', 't2']),
                            DifferentValues(['t2', 'f2']),
                            DifferentValues(['f2', 't2']),
                            DifferentValues(['t2', 'f3']),
                            DifferentValues(['f3', 't2']),
                            DifferentValues(['t3', 'f1']),
                            DifferentValues(['f1', 't3']),
                            DifferentValues(['t3', 'f2']),
                            DifferentValues(['f2', 't3']),
                            DifferentValues(['t3', 'f3']),
                            DifferentValues(['f3', 't3']),
                            DifferentValues(['t4', 'f1']),
                            DifferentValues(['f1', 't4']),
                            DifferentValues(['t4', 'f2']),
                            DifferentValues(['f2', 't4']),
                            DifferentValues(['t4', 'f3']),
                            DifferentValues(['f3', 't4']),
                            DifferentValues(['t5', 'f1']),
                            DifferentValues(['f1', 't5']),
                            DifferentValues(['t5', 'f2']),
                            DifferentValues(['f2', 't5']),
                            DifferentValues(['t5', 'f3']),
                            DifferentValues(['f3', 't5']),
                            EqualValues(['fz1', 'fz2', 'fz3']),
                            DifferentValues(['fs1', 'fz1']),
                            DifferentValues(['fs1', 'fz2']),
                            DifferentValues(['fs1', 'fz3']),
                            DifferentValues(['fz1', 'fs1']),
                            DifferentValues(['fz2', 'fs1']),
                            DifferentValues(['fz3', 'fs1']),
                            MaximumCapacity(self.variables, 6)]



import numpy as np
import random
import itertools

class Game:
    def __init__(self, initial_state, player):
        self.initial_state = initial_state
        self.player = player

    def actions(self, state):
        return []

    def result(self, state, action):
        return []

    def successors(self, state):
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def terminal_test(self, state):
        return False

    def utility(self, state):
        return 0

    def player_utility(self, state):
        if self.player == 'MAX':
            return self.utility(state)
        elif self.player == 'MIN':
            return -self.utility(state)
        else:
            raise ValueError

    def next_player(self):
        if self.player == 'MAX':
            return 'MIN'
        else:
            return 'MAX'

    def play(self, player_one, player_two):
        state = self.initial_state
        players = [player_one, player_two]
        moves = []
        while True:
            for player in players:
                if self.terminal_test(state):
                    print('----- GAME OVER -----\n\n')
                    return moves
                self.display(state)
                move = player.next_move(state)
                state = self.result(state, move)
                self.display_move(state, move)
                moves.append((move, self.player))
                self.player = self.next_player()
                print('_____________________')

    def display(self, state):
        print('_____________________')
        print(self.player, 'in ', state)

    def display_move(self, state, move):
        print(self.player, f'--{move}--> ', state)

class DummyGame(Game):
    def __init__(self, initial_state=None, player='MAX'):
        if initial_state is None:
            initial_state = 'A'
        super(DummyGame, self).__init__(initial_state, player)
        self.initial_state = initial_state
        self.player = player

    def actions(self, state):
        actions = {
            'A': ['a1', 'a2', 'a3'],
            'B': ['b1', 'b2', 'b3'],
            'C': ['c1', 'c2', 'c3'],
            'D': ['d1', 'd2', 'd3'],
        }
        if state in actions:
            return actions[state]
        else:
            return []

    def result(self, state, action):
        result = {
            'A': {
                'a1': 'B',
                'a2': 'C',
                'a3': 'D'},
            'B': {
                'b1': 'B1',
                'b2': 'B2',
                'b3': 'B3'},
            'C': {
                'c1': 'C1',
                'c2': 'C2',
                'c3': 'C3'},
            'D': {
                'd1': 'D1',
                'd2': 'D2',
                'd3': 'D3'},
        }
        return result[state][action]

    def terminal_test(self, state):
        if state in ('B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'D1', 'D2', 'D3'):
            return True
        else:
            return False

    def utility(self, state):
        utility = {'B1': 3,
                   'B2': 12,
                   'B3': 8,
                   'C1': 2,
                   'C2': 4,
                   'C3': 6,
                   'D1': 14,
                   'D2': 5,
                   'D3': 2}
        return utility[state]


class TicTacToe(Game):
    def __init__(self, initial_state=None, height=3, width=3, player='MAX'):
        self.height = height
        self.width = width
        if initial_state is None:
            initial_state = self.init_state()
        super(TicTacToe, self).__init__(initial_state, player)
        self.initial_state = initial_state
        self.squares = self.height * self.width
        self.empty = '.'
        self.X = 'X'
        self.O = 'O'

    @staticmethod
    def init_state():
        state = {'cells': [], 'to_move': 'MAX', 'max_cells': [], 'min_cells': []}
        # state['board'] = []
        return state

    def actions(self, state):
        action_list = [(x, y) for x in range(self.width) for y in range(self.height) if (x, y) not in state['cells']]
        return action_list

    def result(self, state, action):
        copy_state = {}
        for k, v in state.items():
            if k != 'to_move':
                copy_state[k] = state[k].copy()
        copy_state['to_move'] = state['to_move']
        if copy_state['to_move'] == 'MAX':
            copy_state['max_cells'].insert(0, action)
            copy_state['cells'].insert(0, action)
            copy_state['to_move'] = 'MIN'
            return copy_state
        elif copy_state['to_move'] == 'MIN':
            copy_state['min_cells'].insert(0, action)
            copy_state['cells'].insert(0, action)
            copy_state['to_move'] = 'MAX'
            return copy_state
        else:
            raise ValueError

    def terminal_test(self, state):
        if self.utility(state) != 0 or len(state['cells']) == self.squares:
            return True
        else:
            return False

    def utility(self, state):
        for i in range(self.width):
            if len([el for el in state['max_cells'] if i == el[0]]) == 3:
                return 1
            if len([el for el in state['min_cells'] if i == el[0]]) == 3:
                return -1

        for j in range(self.height):
            if len([el for el in state['max_cells'] if j == el[1]]) == 3:
                return 1
            if len([el for el in state['min_cells'] if j == el[1]]) == 3:
                return -1

        temp1 = []
        temp2 = []
        temp3 = []
        temp4 = []
        temp1.append([el for el in state['max_cells'] if el in [(0, 0), (1, 1), (2, 2)]])
        temp2.append([el for el in state['min_cells'] if el in [(0, 0), (1, 1), (2, 2)]])
        if len(temp1[0]) == 3:
            return 1
        if len(temp2[0]) == 3:
            return -1
        temp3.append([el for el in state['max_cells'] if el in [(0, 2), (1, 1), (2, 0)]])
        temp4.append([el for el in state['min_cells'] if el in [(0, 2), (1, 1), (2, 0)]])
        if len(temp3[0]) == 3:
            return 1
        if len(temp4[0]) == 3:
            return -1
        return 0

    def play(self, player_one, player_two):
        state = self.initial_state
        print("----- THE GAME STARTS! -----\n\n")
        self.draw_board(self.initial_state)
        players = [player_one, player_two]
        moves = []
        while True:
            for player in players:
                if self.terminal_test(state):
                    if self.utility(state) == 0:
                        print("IT'S A DRAW! \n\n")
                    elif self.utility(state) == 1:
                        print("MAX WINS! \n\n")
                    elif self.utility(state) == -1:
                        print("MIN WINS! \n\n")
                    print('----- GAME OVER -----\n\n')
                    return moves
                else:
                    print(f'{self.player} plays!')
                move = player.next_move(state)
                state = self.result(state, move)
                self.draw_board(state)
                moves.append((move, self.player))
                self.player = self.next_player()
                print('_____________________')

    def draw_board(self, state):
        print('\t', end='')
        for column in range(0, self.width):
            print(column, '\t\t', end='')
        print()
        copy_state = {}
        for k, v in state.items():
            if k != 'to_move':
                copy_state[k] = state[k].copy()

        for i in range(0, self.height):
            print(i, end='')
            for j in range(0, self.width):
                if (i, j) in state['max_cells']:
                    print('\t{}\t|'.format(self.X), end=" ")
                elif (i, j) in state['min_cells']:
                    print('\t{}\t|'.format(self.O), end=" ")
                else:
                    print('\t{}\t|'.format(self.empty), end=" ")
            print()
        print()


class ConnectFour(Game):
    def __init__(self, initial_state=None, height=6, width=7, player='MAX'):
        self.height = height
        self.width = width
        if initial_state is None:
            initial_state = self.init_state()
        super(ConnectFour, self).__init__(initial_state, player)
        self.initial_state = initial_state
        self.squares = self.height * self.width
        self.empty = '.'

    def init_state(self):
        state = {i: [] for i in range(self.width)}
        state['to_move'] = 'MAX'
        return state

    def actions(self, state):
        action_list = [k for k, v in state.items() if len(v) < self.height and k != 'to_move']
        return action_list

    def result(self, state, action):
        copy_state = {}
        for k, v in state.items():
            if k != 'to_move':
                copy_state[k] = state[k].copy()
        copy_state['to_move'] = state['to_move']
        if copy_state['to_move'] == 'MAX':
            copy_state[action].insert(0, 'MAX')
            copy_state['to_move'] = 'MIN'
            return copy_state
        elif copy_state['to_move'] == 'MIN':
            copy_state[action].insert(0, 'MIN')
            copy_state['to_move'] = 'MAX'
            return copy_state
        else:
            raise ValueError

    def terminal_test(self, state):
        squares = sum([len(v) for k, v in state.items() if k != 'to_move'])
        if abs(self.utility(state)) == 1000000 or squares == self.squares:
            return True
        else:
            return False

    def utility(self, state):
        copy_state = {}
        for k, v in state.items():
            if k != 'to_move':
                copy_state[k] = state[k].copy()

        max_twos = 0
        max_threes = 0
        max_fours = 0
        min_twos = 0
        min_threes = 0
        min_fours = 0

        # vertical case
        for k, v in copy_state.items():
            count_dups = [sum(1 for g in group if g == 'MAX') for _, group in itertools.groupby(v)]
            for c in count_dups:
                if c == 2:
                    max_twos += 1
                elif c == 3:
                    max_threes += 1
                elif c >= 4:
                    max_fours += 1
            count_dups = [sum(1 for g in group if g == 'MIN') for _, group in itertools.groupby(v)]
            for c in count_dups:
                if c == 2:
                    min_twos += 1
                elif c == 3:
                    min_threes += 1
                elif c >= 4:
                    min_fours += 1

        temp = [[] for _ in range(self.height)]
        help = 0
        for k, v in copy_state.items():
            while len(v) < self.height:
                v.insert(0, help)
                help += 1
        for k, v in copy_state.items():
            for i in range(len(v)):
                temp[i].append(v[i])
        for el in temp:
            count_dups = [sum(1 for g in group if g == 'MAX') for _, group in itertools.groupby(el)]
            for c in count_dups:
                if c == 2:
                    max_twos += 1
                elif c == 3:
                    max_threes += 1
                elif c >= 4:
                    max_fours += 1
            count_dups = [sum(1 for g in group if g == 'MIN') for _, group in itertools.groupby(el)]
            for c in count_dups:
                if c == 2:
                    min_twos += 1
                elif c == 3:
                    min_threes += 1
                elif c >= 4:
                    min_fours += 1

        temp = []
        help = 0
        for k, v in copy_state.items():
            while len(v) < self.height:
                v.insert(0, help)
                help += 1
            temp.append(v)
        a = np.array(temp)
        diags = [a[::-1, :].diagonal(i) for i in range(-a.shape[0] + 1, a.shape[1])]
        diags.extend(a.diagonal(i) for i in range(a.shape[1] - 1, -a.shape[0], -1))
        diags = [n.tolist() for n in diags]
        for el in diags:
            count_dups = [sum(1 for g in group if g == 'MAX') for _, group in itertools.groupby(el)]
            for c in count_dups:
                if c == 2:
                    max_twos += 1
                elif c == 3:
                    max_threes += 1
                elif c >= 4:
                    max_fours += 1
            count_dups = [sum(1 for g in group if g == 'MIN') for _, group in itertools.groupby(el)]
            for c in count_dups:
                if c == 2:
                    min_twos += 1
                elif c == 3:
                    min_threes += 1
                elif c >= 4:
                    min_fours += 1
        if max_fours > 0:
            return 1000000
        elif min_fours > 0:
            return -1000000
        else:
            return max_fours * 10 + max_threes * 5 + max_twos * 2 - (min_fours * 10 + min_threes * 5 + min_twos * 2)

    def play(self, player_one, player_two):
        state = self.initial_state
        print("----- THE GAME STARTS! -----\n\n")
        self.draw_board(self.initial_state)
        players = [player_one, player_two]
        moves = []
        while True:
            for player in players:
                if self.terminal_test(state):
                    if self.utility(state) == 1000000:
                        print("MAX WINS! \n\n")
                    elif self.utility(state) == -1000000:
                        print("MIN WINS! \n\n")
                    else:
                        print("IT'S A DRAW! \n\n")
                    print('----- GAME OVER -----\n\n')
                    return moves
                else:
                    print(f'{self.player} plays!')
                move = player.next_move(state)
                state = self.result(state, move)
                self.draw_board(state)
                moves.append((move, self.player))
                self.player = self.next_player()
                print('_____________________')

    def draw_board(self, state):
        # print header
        print('\t', end='')
        for column in range(0, self.width):
            print(column, '\t\t', end='')
        print()
        copy_state = {}
        for k, v in state.items():
            if k != 'to_move':
                copy_state[k] = state[k].copy()

        temp = []
        for k, v in copy_state.items():
            while len(v) < self.height:
                v.insert(0, 0)
            temp.append(v)

        for i in range(0, self.height):
            print(i, end='')
            for j in range(0, self.width):
                if copy_state[j][i] == 0:
                    print('\t{}\t|'.format(self.empty), end=" ")
                else:
                    print('\t{}\t|'.format(copy_state[j][i]), end=" ")
            print()
        print()


class PacmanGame(Game):
    def __init__(self, initial_state=None, player='MAX', board=4):
        self.board = board
        if initial_state is None:
            initial_state = self.init_state()
        super(PacmanGame, self).__init__(initial_state, player)
        self.initial_state = initial_state
        self.player = player
        self.to_eat = len(initial_state['specials'])
        self.min = 'MIN'
        self.max = 'MAX'
        self.empty = '.'
        self.special = '*'
        self.met = 'X'

    def init_state(self):
        temp_specials = list(itertools.permutations(range(self.board-1), 2))
        random.shuffle(temp_specials)
        state = {
            'max_pos': (0, 0),
            'min_pos': (self.board-1, self.board-1),
            'specials': temp_specials[: round(self.board ** 2 / 4)],
            'to_move': 'MAX'
        }

        return state

    def actions(self, state):
        action_list = ['Up', 'Down', 'Right', 'Left']
        if state['to_move'] == 'MAX':
            pos = state['max_pos']
        elif state['to_move'] == 'MIN':
            pos = state['min_pos']
        else:
            raise ValueError

        if pos[0] == 0:
            action_list.remove("Up")
        if pos[0] == self.board - 1:
            action_list.remove("Down")
        if pos[1] == 0:
            action_list.remove("Left")
        if pos[1] == self.board - 1:
            action_list.remove("Right")
        return action_list

    def result(self, state, action):
        if state['to_move'] == 'MAX':
            pos = state['max_pos']
            reached_pos = self.compute_reached_pos(action, pos)
            specials = [sp_pos for sp_pos in state['specials'] if sp_pos != reached_pos]
            reached_state = {
                'max_pos': reached_pos,
                'min_pos': state['min_pos'],
                'specials': specials,
                'to_move': 'MIN'
            }
            return reached_state

        elif state['to_move'] == 'MIN':
            pos = state['min_pos']
            reached_pos = self.compute_reached_pos(action, pos)
            reached_state = {
                'max_pos': state['max_pos'],
                'min_pos': reached_pos,
                'specials': state['specials'],
                'to_move': 'MAX'
            }
            return reached_state
        else:
            raise ValueError

    @staticmethod
    def compute_reached_pos(action, pos):
        if action == 'Up':
            reached_pos = (pos[0] - 1, pos[1])
        if action == 'Down':
            reached_pos = (pos[0] + 1, pos[1])
        if action == 'Left':
            reached_pos = (pos[0], pos[1] - 1)
        if action == 'Right':
            reached_pos = (pos[0], pos[1] + 1)
        return reached_pos

    def terminal_test(self, state):
        if state['max_pos'] == state['min_pos'] or len(state['specials']) == 0:
            return True
        else:
            return False

    def utility(self, state):
        manhattan = abs(state['max_pos'][0] - state['min_pos'][0]) + abs(state['max_pos'][1] - state['min_pos'][1])
        food = self.to_eat - len(state['specials'])
        return manhattan + food

    def play(self, player_one, player_two):
        state = self.initial_state
        print("----- THE GAME STARTS! -----\n\n")
        self.draw_board(self.initial_state)
        players = [player_one, player_two]
        moves = []
        while True:
            for player in players:
                if self.terminal_test(state):
                    print('----- GAME OVER -----\n\n')
                    return moves
                else:
                    print(f'{self.player} plays!')
                move = player.next_move(state)
                state = self.result(state, move)
                self.draw_board(state)
                moves.append((move, self.player))
                self.player = self.next_player()
                print('_____________________')

    def display(self, state):
        print('_____________________')
        if self.player == 'MAX':
            print(self.player, 'in ', state['max_pos'], self.player_utility(state))
        elif self.player == 'MIN':
            print(self.player, 'in ', state['min_pos'], self.player_utility(state))
        else:
            raise ValueError

    def display_move(self, state, move):
        print(self.player, f'--{move}--> ', state)

    def draw_board(self, state):
        # print header
        print('\t', end='')
        for column in range(0, self.board):
            print(column, '\t\t', end='')
        print()

        for i in range(0, self.board):
            print(i, end='')
            for j in range(0, self.board):
                if (i, j) == state['min_pos'] == state['max_pos']:
                    print('\t{}\t|'.format(self.met), end=" ")
                elif (i, j) == state['min_pos']:
                    print('\t{}\t|'.format(self.min), end=" ")
                elif (i, j) == state['max_pos']:
                    print('\t{}\t|'.format(self.max), end=" ")
                elif (i, j) in state['specials']:
                    print('\t{}\t|'.format(self.special), end=" ")

                else:
                    print('\t{}\t|'.format(self.empty), end=" ")
            print()
        print()

import random


class Random:
    def __init__(self, game):
        self.game = game

    def next_move(self, state):
        moves = self.game.actions(state)
        return random.choice(moves)


class Custom:
    def __init__(self, game):
        self.game = game

    def next_move(self, state):
        moves = self.game.actions(state)
        print(moves)
        return input()


class CustomConnectFour(Custom):

    def next_move(self, state):
        moves = self.game.actions(state)
        print(f'Where do you want to insert the disk? The available moves are: {moves}')
        return int(input())


import numpy as np


class Minimax:
    def __init__(self, game):
        self.game = game

    def max_value(self, state):
        if self.game.terminal_test(state):
            return self.game.player_utility(state)
        values = [self.min_value(s) for s, a in self.game.successors(state)]
        return max(values)

    def min_value(self, state):
        if self.game.terminal_test(state):
            return self.game.player_utility(state)
        values = [self.max_value(s) for s, a in self.game.successors(state)]
        return min(values)

    def next_move(self, state):
        moves = self.game.actions(state)
        for move in moves:
            print(move, self.min_value(self.game.result(state, move)))
        return max(moves, key=lambda move: self.min_value(self.game.result(state, move)))


class AlphaBeta:

    def __init__(self, game):
        self.game = game

    def max_value(self, state, alpha, beta):
        if self.game.terminal_test(state):
            return self.game.player_utility(state)

        best_value = -np.inf
        for s, a in self.game.successors(state):
            value = self.min_value(s, alpha, beta)
            best_value = max(best_value, value)
            if best_value > beta:
                return best_value
            alpha = max(alpha, best_value)
        return best_value

    def min_value(self, state, alpha, beta):
        if self.game.terminal_test(state):
            return self.game.player_utility(state)

        best_value = np.inf
        for s, a in self.game.successors(state):
            value = self.max_value(s, alpha, beta)
            best_value = min(best_value, value)
            if best_value < alpha:
                return best_value
            beta = min(beta, best_value)
        return best_value

    def next_move(self, state):
        alpha = -np.inf
        beta = np.inf

        best_move = None

        for s, move in self.game.successors(state):
            value = self.min_value(s, alpha, beta)
            if value > alpha:
                alpha = value
                best_move = move
        return best_move


class LimitedAlphaBeta:

    def __init__(self, game, limit=1000000000):
        self.game = game
        self.limit = limit

    def max_value(self, state, alpha, beta, limit):
        if self.game.terminal_test(state) or limit == 0:
            return self.game.player_utility(state)
        best_value = -np.inf
        for s, a in self.game.successors(state):
            value = self.min_value(s, alpha, beta, limit-1)
            best_value = max(best_value, value)
            # beta test (if MAX choice will never be the choice of MIN, stop searching)
            if best_value > beta:
                return best_value
            # update the best value for MAX
            alpha = max(alpha, best_value)
        return best_value

    def min_value(self, state, alpha, beta, limit):
        if self.game.terminal_test(state) or limit == 0:
            return self.game.player_utility(state)
        best_value = np.inf
        for s, a in self.game.successors(state):
            value = self.max_value(s, alpha, beta, limit-1)
            best_value = min(best_value, value)
            if best_value < alpha:
                return best_value
            beta = min(beta, best_value)
        return best_value

    def next_move(self, state):
        alpha = -np.inf
        beta = np.inf

        best_move = None

        for s, move in self.game.successors(state):
            value = self.min_value(s, alpha, beta, self.limit)
            if value > alpha:
                # update the best value for MAX
                alpha = value
                best_move = move
        return best_move


class LimitedMinimax:
    def __init__(self, game, limit=100000000):
        self.game = game
        self.limit = limit

    def max_value(self, state, limit):
        if self.game.terminal_test(state) or limit == 0:
            return self.game.player_utility(state)
        values = [self.min_value(s, limit - 1) for s, a in self.game.successors(state)]
        return max(values)

    def min_value(self, state, limit):
        if self.game.terminal_test(state) or limit == 0:
            return self.game.player_utility(state)
        values = [self.max_value(s, limit - 1) for s, a in self.game.successors(state)]
        return min(values)

    def next_move(self, state):
        moves = self.game.actions(state)
        return max(moves, key=lambda move: self.min_value(self.game.result(state, move), self.limit))


# AUSTRALIA

problem = MapColors()
initial_state = {}

search = BackTracking(problem=problem,
                      var_criterion=random_variable,
                      value_criterion=random_assignment)

print(f'{search}, Random strategies')
print(search.run(initial_state))

search = BackTracking(problem=problem,
                      var_criterion=minimum_remaining_values,
                      value_criterion=least_constraining_value)

print(f'{search}, Minimum Remaining Values, Least Constraining Value')
print(search.run(initial_state))

search = BackTracking(problem=problem,
                      var_criterion=degree_heuristic,
                      value_criterion=least_constraining_value)

print(f'{search},Degree Heuristic, Least Constraining Value')
print(search.run(initial_state))

print(f'{search},Forward Checking, Degree Heuristic, Least Constraining Value')
print(search.run_with_forward_checking(initial_state, problem.domains))



# TIC TAC TOE


game = TicTacToe()
first_player = LimitedMinimax(game=game, limit=3)
second_player = LimitedMinimax(game=game, limit=3)
moves = game.play(first_player, second_player)

print(moves)



# STREETS

initial_state = 'Andria'
goal_state = 'Bari'
map_problem = StreetProblem(environment=map,
                      initial_state=initial_state,
                      goal_state=goal_state)
strategies = [AStar(map_problem), Greedy(map_problem), Random(), BreadthFirst(), DepthLimitedSearch(limit=5), UniformCost()]

for strategy in strategies:
    search = TreeSearch(problem=map_problem, strategy=strategy)
    result, node = search.run()
    print(f'{strategy}, {search}')
    print(result)
    try:
        print(node.path())
        print(node.cost)
    except AttributeError:
        pass

print("---------")

strategies = [AStar(map_problem), Greedy(map_problem), Random(), BreadthFirst(), DepthFirst(), DepthLimitedSearch(limit=5), UniformCost()]
for strategy in strategies:
    search = GraphSearch(problem=map_problem, strategy=strategy)
    result, node = search.run()
    print(f'{strategy}, {search}')
    print(result)
    try:
        print(node.path())
        print(node.cost)
    except AttributeError:
        pass



# QUEENS



problem = EightQueensProblem()
search = HillClimbing(problem=problem)
result, state = search.run()
print(search)
print(result)
print(problem.value(state))
print(state)
problem.print_chess(state)
search = SimulatedAnnealing(problem=problem, max_time=1000, lam=0.01)
result, state = search.run()
print(search)
print(result)
print(problem.value(state))
print(state)
problem.print_chess(state)
search = Genetic(problem=problem, population=50, generations=100, p_mutation=0.1, gene_pool=list(range(8)))
result, state = search.run()
print(search)
print(result)
print(problem.value(state))
print(state)
problem.print_chess(state)


"""
member2(E, [E|_]).
member2(X, [_|T]):-member2(X, T).

copy([], []).
copy([H|T1],[H|T2]):-copy(T1,T2).

append2([],X,X).
append2([H|T1],X,[H|T2]):-append2(T1, X, T2).

breaks_out([]).
breaks_out([H|T]):-assertz(stuff(H)),breaks_out(T).

putf(List,E,NewList):-NewList=[E|List].

putl([],E,[E]).
putl([H|T1], E, [H|T2]):-putl(T1, E, T2).

remove(E, [E|T], T).
remove(E, [H|T1], [H|T2]):-remove(E, T1, T2),!.

remove_all(_, [], []):-!.
remove_all(E, [E|T], L):-!,remove_all(E, T, L).
remove_all(E, [H|T1], [H|T2]):-remove_all(E, T1, T2).

succ(E, [E|[TH, _]], TH).
succ(E, [_|T], S):-succ(E, T, S).

split(E, [E|T], [E], T).
split(E, [H|T1], [H|T2], L):-split(E, T1, T2, L).

sum(0, []).
sum(Sum, [H|T]):-sum(S,T),Sum is S+H.

count(0, []).
count(Count, [_|T]):-count(C,T),Count is C+1.

all_equals([H|T]):-equals(H, T).
equals(_, []):-!.
equals(E, [E|T]):-equals(E, T).

all_different([]).
all_different([H|T]):-different(H,T),all_different(T).
different(_, []):-!.
different(E, [H,T]):-not(E=H),different(E,T).

last([E], E):-!.
last([_|T], E):-last(T, E).

min(_, []):-!.
min(E, [H|T]):-E<H,min(E, T).

findMin([H|T], H):-min(H, T).
findMin([H|T], Min):-not(min(H,T)),findMin(T, Min),!.

sort2([], []).
sort2(SourceList, [Min|T]):-findMin(SourceList, Min),remove(Min, SourceList, NewList),sort2(NewList, T),!.

mirror([], []).
mirror(List1, [H|T]):-last(List1, H),remove(H,List1,NewList),mirror(NewList,T),!.

index([E|_], E, 1).
index([_|T], E, Index):-index(T, E, Ind),Index is Ind + 1,!.

count_common_elements([], _, 0):-!.
count_common_elements([H|T], List2, Count) :-
    member(H, List2), 
    !,
    count_common_elements(T, List2, RestCount),
    Count is RestCount + 1.
count_common_elements([H|T], List2, Count) :-
    not(member(H, List2)),
    !,
    count_common_elements(T, List2, Count).
"""





# PACMAN

game = PacmanGame(board=5)
first_player = LimitedAlphaBeta(game=game, limit=10)
second_player = LimitedAlphaBeta(game=game, limit=10)
moves = game.play(first_player, second_player)
print(moves)


# MAZE


def print_grid(height, width, p_walls, initial_state, goal_state, path):
    help_list = [initial_state]
    for el in path:
        if el == 'right':
            help_list.append((help_list[-1][0], help_list[-1][1] + 1))
        elif el == 'left':
            help_list.append((help_list[-1][0], help_list[-1][1] - 1))
        elif el == 'up':
            help_list.append((help_list[-1][0] - 1, help_list[-1][1]))
        elif el == 'down':
            help_list.append((help_list[-1][0] + 1, help_list[-1][1]))
    grid = ''
    for k in range(width):
        grid = grid + ' ---'
    grid = grid + '\n'
    for j in range(height):
        grid = grid + '|'
        for k in range(width):
            if (j, k) == initial_state:
                grid = grid + ' i |'
            elif (j, k) == goal_state:
                grid = grid + ' g |'
            elif (j, k) in p_walls:
                grid = grid + ' o |'
            elif (j, k) in help_list:
                grid = grid + ' * |'
            else:
                grid = grid + '   |'
        grid = grid + '\n'
    for k in range(width):
        grid = grid + ' ---'
    grid = grid + '\n'
    print(grid)


height = 3
width = 4
n_walls = 2
p_walls = [(2, 0), (2, 2)]
maze = Maze(height, width, n_walls, p_walls)
print(maze.create_environment())
initial_state = (0, 0)
goal_state = (2, 3)
maze_problem = MazeProblem(environment=maze,
                           initial_state=initial_state,
                           goal_state=goal_state)
strategies = [AStar(maze_problem), Greedy(maze_problem), Random(), BreadthFirst(), DepthLimitedSearch(limit=3), UniformCost()]
for strategy in strategies:
    search = TreeSearch(problem=maze_problem, strategy=strategy)
    result, node = search.run()
    print(f'{strategy}, {search}')
    print(result)
    try:
        print(node.path())
        print(node.cost)
        print_grid(height, width, p_walls, initial_state, goal_state, node.path())
    except AttributeError:
        pass

print("---------")

strategies = [AStar(maze_problem), Greedy(maze_problem), Random(), BreadthFirst(), DepthFirst(), DepthLimitedSearch(limit=6), UniformCost()]

for strategy in strategies:
    search = GraphSearch(problem=maze_problem, strategy=strategy)
    result, node = search.run()
    print(f'{strategy}, {search}')
    print(result)
    try:
        print(node.path())
        print(node.cost)
        print_grid(height, width, p_walls, initial_state, goal_state, node.path())
    except AttributeError:
        pass



# HANOI

problem = HanoiTower(n=3)

strategies = [AStar(problem), DepthFirst()]

for strategy in strategies:
    search = GraphSearch(problem=problem, strategy=strategy)
    result, node = search.run()
    print(f'{strategy}, {search}')
    print(result)
    try:
        print(node.path())
        print(node.cost)
    except AttributeError:
        pass

print("---------")


# GAME



game = DummyGame()
first_player = Minimax(game=game)
second_player = Minimax(game=game)

state = game.initial_state
moves = game.play(first_player, second_player)

game = DummyGame()
first_player = AlphaBeta(game=game)
second_player = AlphaBeta(game=game)

state = game.initial_state
moves = game.play(first_player, second_player)

print(moves)


# CONTAINER


problem = Containers()
initial_state = {}

search = BackTracking(problem=problem,
                      var_criterion=random_variable,
                      value_criterion=random_assignment)

print(f'{search}, Random strategies')
print(search.run(initial_state))

search = BackTracking(problem=problem,
                      var_criterion=minimum_remaining_values,
                      value_criterion=least_constraining_value)

print(f'{search}, Minimum Remaining Values, Least Constraining Value')
print(search.run(initial_state))

search = BackTracking(problem=problem,
                      var_criterion=degree_heuristic,
                      value_criterion=least_constraining_value)

print(f'{search},Degree Heuristic, Least Constraining Value')
print(search.run(initial_state))

print(f'{search},Forward Checking, Degree Heuristic, Least Constraining Value')
print(search.run_with_forward_checking(initial_state, problem.domains))



# CONNECT FOUR

game = ConnectFour()
first_player = LimitedAlphaBeta(game=game, limit=3)
second_player = LimitedAlphaBeta(game=game, limit=3)
moves = game.play(first_player, second_player)

print(moves)


# AC£


problem = MapColors()
initial_state = {}
# Example 1
print('Example 1')
problem = CSP(variables=problem.variables,
              domains=problem.domains,
              constraints=problem.constraints)
state = problem.initial_state
optimizer = AC3(csp=problem)
optimizer.run(state)
print(problem.domains)

# Example 2
print('Example 2')
problem = CSP(variables=problem.variables,
              domains=problem.domains,
              constraints=problem.constraints)
act_state = {'WA': 'red', 'Q': 'green'}
problem.domains['WA'] = ['red']
problem.domains['Q'] = ['green']
optimizer = AC3(csp=problem)
optimizer.run(state)
print(problem.domains)

