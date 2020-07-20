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

#All calls from Bangalore numbers
def bangalore_call(call):
    return call[0][:5] == '(080)'


def get_areacode(call):
    call_to = call[1]

    # Fix land case
    if call_to[:2] == '(0':  
        return call_to.split(sep=')')[0] + ')'

    # Telemarketer case
    if call_to[:3] == '140':  
        return call_to[:3]

    else:  
        # Mobile case
        return call_to[:4]


called_prefix = []

# Part A
for call in calls:
    if bangalore_call(call):
        called_prefix.append(get_areacode(call))

all_called_prefix = list(set(called_prefix))

all_called_prefix.sort()

print("\n The numbers called by people in Bangalore have codes:")
for prefix in all_called_prefix:
    print(prefix)

# Part B
bng_call_num = 0
for prefix in called_prefix:
    if prefix == "(080)":
        bng_call_num += 1

print("\n{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
    round(bng_call_num/len(called_prefix)*100, 2)))



