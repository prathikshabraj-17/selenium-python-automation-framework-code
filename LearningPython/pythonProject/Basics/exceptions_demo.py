# try:
#     print("Input First number:")
#     x = int(input())
#     print("Input second number:")
#     y = int(input())
#
#     if y == 0:
#         raise Exception("The denominator is 0")
#
#     print(x/y)
#
# except Exception as e:
#     print(e)
#     print("In except block")
#
# else:
#     print("In else Block")
#
# finally:
#     print("This is always executed")
#
#
#
# # 2.Full Example with else and finally
# try:
#     num = int(input("Enter a number: "))
#     print("Result:", 100 / num)
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except ValueError:
#     print("Invalid input.")
# else:
#     print("Division successful.")
# finally:
#     print("Program ended.")
#
#
# # 3
# try:
#
#     num = int(input("Input First Number:"))  # This is the risky code
# except:
#     print("Input failed. Please enter a valid number.") # if error happens
# else:
#     if num < 45:
#         print("Pass") # if no error happens
#     else:
#         print("Fail")
# finally:
#     print("Results announced") # always runs at the END
#
# #4 Example 1: Division by Zero
#
# try:
#     a = int(input("Enter numerator: "))
#     b = int(input("Enter denominator: "))
#     print("Result:", a / b)
# except ZeroDivisionError:
#     print("❌ Cannot divide by zero.")
from sys import exception

#5 Invalid Integer Input

# try:
#     age = int(input("Enter your age: "))
#     print("Your age is:", age)
# except ValueError:
#     print("❌ Please enter a valid number.")

#6 Voting
#
# try:
#     age = int(input("Enter your age:"))
#     if age <=0:
#         print("Invalid age")
#     elif age >=21:
#         print("valid age")
#     raise Exception('Not eligible for voting')
#
# except Exception as e:
#     print('error', e)
#     # if age <=0:
#     #     print("Invalid age")
#
#
# else:
#     # if age <= 0:
#     #     print("Invalid age")
#     # elif age > 18:
#         print("Eligible")
#     # elif age < 18:
#     #     print("not eligible")
# finally:
#         print("Voting")

# #7 accepting five user age(if condition)
# try:
#     age = int(input("enter your age"))
#     print("First employee age ")
#     a = int(input("Enter your age:"))
#     print("Second employee age")
#     b = int(input("Enter your age:"))
#     print("third employee age ")
#     c = int(input("Enter your age:"))
#     print("fourth employee age")
#     d = int(input("Enter your age:"))
#     print("Fifth employee age ")
#     e = int(input("Enter your age:"))
#
#     if age <= 18:
#         print("Invalid age")
#     elif age >= 18:
#         print("valid age")
#         raise exception("Not aligble for voting")
# except Exception as e:
#     print('eligible for voting',e)

# #8 accepting five user age(for loop)

for i in range(1, 8):
    try:
        age = int(input(f" Enter age for the user: {i} "))

        if age <= 0:
            raise Exception("Age should be greater than 0")
        elif age < 18:
            raise Exception("Not eligible for voting")

    except ValueError:
        print("Invalid input ! Please enter a number")
    except Exception as e:
        print("Error for user {i}", e)
#
#     else:
#         print(f" User {i} Eligble for voting")
#     finally:
#         print("Finished processing \n")


 #9 List Index Out of Range
# try:
#     fruits = ["apple", "banana", "mango"]
#     print(fruits[1])  # Invalid index
# except IndexError:
#     print("That index doesn't exist in the list.")

#10 KeyError in Dictionary

# try:
#     student = {"name": "Alice", "age": 20 , "grade" : 90}
#     print(student["grade"])  # 'grade' key doesn't exist
# except KeyError:
#     print("That key was not found in the dictionary.")

#11  TypeError

# try:
#     num = 5 + "five"# You can't add int and str
# except TypeError:
#     print(" Cannot add number and string.")

 #12 File Not Found

# try:
#     file = open("nonexistent.txt", "r")
# except FileNotFoundError:
#     print(" File not found.")
# else:
#     print(" File opened successfully.")
#     file.close()
# finally:
#     print(" File operation complete.")

#13 Handling Multiple Errors

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print("Result:", a / b)
except ValueError:
    print(" Please enter only numbers.")
except ZeroDivisionError:
    print(" Cannot divide by zero.")

