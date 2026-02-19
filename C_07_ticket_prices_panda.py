import pandas

# functions
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

def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Please enter an answer.\n")

def int_check(question, low, high):
    """Checks users enter an integer between two values"""
    error = f"Please enter a valid number"
    while True:
        try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

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

def currency(a):
    return "${:.2f}".format(a)

# variables & lists
payment_ans = ('cash', 'credit')
child_price = 7.50
adult_price = 10.50
senior_price = 6.50
credit_surcharge = 0.05

all_names = []
all_ticket_costs = []
all_surcharges = []

mini_movie_dict = {
    'Name': all_names,
    'Ticket Price': all_ticket_costs,
    'Surcharge': all_surcharges
}

# main routine
while True:
    print()

    name = not_blank("Name: ")
    if name == "xxx":
        break

    age = int_check("Age: ", 0, 120)

    if age < 12:
        print(f"{name} is too young")
        continue
    elif age < 16:
        ticket_price = child_price
    elif age < 65:
        ticket_price = adult_price
    elif age < 101:
        ticket_price = senior_price
    else:
        print(f"{name} is too old")
        continue

    pay_method = string_checker("Payment method: ", 2, payment_ans)

    if pay_method == "cash":
        surcharge = 0
    else:
        surcharge = ticket_price * credit_surcharge

    total_pay = ticket_price + surcharge

    all_names.append(name)
    all_ticket_costs.append(ticket_price)
    all_surcharges.append(surcharge)

mini_movie_frame = pandas.DataFrame(mini_movie_dict)

mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

print(mini_movie_frame.to_string(index=False))
print(f"\nTotal Paid: ${total_paid:.2f}")
print(f"Total Profit: ${total_profit:.2f}")
