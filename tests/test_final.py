import os
import sys

sys.path.insert(0, os.path.abspath('.'))

from lambda_calculus.fundation import *


def test_boolean():
    assert eval(IF(TRUE)(Variable('happy'))(Variable('sad'))) == 'happy'
    assert eval(IF(FALSE)(Variable('happy'))(Variable('sad'))) == 'sad'


def test_boolean_AND():
    assert eval(AND(TRUE)(TRUE)) == eval(TRUE)
    assert eval(AND(TRUE)(FALSE)) == eval(FALSE)
    assert eval(AND(FALSE)(TRUE)) == eval(FALSE)
    assert eval(AND(FALSE)(FALSE)) == eval(FALSE)


def test_boolean_OR():
    assert eval(OR(TRUE)(TRUE)) == eval(TRUE)
    assert eval(OR(TRUE)(FALSE)) == eval(TRUE)
    assert eval(OR(FALSE)(TRUE)) == eval(TRUE)
    assert eval(OR(FALSE)(FALSE)) == eval(FALSE)


def test_boolean_NOT():
    assert eval(NOT(TRUE)) == eval(FALSE)
    assert eval(NOT(FALSE)) == eval(TRUE)


def test_predicate():
    assert eval(IS_ZERO(ZERO)) == eval(TRUE)
    assert eval(IS_ZERO(THREE)) == eval(FALSE)
    assert eval((IS_ZERO(FIFTEEN))) == eval(FALSE)


def test_pair():
    pair = PAIR(THREE)(FIVE)
    assert eval(LEFT(pair)) == eval(THREE)
    assert eval(RIGHT(pair)) == eval(FIVE)


def test_pair_2():
    pair = PAIR(ZERO)(FIFTEEN)
    assert eval(LEFT(pair)) == eval(ZERO)
    assert eval(RIGHT(pair)) == eval(FIFTEEN)


def test_increment():
    assert eval(INCREMENT(ZERO)) == eval(ONE)
    assert eval((INCREMENT(TWO))) == eval(THREE)
    # assert eval(INCREMENT(FIFTEEN)) == eval(ADD(FIFTEEN)(ONE))
    assert eval(INCREMENT(FIFTEEN)(Variable('one'))) == eval(ADD(FIFTEEN)(ONE)(Variable('one')))

def test_slide():
    NEXT_PAIR = SLIDE(PAIR(ZERO)(ZERO))
    assert eval(LEFT(NEXT_PAIR)) == eval(ZERO)
    assert eval(RIGHT(NEXT_PAIR)) == eval(ONE)

    NEXT_PAIR = SLIDE(NEXT_PAIR)
    assert eval(LEFT(NEXT_PAIR)) == eval(ONE)
    assert eval((RIGHT(NEXT_PAIR))) == eval(TWO)


def test_decrement():
    assert eval(DECREMENT(ONE)) == eval(ZERO)
    assert eval(DECREMENT(TWO)) == eval(ONE)
    assert eval(DECREMENT(THREE)) == eval(TWO)


def test_math():
    assert eval(ADD(TWO)(THREE)) == eval(alpha(FIVE, Variable('f')))
    assert eval(SUB(FIVE)(THREE)) == eval(alpha(TWO, Variable('p')))
    assert eval(MULTI(THREE)(FIVE)) == eval(alpha(FIFTEEN, Variable('f')))
    assert eval(DIV(TEN)(THREE)) == eval(THREE)
    # assert eval(POWER(THREE)(THREE)) == eval(MULTI(POWER(THREE)(TWO))(THREE))
    assert eval(POWER(THREE)(THREE)(Variable('one'))) == eval(MULTI(POWER(THREE)(TWO))(THREE)(Variable('one')))

def test_less_or_equal():
    assert eval(LESS_OR_EQUAL(ONE)(TWO)) == eval(TRUE)
    assert eval(LESS_OR_EQUAL(FIVE)(THREE)) == eval(FALSE)
    assert eval(LESS_OR_EQUAL(FIFTEEN)(FIFTEEN)) == eval(TRUE)


