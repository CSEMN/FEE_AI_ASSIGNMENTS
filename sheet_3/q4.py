from aima import logic
from aima.utils import expr

claus=list()
# (1) jia is a woman.
claus.append(expr("woman(jia)"))
# (2) john is a man.
claus.append(expr("man(jhon)"))
# (3) john is healthy.
claus.append(expr("healthy(jhon)"))
# (4) jia is healthy.
claus.append(expr("healthy(jia)"))
# (5) john is wealthy.
claus.append(expr("wealthy(jhon)"))
# (6) anyone is a traveler if he is healthy and wealthy.
claus.append(expr("healthy(x) & wealthy(x) ==> traveler(x)"))
# (7) anyone can travel if he is a traveler
claus.append(expr("traveler(y) ==> canTravel(y)"))

#create Knowledge base (KB) from previous clauses.
KB=logic.FolKB(claus)
answer1=logic.fol_fc_ask(KB,expr("canTravel(y)"))
answer2=logic.fol_fc_ask(KB,expr("healthy(x) & wealthy(x)"))

print("who can travel ? : ",list(answer1))
print("who is healthy and wealthy ? : ",list(answer2))