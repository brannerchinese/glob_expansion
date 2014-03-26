# regex_parser.py
# David Prager Branner
# 201400326

"""Parse regex string expression and produce formal representation."""

from collections import deque

def main(s):
    return preparse(deque(s))[1]

def preparse(q, output=None, group=False):
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
        elif c == '[' and not group:
            q, temp_output = preparse(q, group=True)
            output.append(temp_output)
            group = False
        # Character set: treat as sublist containing series of ORs.
        elif c == ']' and group:
            # If end of character group, remove last OR.
            output.pop()
            break
        elif group:
            output.extend([c, '|'])
        else:
            output.append(c)
    return q, output
