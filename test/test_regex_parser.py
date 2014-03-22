import regex_parser as P

s = P.Sequence('ab')

def test_literal_01():
    assert s.in_q[0] == 'a'

def test_literal_02():
    assert s.literal(s.in_q[0]) == ('a', 'lit')

def test_concat_01():
    assert s.normalize() == (('a', 'lit'), ('b', 'lit'), '_')

def test_concat_02():
    s = P.Sequence('abcd')
    assert s.normalize() == (
            (
                (
                    ('a', 'lit'), ('b', 'lit'), '_'), 
                ('c', 'lit'), '_'), 
            ('d', 'lit'), '_')
