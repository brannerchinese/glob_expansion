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
        print('counter: {}; cursor: {} of {}; char: {}'.
                format(counter.counter,  cursor,  len(s) - 1, c))
        counter.counter += 1
        cursor += 1
        if c == ')':
            print('  ) returning:')
            return output
        elif c == '(':
            print('  (; recoursing with ', s[cursor:])
            output.append(preparse(s[cursor:], counter))
            print('   ', output, 'counter:', counter.counter, 'on return')
            print('    increase cursor from', cursor, 'to', end=' ')
            cursor += counter.counter - length_last_output - 1
            print(cursor)
        else:
            output.append(c)
            print('  c', c)
            print('    counter:', counter.counter)
        length_last_output = len(output)
        print('    output now:', output)
        print('    counter:', counter.counter, 'len(s)', len(s))
    print('    cursor: {}, len(s): {}'.format(cursor, len(s)))
    return output
