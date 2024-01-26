"""
Python script to help graphic designers
with arranging pages of a booklet so they 
can be printed with backing and adjacent 
pages in the right order. 
"""

def arrange_pages(total_num_pages :int) -> str:
    """
    Returns nicely formatted page combination and backing information from the supplied total number of pages.
    @param:total_num_pages - total number of pages for the booklet.
    """
    pages_list = []
    for i in range(1, total_num_pages + 1):
        pages_list.append(i)

    print("Pages list: ", pages_list)

    arrangement_string = ""

    while len(pages_list) > 0:
        arrangement_string += f"{pages_list[0]} <-> {pages_list[-1]}\n"
        pages_list.remove(pages_list[0])
        pages_list.remove(pages_list[-1])

    return arrangement_string

clean_num_pages = 0
input_error = False

# Ask user to enter number of pages
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

# Calculate and return results.
output_msgs_list = []
total_inclusive_pages = 0

    # For page total below 4
if clean_num_pages < 4:
    total_inclusive_pages = 4
    num_blank_pages = 4 - clean_num_pages

    output_msgs_list.append(f"You will need to add {num_blank_pages} more page(s) to your document or {num_blank_pages} blank pages at the end of your document so the booklet has enough pages to back each other out.")
    output_msgs_list.append("Having done that, you can lay the following pages on the same sheet (one to the left, one to the right, e.g 1 <-> 2), then back that sheet with the '3 <-> 4' pages combination. \n\nBelow are your page combinations:")
    output_msgs_list.append(arrange_pages((total_inclusive_pages)))

else:
    pass

for msg in output_msgs_list:
    print(msg)


# If the result will include blank pages, present user with further options:
    # Where they want the blank pages (at the begining, at the end)
    # Whether they can get rid of a certain number of pages or not.

input()