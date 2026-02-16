def statement_generator(statement, decoration, amount):
    """Emphasises headings by adding decoration at the start and end"""
    print(f"{decoration * amount} {statement} {decoration * amount}")