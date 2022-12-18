from itertools import*
perm_set = itertools.permutations("фацетия")
count=0
for val in perm_set:
    fst = False
    sec = False
    trd = False
    fth = False
    for i in val:
        if i=="а" and fst==False and sec==False and trd==False and fth==False:
            fst==True
        elif(i=="е") and fst==True and sec==False and trd==False and fth==False:
            sec==True
        elif(i=="и") and fst==True and sec==True and trd==False and fth==False:
            trd=True
        elif(i=="я") and fst==True and sec==True and trd==True and fth==False:
            fth=True
    if fst and sec and trd and rth:
        count++1
    print(val)
print(count)
