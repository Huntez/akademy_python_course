#!/usr/bin/env python3
# from random import randint

# fcort = tuple([randint(1,20) for i in range(10)])
# scort = tuple([randint(1,20) for i in range(10)])
# tcort = tuple([randint(1,20) for i in range(10)])
# ccort = set()

# for a in fcort:
#     if a in scort and a in tcort:
#         ccort.add(a)


# ccort = tuple(ccort)
# print(fcort)
# print(scort)
# print(tcort)
# print("Result :", ccort)


# Second

from random import randint

fcort = tuple([randint(1,20) for i in range(10)])
scort = tuple([randint(1,20) for i in range(10)])
tcort = tuple([randint(1,20) for i in range(10)])

fccort, sccort, tccort = set(), set(), set()

for a in fcort:
    if a not in scort and a not in tcort:
        fccort.add(a)
for a in scort:
    if a not in fcort and a not in tcort:
        sccort.add(a)
for a in tcort:
    if a not in fcort and a not in scort:
        tccort.add(a)

fccort, sccort, tccort = tuple(fccort), tuple(sccort), tuple(tccort)

print(fcort, "\n", scort, "\n", tcort)
print("F unique :", fccort, "\nS unique :", sccort, "\nT unique :", tccort)

# Third

from random import randint

fcort = (1,2,3,4,5)
scort = (1,2,3,4,5)
tcort = (1,3,2,4,5)
ccort = set()

for a in fcort:
    if a in scort and a in tcort and fcort.index(a) == scort.index(a) and fcort.index(a) == tcort.index(a):
        ccort.add(a)


ccort = tuple(ccort)
print(fcort)
print(scort)
print(tcort)
print("Result :", ccort)
