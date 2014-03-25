# regex_parser.py
# David Prager Branner
# 20140322

# to do: escaped characters

"""Convert input regex string to normalized form."""

from collections import deque
import pprint

class Counter():
    def __init__(self):
        self.counter = 0
        self.total = 0

def preparse(s, counter=None):
    if counter == None:
        counter = Counter()
        counter.total = len(s)
    cursor = 0
    output = []
    length_last_output = len(output)
    while cursor < len(s) and counter.counter < counter.total:
        c = s[cursor]
        counter.counter += 1
        cursor += 1
        if c == ')':
            return output
        elif c == '(':
            output.append(preparse(s[cursor:], counter))
            cursor += counter.counter - length_last_output - 1
        else:
            output.append(c)
        length_last_output = len(output)
    return output
