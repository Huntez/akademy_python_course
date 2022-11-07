import os.path

list = ["First line", "Second line", "Third line", "Fourth line"]
file2 = open(os.path.join("lesson13", "text.txt"), "w")

print(list)
for i in range(len(list)):
    file2.write(list[i] + "\n")

file2.close()

# Second

file2 = open(os.path.join("lesson13", "text.txt"), "r")
count = 0; line = file2.read(); line.replace("\n", "")

for i in line:
    count += 1
print("Symbols count :", count)

file2.close()

# Third

file2 = open(os.path.join("lesson13", "text.txt"), "r")
count = 0

for i in file2:
    count += 1

print("Strings count :", count)

file2.close()

