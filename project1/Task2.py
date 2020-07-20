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

timeDict = {}
for phone in calls:
    if phone[0] in timeDict:
        timeDict[phone[0]] += int(phone[3])
    else:
        timeDict[phone[0]] = int(phone[3])
    if phone[1] in timeDict:
        timeDict[phone[1]] += int(phone[3])
    else:
        timeDict[phone[1]] = int(phone[3])

max_call_time = 0
max_telephone_num = ''

for phone in timeDict:
    if timeDict[phone] >= max_call_time:
        max_call_time = timeDict[phone]
        max_telephone_num = phone

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(
        max_telephone_num, max_call_time))