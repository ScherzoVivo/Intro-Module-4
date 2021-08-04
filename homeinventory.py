#==================================================#
# Home Inventory Script -- homeinventory.py --
# C:\Users\Alleg\Python\UW Course\Week 4\homeinventory.py
# Assignment #4 - Create and Maintain External Inventory File
# DJP -- 2021-07-25 -- Initial script composition
# DJP -- 2021-07-26 -- Scrapped original code and started over
# DJP -- 2021-07-28 -- Completed ViewRecord function and tidied up main loop
#==================================================#
import json

import pandas   as pd
######################################################################
# Pretty title
print("\n\n==================================================")
print("Welcome to Home Inventory Tracker v1.0!")
print("==================================================\n")
######################################################################
# Load JSON file
count = 1

with open("homeinventory.json") as json_file:
    inventory = json.load(json_file)

for i in inventory:
    count += 1

json_file.close()
######################################################################
def AddRecord(inventory, count):
    new_record = {}

    name = input("Enter Name: ").title()

    try:
        quantity = int(input("\nQuantity: "))
        val = float(input("\nValue: "))
        value = str(round(val, 2))
        print("\n\n")

        new_record["ID"] = count
        new_record["Name"] = name
        new_record["Quantity"] = quantity
        new_record["Value"] = "$" + value

        inventory.append(new_record)

        return inventory

    except:
        print("\nInvalid Entry. Quantity and Value must be numbers.\n")
######################################################################
def ViewRecords(inventory):
    print("""What would you like to do?
    1. View Most Recent (10)
    2. View All
    """)

    try:
        user_input = int(input("Make a selection [1-2]: "))
    except:
        print("\nInvalid selection.\n\n")

    records = pd.json_normalize(inventory)

    if user_input == 1:
        print("\n")
        df = pd.DataFrame.from_dict(records)
        print(df.tail(10))

    elif user_input == 2:
        print("\n")
        df = pd.DataFrame.from_dict(records)
        df = df.to_string(index = False)
        print("")
        print(df)
######################################################################
running = True
while running:

    print("""Please select an option:
    1. Add Record
    2. Review Records
    3. Exit Application
    """)

    user_choice = input("Make a selection [1 - 3]: ")
####################
    if user_choice == "1":
        print("\n====================")
        print("     Add Record")
        print("====================\n")
        inventory = AddRecord(inventory, count)
        continue

    elif user_choice == "2":
        print("\n====================")
        print("    View Records")
        print("====================\n")
        ViewRecords(inventory)
        print("==================================================\n")

    elif user_choice == "3":
        with open("homeinventory.json", "w") as fhandle:
            json.dump(inventory, fhandle)
        print("\n\n==================================================\n")
        print("Thank you for using the Home Inventory Tool v1.0. Goodbye!")
        print("\n==================================================\n")
        running = False
######################################################################

# homeinventory.py
