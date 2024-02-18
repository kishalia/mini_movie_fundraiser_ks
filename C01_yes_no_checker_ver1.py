# yes/no checker version one
instructions = input("Would you like instructions? ") .lower()
if instructions == "yes" or instructions == "y" :
    print ("Here are the instructions:")

elif instructions == "no" or instructions == "n":
    pass

else:
    print("ERROR!Please answer yes or no.")
