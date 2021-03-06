from .core import *

from .convert import parse

def eval(term):
    return str(reduce(term))


def _call(self, *args, **kwargs):
    return Call(self, args[0])


Term.__call__ = _call


Z = Function('g', Call(Function('x', Call(Variable('g'), Function('y', Call(Call(Variable('x'), Variable('x')), Variable('y'))))), Function('x', Call(Variable('g'), Function('y', Call(Call(Variable('x'), Variable('x')), Variable('y')))))))

ZERO = Function('p', Function('x', Variable('x')))
ONE = Function('p', Function('x', Call(Variable('p'), Variable('x'))))
TWO = Function('p', Function('x', Call(Variable('p'), Call(Variable('p'), Variable('x')))))
THREE = Function('p', Function('x', Call(Variable('p'), Call(Variable('p'), Call(Variable('p'), Variable('x'))))))
FOUR = Function('p', Function('x', Call(Variable('p'), Call(Variable('p'), Call(Variable('p'), Call(Variable('p'), Variable('x')))))))
FIVE = Function('p', Function('x', Call(Variable('p'), Call(Variable('p'), Call(Variable('p'), Call(Variable('p'), Call(Variable('p'), Variable('x'))))))))
TEN = Function('p', Function('x', Call(Variable('p'), Call(Variable('p'), Call(Variable('p'), Call(Variable('p'), Call(Variable('p'), Call(Variable('p'), Call(Variable('p'), Call(Variable('p'), Call(Variable('p'), Call(Variable('p'), Variable('x')))))))))))))
FIFTEEN = Function('p', Function('x', Call(Variable('p'), Call(Variable('p'), Call(Variable('p'), Call(Variable('p'), Call(Variable('p'), Call(Variable('p'), Call(Variable('p'), Call(Variable('p'), Call(Variable('p'), Call(Variable('p'), Call(Variable('p'), Call(Variable('p'), Call(Variable('p'), Call(Variable('p'), Call(Variable('p'), Variable('x'))))))))))))))))))
TRUE = Function('x', Function('y', Variable('x')))
FALSE = Function('x', Function('y', Variable('y')))
IF = Function('b', Variable('b'))
AND = Function('x', Function('y', Call(Call(Variable('x'), Variable('y')), Variable('x'))))
OR = Function('x', Function('y', Call(Call(Variable('x'), Variable('x')), Variable('y'))))
NOT = Function('x', Call(Call(Variable('x'), FALSE), TRUE))
IS_ZERO = Function('l', Call(Call(Variable('l'), Function('n', FALSE)), TRUE))
INCREMENT = Function('n', Function('p', Function('x', Call(Variable('p'), Call(Call(Variable('n'), Variable('p')), Variable('x'))))))
PAIR = Function('x', Function('y', Function('f', Call(Call(Variable('f'), Variable('x')), Variable('y')))))
LEFT = Function('f', Call(Variable('f'), TRUE))
RIGHT = Function('f', Call(Variable('f'), FALSE))
SLIDE = Function('p', Call(Call(PAIR, Call(RIGHT, Variable('p'))), Call(INCREMENT, Call(RIGHT, Variable('p')))))
EMPTY = Call(Call(PAIR, TRUE), TRUE)
IS_EMPTY = LEFT
DECREMENT = Function('n', Call(LEFT, Call(Call(Variable('n'), SLIDE), Call(Call(PAIR, ZERO), ZERO))))
ADD = Function('m', Function('n', Function('f', Function('x', Call(Call(Variable('m'), Variable('f')), Call(Call(Variable('n'), Variable('f')), Variable('x')))))))
SUB = Function('m', Function('n', Call(Call(Variable('n'), DECREMENT), Variable('m'))))
LESS_OR_EQUAL = Function('m', Function('n', Call(IS_ZERO, Call(Call(SUB, Variable('m')), Variable('n')))))
MULTI = Function('m', Function('n', Function('f', Call(Variable('m'), Call(Variable('n'), Variable('f'))))))
DIV = Call(Z, Function('f', Function('m', Function('n', Call(Call(Call(IF, Call(Call(LESS_OR_EQUAL, Variable('n')), Variable('m'))), Function('x', Call(Call(INCREMENT, Call(Call(Variable('f'), Call(Call(SUB, Variable('m')), Variable('n'))), Variable('n'))), Variable('x')))), ZERO)))))
POWER = Function('b', Function('e', Call(Variable('e'), Variable('b'))))
MOD = Call(Z, Function('f', Function('m', Function('n', Call(Call(Call(IF, Call(Call(LESS_OR_EQUAL, Variable('n')), Variable('m'))), Function('x', Call(Call(Call(Variable('f'), Call(Call(SUB, Variable('m')), Variable('n'))), Variable('n')), Variable('x')))), Variable('m'))))))
UNSHIFT = Function('l', Function('x', Call(Call(PAIR, FALSE), Call(Call(PAIR, Variable('x')), Variable('l')))))
FIRST = Function('l', Call(LEFT, Call(RIGHT, Variable('l'))))
REST = Function('l', Call(RIGHT, Call(RIGHT, Variable('l'))))
RANGE = Call(Z, Function('f', Function('m', Function('n', Call(Call(Call(IF, Call(Call(LESS_OR_EQUAL, Variable('m')), Variable('n'))), Function('x', Call(Call(Call(UNSHIFT, Call(Call(Variable('f'), Call(INCREMENT, Variable('m'))), Variable('n'))), Variable('m')), Variable('x')))), EMPTY)))))
INFINITY = Call(Z, Function('f', Call(Call(UNSHIFT, Variable('f')), ZERO)))
PROGRESS = Call(Z, Function('f', Function('n', Call(Call(UNSHIFT, Function('x', Call(Call(Variable('f'), Call(INCREMENT, Variable('n'))), Variable('x')))), Variable('n')))))
MULTIPLE = Function('m', Call(Call(Z, Function('f', Function('n', Call(Call(UNSHIFT, Function('x', Call(Call(Variable('f'), Call(Call(ADD, Variable('m')), Variable('n'))), Variable('x')))), Variable('n'))))), Variable('m')))
GENERATOR = Call(Z, Function('f', Function('n', Function('g', Call(Call(UNSHIFT, Function('x', Call(Call(Call(Variable('f'), Call(Variable('g'), Variable('n'))), Variable('g')), Variable('x')))), Variable('n'))))))
FOLD = Call(Z, Function('f', Function('l', Function('x', Function('g', Call(Call(Call(IF, Call(IS_EMPTY, Variable('l'))), Variable('x')), Function('y', Call(Call(Call(Variable('g'), Call(Call(Call(Variable('f'), Call(REST, Variable('l'))), Variable('x')), Variable('g'))), Call(FIRST, Variable('l'))), Variable('y')))))))))
MAP = Function('k', Function('f', Call(Call(Call(FOLD, Variable('k')), EMPTY), Function('l', Function('x', Call(Call(UNSHIFT, Variable('l')), Call(Variable('f'), Variable('x'))))))))
MERGE = Call(Z, Function('f', Function('s', Function('t', Function('g', Call(Call(UNSHIFT, Function('x', Call(Call(Call(Call(Variable('f'), Call(REST, Variable('s'))), Call(REST, Variable('t'))), Variable('g')), Variable('x')))), Call(Call(Variable('g'), Call(FIRST, Variable('s'))), Call(FIRST, Variable('t')))))))))
PUSH = Function('l', Function('x', Call(Call(Call(FOLD, Variable('l')), Call(Call(UNSHIFT, EMPTY), Variable('x'))), UNSHIFT)))
FIZZ = Call(Call(UNSHIFT, Call(Call(UNSHIFT, Call(Call(UNSHIFT, Call(Call(UNSHIFT, EMPTY), Call(Call(ADD, TEN), FOUR))), Call(Call(ADD, TEN), FOUR))), Call(Call(ADD, TEN), TWO))), Call(Call(ADD, TEN), ONE))
BUZZ = Call(Call(UNSHIFT, Call(Call(UNSHIFT, Call(Call(UNSHIFT, Call(Call(UNSHIFT, EMPTY), Call(Call(ADD, TEN), FOUR))), Call(Call(ADD, TEN), FOUR))), Call(Call(ADD, TEN), THREE))), Call(Call(ADD, TEN), ZERO))
FIZZBUZZ = Call(Call(UNSHIFT, Call(Call(UNSHIFT, Call(Call(UNSHIFT, Call(Call(UNSHIFT, BUZZ), Call(Call(ADD, TEN), FOUR))), Call(Call(ADD, TEN), FOUR))), Call(Call(ADD, TEN), TWO))), Call(Call(ADD, TEN), ONE))
DIGITS = Call(Z, Function('f', Function('n', Call(Call(PUSH, Call(Call(Call(IF, Call(Call(LESS_OR_EQUAL, Variable('n')), Call(Call(SUB, TEN), ONE))), EMPTY), Function('x', Call(Call(Variable('f'), Call(Call(DIV, Variable('n')), TEN)), Variable('x'))))), Call(Call(MOD, Variable('n')), TEN)))))
