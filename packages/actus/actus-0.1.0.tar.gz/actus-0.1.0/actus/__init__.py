
__version__ = "0.1.0"
__all__ = [
    "info",
    "warn",
    "error"
]

import sys as _sys
from typing import TypeVar as _TypeVar, Protocol as _Protocol


_T_contra = _TypeVar("_T_contra", contravariant=True)

class _SupportsWrite(_Protocol[_T_contra]):
    def write(self, stream: _T_contra, /) -> object: ...


def info(*message_segments: str, sep: str = " ", end: str = "\n", file: _SupportsWrite[str] | None = None) -> None:
    message = "[Info] " + sep.join(message_segments) + end
    if file is not None:
        file.write(message)
    _sys.stdout.write(message)


def warn(*message_segments: str, sep: str = " ", end: str = "\n", file: _SupportsWrite[str] | None = None) -> None:
    message = "[Warning] " + sep.join(message_segments) + end
    if file is not None:
        file.write(message)
    _sys.stdout.write(message)


def error(*message_segments: str, sep: str = " ", end: str = "\n", file: _SupportsWrite[str] | None = None) -> None:
    message = "[Error] " + sep.join(message_segments) + end
    if file is not None:
        file.write(message)
    _sys.stdout.write(message)
