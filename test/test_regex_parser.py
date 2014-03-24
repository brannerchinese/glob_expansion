import regex_parser as P

def test_preparse_01():
    assert P.preparse('abc') == ['a', 'b', 'c']

def test_preparse_02():
    assert P.preparse('a(b)c') == ['a', ['b'], 'c']

def test_preparse_03():
    assert P.preparse('a(bcd)e') == ['a', ['b', 'c', 'd'], 'e']

def test_preparse_04():
    assert P.preparse('a(bc)de') == ['a', ['b', 'c'], 'd', 'e']

def test_preparse_05():
    assert P.preparse('a(bcde)') == ['a', ['b', 'c', 'd', 'e']]

def test_preparse_06():
    assert P.preparse('(abcde)') == [['a', 'b', 'c', 'd', 'e']]

def test_preparse_07():
    assert P.preparse('a(b)c(d)e') == ['a', ['b'], 'c', ['d'], 'e']

def test_preparse_08():
    assert P.preparse('a(bc)(d)e') == ['a', ['b', 'c'], ['d'], 'e']

def test_preparse_09():
    assert P.preparse('a(b(c)d)e') == ['a', ['b', ['c'], 'd'], 'd']

def test_preparse_10():
    assert P.preparse('a(b(cd))e') == ['a', ['b', ['c', 'd']], 'd']

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
