# regex_parser.py
# David Prager Branner
# 20140322

# to do: escaped characters

"""Convert input regex string to normalized form."""

from collections import deque
import inspect
import pprint

class Sequence:
    def __init__(self, s):
        self.out_seq = []
        self.in_q = deque(s)

    def normalize(self):
        # n: normalized regex string; now list, later nested tuple
        n = []
        process = {
                '(': self.open_substring,
                ')': self.close_substring,
                '|': self.disjunction,
                '[': self.open_group,
                ']': self.close_group,
                '*': self.star,
                '?': self.disjunction,
                '^': self.start_string,
                '$': self.end_string,
                '.': self.any_char,
                }
        concatenate_me = ()
        while self.in_q:
            c = self.in_q.popleft()
            if c not in process:
                self.out_seq.append(self.literal(c))
            else:
                self.out_seq.append(process[n])
        pprint.pprint('As list: {}'.format(self.out_seq))
        return self.concatenate()

    def open_substring(self, c):
        # begin new run
        substring_open = False
        return (c, '(')

    def close_substring(self, c):
        # end run and process
        # next substring concatenates
        substring_open = False
        return (c, ')')

    def disjunction(self):
        # end run and begin new run, after which perform disjunction of substring
        return (c, '|')

    def open_group(self, c):
        # begin series of disjunctions
        substring_open = False
        return (c, '[')

    def close_group(self):
        # end series of disjunctions
        # next substring concatenates
        substring_open = False
        return (c, ']')

    def star(self, s1):
        # next substring concatenates
        substring_open = True
        return (s1, '*')

    def literal(self, c):
        return (c, 'lit')

    def start_string(self, c):
        pass

    def end_string(self, c):
        pass

    def any_char(self, c):
        pass

    def concatenate(self):
        concatenated = (self.out_seq[0])
        for item in self.out_seq[1:]:
            concatenated = (concatenated, item, '_')
        return concatenated

