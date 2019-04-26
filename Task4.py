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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
print("These numbers could be telemarketers: ")
telemarketers = {}
white_list = {}

for call in calls:
    receiving_call = call[1]
    if receiving_call not in white_list:
        white_list[receiving_call] = 0

for text in texts:
    sending_text = text[0]
    receiving_text = text[1]
    if sending_text not in white_list:
        white_list[sending_text] = 0
    if receiving_text not in white_list:
        white_list[receiving_text] = 0


def is_telemarketer(phone_number):
    if phone_number.startswith("140"):
        return True
    if phone_number not in white_list:
        return True
    return False


for call in calls:
    outgoing_call = call[0]

    if outgoing_call not in telemarketers and is_telemarketer(outgoing_call):
        telemarketers[outgoing_call] = 0
        print(outgoing_call)
