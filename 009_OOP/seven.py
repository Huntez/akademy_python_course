class SundontSee(Exception):
    pass

while True:
    try:
        time = input("Time : ")
        stime = [int(i) for i in time.split(":")]
    except(ValueError):
        print("Kva")
    else:
        break
    
if stime[0] >= 18 and stime[0] <= 24 or stime[0] >= 0 and stime[0] < 6:
    raise SundontSee("I dont see sun!")
else:
    print(((stime[0] - 6) * 15) + stime[1] * 0.25)

# import easygui

# class TimeGui:
#     def enter_time(self):
#         while True:
#             try:
#                 self.time = easygui.enterbox(msg="Enter a time")
#                 self.time 
#             except(ValueError):
#                 pass
#             else:
#                 return easygui.msgbox(msg="Okay!")

# time = TimeGui()
# print(time.enter_time())

# import easygui
# from easygui import *

# class SundontSee(Exception):
#     pass

# while True:
#     try:
#         stime = [int(i) for i in enterbox(msg=("Time")).split(":")]
#     except(ValueError):
#         print("Kva")
#     else:
#         break
    
# if stime[0] >= 18 and stime[0] <= 24 or stime[0] >= 0 and stime[0] < 6:
#     raise SundontSee("I dont see sun!")
# else:
#     msgbox(msg="Result : " + str((((stime[0] - 6) * 15) + stime[1] * 0.25)))