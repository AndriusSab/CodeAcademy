# write a python script that adds all the numbers entered in the command line as arguments.
# Throw an error if user enters something other than number

import sys

summary = 0

for arg in sys.argv[1:]:
    try:
        number = float(arg)
        summary += number
    except ValueError:
        print(f"Error: {arg} is not a number")

print(f"Total: {summary}")
