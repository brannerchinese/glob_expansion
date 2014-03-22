# regex_objects.py
# David Prager Branner
# 20140320

""""""

import heapq

class State():
    """Model a state as a node in an FSM."""
    def __init__(self, accepting=False, label=None, fail=False):
        # transitions is a set, but must be converted to list before use.
        self.transitions = set()
        self.accepting = accepting
        self.fail = fail
        # Labels not implemented now.
        self.label = label

    # Functions to construct atomic submachines and add them to a state's
    # transitions
    def concatenate(self, char, dest):
        """Epsilon transition between self and dest."""
        self.transitions.append(Transition(self, dest))

    def disjunction(self, chars_and_dests):
        """Two (or more) conditioned transitions between self and dests."""
        for char, dest in chars_and_dests:
            self.transitions.append(Transition(self, char, dest))

    def question(self, dest):
        """Both conditioned and epsilon transitions between self and dest."""
        self.transitions.append(Transition(self, dest))
        self.transitions.append(Transition(self, char, dest))

    def star(self, state1):
        """Epsilon transition to dest and conditioned transition to self."""
        self.transitions.append(Transition(self, dest))
        self.transitions.append(Transition(self, char, self))

class Transition():
    """Model a transition (conditioned or epsilon) in an FSM."""
    def __init__(self, destination, char=None):
        # char=None for epsilon: an unconditioned transition.
        self.char = char
        self.destination = destination

class FSM():
    """Construct finite state machine. Machine may contain sub-machines."""
    def __init__(self, start, end, *states):
        # Start has epsilon transition to one or more actual states.
        self.start = start
        # One or more actual states have epsilon transitions to end.
        self.end = end
        self.states = set(tuple(*states))

    def add_states(self, *states):
        self.states.update(states)

    def find_unreachable(self):
        """Report any unreachable states."""
        pass

    def find_hopeless(self):
        """Report any states from which an accept state is not reachable."""
        pass
