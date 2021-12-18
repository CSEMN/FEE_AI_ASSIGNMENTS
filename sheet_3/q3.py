from KRLib.aima import logic,utils
from sheet_3.KRLib.aima.utils import expr

claus=list()

# (1) hates(X,Y), hates(Y,X) :- enemies(X, Y)
claus.append(expr("hates(x,y) & hates(y,x) ==> enemies(x,y)"))
# (2) p(X):-(q(X):-r(X))
claus.append(expr("q(x) ==> r(x)"))
claus.append(expr("p(x) ==> q(x)"))