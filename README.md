# Lazy CLI

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
{'OK', 'status'}
```

**pass args to a command**
```
$ python run.py example_command True
Traceback (most recent call last):
  File "run.py", line 36, in <module>
    main()
  File "run.py", line 31, in main
    result = getattr(cmd, args.command)(*args.args)
  File "/media/data/mdavis/code/self-ref-cli/cli/__init__.py", line 26, in example_command
    inspect.currentframe(), 404, {"message": "You failed me on purpose"})
  File "/media/data/mdavis/code/self-ref-cli/cli/__init__.py", line 12, in raise_exception
    .format(frame.f_code.co_name, status, resp))
Exception:

Error running example_command: 404
{'message': 'You failed me on purpose'}
```

> As you can see, argparse handles typing of input to the best of it's ability and will distiguish bool vs string vs int, etc. Happy lazy coding!

## Test

Just a linter, but here you go...

```tox -e flake8```

## Development

Argparse and error handling via raise_exception are dynamic. Use the class to buildout commands. Pass the frames and any status/msg into the raise_exception function. Never need to update valid commands or wade through messy tracebacks.

## Why?

Lazy coding idea.

## Caveats

Error handling is posslibly a little redundant, but is extremely human readable since you can ignore most of the stack trace if you write proper error handling. A few extra seconds into error handling == much faster debugging.
