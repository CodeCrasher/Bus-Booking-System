Destination_city = {'Sydney': 10, 'Melbourne': 15, 'Brisbane': 20, 'Adelaide': 25} #Creating dictionary for data to choose
services = {'internet':0 , 'snacks':10,'drink':5}
all_customers = []
Transaction_register_without_membership = []
customer_purchase = {}
customer_history = {}
Transaction_register_with_membership = []
global Customer_name,total_cost,Customer_destination,Tickets #Creating global variables
##Function to book tickets##
def book_a_new_trip():
  global services,Customer_name,total_cost,Customer_destination,Tickets
  Customer_name = input("Enter the name of the customer[e.g Ambhoj]:")  #Taking input for customer_name
  while True:
    try:
      Customer_destination = input('Enter the destination[enter a valid destination only,e.g.' + ",".join(Destination_city) +']'+':')
      if Customer_destination in Destination_city.keys(): #checking destination is present in the places mentioned in dictionary
        break
      print("Invalid value entered")
    except Exception as e:
      print(e)

  while True:
    try:
      Tickets = int(input('Enter the number of the tickets[enter a positive integer only,e.g. 1,2,3]:')) #Taking input for number of tickets which must be a positive integer
      if Tickets > 0:
        break
      print("Invalid value entered")
    except Exception as e:
      print(e)
  while True:
    try:
      Membership = input('Customer does not have a membership.Does the customer want to have a membership[enter y or n]?')
      if Membership == 'y' or Membership == 'n': #Checking whether the input for Membership belongs to y or n,else throw an error
        break
      print("Invalid value entered")
    except Exception as e:
      print(e)

      global Transaction_register_with_membership
      global Transaction_register_without_membership

  total_cost = Tickets * Destination_city[Customer_destination] #Calculating total cost for the trip without discount
  Transaction_register_without_membership = []
  Transaction_register_with_membership = []
#Creating customers with membership list
  if Membership == 'y':
    Transaction_register_with_membership.append(Customer_name)
    print('Customer list for members:' + str(Transaction_register_with_membership))
    total_cost = Tickets * Destination_city[Customer_destination]-(Tickets * Destination_city[Customer_destination] * 0.05)
    discount_percentage = 5
#Creating customers with non_membership list
  elif Membership == 'n':
    Transaction_register_without_membership.append(Customer_name)
    print('Customer list for non members: ' + str(Transaction_register_without_membership))
    discount_percentage = 0
#Extra services for the customer
  while True:
    try:
      extra_service_choice = input('Do you want an extra service (y or n)')
      if extra_service_choice == 'y' or extra_service_choice == 'n':
        break
      print("Invalid value entered")
    except Exception as e:
      print(e)

  priceofextraservice = 0
  if extra_service_choice == 'y':
    extra_service = input('Select an extra service e.g:' + ",".join(services) + ':')
    if extra_service == ('internet') and Membership == 'n': #if customer is not having membership but entered for free services
      print("Only membership customers can avail this service")
    else:
      priceofextraservice = services[extra_service]
      total_cost += priceofextraservice
  customer_purchase_list()
  customer_order_history()
  print(Customer_name + ' ' + 'books' + ' ' + str(Tickets) + ' ' + 'tickets to' + ' ' + Customer_destination)
  print(Customer_name + ' ' + 'gets a discount of' + ' ' + str(discount_percentage) + '%')
  print('Unit price:'.ljust(30) + str(Destination_city[Customer_destination]) + ' ' + 'AUD')
  print('Extra service price:'.ljust(30)+ str(priceofextraservice) + ' ' + 'AUD')
  print('Total price:'.ljust(30) + str(total_cost) + ' ' + 'AUD')
  print('Please enter to go back to menu!')
##Function to add new destination as per customer
def add_a_new_destination():
  global Customer_destination
  selection = input('Do you want to enter new destination y/n:')
  while selection == 'y':
    try:
      Customer_destination = input('Enter new destination you want to add:')
      if Customer_destination in Destination_city.keys(): #Checking customer destination whether destination already exists
        print("City value already exist")
      else:
        while True:
          try:
            price = int(input('Enter the price of new destination:')) #Enter price for new destination and it should be positive integer
            if price > 0:
              break
            print("Invalid value entered")
          except Exception as e:
            print(e)
        Destination_city[Customer_destination] = price
        selection = input('Do you want to enter new destination y/n:')
    except selection == 'n':
      break
  print(Destination_city)

## function to view all the customers
def display_all_customers():
  global Transaction_register_with_membership
  global Transaction_register_without_membership
  all_customers=Transaction_register_without_membership+Transaction_register_with_membership
  print('Please find the list of all the existing customers:\n',all_customers)
## function to list all the customers with membership
def all_membership():
  global Transaction_register_with_membership
  print('List of all the customers with membership \n',Transaction_register_with_membership)
## fucntion to list all the valid destinations
def valid_destination():
  print('List of all the valid destinations are as follow:\n',Destination_city)
##function to create a purchase list for all the customers
def customer_purchase_list():
  global Transaction_register_with_membership
  global customer_purchase
  global Customer_name
  global total_cost
  if Customer_name in customer_purchase:
    customer_purchase[Customer_name] += float(total_cost)
  else:
    customer_purchase[Customer_name] = float(total_cost)
  print('List of all the customers purchase \n', customer_purchase)
##fucntion to create an order history for all the orders placed by the customer
def customer_order_history():
  global Customer_destination
  global Customer_name
  global Tickets
  if Customer_name in customer_history:
    customer_history[Customer_name].append([Customer_destination, Tickets])
  else:
    customer_history[Customer_name] = [[Customer_destination, Tickets]]
    print(customer_history)

##function to print out the customer history
def customer_history_print():
  global Customer_name
  print("This is the order history for " + Customer_name + ".")
  print("Destination".ljust(15) + "Number of Tickets")
  for value in customer_history[Customer_name]:
    print(customer_history[Customer_name])
    print(value[0].ljust(15) + str(value[1]).ljust(10))
##Creating the menu for the bus booking system
while True:
  print("#"*40)
  print("Welcome to sydney bus booking system")
  print("1. Book a new trip")
  print("2. Add a new destination")
  print("3. Display all existing customers")
  print("4. Display all customers with membership")
  print("5. Display all valid destinations")
  print("6. Most valuable customer")
  print("7. Customer order history")
  print("0. Exit the program")
  choice = int(input("Enter your choice:"))
  print("#"*40)
  if choice==1:     #Creating the choices and feeding the conditions accordingly
    book_a_new_trip()
  elif choice==2:
    add_a_new_destination()
  elif choice==3:
    display_all_customers()
  elif choice==4:
    all_membership()
  elif choice==5:
    valid_destination()
  elif choice==6:
    most_valued_customer = max(customer_purchase, key=customer_purchase.get) #getting the maximum purchase value among customers
    print("Most valued customer:", most_valued_customer)
  elif choice==7:  #Enter customer name to check for their order history
    customer_name_history = input("Enter the customer name to get their order history:\n")
    while customer_name_history not in customer_history:
      print("This customer does not exist.")
      customer_name_history = input("Please enter a valid customer name: \n")
    customer_history_print()
  elif choice==0: #Breaking out from the program and exiting
      break
  else:
    print("wrong choice") #If the user input is not valid
