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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.


Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def get_code(call):
    if call.startswith("("):
        return call.split(")")[0] + ")"
    elif call[0] in ["7", "8", "9"]:
        return call[0:4]
    elif call.startswith("140"):
        return "140"
    else:
        return None


codes = {}
print("The numbers called by people in Bangalore have codes:")
for call in calls:
    incoming_call = call[0]
    if incoming_call.startswith("(080)"):
        answering_call = call[1]
        code = get_code(answering_call)
        if code is not None and code not in codes:
            print(code)
            codes[code] = 0


calls_from_bangalore_count = 0
calls_to_bangalore_count = 0
for call in calls:
    incoming_call = call[0]
    if incoming_call.startswith("(080)"):
        calls_from_bangalore_count += 1
        answering_call = call[1]
        if answering_call.startswith("(080)"):
            calls_to_bangalore_count += 1

print("{0:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
    calls_to_bangalore_count * 100 / calls_from_bangalore_count))
