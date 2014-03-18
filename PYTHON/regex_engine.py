#!python3
# regex_engine.py
# David Prager Branner
# 20140318

class Machine():
    def _init_(self):
        self.start = None
        self.end = None
        self.states = set()

class State():
    def _init_(self):
        self.matching = False
        self.conditions = []

class Condition():
    def _init_(self, condition, target_state):
        self = (condition, target_state)

def main():
    m = Machine()
    match = False
    #
    # construct machine using series of calls to add_state and add_condition;
    # use states and transitions from STDIN or file
    #
    # get input string from STDIN or file
    #
    # return match
    return match

def add_state(state):
    pass

def del_state(state):
    pass

def add_condition(state, condition):
    pass

def del_condition(state, condition):
    pass

