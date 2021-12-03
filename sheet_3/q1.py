from KRLib.aima import logic,utils
from sheet_3.KRLib.aima.utils import expr

claus=list()
#(1) color(carrots, orange).
#EN: carrots color is orange.
claus.append(expr("carrots(c) ==> color(c,orange)"))
#(2) likes(Person, carrots):-vegetarian(Person).
#EN: Vegetarians likes carrots
claus.append(expr("vegetarian(p) & carrots(c) ==> likes(p,c)")) 
#(3) pass(Student) :- study_hard(Student).
#EN: If student study hard he will pass.
claus.append(expr("student(s) & study_hard(s) ==> pass(s)"))
#(4) ?- pass(Who).
#EN: Who pass.

#(5) ?- teaches(professor, Course).
#EN: professor teaches course.
claus.append(expr("professor(p) ==> teaches(p,course)"))
#(6) enemies(X, Y) :- hates(X, Y), fights(X, Y).
#En: if someone hate and fitght someone else then they are enemies.
claus.append(expr("hates(x,y) & fights(x,y) ==> enemies(x,y)"))