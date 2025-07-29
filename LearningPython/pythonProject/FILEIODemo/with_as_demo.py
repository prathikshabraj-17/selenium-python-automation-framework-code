fw = open("demofile.txt", "w")
fw.write("1st line")
fw.close()

fr = open("demofile.txt", "r")
print(fr.read())
fr.close()

# with open("demofile.txt", "w")as fw:
#     fw.write("This line is from with operation")
#
# with open("demofile.txt", "r")as fr:
#     print(fr.read())

# Read line by line using readline()


# with open("writedemo1.txt", "r") as f:
#     line1 = f.readline()
#     line2 = f.readline()
#     print("First Line:", line1.strip())
#     print("Second Line:", line2.strip())


# Read all lines using a loop
# with open("writedemo2.txt", "r") as f:
#     for line in f:
#         print(line.strip())

# Read all lines into a list
#
# with open("writedemo1 .txt", "r") as f:
#     lines = f.readlines()
#     print(lines)

#Read file with error handling

try:
    with open("writedemo1 .txt", "r") as f:
        print(f.read())
except FileNotFoundError :
    print("File not found")

#Write multiple lines using writelines()
try:
    with open("writedemo2 .txt", "r") as f:
        print(f.read())
except FileNotFoundError :
    print("File not found")

