from pyomo.environ import*
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

gygg

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
results = opt.solve(model)


print("stop\n\n\n")
print(round(results.get('Problem').get('Upper bound').value, 4))
print("stop\n\n\n")
print(model.pprint())
