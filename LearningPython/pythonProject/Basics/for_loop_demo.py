
cities = [["usa","alaska"],["india", "delhi"],["australia", "melborne"]]
# for c in cities:
#     print(c)
# for country,city in cities:
#    print("country is "  +country+ " and city is " +city)
my_dictionary = dict(cities)
print(my_dictionary)
for country, city in my_dictionary.items():
    print(country, city)

# cities = { "Delhi" , "newyork"}
# for city in cities:
#     print (city)
#
#
# cities = "Mysuru"
# for c in cities:
#     print(c)

 # 1. Print numbers from 1 to 5
for i in range(1, 6):
    print(i)



# 2. Print each character in a string
word = "apple"

for char in word:
    print(char)

# 3. Print each item in a list

fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)


# 4. Print even numbers from 2 to 10
for i in range(2, 11, 2):
    print(i)

#  5. Sum of numbers in a list

numbers = [10, 20, 30, 40]
total = 0

for num in numbers:
    total += num

print("Total:", total)


#6 Using for with if – print only vowels

word = "pineapple"

for ch in word:
    if ch in "aeiou":
        print(ch)


# 7. Nested for loop – Print a pattern

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
