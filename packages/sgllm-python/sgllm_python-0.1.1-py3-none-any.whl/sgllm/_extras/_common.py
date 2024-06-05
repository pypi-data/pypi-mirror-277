from .._exceptions import SGLLMError

INSTRUCTIONS = """

SGLLM error:

    missing `{library}`

This feature requires additional dependencies:

    $ pip install sgllm[{extra}]

"""


def format_instructions(*, library: str, extra: str) -> str:
    return INSTRUCTIONS.format(library=library, extra=extra)


class MissingDependencyError(SGLLMError):
    pass
