from __future__ import annotations as _annotations

from math import (
    sqrt as _sqrt,
    cos as _cos,
    sin as _sin
)
from typing import TypeVar as _TypeVar, Iterator as _Iterator

from ._numerical_tools import (
    lerp as _lerp,
    sign as _sign,
    clamp as _clamp
)

_Vec3 = _TypeVar("_Vec3", bound="Vec3")


class Vec3:
    """`Vector3` data structure

    Components: `x`, `y`, `z`

    Usefull for storing position or direction in 3D space
    """
    __slots__ = ("x", "y", "z")

    @classmethod
    @property
    def ZERO(cls: type[_Vec3]) -> _Vec3:
        return cls(0, 0, 0)
    
    def __init__(self, x: float = 0, y: float = 0, z: float = 0, /) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def __len__(self) -> int:
        return 3

    def __iter__(self) -> _Iterator[float]:
        return iter((self.x, self.y, self.z))
    
    def __getitem__(self, item: int) -> float:
        if not (0 <= item < 3) or not isinstance(item, int):
            raise ValueError("item does not correspond to component")
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item == 2:
            return self.z
        return -1 # will never be returned

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y}, {self.z})"
    
    def __bool__(self) -> bool:
        """Returns whether x or y is not zero

        Returns:
            bool: truthiness
        """
        return bool(self.x or self.y or self.z)

    def __round__(self, ndigits: int = 0) -> Vec3:
        return Vec3(round(self.x, ndigits),
                    round(self.y, ndigits))
    
    def __add__(self, other: Vec3) -> Vec3:
        return Vec3(self.x + other.x,
                    self.y + other.y,
                    self.z + other.z)

    def __iadd__(self, other: Vec3) -> Vec3:
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self
    
    def __sub__(self, other: Vec3) -> Vec3:
        return Vec3(self.x - other.x,
                    self.y - other.y,
                    self.z - other.z)

    def __isub__(self, other: Vec3) -> Vec3:
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __mul__(self, other: Vec3 | int | float) -> Vec3:
        if isinstance(other, Vec3):
            return Vec3(self.x * other.x,
                        self.y * other.y,
                        self.z * other.z)
        return Vec3(self.x * other,
                    self.y * other,
                    self.z * other)
    
    def __imul__(self, other: Vec3 | int | float) -> Vec3:
        if isinstance(other, Vec3):
            self.x *= other.x
            self.y *= other.y
            self.z *= other.z
        else:
            self.x *= other
            self.y *= other
            self.z *= other
        return self
    
    def __floordiv__(self, other: Vec3 | int | float) -> Vec3:
        if isinstance(other, Vec3):
            if not other.x or not other.y or not other.z: # any x, y, z == 0
                return Vec3(0, 0, 0)
            return Vec3(self.x // other.x,
                        self.y // other.y,
                        self.z // other.z)
        return Vec3(self.x // other,
                    self.y // other,
                    self.z // other)
    
    def __ifloordiv__(self, other: Vec3 | int | float) -> Vec3:
        if isinstance(other, Vec3):
            if not other.x or not other.y or not other.z: # any x, y, z == 0
                return Vec3(0, 0, 0)
            self.x //= other.x
            self.y //= other.y
            self.z //= other.z
        else:
            self.x //= other
            self.y //= other
            self.z //= other
        return self
    
    def __truediv__(self, other: Vec3 | int | float) -> Vec3:
        if isinstance(other, Vec3):
            if not other.x or not other.y or not other.z: # any x, y, z == 0
                return Vec3(0, 0, 0)
            return Vec3(self.x / other.x,
                        self.y / other.y,
                        self.z / other.z)
        return Vec3(self.x / other,
                    self.y / other,
                    self.z / other)
    
    def __itruediv__(self, other: Vec3 | int | float) -> Vec3:
        if isinstance(other, Vec3):
            if not other.x or not other.y or not other.z: # any x, y, z == 0
                return Vec3(0, 0, 0)
            self.x /= other.x
            self.y /= other.y
            self.z /= other.z
        else:
            self.x /= other
            self.y /= other
            self.z /= other
        return self
    
    def __mod__(self, other: Vec3 | int | float) -> Vec3:
        if isinstance(other, Vec3):
            return Vec3(self.x % other.x,
                        self.y % other.y,
                        self.z % other.z)
        return Vec3(self.x % other,
                    self.y % other,
                    self.z % other)
    
    def __imod__(self, other: Vec3 | int | float) -> Vec3:
        if isinstance(other, Vec3):
            self.x %= other.x
            self.y %= other.y
            self.z %= other.z
        else:
            self.x %= other
            self.y %= other
            self.z %= other
        return self
    
    def __eq__(self, other: Vec3) -> bool:
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)
    
    def __ne__(self, other: Vec3) -> bool:
        return (self.x != other.x) or (self.y != other.y) and (self.z != other.z)
    
    def __gt__(self, other: Vec3) -> bool:
        return (self.x > other.x) and (self.y > other.y) and (self.z > other.z)
    
    def __lt__(self, other: Vec3) -> bool:
        return (self.x < other.x) and (self.y < other.y) and (self.z < other.z)
    
    def __ge__(self, other: Vec3) -> bool:
        return (self.x >= other.x) and (self.y >= other.y) and (self.z >= other.z)

    def __le__(self, other: Vec3) -> bool:
        return (self.x <= other.x) and (self.y <= other.y) and (self.z <= other.z)
    
    def __copy__(self) -> Vec3:
        return __class__(self.x, self.y, self.z)
    
    def __deepcopy__(self, _memo) -> Vec3:
        return __class__(self.x, self.y, self.z)
    
    def copy(self) -> Vec3:
        return Vec3(self.x, self.y, self.z)

    def length(self) -> float:
        return _sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

    def normalized(self) -> Vec3:
        length = self.length()
        if length == 0:
            return Vec3(0, 0, 0)
        return Vec3(self.x / length, self.y / length, self.z / length)

    def lerp(self, target: Vec3, /, weight: float) -> Vec3:
        return Vec3(_lerp(self.x, target.x, weight),
                    _lerp(self.y, target.y, weight),
                    _lerp(self.z, target.z, weight))

    def distance_to(self, target: Vec3, /) -> float:
        return (target - self).length()
    
    def direction_to(self, target: Vec3, /) -> Vec3:
        return (target - self).normalized()
    
    def dot(self, other: Vec3, /) -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other: Vec3, /) -> Vec3:
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vec3(x, y, z)

    def to_tuple(self) -> tuple[float, float, float]:
        return (self.x, self.y, self.z)

    def rotate_around_x(self, angle: float, /) -> Vec3:
        cos_theta = _cos(angle)
        sin_theta = _sin(angle)
        new_y = self.y * cos_theta - self.z * sin_theta
        new_z = self.y * sin_theta + self.z * cos_theta
        return Vec3(self.x, new_y, new_z)

    def rotate_around_y(self, angle: float, /) -> Vec3:
        cos_theta = _cos(angle)
        sin_theta = _sin(angle)
        new_x = self.x * cos_theta + self.z * sin_theta
        new_z = -self.x * sin_theta + self.z * cos_theta
        return Vec3(new_x, self.y, new_z)

    def rotate_around_z(self, angle: float, /) -> Vec3:
        cos_theta = _cos(angle)
        sin_theta = _sin(angle)
        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta
        return Vec3(new_x, new_y, self.z)
    
    def rotated(self, angles: Vec3, /) -> Vec3:
        return (
            self
            .rotate_around_x(angles.x)
            .rotate_around_y(angles.y)
            .rotate_around_z(angles.z)
            )
    
    def rotated_around(self, target: Vec3, angles: Vec3, /) -> Vec3:
        # FIXME: rotate properly
        rel = self - target
        return (
            rel
            .rotate_around_x(angles.x)
            .rotate_around_y(angles.y)
            .rotate_around_z(angles.z)
            ) + target