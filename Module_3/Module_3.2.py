cabin=input("enter your cabin class (LUX/A/B/C): ")
if cabin.lower()=="lux":
    print("upper-deck cabin with balcony.")
elif cabin.lower()=="a":
    print("above the car deck, equipped with a window.")
elif cabin.lower()=="b":
    print("windowless cabin above the car deck.")
elif cabin.lower()=="c":
    print("windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")