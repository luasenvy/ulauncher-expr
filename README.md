# Ulauncher Expr

> [ulauncher](https://ulauncher.io/) Extension for A Simple Calculator.

## Usage

![demo](demo.gif)

## Requirements

* [ulauncher](https://ulauncher.io/)
* Python >= 2.7

## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```
https://github.com/luasenvy/ulauncher-expr
```

## Usage

This plugin calcaulating with `python eval()`

When you want float result
concat `.0` to expression:
```
expr 10 / 3   = 3
expr 10 / 3.0 = 3.33333333
```

You can use braket:
```
expr 2 + 2 * 2     = 6
expr ( 2 + 2 ) * 2 = 8
```

And You can use python `math` Class and `expression`:
```
math.pow(2, 2)         = 4
2 + math.pow(2, 2)     = 6
'py' * 5          = 'pypypypypy'
'hello' + 'world' = 'helloworld'
```

**IMPORTANT** Python's `eval` function can be dangerous.
global variables are restricted to use only math. But use careful.

There are a variety of issues with the vulnerability, but the following documents provide a brief overview.

* [Code injection](https://en.wikipedia.org/wiki/Code_injection)
* [Why is using 'eval' a bad practice?](https://stackoverflow.com/questions/1832940/why-is-using-eval-a-bad-practice)

## Icon

[Calculator Icon](https://www.iconfinder.com/icons/532810/accountant_accounting_calculate_calculation_calculator_math_mathematics_icon) by [Eezy](https://www.iconfinder.com/Vecteezy) in [E-commerce And Shopping](https://www.iconfinder.com/iconsets/e-commerce-and-shopping-3) find with [iconfinder](https://www.iconfinder.com/search/?q=calculator&price=free&type=vector&style=flat)

Creative Commons (Attribution-Share Alike 3.0 Unported)

## Development

```
git clone https://github.com/luasenvy/ulauncher-expr
cd ~/.cache/ulauncher_cache/extensions/ulauncher-expr
ln -s <repo_location> ulauncher-expr
```

To see your changes, stop ulauncher and run it from the command line with:
```
ulauncher -v
```

## License 

MIT
