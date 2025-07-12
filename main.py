import datetime


from operations import *             # Importing functions from the 'operations' module

from read import Writing_on_txtfile  # Importing a function for writing to a text file

from write import Bill_on_txtfile    # Importing a function for writing billing information to a text file


def main():
    # Printing company information
    print("\n\n----------------------------------------------------------------------\n")
    print("\n                    TerraEstate Land Rentals PVT.LTD\n ")
    print("                      Address: Lalitpur, Nepal      ")
    print("                       Contact No: +977-9876345630       ")
    print("                      Email: TerraEstate1@gmail.com\n\n  ")
    print("----------------------------------------------------------------------\n")
    
    print("Kitta\tCity\t\tDirection\tAnna\tPrice\tAvailability")
    print("----------------------------------------------------------------------\n")

    
    # Dictionary containing land details
    land_dict = {
        '010': [ 'Mahendranager', 'East' , '9', '100000', 'Available'     ],
        '020': [ 'Dhangadi',      'East' , '5', '55000' , 'Not Available' ],
        '030': [ 'Nepalgung',     'North', '4', '38000' , 'Available'     ],
        '040': [ 'Mahendranager', 'West' , '5', '65000' , 'Not Available' ],
        '050': [ 'Dhangadi',      'East' , '7', '80000' , 'Available'     ]
    }

    
    # Printing land details
    for key, value in land_dict.items():
        print(f"{key}\t{value[0]}\t{value[1]}\t\t{value[2]}\t{value[3]}\t{value[4]}")
        
    print("\n----------------------------------------------------------------------")    
    print("\n")
    print("Warm welcome! to our company Sir/Mam\n")

    
    # Taking customer information
    name  = input("Enter your Full Name: ").upper()
    add   = input("Enter the Address: ").upper()
    phone = input("Enter the Contact Number: ")

    print("\n\nTo rent a land type(rent).")
    print("To return a land type(return).")

    # Rented Lands Dictionary
    rented_lands = {}

    # Returned Lands Dictionary
    returned_lands = {}

    
    # Loop for renting or returning lands
    more = True
    while more:
        reason = input("\nDo you want to rent or return the land Sir/Mam :").lower()
        print("\n")
        
        try:
            
            # Renting a land
            if reason == "rent":
                rent_land(land_dict, rented_lands)

                
            # Returning a land
            elif reason == "return":
                return_land(land_dict, returned_lands)

            else:
                print("Enter a valid input!!")
                
        except Exception as e:
            print("An error occurred:", e)

        
        # Asking if the user wants to continue
        if more:
            try:
                choice = input("\nDo you want to continue? (continue/exit): ").lower()
                if choice != "continue":
                    more = False
                    
            except Exception as e:
                print("An error occurred:", e)

    
    # Check if there are rented or returned lands before generating the bill
    if rented_lands or returned_lands:
        try:
            
            # Displaying billing information
            print("\n----------------------------------------------------------------------") 
            print("\n                  TerraEstate Land Rentals PVT.LTD\n ")
            print("                     Address: Mahendranager, Nepal     ")
            print("                       Contact: +977-9876345630        ")
            print("                     Email: TerraEstate1@gmail.com\n\n ")

            # Getting current date and time
            current_datetime = datetime.datetime.now()
            year = str(current_datetime.year)
            month = str(current_datetime.month)
            day = str(current_datetime.day)
            hour = str(current_datetime.hour)
            minute = str(current_datetime.minute)
            second = str(current_datetime.second)
            generate_bill_id = year + month + day + hour + minute + second
     
            # Generating a unique bill ID based on the current date and time
            bill_id = generate_bill_id
           
            print("Bill ID: ", bill_id , "\t\t\t\t    Date: ", datetime.datetime.now().strftime('%Y/%m/%d'), "\n")
            print("Customer Name: ", name)
            print("Customer Address: ", add)
            print("Customer Contact No: ", phone,"\n")


            # Generating and displaying the bill
            total_cost = generate_bill(rented_lands, returned_lands)

            
            # Writing billing information to a file
            Bill_on_txtfile(name, add, phone, rented_lands, returned_lands)
            print("\nThank you for choosing us")
            
        except Exception as e:
            print("\nPls Try Again, An Error occured while generatiing the bill:", e)
            
    else:
        print("\nU should rent or return a land in order to get a bill")


    # Writing all land details to a file
    Writing_on_txtfile("Land_Details.txt", land_dict)

if __name__ == "__main__":
    main()
