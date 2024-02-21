# checks if user had answered yes or no to any of the questions
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("ERROR!Please answer yes or no.")


# function checks if user responded with a blank.

# checks if user entered a blank as their response

def yes_no (question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("ERROR!Please answer yes or no.")

def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("This cannot be blank.Please try again.")

        else:
            return response


# integer checker: checks whether user entered an integer as their response
def number_checker(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer.")


# function calculates the ticket price based on the age of the user
def calc_ticket_price(var_age):
    # ticket is $7.50 for users under 16
    if var_age < 16:
        price = 7.5

    # ticket is $10.50 for users between 16 and 64
    elif var_age < 65:
        price = 10.5

    # ticket price is $6.50 for seniors (65+)
    else:
        price = 6.5

    return price


# main routine starts here


# maximum number of tickets
MAX_TICKETS = 10
tickets_sold = 0

# asks user if they would like instructions.
instructions = yes_no("Would you like instructions? ")
if instructions == "yes":
    print("Here are the instructions:")


print("We are done!")
# loop to sell tickets

while tickets_sold < MAX_TICKETS:
    name = not_blank("Please enter your name or enter 'QUIT'to exit program ").upper()

    if name == 'QUIT':
        break

    age = number_checker("Age: ")

    if 12 <= age <= 120:
        pass

    elif age < 12:
        print("Sorry, you are too young to watch this movie.")
        continue

    else:
        print("ERROR!Please enter a valid age.")
        continue

    tickets_sold += 1

    # calculate the ticket cost
    ticket_cost = calc_ticket_price(age)
    print("Age: {}, Ticket Price: ${:.2f}".format(age, ticket_cost))

# output for the number of tickets sold

if tickets_sold == MAX_TICKETS:
    print("Congratulations! You sold all the tickets!")

else:
    print("You have sold {}ticket/s.There are {} ticket/s remaining.".format(tickets_sold, MAX_TICKETS - tickets_sold))
