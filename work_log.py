import datetime
import os


# Clear screen function
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Display Menu
def display_main_menu():
    menu_option = 0
    while menu_option != 3:
        #clear screen
        #clear_screen()
        print("""Work Log
        Menu:
        1) Add new entry
        2) Search entries
        3) Quit
        """)
        # Get menu option from user
        menu_option = int(input("Please select a menu option: "))
        try:
            if menu_option < 1 or menu_option > 3:
                print("That is not a valid option, please enter a number from the menu")
            if menu_option == 1:
                # Call add entry function
                new_entry = add_entry()
                #add new entry to task_list
                task_list.append(new_entry)
            elif menu_option == 2:
                # Call search menu function
                display_search_menu()
            elif menu_option == 3:
                break
        except ValueError:
            print("That is not a valid option, please enter a number from the menu")

# Add entry function
def add_entry():
    # Get Task Name
    task_name = input("Task name: ")
    # Get Date (from user or system?)
    now = datetime.datetime.now()
    task_date = now.strftime("%m/%d/%Y")
    # Get Time Spent
    task_duration = input("Time spent (in minutes): ")
    # Get Notes
    task_notes = input("Task notes (optional, press Enter to skip): ")
    task = {"task": task_name,
            "date": task_date,
            "time": task_duration,
            "notes": task_notes
           }
    return task
    
# Search entries menu
def display_search_menu():
    search_option = 0
    print("""Search Menu:
    1) Exact Date
    2) Date Range
    3) Time Spent
    4) Exact Search
    5) Regex Pattern
    6) Return to Main Menu
    """)
    # Get search option from user
    search_option = int(input("Please select a search option: "))
    try:
            if search_option < 1 or search_option > 6:
                print("That is not a valid option, please enter a number from the menu")
            if search_option == 1:
                date_search()
            elif search_option == 2:
                date_range_search()
            elif search_option == 3:
                time_spent_search()
            elif search_option == 4:
                exact_string_search()
            elif search_option == 5:
                regex_search()
            elif search_option == 6:
                display_main_menu()
    except ValueError:
        print("That is not a valid option, please enter a number from the menu")
        

# Search Exact Date function
def date_search():
    # List dates
    unique_dates = []
    for item in task_list:
        if item["date"] in unique_dates:
            continue
        else:
            unique_dates.append(str(item["date"]))
        #print(item["date"])
    #print(unique_dates)
    for item in unique_dates:
        print(item)
    # Get Date
    search_date = input("Enter date to search for (MM/DD/YYYY): ")
    # Call display entry w/ search date
# Search Date Range function
def date_range_search():
    # Get Start Date
    start_date = input("Enter the start date (MM/DD/YYYY): ")
    # Get End Date
    end_date = input("Enter the end date (MM/DD/YYYY): ")
    # Call display entries
# Time Spent function
def time_spent_search():
    # Get time spent (in minutes)
    time_spent = input("Enter the time spend (in minutes): ")
# Exact Search function
def exact_string_search():
    # Get word or phrase to search for
    search_string = input("Enter a word or phrase to search for: ")
# Regex Pattern function
def regex_search():
    # Get the Regex pattern to search for
    search_pattern = input("Enter a regular expression pattern to search for: ")
# Display Entry function
    # Task Name:
    # Date:
    # Time Spent:
    # Notes:
    # Result # of Total#
    # Next
    # Edit
    # Delete
    # Previous
    # Return to Search Menu
# Delete Entry function
# Edit Entry function

# Read / Open File Function
# Write / Cloase File Function

if __name__ == "__main__":
    task_list = []
    search_results = []
    display_main_menu()

          

