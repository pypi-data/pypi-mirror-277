"""
Linflex
-------

A linear algebra package written in Python

Includes:
- lerp
- sign
- clamp
- Vec2
- Vec2i
- Vec3
"""

from __future__ import annotations as _annotations

__version__ = "0.1.2"
__all__ = [
    "lerp",
    "sign",
    "clamp",
    "Vec2",
    "Vec2i",
    "Vec3"
]

from ._numerical_tools import lerp, sign, clamp
from ._vec2 import Vec2, Vec2i
from ._vec3 import Vec3
