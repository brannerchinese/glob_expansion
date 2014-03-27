# regex_parser.py
# David Prager Branner
# 201400326

"""Parse regex string expression and produce formal representation.

Presently handled:

    Single characters, explicitly shown.
    Character sets within square brackets [...], all explicitly shown.
    Groups of characters or character sets.

Planned:
    Disjunction (|).
    Zero or one (?).
    Zero or more (*).
    Any character (.).
"""

from collections import deque
import regex_node as N

def main(s):
    return preparse(deque(s))[1]

def preparse(q, output=None, charset=False):
    """Change flat input deque to nested deque, nesting groups and char-sets."""
    if output == None:
        output = []
    while q:
        c = q.popleft()
        # Group: treat as sublist.
        if c == ')' and not charset:
            break
        elif c == '(' and not charset:
            q, temp_output = preparse(q)
            output.append(temp_output)
        # Character set: treat as sublist containing series of ORs.
        elif c == '[' and not charset:
            q, temp_output = preparse(q, charset=True)
            output.append(temp_output)
            charset = False
        elif c == ']' and charset:
            # If end of character set, remove last OR.
            output.pop()
            break
        elif charset:
            output.extend([c, '|'])
        # Handle undifferentiated single character as last resort.
        else:
            output.append(c)
    return q, output

def make_objects(q):
    """Convert deque-output of preparse() to list of Node-objects."""
    output = []
    branch_dict = {
            '*': N.Star,
            '|': N.Or,
            '?': N.Question,
            '.': N.Period,}
    for item in q:
        # Skip empty items.
        if len(item) == 0:
            continue
        # Send sublists to recursion.
        if len(item) > 1:
            output.append(make_objects(item))
        # Simplify redundantly nested single items such as [[2]] => 2.
        while isinstance(item, list):
            item = item[0]
        # Special characters.
        if item in branch_dict:
            output.append(branch_dict[item](item))
        # Single character.
        output.append(N.Literal(item))
    return output
