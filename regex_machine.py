# regex_machine.py.py
# David Prager Branner
# 20140328

class Machine:
    def __init__(self, data):
        self.data = data

    def matcher(self, q):
        """Match leftmost item of q against Machine."""
        pass

class Or(Machine):
    pass

class Star(Machine):
    pass

class Period(Machine):
    pass

class Question(Machine):
    pass

class Literal(Machine):
    pass

