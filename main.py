#FileNotFound
# with open("a_file.txt") as file:
#   file.read()

# try:
#   file = open("a_file.txt")
#   a_dictionary = {"key": "value"}
#   print(a_dictionary["key"])
# except FileNotFoundError:
#   file = open("a_file.txt", "w")
#   file.write("Something")
# except KeyError as error_message:
#   print(f"That key {error_message} does not exist.")
# else:
#   content = file.read()
#   print(content)
# finally:
#   # file.close()
#   # print("File was closed.")
#   raise TypeError

height = float(input("Height: "))
weight = int(input("Weight "))

if height > 3:
  raise ValueError("You are definitely not over 9 feet tall bro, please enter your correct height")

bmi = weight / height ** 2
print(bmi)



#KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

#IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text + 5)

