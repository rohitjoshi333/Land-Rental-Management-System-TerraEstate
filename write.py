import datetime


# Function to write billing information to a file
def Bill_on_txtfile(name, add, phone, rented_lands, returned_lands):

    """
    This function writes billing information to a text file.

    Args:
        name (str): The Name of the customer.
        add (str): The Address of the customer.
        phone (str): The ContactNo of the customer.
        rented_lands (dict): A dictionary containing details of rented lands.
        returned_lands (dict): A dictionary containing details of returned lands.
    """


    # Getting current date and time
    current_datetime = datetime.datetime.now()
    year = str(current_datetime.year)
    month = str(current_datetime.month)
    day = str(current_datetime.day)
    hour = str(current_datetime.hour)
    minute = str(current_datetime.minute)
    second = str(current_datetime.second)
    generate_bill_id = year + month + day + hour + minute + second

    
    # Generating file name based on customer name and bill ID
    file_name = name + "(" + generate_bill_id + ")" + ".txt"

    
    # Opening the file in write mode
    with open(file_name, "w") as file:

        
        # Writing company information to the file
        company_info = (
            "-----------------------------------------------------------------------\n" +
            "                    TerraEstate Land Rentals PVT.LTD  \n" +
            "                      Address: Mahendranager, Nepal   \n" +
            "                       Contact No: +977-9876345630    \n" +
            "                      Email: TerraEstate1@gmail.com   \n" +
            "-----------------------------------------------------------------------\n"
        )
        file.write(company_info)

        
        # Writing date and billing information to the file
        bill_info = (
            "\n\n\nBill ID: " + generate_bill_id + "\t\t\t\tDate: " + year + "/" + month + "/" + day + "\n" +
            "Customer Name: " + name + "\n" +
            "Customer Address: " + add + "\n" +
            "Customer Contact No: " + phone + "\n\n"
        )
        file.write(bill_info)

        total_cost = 0

        
        # Writing header for the bill details
        file.write("|-----------------------------------------------------------------------|\n")
        file.write("|Kitta\tCity\t\tPrice\tStatus\tDuration\t| Cost\t\t|\n")
        file.write("|-------------------------------------------------------|---------------|\n")

        
        # Displaying rented lands and calculating total cost
        for kitta, land_info in rented_lands.items():
            duration = land_info["duration"]
            cost = land_info["cost"]
            total_cost += cost
            land_details = (
                f"|{kitta}\t{land_info['city']}\t{land_info['price']}\tRented\t{duration} months\t| {cost}\t|\n"
            )
            file.write(land_details)

        
        # Displaying returned lands and calculating total cost
        for kitta, land_info in returned_lands.items():
            duration = land_info["duration"]
            rental_cost = land_info["rental_cost"]
            fine = land_info["fine"]
            returned_cost = rental_cost + fine
            total_cost += returned_cost
            returned_land_details = (
                f"|{kitta}\t{land_info['city']}\t{land_info['price']}\tReturn\t{duration} months\t| {returned_cost}\t|\n"
            )
            file.write(returned_land_details)
            file.write("|-------------------------------------------------------|---------------|\n")
            fine_details = f"|Fine\t\t\t\t\t\t\t| {fine}\t|\n"
            file.write(fine_details)

        file.write("|-------------------------------------------------------|---------------|\n")
        total_details = f"|Total Amount\t\t\t\t\t\t| {str(total_cost)}\t|\n"
        file.write(total_details)
        file.write("|-----------------------------------------------------------------------|\n")

        file.write("\n\nThank you for choosing us\n")
