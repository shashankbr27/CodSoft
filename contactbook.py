name=[]
phone_number=[]
quantity=4

for i in range(quantity):
    names=input("Name: ")
    phone_numbers=input("Phone number: ")
    name.append(names)
    phone_number.append(phone_numbers)

print("\n Name\t\t\t Phone Number\n")

for i in range(quantity):
    print("{}\t\t\t{}".format(name[i],phone_number[i]))
search=input("\n Enter the search term: ")
print("Search Results")
if search in name:
    index=name.index(search)
    phone_number=phone_number[index]
    print("Name: {},Phone Number: {}".format(search,phone_number))
else:
    print("Name not found! ")