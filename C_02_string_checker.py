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

payment_ans = ("cash", "credit")

want_instructions = string_checker("Show instructions? ")
print(f"Chose {want_instructions}")
pay_method = string_checker("Payment method: ", 2, payment_ans)
print(f"Chose {pay_method}")