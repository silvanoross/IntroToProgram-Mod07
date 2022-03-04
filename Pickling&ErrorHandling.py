# ---------------------------------------------------------------------------- #
# Title: Assignment 07 Pickling
# Description: A demo of pickling and structured error-handling in form of a
# program that asks for the type of food that the user wants to pickle and for
# how many days they want to pickle it. The user must enter a minimum of
# a certain number of days and the input must be a number,
# but they can pickle for as long as they would like.
# ChangeLog (Who,When,What):
# SRoss,02/28/2022, Started Assignment 07, began researching pickling
# SRoss,02/28/2022, began pseudocode outline
# SRoss,03/01/2022, finished majority of actual coding
# SROss,03/04/2022, finalized code
# ---------------------------------------------------------------------------- #

# import statement
import pickle

# Data ----------------------------------------------------------------------- #
str_pickle_file = "PicklingFood.dat"
file_pickle = None
lst_pickle = []
#lst_savepickle = []
shelve_obj = ""
str_choice = ""
counter = 0


# Processing  ---------------------------------------------------------------- #
# Pickling Class
class Pickling:
    """  Performs Pickling actions """

    # Pickling Example Functions

    @staticmethod
    def read_pickled_data(file_name, lst_of_dic):
        """ Reads data from binary files as a result of pickling

               :param file_name: (string) with name of file:
               :param list_of_rows: (list) you want filled with file data:
               :return: (list) of dictionary rows
               """
        # Unpickling pickling list
        # Not able to read from the pickled file successfully, not sure why


        try:
            lst_of_dic.clear()
            pickle_file = open(file_name, "rb")
            # Stores data variable with pickled list
            data = pickle.load(pickle_file)

            # creates list of dictionaries
            for line in data:
                item, days = line.split(",")
                row = {"Pickling": item.strip(), "Days": days.strip()}
                lst_of_dic.append(row)
            # closes file
            pickle_file.close()
        except:
            lst_of_dic.clear()
            pickle_file = open(file_name, "wb")
            pickle_file.close()
            print("Nothing to pickle, a new pickling file was created")

        return lst_of_dic

    @staticmethod
    def write_pickled_data_to_file(file_name, lst_of_dic):
        """ Stores a list of dictionaries into a pickled binary file

                       :param file_name: (string) with name of file:
                       :param list_of_rows: (list) you want filled with file data:
                       :return: (list) of dictionary rows
                       """
        print("~~~~~~~ The current foods to Pickle are: ~~~~~~~")
        for row in lst_of_dic:
            print(row["Pickling"] + "(" + row["Days"] + ")")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # Asking for confirmation to save data to a file
        #print(lst_of_dic)
        if ("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):
            # taking a list of dictionaries and dumbing down to a simple list for storage
            # creating a local variable for a list to be compiled
            lst_savepickle = []
            for row in lst_of_dic:
                data = [row["Pickling"], row["Days"], "\n"]
                lst_savepickle.append(data)

            pickle_file = open(file_name, "wb")
            pickle.dump(lst_savepickle, pickle_file)
            pickle_file.close()
            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:
            input("New data was NOT Saved, but previous data still exists! Press\
                          the [Enter] key to return to menu.")
        return lst_of_dic

    @staticmethod
    def add_data_for_pickling(item, days, lst_of_dic):
        """ Adds items to list for pickling

                       :param file_name: (string) with name of file:
                       :param list_of_rows: (list) you want filled with file data:
                       :return: (list) of dictionary rows
                       """
        row = {"Pickling": str(item).strip(), "Days": str(days).strip()}
        lst_of_dic.append(row)
        return lst_of_dic

    @staticmethod
    def remove_pickled_data(item, list_of_dic):
        """ Deletes items from working pickling list

                       :param file_name: (string) with name of file:
                       :param list_of_rows: (list) you want filled with file data:
                       :return: (list) of dictionary rows
                       """
        for row in list_of_dic:
            if row["Pickling"].lower() == item.lower():
                list_of_dic.remove(row)
        return list_of_dic


# Presentation (Input/Output) with structured error- handling ----------------- #
class IO:
    """ Performs Input and Output tasks with Error-Handling """

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
            Menu of Options
            1) Add a new item to Pickle
            2) Remove a item to be Pickled
            3) Save Pickling Data to Binary       
            4) Exit Program
            ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        try:
            choice = int(input("Which option would you like to perform? [1 to 4] - "))
        except ValueError:
            print("please enter a numerical option")
            pass


        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def output_current_pickling_items(lst_of_dic):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current items for Pickling are: *******")
        print(lst_of_dic)
        print("***************************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_pickling_item():
        """  Gets task and priority values to be added to the list

        :return: (string, string) with task and priority
        """
        item = input("Enter the food item you would like to Pickle: ")

        days = input("Enter the enter the number of recommended Pickling days: ")
        return item, days  # maybe needs to be a tuple?

    @staticmethod
    def input_pickle_to_remove():
        """  Gets the task name to be removed from the list

        :return: (string) with task
        """
        item = input("Type in which task you would like to delete: ")
        return item

    # Step 1 - When the program starts, Load data from PicklingFood.dat.


Pickling.read_pickled_data(file_name=str_pickle_file, lst_of_dic=lst_pickle)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.output_current_pickling_items(lst_of_dic=lst_pickle)  # Show current data in the list/table
    IO.output_menu_tasks()  # Shows menu
    try:
        str_choice = str(IO.input_menu_choice())  # Get menu option
        if int(str_choice) <= 4:
            print("you chose option", str_choice)
            pass
    except (ValueError, TypeError):
        print("Make sure to enter a numerical option 1-4")
        pass
    # Step 4 - Process user's menu choice
    if str_choice == '1':  # Add a new Task
        item, days = IO.input_new_pickling_item()
        lst_pickle = Pickling.add_data_for_pickling(item=item, days=days, lst_of_dic=lst_pickle)
        continue  # to show the menu

    elif str_choice == '2':  # Remove an existing Task
        item = IO.input_pickle_to_remove()
        lst_pickle = Pickling.remove_pickled_data(item=item, list_of_dic=lst_pickle)
        continue  # to show the menu

    elif str_choice == '3':  # Save Data to File
        lst_pickle = Pickling.write_pickled_data_to_file(file_name=str_pickle_file, lst_of_dic=lst_pickle)
        print("Data Saved!")
        continue  # to show the menu

    elif str_choice == '4':  # Exit Program
        input("Press the Enter key to quit: ")  # Added a pause to allow for user input
        print("Goodbye!")
        break  # by exiting loop
