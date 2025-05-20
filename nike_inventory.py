from tabulate import tabulate

# This list will store a list of objects of shoes.
shoe_list = []

# This variable will be used to create a new line in f-strings.
new_line = "\n"


class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        """
        Initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_country(self):
        """
        Return the country of the shoe.
        """
        return self.country
    
    def get_code(self):
        """
        Return the code of the shoe.
        """
        return self.code
    
    def get_product(self):
        """
        Return the product of the shoe.
        """
        return self.product

    def get_cost(self):
        """
        Return the cost of the shoe in currency format.
        """
        return self.cost

    def get_quantity(self):
        """
        Return the quantity of the shoe.
        """
        return self.quantity

    def __str__(self):
        """
        Return a string representation of the shoe object.
        """
        return (f"{new_line}Country: {self.country}"
                f"{new_line}Code: {self.code}"
                f"{new_line}Product: {self.product}"
                f"{new_line}Cost: £{self.cost:,.2f}"
                f"{new_line}Quantity: {self.quantity}")


def read_shoes_data():
    """
    The following will:
        ● open the file inventory.txt,
        ● read the data from this file,
        ● create a shoes object with this data, and
        ● append this object into the shoes list. 
    """
    try:
        with open('inventory.txt', 'r') as file:
            next(file) 
            for line in file:
                country, code, product, cost, quantity = line.strip().split(',')
                shoe = Shoe(country, code, product, int(cost), int(quantity))
                shoe_list.append(shoe)
    
    # Handle possible errors.
    except IOError:
        print("An error occurred while reading the file.")
    except ValueError:
        print("Error in data format. Please check the file.")
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def capture_shoes():
    """
    The following will:
        ● allow a user to capture data about a shoe,
        ● use this data to create a shoe object,
        ● append this object inside the shoe list, and
        ● print the added shoe object to the console.
    """

    # Check user input if the country is valid.
    while True:
        country = input("Enter the country: ")
        if type(country) == str and len(country) > 0:
            break
        else:
            print("Invalid country. Please enter a valid country name.")
    
    # Check user input if the code is valid.
    while True:
        code = input("Enter the code of the shoe: ")
        if code.isalnum() and len(code) > 0:
            break
        else:
            print("Invalid code. Please enter a valid code.")

    # Check user input if the product is valid and not empty.
    while True:
        product = input("Enter the product/shoe name: ")
        if len(product) > 0:
            break
        else:
            print("Please enter a valid product/shoe name.")

    # Check user input if the cost is a valid number.
    while True:
        try:
            cost = float(input("Enter the cost per pair of shoes: "))
            if cost > 0:
                break
            else:
                print("Cost must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid cost.")
 
    # Check user input if the quantity is a valid number.
    while True:
        try:
            quantity = int(input("Enter the quantity of shoes available: "))
            if quantity > 0:
                break
            else:
                print("Quantity must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid quantity.")
    
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)


def view_all():
    """
    Display all the shoes in the inventory.
    """
    print("Here are all the shoes in the inventory:")
    print(tabulate([[shoe.get_country(), shoe.get_code(),
                    shoe.get_product(), shoe.get_cost(),
                    shoe.get_quantity()] for shoe in shoe_list],
                    headers=["Country", "Code", "Product", "Cost", "Quantity"]))


def re_stock():
    """
    This following will:
        ● find the shoe with the lowest quantity,
        ● print this shoe to the console,
        ● ask the user to enter the quantity of shoes to add,
        ● update the quantity of this shoe in the list, and
        ● update the inventory.txt file with the new quantity.
    """
    if not shoe_list:
        print("The shoe entered can't be located." \
            "Please try a different shoe.")
        return

    min_shoe = min(shoe_list, key=lambda x: x.get_quantity())
    print(f"This is the shoe with the lowest quantity: {min_shoe}")
    add_quantity = int(input("Enter the shoe quantity to add: "))
    min_shoe.quantity += add_quantity

    # Update the file
    with open('inventory.txt', 'w') as file:
        file.write("Country,Code,Product,Cost,Quantity\n")
        for shoe in shoe_list:
            file.write(f"{shoe.country},{shoe.code},{shoe.product}," \
                       f"{shoe.cost},{shoe.quantity}\n")


def search_shoe():
    """
    Search for a shoe from the list using the shoe code, and 
    return this object so that it will be printed.
    """
    code = input("Enter the shoe code to search: ")
    for shoe in shoe_list:
        if shoe.get_code().strip().lower() == code.strip().lower():
            print(f"Details of the shoe found: {shoe}")
            return
    print("Shoe not found.")


def value_per_item():
    """
    Calculate the total value for each item, and
    print this information to the console.
    """
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"Value of {shoe.get_product()} ({shoe.get_code()}):" \
              f" £{value:,.2f}")


def highest_qty():
    """
    Determine the product with the highest quantity, and
    print this shoe as being for sale.
    """
    if not shoe_list:
        print("No shoes available.")
        return
    
    max_shoe = max(shoe_list, key=lambda x: x.get_quantity())
    print(f"Product: {max_shoe.get_product()} is available for sale.")


def main():
    """
    User menu allowing the user to select an option.
    """
    read_shoes_data()

    while True:
        print("\nMenu:")
        print("1. Add a new Shoe to the Inventory List")
        print("2. View All Shoes")
        print("3. View Shoes to Re-stock")
        print("4. Search for a Shoe")
        print("5. View Value Per Item by Shoe Code")
        print("6. View Shoe with the Highest Quantity")
        print("7. Exit the Program")

        choice = input("Enter your choice: ")
        print() # Add a new line for better readability

        if choice == '1':
            capture_shoes()
        elif choice == '2':
            view_all()
        elif choice == '3':
            re_stock()
        elif choice == '4':
            search_shoe()
        elif choice == '5':
            value_per_item()
        elif choice == '6':
            highest_qty()
        elif choice == '7':
            break
        else:
            print("Invalid choice, please enter valid numeric choice.")
    print("Exiting the program. Goodbye!")


# Call the main function to start the program.
main()