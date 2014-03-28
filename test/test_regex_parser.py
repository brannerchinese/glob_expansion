import regex_parser as P
from collections import deque
import random, string

def test_preparse_01():
    assert P.preparse(deque('abc'))[1] == ['a', 'b', 'c']

def test_preparse_02():
    assert P.preparse(deque('a(b)c'))[1] == ['a', ['b'], 'c']

def test_preparse_03():
    assert P.preparse(deque('a(bcd)e'))[1] == ['a', ['b', 'c', 'd'], 'e']

def test_preparse_04():
    assert P.preparse(deque('a(bc)de'))[1] == ['a', ['b', 'c'], 'd', 'e']

def test_preparse_05():
    assert P.preparse(deque('a(bcde)'))[1] == ['a', ['b', 'c', 'd', 'e']]

def test_preparse_06():
    assert P.preparse(deque('(abcde)'))[1] == [['a', 'b', 'c', 'd', 'e']]

def test_preparse_07():
    assert P.preparse(deque('a(b)c(d)e'))[1] == ['a', ['b'], 'c', ['d'], 'e']

def test_preparse_08():
    assert P.preparse(deque('a(bc)(d)e'))[1] == ['a', ['b', 'c'], ['d'], 'e']

def test_preparse_09():
    assert P.preparse(deque('a(b(c)d)e'))[1] == ['a', ['b', ['c'], 'd'], 'e']

def test_preparse_10():
    assert P.preparse(deque('a(b(cd))e'))[1] == ['a', ['b', ['c', 'd']], 'e']

def test_preparse_11():
    assert P.preparse(deque('a(b(c))(d)e'))[1] == [
            'a', ['b', ['c']], ['d'], 'e']

def test_preparse_12():
    assert P.preparse(deque('a(b((c)))(d)e'))[1] == [
            'a', ['b', [['c']]], ['d'], 'e']

def test_preparse_13():
    assert P.preparse(deque('a[bc]d'))[1] == ['a', ['b', '|', 'c'], 'd']

def test_preparse_14():
    assert P.preparse(deque('a[b[c]d'))[1] == [
            'a', ['b', '|', '[', '|', 'c'], 'd']

def test_preparse_15():
    assert P.preparse(deque('a[b(c]d'))[1] == [
            'a', ['b', '|', '(', '|', 'c'], 'd']

def test_preparse_16():
    assert P.preparse(deque('a[b)c]d'))[1] == [
            'a', ['b', '|', ')', '|', 'c'], 'd']

def test_make_objects_01():
    q = deque('a')
    _, q = P.preparse(q)
    machines = P.make_objects(q)
    assert isinstance(machines[0], P.M.Literal)

def test_make_objects_02():
    random_string = ''.join(random.sample(string.ascii_letters, 30))
    q = deque(random_string)
    _, q = P.preparse(q)
    machines = P.make_objects(q)
    assert all([isinstance(machine, P.M.Literal) for machine in machines])

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
