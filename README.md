# Nike Warehouse Shoe Inventory

This Python program manages a sample shoe inventory. It reads shoe information from a comma delimited file, displays inventory details and provides options to modify the stock levels through the command line.

## Features of the Program

- Load data from the comma delimited file `inventory.txt`
- Add new shoes to the inventory
- View all shoes
- Search for and restock the lowest quantity shoes
- Search for shoes by their shoe code
- Calculate and display the value of each shoe
- Search for and display the shoes with the highest quantity for sale
- Save updates back to the inventory file

## How it Works

**Data Storage:**  
Shoes are stored as objects of the `Shoe` class, with attributes like country, code, product name, cost, and quantity.

**Reading Data:**  
The `read_shoes_data()` function reads data from `inventory.txt`, creates `Shoe` objects, and stores them in a list.

**User Interaction:**  
The `main()` function presents the user with a menu to select an option.

**Updating Data:**  
Changes such as restocking and adding shoes are updated in a list and can be saved to  `inventory.txt`.

## Usage

Run the Python script and follow the on-screen menu prompts.

## Requirements

- Python
- `tabulate` library (install using `pip install tabulate`)
- `inventory.txt`: The comma delimited inventory data file. This file must exist in the same directory as the script or the path must be modified.