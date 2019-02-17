import inspect

# TODO: Generic. Should be placed in a utils package.


def raise_exception(frame, status=None, resp=None):
    """Use to dynamically raise a frame specific exception

    Especially useful for api responses but can be used for whatever.
    """
    raise Exception("\n\nError running {}: {}\n{}"
                    .format(frame.f_code.co_name, status, resp))


class Cli():
    def __init__(self, *args, **kwargs):
        """
        If this was an Api client class,
        here's where you'd instantiate keys, headers, domain, etc
        """
        return super().__init__(*args, **kwargs)

    def example_command(self, fail=False):
        if fail:
            raise_exception(
                inspect.currentframe(), 404, {"message": "You failed me on purpose"})
        return {"status": "OK"}
