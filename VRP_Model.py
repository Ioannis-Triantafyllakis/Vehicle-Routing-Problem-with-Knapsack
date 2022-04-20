import random
import math


class Model:

    def __init__(self):
        self.allNodes = []
        self.customers = []
        self.matrix = []
        self.capacity = -1

    def BuildModel(self):
        depot = Node(0, 50, 50, 0, 0) 
        self.allNodes.append(depot)
        birthday = 421997 #
        random.seed(birthday)
        self.capacity = 150
        totalCustomers = 300

        for i in range (0, totalCustomers):
            x = random.randint(0, 100)
            y = random.randint(0, 100)
            service_time = random.randint(5, 10)
            profit = random.randint(5, 20)
            cust = Node(i + 1, x, y, service_time, profit)
            self.allNodes.append(cust)
            self.customers.append(cust)

        rows = len(self.allNodes)   # 300
        self.matrix = [[0.0 for x in range(rows)] for y in range(rows)]  # Here we initialize the matrix

        for i in range(0, len(self.allNodes)):
            for j in range(0, len(self.allNodes)):
                a = self.allNodes[i]
                b = self.allNodes[j]
                dist = math.sqrt(math.pow(a.x - b.x, 2) + math.pow(a.y - b.y, 2))
                self.matrix[i][j] = dist    # Here we fill the matrix

class Node:
    def __init__(self, idd, xx, yy, dem, prof):
        self.x = xx
        self.y = yy
        self.ID = idd
        self.service_time = dem
        self.profit = prof
        self.isRouted = False

class Route:
    def __init__(self, dp, cap):
        self.sequenceOfNodes = []
        self.sequenceOfNodes.append(dp) # Here we append the depot (as a starting point)
        self.sequenceOfNodes.append(dp) # Here we append it again as the last point of the route (because routes are closed)
        self.cost = 0
        self.capacity = cap
        self.load = 0
        self.prof = 0
        self.service_time = 0