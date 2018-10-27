import datetime
import os


# Clear screen function
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Display Menu
def display_main_menu():
    menu_option = 0
    while menu_option != 3:
        clear_screen()
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
            # Potential issue with quitting?
            elif menu_option == 3:
                break
        except ValueError:
            print("That is not a valid option, please enter a number from the menu")

# Add entry function
def add_entry():
    clear_screen()
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
    clear_screen()
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
    clear_screen()
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
    # Add matching results to search_results
    for item in task_list:
        if item["date"] == search_date:
            search_results.append(item)
    display_entry(search_results, result_count)

# Search Date Range function
def date_range_search():
    clear_screen()
    # Get Start Date
    start_date = input("Enter the start date (MM/DD/YYYY): ")
    # Get End Date
    end_date = input("Enter the end date (MM/DD/YYYY): ")
    # Call display entries
# Time Spent function
def time_spent_search():
    clear_screen()
    # Get time spent (in minutes)
    time_spent = input("Enter the time spend (in minutes): ")
# Exact Search function
def exact_string_search():
    clear_screen()
    # Get word or phrase to search for
    search_string = input("Enter a word or phrase to search for: ")
# Regex Pattern function
def regex_search():
    clear_screen()
    # Get the Regex pattern to search for
    search_pattern = input("Enter a regular expression pattern to search for: ")
# Display Entry function
def display_entry(search_results, result_count):
    clear_screen()
    # Add check for end or beginning of search_results
    current_entry = search_results[result_count]

    print("Task Name: {}".format(current_entry["task"]))
    print("Date: {}".format(current_entry["date"]))
    print("Time Spent: {}".format(current_entry["time"]))
    print("Notes: {}\n".format(current_entry["notes"]))

    print("[N]ext\t[E]dit\t[D]elete\t[P]revious")
    print("[R]eturn to search menu")

    choice = input()
    entry_navigation(choice, result_count, current_entry)

# Entry Navigation function
def entry_navigation(choice, result_count, current_entry):
    if choice.upper() == "N":
        result_count += 1
        display_entry(search_results, result_count)
    elif choice.upper() == "E":
        edit_entry(current_entry, task_list)
    elif choice.upper() == "D":
        delete_entry(current_entry, task_list)
    elif choice.upper() == "P":
        result_count -= 1
        display_entry(search_results, result_count)
    elif choice.upper() == "R":
        display_search_menu()

# Delete Entry function
def delete_entry(current_entry, task_list):
    # How to delete this from task_list?
    # Check for match of current entry against task_list entries?
    pass

# Edit Entry function
def edit_entry(current_entry, task_list):
    #check current entry against task_list
    #edit match 
    pass

# Read / Open File Function
# Write / Cloase File Function

if __name__ == "__main__":
    task_list = []
    search_results = []
    result_count = 0
    display_main_menu()

          

