person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

# print out the name of the spouse
print(person["spouse"])
print()

# print out the name of the second child
print(person["children"][1])
print()

# print out the name of the cat
print(person["pets"]["cat"])
print()

# use a loop to print out the name of each child
for x in person["children"]:
    print(x)
    print()

# use a loop to print out the pets in the following format:
# The type of pet is:dog and the name of the pet is: Fido
for key, value in person["pets"].items():
    print(f"The type of pet is:{key} and the name of the pet is: {value}")
print()
# option 2
pet_dict = person["pets"]
for key in pet_dict:
    print(f"The type of pet is:{key} and the name of the pet is: {pet_dict[key]}")
print()
