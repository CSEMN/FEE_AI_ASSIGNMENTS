from aima import logic
from aima.utils import expr

claus=list()
# vegetarian(jose).  
claus.append(expr("vegetarian(jose)"))
#   vegetarian(james). 
claus.append(expr("vegetarian(james)")) 
#   vegetable(carrot).  
claus.append(expr("vegetable(carrot)"))
#   vegetable(egg_plant).  
claus.append(expr("vegetable(egg_plant)"))
#   likes(jose, X) :- vegetable(X).  
claus.append(expr("vegetable(x) ==> likes(jose,x)"))
#   loves(Who, egg_plant) :- vegetarian(Who).
claus.append(expr("vegetarian(who) ==> loves(who,egg_plant)"))

KB=logic.FolKB(claus)

# Queries :
#   ?- vegetable(X).
answer=logic.fol_fc_ask(KB,expr("vegetable(x)"))
print("vegetable(X) : ",list(answer))
#   ?- vegetable(potato).
answer=logic.fol_fc_ask(KB,expr("vegetable(potato)"))
print("vegetable(potato) : ",list(answer))
#   ?- vegetarian(_).
answer=logic.fol_fc_ask(KB,expr("vegetarian(v)"))
print("vegetarian(v) : ",list(answer))
#   ?- likes(jose, What).
answer=logic.fol_fc_ask(KB,expr("likes(jose,v)"))
print("likes(jose, What) : ",list(answer))
#   ?- likes(Who, egg_plant).
answer=logic.fol_fc_ask(KB,expr("likes(x, egg_plant)"))
print("likes(Who, egg_plant) : ",list(answer))
#   ?- loves(Who, egg_plant).
answer=logic.fol_fc_ask(KB,expr("loves(y, egg_plant)"))
print("loves(Who, egg_plant). : ",list(answer))