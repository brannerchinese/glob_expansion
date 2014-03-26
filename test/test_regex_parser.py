import regex_parser as P

def test_main_01():
    assert P.main('abc') == ['a', 'b', 'c']

def test_main_02():
    assert P.main('a(b)c') == ['a', ['b'], 'c']

def test_main_03():
    assert P.main('a(bcd)e') == ['a', ['b', 'c', 'd'], 'e']

def test_main_04():
    assert P.main('a(bc)de') == ['a', ['b', 'c'], 'd', 'e']

def test_main_05():
    assert P.main('a(bcde)') == ['a', ['b', 'c', 'd', 'e']]

def test_main_06():
    assert P.main('(abcde)') == [['a', 'b', 'c', 'd', 'e']]

def test_main_07():
    assert P.main('a(b)c(d)e') == ['a', ['b'], 'c', ['d'], 'e']

def test_main_08():
    assert P.main('a(bc)(d)e') == ['a', ['b', 'c'], ['d'], 'e']

def test_main_09():
    assert P.main('a(b(c)d)e') == ['a', ['b', ['c'], 'd'], 'e']

def test_main_10():
    assert P.main('a(b(cd))e') == ['a', ['b', ['c', 'd']], 'e']

def test_main_11():
    assert P.main('a(b(c))(d)e') == ['a', ['b', ['c']], ['d'], 'e']

def test_main_12():
    assert P.main('a(b((c)))(d)e') == ['a', ['b', [['c']]], ['d'], 'e']

#s = P.Sequence('ab')
#
#def test_literal_01():
#    assert s.in_q[0] == 'a'
#
#def test_literal_02():
#    assert s.literal(s.in_q[0]) == ('a', 'lit')
#
#def test_concat_01():
#    assert s.normalize() == (('a', 'lit'), ('b', 'lit'), '_')
#
#def test_concat_02():
#    s = P.Sequence('abcd')
#    assert s.normalize() == (
#            (
#                (
#                    ('a', 'lit'), ('b', 'lit'), '_'), 
#                ('c', 'lit'), '_'), 
#            ('d', 'lit'), '_')
