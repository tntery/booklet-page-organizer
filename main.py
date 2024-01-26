"""
Python script to help graphic designers
with arranging pages of a booklet so they 
can be printed with backing and adjacent 
pages in the right order. 
"""

# Ask user to enter number of pages
num_pages = input("Please enter total number of pages on your document:")

response_text = ""

# while True:

try:
    num_blank_pages = int(num_pages) % 4
    response_text = "Hurray!!"
    print(response_text, num_blank_pages)
    # break
except ZeroDivisionError:
    response_text = "Number of pages must be greater than 0"
except Exception as e:
    print("Exception", e)
    response_text = "Please enter a number."

input()

# Calculate and return results.

# If the result will include blank pages, present user with further options:
    # Where they want the blank pages (at the begining, at the end)
    # Whether they can get rid of a certain number of pages or not.