gen=input("enter your gender: ")
hemoglobin=float(input("enter your hemoglobin value in gram per litre: "))
if gen.lower()=="f" or "female":
    if hemoglobin<=117:
        print("your hemoglobin level is low")
    elif hemoglobin<=155:
        print("your hemoglobin level is high")
    else:
        print("your hemoglobin level is normal")

elif gen.lower()=="m" or  "male":
        if hemoglobin <= 134:
            print("your hemoglobin level is low")
        elif hemoglobin <=167:
            print("your hemoglobin level is high")
        else:
            print("your hemoglobin level is normal")
else:
    print("Sorry , We dont have data except for male and female")