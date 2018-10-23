from pyomo.environ import *
import pyomo.environ as pyo
#import numpy as np
from pyomo import *
#from coopr.pyomo import Constraint

#Parameters

R_max = 5
R_min = 0
n =1
vh = 10
Pmax = 4
G=2
D=4
Pm=7
a0=0


#Modell
model = ConcreteModel()


#Parameters
model.R_max = R_max
model.R_min = R_min
model.n = n
model.vh = vh
model.Pmax = Pmax
model.G = G
model.D = D
model.Pm = Pm
model.a0 =a0

#Variables
model.xbh = Var(initialize=1, bounds=(1,2))
model.xbm = Var(initialize=1, bounds=(1,2))
model.xmb = Var(initialize=1, bounds=(1,2))
model.xmh = Var(initialize=1, bounds=(1,2))


#Constraints
model.constraints = ConstraintList()
model.constraints.add( model.xmb + model.G <= model.Pmax )
model.constraints.add( model.xbh + model.xbm >= model.Pmax )
model.constraints.add( model.a0 + model.xmb + model.G - model.xbh - model.xbm <= model.R_max )
model.constraints.add( model.a0 + model.xmb + model.G - model.xbh - model.xbm >= model.R_min )
model.constraints.add( model.xbh + model.xmh <= model.D )


#Objective

model.value = Objective(
            expr= (model.Pm*(model.xbm - model.xmb - model.xmh)) - model.vh*(model.D - model.xbh - model.xmh),
            sense = maximize)

opt = SolverFactory("gurobi")

#Record results for each battery state
#for i in range (0,4):

results = opt.solve(model)
stage_results = [[]]
stage_results[0]
optimal_x = [pyo.value(model.xbh),pyo.value(model.xbm),pyo.value(model.xmb),pyo.value(model.xmh)]
optimal_value= round(results.get('Problem').get('Upper bound').value, 4)


#print(results.get(xbh))
# Write the output
#results.write(num=1)


print(optimal_x)


print(optimal_value)
#print("stop\n\n\n")
#print(model.pprint())
