from logic2 import *


jia=Symbol("Jia")
jhon=Symbol("Jhon")
travel=Symbol("travel")
traveler=Symbol("traveler")
healthy=Symbol("healthy")
wealthy=Symbol("wealthy")
man=Symbol('man')
woman=Symbol('woman')

KB=And(
    Implication(jia,woman),
    Implication(jhon,man),
    Implication(jhon,healthy),
    Implication(jia,healthy),
    Implication(jhon,wealthy),
    Implication(traveler,And(healthy,wealthy)),
    Implication(travel,traveler),
)
print(model_check(KB,And(healthy,wealthy)))
print(KB.formula())
