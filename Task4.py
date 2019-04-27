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
telemarketers = set()
white_list = set()

for call in calls:
    white_list.add(call[1])

for text in texts:
    white_list.update([text[0], text[1]])


def is_telemarketer(phone_number):
    if phone_number.startswith("140"):
        return True
    if phone_number not in white_list:
        return True
    return False


for call in calls:
    outgoing_call = call[0]

    if is_telemarketer(outgoing_call):
        telemarketers.add(outgoing_call)

for telemarketer in sorted(telemarketers):
    print(telemarketer)
