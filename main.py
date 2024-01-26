"""
Python script to help graphic designers
with arranging pages of a booklet so they 
can be printed with backing and adjacent 
pages in the right order. 
"""
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
response_text = "Hurray!!"
print(response_text, clean_num_pages, "Pages")

# If the result will include blank pages, present user with further options:
    # Where they want the blank pages (at the begining, at the end)
    # Whether they can get rid of a certain number of pages or not.

input()