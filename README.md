# Ulauncher Expr

![demo](demo.gif)

> [ulauncher](https://ulauncher.io/) Extension for A Python Expression Evaluator.

## Features

Evaluate the formula using [`Python eval()`](https://docs.python.org/2/library/functions.html#eval).

## Useful Examples

Arithmetic Operation:
```
expr 1 + 1 = 2
expr 2 * 4 = 8
```

[`Math`](https://docs.python.org/2/library/math.html#module-math) Functions:
```
expr math.pow(2, 5)   = 32.0
expr math.floor(10.5) = 10.0
```

[`Python String Expression`](https://docs.python.org/2/reference/expressions.html):
```
expr 1000 >> 1  = 500
expr 'x' == 'x' = True
```

[`Python String Format`](https://docs.python.org/2/library/string.html#format-string-syntax)

[`Python String Format Examples`](https://docs.python.org/2/library/string.html#format-examples):
```
expr '{0}, {1}!'.format('hello', 'world') = hello, world!
expr '%s, %s!' % ('hello', 'world')       = hello, world!
expr 'py' * 3                             = pypypy
expr '{:,}'.format(10000000)              = 10,000,000
```

## More Informations

When you want float result, concat `.0` to expression:
```
expr 10 / 3   = 3
expr 10 / 3.0 = 3.33333333
```

You can use braket:
```
expr 2 + 2 * 2     = 6
expr ( 2 + 2 ) * 2 = 8
```

**IMPORTANT** Restricted to use only `math` Functions:
```
expr dir()         // name 'dir' is not defined
```

## Risks of `eval()`

**IMPORTANT** Python's `eval` function can be dangerous.
global variables are restricted to use only `math` Functions. But use careful.

There are a variety of issues with the vulnerability, but the following documents provide a brief overview.

* [Code injection](https://en.wikipedia.org/wiki/Code_injection)
* [Why is using 'eval' a bad practice?](https://stackoverflow.com/questions/1832940/why-is-using-eval-a-bad-practice)

## Requirements

* [ulauncher](https://ulauncher.io/)
* Python >= 2.7

## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```
https://github.com/luasenvy/ulauncher-expr
```

## Icon

[Calculator Icon](https://www.iconfinder.com/icons/532810/accountant_accounting_calculate_calculation_calculator_math_mathematics_icon) by [Eezy](https://www.iconfinder.com/Vecteezy) in [E-commerce And Shopping](https://www.iconfinder.com/iconsets/e-commerce-and-shopping-3) find with [iconfinder](https://www.iconfinder.com/search/?q=calculator&price=free&type=vector&style=flat)

[Creative Commons (Attribution-Share Alike 3.0 Unported)](http://creativecommons.org/licenses/by-sa/3.0/)

## Development

```
git clone https://github.com/luasenvy/ulauncher-expr
cd ~/.local/share/ulauncher/extensions/
ln -s <repo_location>
```

To see your changes, stop ulauncher and run it from the command line with:
```
ulauncher -v
```

## License 

MIT
