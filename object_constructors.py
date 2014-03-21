# object_constructors.py
# David Prager Branner
# 20140320

class State():
    """Model a state as a node in an FSM."""
    def __init__(self, accepting=False, label=None):
        # Appending and removing transitions to be done manually with 
        # list.append() and list.remove().
        self.transitions = set()
        self.accepting = accepting
        # Labels not implemented now.
        self.label = label

    # Functions to construct atomic submachines and add them to a state's
    # transitions
    def concatenate(self, fsm1, fsm2):
        # Epsilon transition between fsm1 and fsm2.
        self.start.transitions.append(Transition(fsm1.end, fsm2.start))

    def disjunction(self, fsm1, fsm2):
        self.start.transitions.append()
        pass

    def question(self, fsm):
        pass

    def star(self, fsm):
        pass

class Transition():
    """Model a transition (conditioned or epsilon) in an FSM."""
    def __init__(self, char=None, origin, destination):
        # char=None for epsilon: an unconditioned transition.
        self.char = char
        self.origin = origin
        self.destination = destination

class FSM():
    """Construct finite state machine. Machine may contain sub-machines."""
    def __init__(self, start, end, *states):
        self.states = set(tuple(*states))
        # Start and end refer to the start and end of the FSM, which may be a
        # sub-machine. "End" is not intrinsically an accept state.
        self.start = start
        self.end = end

    def add_states(self, *states):
        self.states.update(states)

