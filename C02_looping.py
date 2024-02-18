#main routine starts here

#maximum number of tickets
MAX_TICKETS = 3

#loop to sell tickets
tickets_sold = 0
while tickets_sold < MAX_TICKETS :
    name = input("Please enter your name or enter 'QUIT' to exit the program. ") .upper()


    if name == 'QUIT':
        break

    tickets_sold += 1


#output for the number of tickets sold

if tickets_sold == MAX_TICKETS:
    print ("Congratulations! You sold all the tickets!")

else:
    print("You have sold {} ticket/s.There are {} ticket/s remaining.".format(tickets_sold,MAX_TICKETS - tickets_sold))
