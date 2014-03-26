# regex_parser.py
# David Prager Branner
# 201400326

"""Parse regex string expression and produce formal representation.

Presently handled:

    Single characters, explicitly shown.
    Character sets within square brackets [...], all explicitly shown.
    Groups of characters or character sets.
"""

from collections import deque

def main(s):
    return preparse(deque(s))[1]

def preparse(q, output=None, group=False):
    """Change flat input deque to nested deque, nesting groups and char-sets."""
    if output == None:
        output = []
    while q:
        c = q.popleft()
        # Group: treat as sublist.
        if c == ')' and not group:
            break
        elif c == '(' and not group:
            q, temp_output = preparse(q)
            output.append(temp_output)
        # Character set: treat as sublist containing series of ORs.
        elif c == '[' and not group:
            q, temp_output = preparse(q, group=True)
            output.append(temp_output)
            group = False
        elif c == ']' and group:
            # If end of character set, remove last OR.
            output.pop()
            break
        elif group:
            output.extend([c, '|'])
        # Handle undifferentiated single character as last resort.
        else:
            output.append(c)
    return q, output

def make_objects(q):
    """Convert deque-output of preparse() to list of Node-objects."""
