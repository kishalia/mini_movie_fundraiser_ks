#checks if user had answered yes or no to any of the questions
def yes_no (question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("ERROR!Please answer yes or no.")

#function checks if user responded with a blank.

def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("This cannot be blank.Please try again.")

        else:
            return response

def number_checker (question):
    while True:

      try:
        response = int(input(question))
        return response

      except ValueError:
        print("Please enter an integer.")

#main routine starts here

#maximum number of tickets
MAX_TICKETS = 3
tickets_sold = 0

#asks user if they would like instructions.
instructions = input("Would you like instructions? ") .lower()
if instructions == "yes" or instructions == "y" :
    print ("Here are the instructions:")

elif instructions == "no" or instructions == "n":
    pass

else:
    print("ERROR!Please answer yes or no.")

    instructions = yes_no("Would you like instructions? ") .lower()
    if instructions == "yes" or instructions == "y" :
        print ("Here are the instructions:")

print("We are done!")
#loop to sell tickets

while tickets_sold < MAX_TICKETS :
    name = not_blank("Please enter your name or enter 'QUIT'to exit program ").upper()


    if name == 'QUIT':
        break

    if name == 'QUIT':
        break

    age =  number_checker("Age: ")

    if 12 <= age <= 120:
      pass

    elif age < 12 :
        print("Sorry, you are too young to watch this movie.")
        continue

    else:
        print("ERROR!Please enter a valid age." )
        continue


    tickets_sold += 1


#output for the number of tickets sold

if tickets_sold == MAX_TICKETS:
    print ("Congratulations! You sold all the tickets!")

else:
    print("You have sold {}ticket/s.There are {} ticket/s remaining.".format(tickets_sold,MAX_TICKETS - tickets_sold))

