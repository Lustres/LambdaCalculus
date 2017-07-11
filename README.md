# LambdaCalculus
 This module could simulate the execute of λ-calculus by Python

# Module Structure
* core.py: core component of lambda like Variable, Function reduction
* convert.py: convert python lambda expression to executable object
* fundation.py: some useful tools like combinators, pairs, control flows and common numbers

# Implement Detail
 As mentioned above, this program is **simulate** the execute of lambda. To do this, this program use `Function` object to represent Python lambda, use `Call` object to mock Python call, `Variable` object to store names.
 
 
 So the original input and output is not Python lambda format. You need two functions `parse`, `eval` to convert them, which introduced in next.
 
# Example
```
from lambda_calculus.fundation import *
```
## eval
Convert output to Python lambda
```Python3
## Without eval could get very long (but equivalent) answer
>>> ADD(ONE)(ONE) 
Call(Function('x', Call(Call(Variable('x'), Function('x', Function('y', Variable('y')))), Function('x', Function('y', Variable('x'))))), Function('x', Function('y', Variable('x'))))

## Use like this
>>> eval(ADD(ONE)(ONE)) 
'lambda f: lambda x: f(f(x))'
```	

## parse
Convert Python lambda to input
Return value is a list
You could run `python3 convert.py input.py output.txt` to convert file
**ONLY SUPPORT SINGLE PARAMETER LAMBDA EXPRESSION**
```Python3
## Use Python lambda without parse is meaningless
>>> NOT('lambda x: lambda y: x')
Call(Function('x', Call(Call(Variable('x'), Function('x', Function('y', Variable('y')))), Function('x', Function('y', Variable('x'))))), 'lambda x: lambda y: x')

## Use like this
>>> NOT(parse('lambda x: lambda y: x')[0])
Call(Function('x', Call(Call(Variable('x'), Function('x', Function('y', Variable('y')))), Function('x', Function('y', Variable('x'))))), Function('x', Function('y', Variable('x'))))

## Don't forget `eval`
>>> eval(NOT(parse('lambda x: lambda y: x')[0]))
'lambda x: lambda y: y'
```

## Arithmetic
```Python3
>>> eval(ADD(THREE)(TWO))
'lambda f: lambda x: f(f(f(f(f(x)))))'

>>> eval(SUB(FIVE)(THREE))
'lambda p: lambda x: p(p(x))'

>>> eval(DIV(TEN)(THREE))
'lambda p: lambda x: p(p(p(x)))'

>>> eval(MOD(FIFTEEN)(FIVE))
'lambda p: lambda x: x'
```

## Relational
```Python3
>>> eval(TRUE)
'lambda x: lambda y: x'

>>> eval(AND(TRUE)(TRUE))
'lambda x: lambda y: x'

>>> eval(NOT(TRUE)) 
'lambda x: lambda y: y'

>>> eval(IF(TRUE)(Variable('happy'))(Variable('sad')))
'happy'
```

## And More
```Python3
## fold add
>>> eval(FOLD(RANGE(ONE)(FIVE))(ZERO)(ADD))
'lambda f: lambda x: f(f(f(f(f(f(f(f(f(f(f(f(f(f(f(x)))))))))))))))'

## map inc
>>> MAP(RANGE(ONE)(THREE))(INCREMENT)

## merge two infinity list
>>> MERGE(PROGRESS(ZERO))(PROGRESS(ZERO))(ADD)

## generator
>>> GENERATOR(FIVE)(ADD(FIVE))
```
You could get more info from [https://github.com/Lustres/Under-Computeration/tree/master/partII/lambda](https://github.com/Lustres/Under-Computeration/blob/master/partII/lambda/test_FizzBuzz.py)

# Test
	 $ pytest

