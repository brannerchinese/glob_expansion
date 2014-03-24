# regex_parser.py
# David Prager Branner
# 20140322

# to do: escaped characters

"""Convert input regex string to normalized form."""

from collections import deque
import inspect
import pprint

def preparse(s):
    output = []
    for c in s:
        if c == ')':
            return output
        if c == '(':
            output.append(preparse(s[1:]))
        else:
            output.append(c)


class Sequence:
    def __init__(self, s):
        self.out_seq = []
        self.in_q = deque(s)
        self.is_substring = False
        self.c = ''

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
            self.c = self.in_q.popleft()
            print(self.c)
            if self.c not in process:
                self.out_seq.append(self.literal(self.c))
            else:
                self.out_seq.append(process[self.c]())
            print(self.out_seq)
#        pprint.pprint('As list: {}'.format(self.out_seq)) # debug
        return self.concatenate()

    def open_substring(self):
        """Begin recursive normalization of substring, to be stopped by ')'."""
        # Haven't thought this out, but each () pair should be handled by
        # stack.
        substring = Sequence(self.in_q)
        substring.is_substring = True
        normalized = normalize(substring)
        substring.is_substring = False


    def close_substring(self):
        return

    def disjunction(self):
        # end run and begin new run, after which perform disjunction of substring
        return (c, '|')

    def open_group(self):
        # begin series of disjunctions
        pass

    def close_group(self):
        # end series of disjunctions
        # next substring concatenates
        substring_open = False
        return (c, ']')

    def star(self):
        return (self, '*')

    def literal(self, c):
        return (c, 'lit')

    def start_string(self, c):
        pass

    def end_string(self, c):
        pass

    def any_char(self, c):
        pass

    def concatenate(self):
        if isinstance(self.out_seq, tuple):
            return self.out_seq
        else:
            concatenated = (self.out_seq[0])
            for item in self.out_seq[1:]:
                concatenated = (concatenated, item, '_')
            return concatenated

