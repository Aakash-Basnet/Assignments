names=set()
store=input("enter the names: ")
while store!="":
    if store in names:
        print("Existing name")
    else:
        print("New name")
        names.add(store)

    store=input("enter a name: ")
print("The names in the set are : \n")
for i in names:
    print(i)





