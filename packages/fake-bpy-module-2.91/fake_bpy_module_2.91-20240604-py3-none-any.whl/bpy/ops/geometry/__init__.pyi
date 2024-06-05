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
    data_type: str | None = "FLOAT",
    domain: str | None = "POINT",
):
    """Add attribute to geometry

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param name: Name, Name of new attribute
        :type name: str | typing.Any
        :param data_type: Data Type, Type of data stored in attribute

    FLOAT
    Float, Floating point value.

    INT
    Integer, 32 bit integer.

    FLOAT_VECTOR
    Vector, 3D vector with floating point values.

    FLOAT_COLOR
    Float Color, RGBA color with floating point precisions.

    BYTE_COLOR
    Byte Color, RGBA color with 8-bit precision.

    STRING
    String, Text string.
        :type data_type: str | None
        :param domain: Domain, Type of element that attribute is stored on

    VERTEX
    Vertex, Attribute on mesh vertex.

    EDGE
    Edge, Attribute on mesh edge.

    CORNER
    Corner, Attribute on mesh polygon corner.

    POLYGON
    Polygon, Attribute on mesh polygons.

    POINT
    Point, Attribute on point.

    CURVE
    Curve, Attribute on hair curve.
        :type domain: str | None
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
