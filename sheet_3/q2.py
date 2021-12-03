from KRLib.aima import logic,utils
from sheet_3.KRLib.aima.utils import expr

claus=list()

#(1) Maria reads logic programming book by author peter lucas.
claus.append(expr("author(peter lucas,logic progamming book) & read(Maria,logic programming book)"))
#(2) Anyone likes shopping if she is a girl.
claus.append(expr("girl(g) ==> likes(g,Shopping)"))
#(3) Who likes shopping?
#(4) kirke hates any city if it is big and crowdy
claus.append(expr("city(c) & big(c) & crowdy(c) ==> hates(Kirke,c)"))