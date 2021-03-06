# Lazy Python CLI

Basic python "cli" framework for lazy development and debugging.

Not _necessarily_ a cli that can be installed, but it gets the job done with minimal effort and easy debugging assuming you put a few seconds into the "builtin" error handling.

## Requirements

- Python 3.7
- pip
- tox: `pip install tox`

## Setup

```tox -e dev```

## Usage

**help**
```
$ python run.py -h
usage: run.py [-h] COMMAND ...

Run commands.

positional arguments:
  COMMAND
  args

optional arguments:
  -h, --help  show this help message and exit
```

**run a command from the cli class**
```
$ python run.py example_command
{'status': 'OK'}
```

**pass args to a command**
```
$ python run.py example_command True
Traceback (most recent call last):
  File "run.py", line 36, in <module>
    main()
  File "run.py", line 31, in main
    result = getattr(cmd, args.command)(*args.args)
  File "/media/data/mdavis/code/lazy-python-cli/cli/__init__.py", line 27, in example_command
    inspect.currentframe(), 404, {"message": "You failed me on purpose"})
  File "/media/data/mdavis/code/lazy-python-cli/cli/__init__.py", line 13, in raise_exception
    raise Exception("\n{}{}\n{}".format(banner, msg, resp))
Exception:
-----------------BORK----------------
Error running `example_command`: 404
{'message': 'You failed me on purpose'}
```

> As you can see, argparse handles typing of input to the best of it's ability and will distiguish bool vs string vs int, etc. Happy lazy coding!

## Test

Just a linter, but here you go...

```tox -e flake8```

## Development

Argparse and error handling are dynamic. Use the class to buildout commands. Pass the frames and any status/msg into the raise_exception function. Never need to update valid commands or wade through messy tracebacks if you spend a few seconds on custom error handling.

## Why?

Argparse is tedious and I hate parsing long tracebacks.

- If I want to access a class method, it should be easy.
- If I want to know exactly why something is _borked_, it should only take a quick glance.

## Caveats

Error handling is posslibly a little redundant, but is extremely human readable since you can ignore most of the stack trace if you write proper error handling. A few extra seconds into error handling == much faster debugging.
