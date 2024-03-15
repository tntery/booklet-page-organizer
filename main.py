"""

A Python script to help graphic designers
with arranging pages of a booklet so they 
can be printed with backing and adjacent 
pages in the right booklet order.

v 0.1

Author: Tawanda Terrence Nyamakope
Github: @tntery
X: @tntery21

"""

import time

def get_blank_pages_info_string(num_blank_pages: int) -> str:
    """
    Returns a string explaining the required number of blank pages.

    @param:num_blank_pages - An intenger representing the number of blank pages.

    """

    return f"\nYou will need to add {num_blank_pages} more page(s) to your document or {num_blank_pages} blank page(s) at the end of your document so the booklet has enough pages to back each other out."

def get_page_layout_heading_string(capitalize: bool = False) -> str:
    """ 
    Returns a string to use as an informative heading to explain how to interpret the proposed page layout info.
    
    @param:capitalize - A boolean to determine whether to capitalize the string or not.

    """

    heading_string = f"you can lay the following pages on the same sheet, one to the left and the other to the right (e.g 1 <-> 2 means page 1 to the left and page 2 to the right), then back that sheet with the '3 <-> 4' pages combination. \n\nBelow are your page combinations:\n"
    if capitalize:
        heading_string = f"\n{heading_string}"
        return heading_string.title()
    else:
        return heading_string

def arrange_pages(total_num_pages :int) -> str:
    """
    Returns nicely formatted page combination and backing information from the supplied total number of pages.

    @param:total_num_pages - total number of pages for the booklet.

    """
    pages_list = []
    for i in range(1, total_num_pages + 1):
        pages_list.append(i)

    arrangement_string = ""

    count = 0

    while len(pages_list) > 0:

        if count % 2 == 0:
            arrangement_string += f"|> {pages_list[-1]} <|> {pages_list[0]} <|\n"
            print(pages_list[-1], pages_list[0])
        else:
            arrangement_string += f"|> {pages_list[0]} <|> {pages_list[-1]} <|\n"
            print(pages_list[0], pages_list[-1])

        pages_list.remove(pages_list[0])
        pages_list.remove(pages_list[-1])
        count += 1

        if count % 2 == 0:
            arrangement_string += "\n"

        

    return arrangement_string

def main():

    # Get initial user input

    clean_num_pages = 0
    input_error = False

    while True:

        if input_error:
            num_pages = input("Please enter a VALID number for total number of pages on your document (Greater than 0)")
        else:
            num_pages = input("Please enter total number of pages on your document. \n(Must be a number greater than 0):")

        # Try and convert input to number and break if input is valid
        try:
            clean_num_pages = int(num_pages)
            if clean_num_pages > 0:
                input_error = False
                break
            else:
                print("Please enter a valid number of pages (Greater than 0)")
        except Exception as e:
            input_error = True
            print("Exception", e)

    # Compute and return results.
            
    output_msgs_list = []
    total_inclusive_pages = 0

    if clean_num_pages < 4:
        total_inclusive_pages = 4
        num_blank_pages_to_add = 4 - clean_num_pages

        output_msgs_list.append(get_blank_pages_info_string(num_blank_pages_to_add))
        output_msgs_list.append(f"\nHaving done that, {get_page_layout_heading_string()}")
        output_msgs_list.append(arrange_pages((total_inclusive_pages)))

    elif clean_num_pages == 4 or clean_num_pages % 4 == 0:
        output_msgs_list.append(get_page_layout_heading_string(True))
        output_msgs_list.append(arrange_pages((clean_num_pages)))
    else:
        num_extra_pages = clean_num_pages % 4
        num_blank_pages_to_add = 4 - num_extra_pages
        total_inclusive_pages = clean_num_pages + num_blank_pages_to_add

        output_msgs_list.append(get_blank_pages_info_string(num_blank_pages_to_add))
        output_msgs_list.append(f"Having done that, {get_page_layout_heading_string()}")
        output_msgs_list.append(arrange_pages((total_inclusive_pages)))
        

    # Output result
    for msg in output_msgs_list:
        print(msg)

main()

# All user the ability to choose if they want to run the program again.
while True:
    rerun_main = input('Would you like to try another booklet? Enter "Y" for YES or "N" for NO:')
    if rerun_main.lower() == "y":
        main()
    elif rerun_main.lower() == "n":
        print("Program will automatically exit in 3 seconds.")
        time.sleep(3)
        break
    else:
        print("INVALID INPUT: Please try again.")
