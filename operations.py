import datetime


# Function to rent a land
def rent_land(lands, rented_lands):

    """
    Allows the user to rent a land from the available lands.

    Args:
        lands (dict): A dictionary containing details of all lands.
        rented_lands (dict): A dictionary containing details of currently rented lands.
    """


    # Filtering available lands
    available_lands = {k: v for k, v in lands.items() if v[4] == 'Available'}
    display_lands(available_lands)
    print("\n----------------------------------------------------------------------")
    choice = input("\nEnter the Kitta number of land you want to rent:")
    if choice in available_lands:
        duration = int(input("For how many months do you want to rent? "))
        try:

            # Calculating total cost based on duration
            cost = int(available_lands[choice][3]) * duration
            print(f"\nYour total cost for renting land {choice} for {duration} month(s) is: NPR {cost}")


            # Storing rented land details
            rented_lands[choice] = {"city": available_lands[choice][0], "price": available_lands[choice][3], "duration": duration, "cost": cost}
            lands[choice][4] = "Not Available"  # Updating land availability
        except ValueError:
            print("\nInvalid input! Please enter a valid duration.")
    else:
        print("\nThe kitta number of land you entered does not exist or is not available at the moment!")


# Function to return a rented land
def return_land(lands, returned_lands):
    
    """
    Allows the user to return a rented land.

    Args:
        lands (dict): A dictionary containing details of all lands.
        returned_lands (dict): A dictionary containing details of lands returned by customers.
    """

    
    # Filtering rented lands
    rented_lands = {k: v for k, v in lands.items() if v[4] == 'Not Available'}
    display_lands(rented_lands)
    choice = input("\nEnter the kitta number of the land you rented:")
    
    if choice in rented_lands:
        duration = int(input("\nFor how many months did you rent the land? "))
        actual_duration = int(input("\nAfter how many months are you returning the land? ")) 
        
        try:
            
            # Validating return duration
            if actual_duration < duration:
                print("\nInvalid input! The rented duration cannot be greater than the actual (returning) duration!")
                return
            
            back = actual_duration - duration
            cost_per_month = int(rented_lands[choice][3])
            total_cost = cost_per_month * duration

            
            # Calculating fine for exceeding duration
            if actual_duration > duration:
                fine_per_month = 0.1 * cost_per_month
                fine = fine_per_month * back
                total_cost += fine
                print(f"\nYou will be charged a fine for every exceeding month: NPR {fine}")
            
            print(f"\nYour total cost for renting Land {choice} with/without fine is: NPR {total_cost}")

            
            # Including rental cost and fine in returned_lands dictionary
            returned_lands[choice] = {
                "city": rented_lands[choice][0],
                "price": cost_per_month,
                "rental_cost": cost_per_month * duration,
                "duration": actual_duration,
                "cost": total_cost,
                "fine": fine if actual_duration > duration else 0,
                "total": total_cost - (fine if actual_duration > duration else 0)
            }
            
            # Updating land availability
            lands[choice][4] = "Available"  
        
        except ValueError:
            print("\nInvalid input! Please enter valid duration.")
    else:
        print("\nThe kitta number you entered does not exist.")


# Function to display lands
def display_lands(lands):
    
    """
    Displays the details of lands.

    Args:
        lands (dict): A dictionary containing details of lands to be displayed.
    """

    print("Kitta\tCity\t\tDirection\tAnna\tPrice\tAvailability")
    print("---------------------------------------------------------------------")
    for key, value in lands.items():
        print(f"{key}\t{value[0]}\t{value[1]}\t\t{value[2]}\t{value[3]}\t{value[4]}")


# Function to generate bill
def generate_bill(rented_lands, returned_lands):

    """
    Generates a bill for rented and returned lands.

    Args:
        rented_lands (dict): A dictionary containing details of currently rented lands.
        returned_lands (dict): A dictionary containing details of lands returned by customers.

    Returns:
        total_cost (int): The total cost for rented and returned lands.
    """

    total_cost = 0
    print(" -----------------------------------------------------------------------")
    print("|Kitta\tCity\t\tPrice\tStatus\tDuration\t| Cost\t\t|")
    print("|-------------------------------------------------------|---------------|")


    # Display rented lands and calculate total cost
    for kitta, land_info in rented_lands.items():
        duration = land_info["duration"]
        cost = land_info["cost"]
        total_cost += cost
        print(f"|{kitta}\t{land_info['city']}\t{land_info['price']}\tRented\t{duration} months\t| {cost}\t|")

    
    # Display returned lands and calculate total cost
    for kitta, land_info in returned_lands.items():
        duration = land_info["duration"]
        rental_cost = land_info["rental_cost"]
        fine = land_info["fine"]
        returned_cost = rental_cost + fine
        total_cost += returned_cost
        print(f"|{kitta}\t{land_info['city']}\t{land_info['price']}\tReturn\t{duration} months\t| {returned_cost}\t|")
        print("|-------------------------------------------------------|---------------|")
        print(f"|Fine\t\t\t\t\t\t\t| {fine}\t|")
    print("|-------------------------------------------------------|---------------|")
    print("|Total Amount\t\t\t\t\t\t|", total_cost, "\t|")
    print(" -----------------------------------------------------------------------")

    return total_cost
