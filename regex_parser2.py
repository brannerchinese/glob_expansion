from collections import deque

def main(s):
    return preparse(deque(s))[1]

def preparse(q, output=None):
    if output == None:
        output = []
    while q:
        c = q.popleft()
        if c == ')':
            break
        elif c == '(':
            q, temp_output = preparse(q)
            output.append(temp_output)
        else:
            output.append(c)
    return q, output
