#!/usr/bin/env python3

import gurobipy as g  # import Gurobi module
import sys

# model -----------------------------------------------------
m = g.Model()

# - add variables
x = m.addVars(2, vtype=g.GRB.INTEGER, lb=0, name="x")

# - add constraints
m.addConstr(x[0] + x[1] <= 3)
m.addConstr(-2*x[0] + 2*x[1] <= 1)

# - set objective
m.setObjective(x[0] + 2*x[1], g.GRB.MAXIMIZE)

# call the solver -------------------------------------------
m.optimize()

m.write('model.lp')

# print the solution ----------------------------------------
print(int(m.objVal))
print(int(round(x[0].x)))
print(int(round(x[1].x)))
