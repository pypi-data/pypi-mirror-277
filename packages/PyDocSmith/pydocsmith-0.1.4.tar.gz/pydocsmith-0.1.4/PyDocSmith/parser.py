"""The main parsing routine."""

import inspect
import typing as T

from PyDocSmith import epydoc, google, numpydoc, rest
from PyDocSmith.attrdoc import add_attribute_docstrings
from PyDocSmith.common import (
    Docstring,
    DocstringStyle,
    ParseError,
    RenderingStyle,
    format_docstring_to_pep257,
)

_STYLE_MAP = {
    DocstringStyle.REST: rest,
    DocstringStyle.GOOGLE: google,
    DocstringStyle.NUMPYDOC: numpydoc,
    DocstringStyle.EPYDOC: epydoc,
}


def detect_docstring_style(docstring) -> DocstringStyle:
    """
    Attempt to detect the docstring style based on simple heuristics.

    Args:
        docstring (str): The docstring to analyze.

    Returns:
        str: The detected style ('REST', 'GOOGLE',
        'NUMPYDOC', 'EPYDOC', or 'UNKNOWN').
    """
    if "@param" in docstring or "@return" in docstring:
        return DocstringStyle.EPYDOC
    if (
        ":param:" in docstring
        or ":return:" in docstring
        or ":returns:" in docstring
    ):
        return DocstringStyle.REST
    if "Args:" in docstring or "Returns:" in docstring:
        return DocstringStyle.GOOGLE
    if "Parameters" in docstring or "Returns" in docstring:
        return DocstringStyle.NUMPYDOC
    return None


def parse(text: str, style: DocstringStyle = DocstringStyle.AUTO) -> Docstring:
    """Parse the docstring into its components.

    :param text: docstring text to parse
    :param style: docstring style
    :returns: parsed docstring representation
    """
    if style != DocstringStyle.AUTO:
        return _STYLE_MAP[style].parse(text)

    doc_string_style = detect_docstring_style(text)

    if doc_string_style is not None:
        try:
            return _STYLE_MAP[doc_string_style].parse(text)
        except ParseError as ex:
            raise ex

    exc: T.Optional[Exception] = None
    rets = []
    for module in _STYLE_MAP.values():
        try:
            ret = module.parse(text)
        except ParseError as ex:
            exc = ex
        else:
            rets.append(ret)

    if not rets:
        raise exc

    return sorted(rets, key=lambda d: len(d.meta), reverse=True)[0]


def parse_from_object(
    obj: T.Any,
    style: DocstringStyle = DocstringStyle.AUTO,
) -> Docstring:
    """Parse the object's docstring(s) into its components.

    The object can be anything that has a ``__doc__`` attribute. In contrast to
    the ``parse`` function, ``parse_from_object`` is able to parse attribute
    docstrings which are defined in the source code instead of ``__doc__``.

    Currently only attribute docstrings defined at class and module levels are
    supported. Attribute docstrings defined in ``__init__`` methods are not
    supported.

    When given a class, only the attribute docstrings of that class are parsed,
    not its inherited classes. This is a design decision. Separate calls to
    this function should be performed to get attribute docstrings of parent
    classes.

    :param obj: object from which to parse the docstring(s)
    :param style: docstring style
    :returns: parsed docstring representation
    """
    docstring = parse(obj.__doc__, style=style)

    if inspect.isclass(obj) or inspect.ismodule(obj):
        add_attribute_docstrings(obj, docstring)

    return docstring


def compose(
    docstring: Docstring,
    style: DocstringStyle = DocstringStyle.AUTO,
    rendering_style: RenderingStyle = RenderingStyle.COMPACT,
    indent: str = "    ",
    line_width: int = 72
) -> str:
    """Render a parsed docstring into docstring text.

    :param docstring: parsed docstring representation
    :param style: docstring style to render
    :param indent: the characters used as indentation in the docstring string
    :returns: docstring text
    """
    module = _STYLE_MAP[
        docstring.style if style == DocstringStyle.AUTO else style
    ]

    if line_width >= 72:
        docstring = format_docstring_to_pep257(docstring, width=line_width)

    return module.compose(
        docstring, rendering_style=rendering_style, indent=indent
    )
