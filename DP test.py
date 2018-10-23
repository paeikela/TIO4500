from pyomo.environ import *
import pyomo.environ as pyo
import numpy as np
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

stage_results = opt.solve(model)

optimal_x = [pyo.value(model.xbh),pyo.value(model.xbm),pyo.value(model.xmb),pyo.value(model.xmh)]
optimal_value= round(stage_results.get('Problem').get('Upper bound').value, 4)

a = np.array([[optimal_x,optimal_value],0])
print(a)
b = np.append(a,a)
print(b)

#Få ut første element i x-vektor for første state i første steg
print(b[0])
#print(b[0][0])
#print(b[0][1])
"""
#La results i en numpy matrise
state_results = np.array([optimal_x,optimal_value])
print(state_results)
state_results2 = np.array([optimal_x,optimal_value])
#Utvider matrisen med flere results
results = np.append(state_results,np.array([optimal_x,optimal_value]),axis=0)
print(results)

#TODO: Legge til funksjonsverdi og optimal vektor for hver state i en 5X1-numpy array
#TODO: Kjøre forløkke for hver state og legge verdiene i numpy array

a= np.array(state_results,state_results2)
print(a)

total_results = np.array(([]))
print(results[0])
print(results[1])
print(results[2])
print(results[3])
"""


#print(results.get(xbh))
# Write the output
#results.write(num=1)


#print(optimal_x)


#print(optimal_value)
#print("stop\n\n\n")
#print(model.pprint())

