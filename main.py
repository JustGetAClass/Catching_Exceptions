# Catching Exceptions

# try - something that my cause an exception
#
# except  - do this if there was an exception
#
# else - do this if there was no exception
#
# finally - do this no matter what happens

# try:
#     file = open("a_file.txt")
#     dictionary = {"key": "value"}
#     print(dictionary["key"])
# except FileNotFoundError:
#     file = open(file="a_file.txt", mode="w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:                                                   # will not happen if try fails
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("file was closed")
#     raise TypeError("This is an error i made up")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("You should not be this tall")

bmi = weight / height ** 2
print(bmi)
