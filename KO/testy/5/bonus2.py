#!/usr/bin/env python3

import gurobipy as g  # import Gurobi module
import sys

# data ------------------------------------------------------
price = [5, 7, 4, 3, 4, 6]
gain = [16, 22, 12, 8, 11, 19]
R = 12
# model -----------------------------------------------------
m = g.Model()

# - add variables
x = m.addVars(6, vtype=g.GRB.INTEGER, lb=0, name="x")

# - add constraints
m.addConstr(g.quicksum(x[i]*price[i] for i in range(6)) <= R)
for i in range(5):
    m.addConstr(x[i] <= 1)
m.addConstr(x[5] <= 10)
m.addConstr(x[1] + x[2] <= x[3] + 1)


# - set objective
m.setObjective(g.quicksum(x[i]*gain[i] for i in range(6)), g.GRB.MAXIMIZE)

# call the solver -------------------------------------------
m.optimize()

m.write('model.lp')

# print the solution ----------------------------------------
print(int(m.objVal))
for i in range(6):
    print(int(round(x[i].x)))
