import regex_parser as P


def test_concat_01():
    s = P.Sequence('ab')
    assert s.normalize() == (('a', 'lit'), ('b', 'lit'), '_')

def test_concat_02():
    s = P.Sequence('abcd')
    assert s.normalize() == (
            (
                (
                    ('a', 'lit'), ('b', 'lit'), '_'), 
                ('c', 'lit'), '_'), 
            ('d', 'lit'), '_')
