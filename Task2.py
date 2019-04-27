from collections import defaultdict
"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


class Records:
    def __init__(self):
        self.curr_highest_num = None
        self.curr_highest_time = 0
        self.records = defaultdict(int)

    def add_record(self, phone_num, time):
        self.records[phone_num] += time

        if self.records[phone_num] > self.curr_highest_time:
            self.curr_highest_time = self.records[phone_num]
            self.curr_highest_num = phone_num


records = Records()

for call in calls:
    time_spent = int(call[3])
    records.add_record(call[0], time_spent)
    records.add_record(call[1], time_spent)

print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(
    records.curr_highest_num, records.curr_highest_time))
