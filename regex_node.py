# regex_node.py
# David Prager Branner
# 20140326

class Node:
    def __init__(self, data):
        self.data = data

class Or(Node):
    pass

class Star(Node):
    pass

class Period(Node):
    pass

class Question(Node):
    pass

class Literal(Node):
    pass

