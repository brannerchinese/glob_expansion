# regex_parser.py
# David Prager Branner
# 20140322

"""Convert input regex string to normalized form."""

from collections import deque
import inspect
import pprint

#def parse(pattern):
#    """Convert regex pattern to FSM."""
#    # Instantiate FSM.
#    fsm = FSM()
#    branches = {
#            '|': self.either(*args),
#            '?': self.question(*args),
#            '*': self.star(*args),
#            }
#    # Traverse regex pattern and concatenate FSMs for each element.
#    for operator in pattern:
#        fsm = fsm.concatenate(fsm, branches[operator](*args)
#    # Return resulting FSM.
#    return fsm

Class Run():
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
            }
    while q:
        c = q.popleft()
        if c not in process:
            n.append(literal(n, c))
        else:
            n.append(process[n])
    pprint.pprint(n)

def open_substring(c):
    # begin new run
    return (c, '(')

def close_substring(c):
    # end run and process
    # next substring concatenates
    return (c, ')')

def disjunction(c):
    # end run and begin new run, after which perform disjunction of substring
    return (c, '|')

def open_group(c):
    # begin series of disjunctions
    return (c, '[')

def close_group(c):
    # end series of disjunctions
    # next substring concatenates
    return (c, ']')

def star(c):
    # next substring concatenates
    return (n, '*')

def literal(n, c):
    # next substring concatenates
    if n:
        return concatenate(n, (c, 'lit'))
    else:
        return (c., 'lit')

def concatenate(n, m):
    return (n, (m), 'concat')

