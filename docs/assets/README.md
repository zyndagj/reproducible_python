# Summarize

A package for summarizing a specified list of random numbers.

## Requirements

Summarize runs on Python >= 3.6 and requires Numpy.

## Installing

Install with pip from master

```
$ pip install --user git+https://github.com/zyndagj/summarize.git
```

or a specific release

```
$ pip install --user git+https://github.com/zyndagj/summarize.git@release
```

## Testing

Install test dependencies and run tests

```
$ git clone https://github.com/zyndagj/summarize.git
$ cd summarize
$ pip install --user .[dev]

# Run tests with tox
$ tox

# Run tests with pytest
$ pip install .
$ pytest
```

## Usage

```
usage: summarize [-h] [-N INT]

A simple tool for computing the mean of a random list

optional arguments:
  -h, --help  show this help message and exit
  -N INT      Number of random integers [5]
```

```
$ summarize -N 5
48.8
```
