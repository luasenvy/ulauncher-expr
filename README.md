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

And You can use python Math Functions:
```
pow(2, 2) = 4
2 + pow(2, 2) = 6
```

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
