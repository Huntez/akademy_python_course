class WorkList:
    def __init__(self, slist):
        self.slist = slist

    def add_to_list(self, element):
        self.slist.append(element)
        return "Element added!"
    
    def remove_from_list(self, element):
        if element in self.slist:
            self.slist.remove(element)
            return "Element removed!"
        else:
            return "List dont have this element!"
    
    def show_list(self):
        return f"{self.slist}"

    def count_list(self):
        return f"Len : {len(self.slist)}"

    def empty_or_not(self):
        if self.slist == []:
            return True
        else:
            return False
    
    def clear_list(self):
        self.list = []
        return "List cleared!"

    def check_element(self, element):
        if element in self.slist:
            return True
        else:
            return False

    def replace_element(self, ritem, element):
        if ritem in self.slist:
            self.slist[self.slist.index(ritem)] = element
            return "Okay!"
        else:
            return "Error"

    def priority_insert(self, element):
        self.slist.insert(0, element)
        return "Element added on high priority!"

    def delete_priority_element(self):
        self.slist.pop(0)
        return "Element deleted!"
    
    def show_with_priority(self):
        return f"{[i for i in range(10)]}"


enter = int(input("1, 2, 3 : "))
if enter == 1:
    worklist = WorkList(slist=list(map(int, input(": ").split())))
elif enter == 2:
    worklist = WorkList(slist=list(map(str, input(": ").split())))
elif enter == 3:
    worklist = WorkList(slist=["word", "sword", "tword"])

while True:
    enter = int(input("1 - a, 2 - d, 3 - s, 4 - c, 5 - ch "))
    if enter == 1:
        print(worklist.add_to_list(input("Element to add : ")))
    elif enter == 2:
        print(worklist.remove_from_list(input("Element to remove : ")))
    elif enter == 3:
        print(worklist.show_list())
    elif enter == 4:
        print(worklist.check_element(input("Element to check : ")))
    elif enter == 5:
        print(worklist.replace_element(input("Element to replace : "), 
        input("Element : ")))

