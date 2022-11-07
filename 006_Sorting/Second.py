# list = [5,7,4,3,8,2]
# for i in range(len(list) - 2):
#     for j in range(len(list) - 1 - i):
#         if list[j] > list[j+1]:
#             list[j], list[j+1] = list[j+1], list[j]

# print(list)

# list = [5,7,4,3,8,2]

# for i in range(1, len(list)):
#     item = list[i]
#     j = i
#     while j - 1 >= 0 and list[j - 1] > item:
#         list[j], list[j - 1] = list[j - 1], list[j]
#         j -= 1
#     list[j] = item

# print(list)

# list = [5,7,4,3,8,2]
# flist = list[:int(len(list)/2)]
# slist = list[int(len(list)/2):]

# for i in range(len(flist) - 2):
#     for j in range(len(flist) - 1 - i):
#         if flist[j] > flist[j+1]:
#             flist[j], flist[j+1] = flist[j+1], flist[j]
# for i in range(len(slist) - 2):
#     for j in range(len(slist) - 1 - i):
#         if slist[j] < slist[j+1]:
#             slist[j], slist[j+1] = slist[j+1], slist[j]

# print("Upper :", flist, "Lower :", slist)

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

alist = [54,26,93,17,77,31,44,55,20]; print(alist)
mergeSort(alist)
print(alist)