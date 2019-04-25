"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""


class PhoneBook:
    def __init__(self):
        self.phone_numbers = {}

    def add_number(self, number):
        if number not in self.phone_numbers:
            self.phone_numbers[number] = 0

    def get_count(self):
        return len(self.phone_numbers.keys())


phone_book = PhoneBook()

for text in texts:
    phone_book.add_number(text[0])
    phone_book.add_number(text[1])
for call in calls:
    phone_book.add_number(call[0])
    phone_book.add_number(call[1])


print("There are {0} different telephone numbers in the records.".format(
    phone_book.get_count()))
