# x = 0
# while x <= 10:
#     print(x)
#     x = x + 1
#     print("inside while")
# print("out of while loop")

# city = "mysuru"
# x = 1
# while x < len(city):
#     print(city[x])
#     x = x + 1

# city = "Delhi"
# x = 1
# while x < len(city):
#     print(city[x])
#     x = x + 2

city = "Bengaluru"
x = 2
while x < len(city):
    print(city[x])
    x = x + 1

i = 1
while i <= 5:
    print(i)
    i += 1


# total = 0
# num = int(input("Enter a number (0 to stop): "))
#
# while num != 0:
#     total += num
#     num = int(input("Enter a number (0 to stop): "))
#
# print("Total sum is:", total)


while True:
    name = input("Enter your name ")
    if name == "start":
        break
    print("Hello,", name)
