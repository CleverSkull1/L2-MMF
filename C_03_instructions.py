def string_checker(question, num_letters=1, valid_ans=("yes", "no")):
    """Checks that users enter a full word
     or the 'n' letters of a word from a list of valid responses"""

    while True:
        response = input(question).lower()

        for item in valid_ans:
            if response == item:
                return item
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans}")

def statement_generator(statement, decoration, amount):
    """Emphasises headings by adding decoration at the start and end"""
    print(f"{decoration * amount} {statement} {decoration * amount}")

def instructions():
    statement_generator("Instructions", "ℹ️", 1)
    print('''
    
For each ticket holder enter:
- Their name
- Their age
- The payment method (cash / credit)

The program will record the ticket sale and calculate the
ticket cost and profit

Once you have either sold all of the tickets or entered the 
exit code ('exit8'), the program will display the ticket 
sales information and write the data to a text file.

It will also choose one lucky ticket holder who wins the draw.
Their ticket is free.

    ''')

# main routine
statement_generator("Mini-Movie Fundraiser", "🍿", 3)

print()
want_instructions = string_checker("Show instructions? ")

if want_instructions == "yes":
    instructions()

print()
print("continue")