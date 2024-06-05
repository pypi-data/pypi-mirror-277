import typing
import collections.abc
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def attribute_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str | typing.Any = "Attribute",
    domain: str | None = "POINT",
    data_type: str | None = "FLOAT",
):
    """Add attribute to geometry

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param name: Name, Name of new attribute
        :type name: str | typing.Any
        :param domain: Domain, Type of element that attribute is stored on

    POINT
    Point -- Attribute on point.

    EDGE
    Edge -- Attribute on mesh edge.

    FACE
    Face -- Attribute on mesh faces.

    CORNER
    Face Corner -- Attribute on mesh face corner.

    CURVE
    Spline -- Attribute on spline.
        :type domain: str | None
        :param data_type: Data Type, Type of data stored in attribute

    FLOAT
    Float -- Floating-point value.

    INT
    Integer -- 32-bit integer.

    FLOAT_VECTOR
    Vector -- 3D vector with floating-point values.

    FLOAT_COLOR
    Color -- RGBA color with floating-point values.

    BYTE_COLOR
    Byte Color -- RGBA color with 8-bit values.

    STRING
    String -- Text string.

    BOOLEAN
    Boolean -- True or false.

    FLOAT2
    2D Vector -- 2D vector with floating-point values.
        :type data_type: str | None
    """

    ...

def attribute_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove attribute from geometry

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...
