#functions go here
#checks if user responded to the program with an integer
def number_checker (question):
    while True:

      try:
        response = int(input(question))
        return response

      except ValueError:
        print("Please enter an integer.")



#main routine goes here

tickets_sold = 0

while True:

    name = input("Please enter your name or enter 'QUIT' to exit the program. ").upper()

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

    tickets_sold +=1
