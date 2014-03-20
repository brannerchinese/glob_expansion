# object_constructors.py
# David Prager Branner
# 20140320

class State():
    """Model a node in an FSM."""
    def __init__(self, accepting=False, label=None):
        # Appending and removing transitions to be done manually with 
        # list.append() and list.remove().
        self.transitions = set()
        self.accepting = accepting
        self.label = label

class Transition():
    """Model a transition (conditioned or epsilon) in an FSM."""
    def __init__(self, char=None, origin, destination):
        # char=None for epsilon: an unconditioned transition.
        self.char = char
        self.origin = origin
        self.destination = destination

class FSM():
    """Construct finite state machine."""
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def concatenate(self, fsm1, fsm2):
        # Epsilon transition between fsm1 and fsm2.
        self.start.transitions.append(Transition(fsm1.end, fsm2.start))

    def union(self, fsm1, fsm2):
        pass

    def question(self, fsm):
        pass

    def star(self, fsm):
        pass
