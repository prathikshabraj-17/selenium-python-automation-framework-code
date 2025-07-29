# Mode
# read mode = r
# write mode = w
# append mode = a
# Read/write+ = r+
# from typing import TextIO
#
# f = open("C:\\python selenium\\LearningPython\\pythonProject\\FILEIODemo\\writedemo1.word", "w")
# from typing import TextIO
#
# f = open("C:\\python selenium\\LearningPython\\pythonProject\\FILEIODemo\\writedemo1.txt", "w")
# f1 = open("C:\\python selenium\\LearningPython\\pythonProject\\FILEIODemo\\writedemo2.txt", "w")
# f.write("First line code")
# f1.write("Second line code")
# f.close()

# f: TextIO = open("C:\\python selenium\\LearningPython\\pythonProject\\FILEIODemo\\writedemo1 .txt", "w")
# l = [65,78,86,97]
# for items in l:
#     f.write(str(items)+"\n")
# f.close()


# Open file in append mode (adds content to the end)
file = open("myfile.txt", "a")

file.write("What it does:Opens the file example.txt in read mode. Reads the entire content as one string.Closes the file automatically (because of with)..\n")

file.close()


# write file using try
#
try:
   with open("writedemo2.txt", "w") as f:
    print(f.write("line"))
except FileExistsError:
   print("file not found")
#
#
#
# #Write multiple lines using writelines()
lines = ["Line 1: Python\n", "Line 2: File writing\n", "Line 3: Done!\n"]

with open("write_demo.txt", "w") as f:
    f.writelines(lines)

lines = ["Line 1: Prathiksha\n" , "Line 2: Software test engineer\n" , "Line 3: 27\n"]
with open("write_demo.txt", "w") as f:
       f.writelines(lines)
#
# #Append text to an existing file
#
with open("write_demo.txt", "a") as f:
    f.write("Line 4: Eoxvantage")

#Write using a loop

numbers = [1, 2, 3, 4, 5]

with open("write_demo.txt", "w") as f:
    for num in numbers:
        f.write(f"Number: {num}\n")

#Writing Squares of Numbers

with open("squares.txt", "w") as f:
    for i in range(1, 6):
        f.write(f"{i} squared is {i**2}\n")

with open("squares1.txt", "w") as f:
    for i in range(1,5):
        f.write(f"{i} squared is {i**2}\n")

#Writing Names from a List
names = ["Alice", "Bob", "Charlie", "David"]

with open("names.txt", "w") as f:
    for name in names:
        f.write(name + "\n")




