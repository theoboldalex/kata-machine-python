# Kata Machine Python

This is a port of [ThePrimeagen](https://github.com/ThePrimeagen)'s Kata Machine repo used in his Front End Masters course.
It contains a host of algorithm problems that in the original repo are written in Typescript. This repo simply converts the 
tests and implemetation files to Python.

To scaffold the implementation files, and ensure you have the required dependencies, first create and activate a virtual environment

```shell
python3 -m venv .venv
source .venv/bin/activate
```

Next, install the dependencies with the Makefile

```shell
make install
```

Then scaffold the implementation files with

```shell
make generate
```

To run the tests, again, use the Makefile

```shell
make test
```

or to run a single test file

```shell
make test file=linear_search_list
```


