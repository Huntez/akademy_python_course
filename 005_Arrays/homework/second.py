from random import randint

nlist = [randint(-10, 10) for a in range(5)]
slist = [randint(-10, 10) for a in range(5)]
frlist, thlist, splist, flist = [], [], [], []

for a in nlist + slist:
    if a not in flist:
        flist.append(a)

for a in nlist + slist:
    if a in nlist and a in slist and a not in splist:
        splist.append(a)

for a in nlist:
    if a not in slist:
        thlist.append(a)

for a in slist:
    if a not in nlist:
        frlist.append(a)

print("Flist :", nlist, "\nSlist :", slist)
print("f + s list : ", nlist + slist)
print("Without repeat :", flist, "\nRepeat :", splist)
print("Min flist :", min(flist), "Max flist :", max(flist))
print("Max slist :", min(slist), "Max flist :", max(slist))
print("Unique flist :", thlist, "\nUnique nslist :", frlist)