def test_mod():
    assert eval(MOD(FIFTEEN)(FIVE)) == eval(ZERO)
    assert eval(MOD(FIFTEEN)(THREE)) == eval(ZERO)
    assert eval(MOD(FIFTEEN)(TWO)) == eval(ONE)


def test_array():
    L = UNSHIFT(
        UNSHIFT(
            UNSHIFT(EMPTY)(THREE)
        )(TWO)
    )(ONE)

    assert eval(IS_EMPTY(L)) == eval(FALSE)
    assert eval(FIRST(L)) == eval(ONE)
    assert eval(FIRST(REST(L))) == eval(TWO)
    assert eval(FIRST(REST(REST(L)))) == eval(THREE)
    assert eval(IS_EMPTY(FIRST(REST(REST(REST))))) == eval(TRUE)

#
# def test_array_2():
#     L = UNSHIFT(
#         UNSHIFT(
#             UNSHIFT(EMPTY)(THREE)
#         )(TWO)
#     )(ONE)
#
#     assert array(EMPTY) == []
#     assert list(map(integer, array(L))) == [1,2,3]
#
#
# def test_range():
#     assert list(map(integer, array(RANGE(ONE)(ONE)))) == [1]
#     assert list(map(integer, array(RANGE(ZERO)(FIFTEEN)))) == list(range(0, 15+1))
#     assert list(map(integer, array(RANGE(ONE)(POWER(MULTI(TWO)(FIVE))(TWO))))) == list(range(1, (2 * 5) ** 2 + 1))
#

def test_infinity():
    assert eval(FIRST(INFINITY)) == eval(ZERO)
    assert eval(FIRST(REST(INFINITY))) == eval(ZERO)
    assert eval(FIRST(REST(REST(INFINITY)))) == eval(ZERO)

#
# def test_infinity_2():
#     assert list(map(integer, array(INFINITY, 5))) == [0 for i in range(5)]
#     assert list(map(integer, array(INFINITY, 10))) == [0 for i in range(10)]
#     assert list(map(integer, array(INFINITY, 20))) == [0 for i in range(20)]
#
#
# def test_progress():
#     assert list(map(integer, array(PROGRESS(ZERO), 5))) == [i for i in range(5)]
#     assert list(map(integer, array(PROGRESS(FIFTEEN), 20))) == [i for i in range(15, 15 + 20)]
#
#
# def test_multiple():
#     assert list(map(integer, array(MULTIPLE(TWO),   10))) == [i * 2 for i in range(1, 10 + 1)]
#     assert list(map(integer, array(MULTIPLE(THREE), 10))) == [i * 3 for i in range(1, 10 + 1)]
#     assert list(map(integer, array(MULTIPLE(FIVE),  20))) == [i * 5 for i in range(1, 20 + 1)]
#
#
# def test_generator():
#     assert list(map(integer, array(GENERATOR(TWO)(ADD(TWO)), 10))) == [i * 2 for i in range(1, 10 + 1)]
#     assert list(map(integer, array(GENERATOR(FIVE)(ADD(FIVE)), 20))) == [i * 5 for i in range(1, 20 + 1)]
#

def test_fold():
    assert eval(FOLD(RANGE(ONE)(FIVE))(ZERO)(ADD)) == eval(alpha(FIFTEEN, Variable('f')))
    # assert eval(FOLD(RANGE(ONE)(FIVE))(ONE)(MULTI)) == eval(alpha(MULTI(MULTI(POWER(TWO)(THREE))(THREE))(FIVE), Variable('f')))
    assert eval(FOLD(RANGE(ONE)(FIVE))(ONE)(MULTI)(Variable('one'))) == eval(MULTI(MULTI(POWER(TWO)(THREE))(THREE))(FIVE)(Variable('one')))
#
# def test_map():
#     assert list(map(integer, array(MAP(RANGE(ONE)(THREE))(INCREMENT)))) == [2, 3, 4]
#
#
# def test_merge():
#     assert list(map(integer,  array(MERGE(PROGRESS(ZERO))(PROGRESS(ZERO))(ADD), 10))) == [i * 2 for i in range(10)]
