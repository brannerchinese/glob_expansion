# regex_parser.py
# David Prager Branner
# 20140322

"""Convert input regex string to normalized form."""

from collections import deque
import inspect
import pprint

class Run():
    def __init__(self):
        self.run = []

def normalize(s):
    q = deque(s)
    # n: normalized regex string; now list, later nested tuple
    n = []
    process = {
            '(': open_substring,
            ')': close_substring,
            '|': disjunction,
            '[': open_group,
            ']': close_group,
            '*': star,
            '?': disjunction,
            '^': start_string,
            '$': end_string,
            '.': any_car,
            }
    concatenate_me = ()
    while q:
        c = q.popleft()
        if c not in process:
            n.append(literal(n, c))
        else:
            n.append(process[n])
    pprint.pprint(n)

def open_substring(c):
    # begin new run
    substring_open = False
    return (c, '(')

def close_substring(c):
    # end run and process
    # next substring concatenates
    substring_open = False
    return (c, ')')

def disjunction(c):
    # end run and begin new run, after which perform disjunction of substring
    return (c, '|')

def open_group(c):
    # begin series of disjunctions
    substring_open = False
    return (c, '[')

def close_group(c):
    # end series of disjunctions
    # next substring concatenates
    substring_open = False
    return (c, ']')

def star(c):
    # next substring concatenates
    substring_open = True
    return (n, '*')

def literal(n, c):
    # next substring concatenates
    substring_open = True
    if n:
        return concatenate(n, (c, 'lit'))
    else:
        return (c, 'lit')

def start_string(c):
    pass

def end_string(c):
    pass

def any_car(c):
    pass


def concatenate(n, m):
    substring_open = False
    return (n, (m), 'concat', substring_open)

