#functions go here

def yes_no (question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("ERROR!Please answer yes or no.")


#main routine goes here

while True:
    instructions = yes_no("Would you like instructions? ") .lower()
    if instructions == "yes" or instructions == "y" :
        print ("Here are the instructions:")

    print("program continues...")
