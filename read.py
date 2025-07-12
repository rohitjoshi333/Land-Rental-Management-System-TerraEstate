# Function to write land details to a file
def Writing_on_txtfile(filename, lands):
    
    """
    Writes the details of lands to a text file.

    Args:
        filename (str): The name of the file to write the land details.
        lands (dict): A dictionary containing details of lands to be written to the file.
    """

    
    # Open the file in write mode
    with open(filename, "w") as file:

        
        # Writing headers to the file
        file.write("Kitta\tCity\t\tDirection\tAnna\tPrice\tAvailability\n")
        file.write("---------------------------------------------------------------------\n")


        # Writing land details to the file
        for key, value in lands.items():
            file.write(f"{key}\t{value[0]}\t{value[1]}\t\t{value[2]}\t{value[3]}\t{value[4]}\n")
