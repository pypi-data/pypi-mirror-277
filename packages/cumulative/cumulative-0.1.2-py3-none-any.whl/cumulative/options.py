from mltraq.utils.base_options import BaseOptions


class Options(BaseOptions):
    default_values = {
        "reproducibility": {"random_seed": 123},
        "tqdm": {"disable": False, "leave": False, "delay": 0},
        "transforms": {
            "destination": "base",
            "source": "base",
            "tmp": "temp",
            "sequence": {"attributes": "attrs"},
            "fit": {"curve_fit": {"maxfev": 10000}},
        },
        "warnings": {"disable": True},
        "doc": {"url": "https://elehcimd.github.io/cumulative/"},
    }


def options() -> BaseOptions:
    """
    Returns singleton object of options.
    """

    # In some complex cases (parallel execution of runs, options
    # imported in different ways by different modules), the
    # object is quietly copied, causing errors hard to debug.
    #
    # By always calling options(), this issue disappears and
    # things work as expected.
    return Options.instance()
