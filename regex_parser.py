# regex_parser.py
# David Prager Branner
# 20140319

def parse(pattern):
    """Convert regex pattern to FSM."""
    # Instantiate FSM.
    fsm = FSM()
    branches = {
            '|': self.union(*args),
            '?': self.question(*args),
            '*': self.star(*args),
            }
    # Traverse regex pattern and concatenate FSMs for each element.
    for operator in pattern:
        fsm = fsm.concatenate(fsm, branches[operator](*args)
    # Return resulting FSM.
    return fsm
