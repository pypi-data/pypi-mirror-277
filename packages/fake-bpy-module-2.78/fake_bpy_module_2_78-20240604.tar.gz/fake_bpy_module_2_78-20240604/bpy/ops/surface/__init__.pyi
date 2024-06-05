import typing
import collections.abc
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def primitive_nurbs_surface_circle_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    radius: typing.Any | None = 1.0,
    view_align: bool | typing.Any | None = False,
    enter_editmode: bool | typing.Any | None = False,
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
    layers: list[bool] | typing.Any | None = (
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
    ),
):
    """Construct a Nurbs surface Circle

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param radius: Radius
    :type radius: typing.Any | None
    :param view_align: Align to View, Align the new object to the view
    :type view_align: bool | typing.Any | None
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
    :type enter_editmode: bool | typing.Any | None
    :param location: Location, Location for the newly added object
    :type location: typing.Any | None
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Any | None
    :param layers: Layer
    :type layers: list[bool] | typing.Any | None
    """

    ...

def primitive_nurbs_surface_curve_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    radius: typing.Any | None = 1.0,
    view_align: bool | typing.Any | None = False,
    enter_editmode: bool | typing.Any | None = False,
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
    layers: list[bool] | typing.Any | None = (
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
    ),
):
    """Construct a Nurbs surface Curve

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param radius: Radius
    :type radius: typing.Any | None
    :param view_align: Align to View, Align the new object to the view
    :type view_align: bool | typing.Any | None
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
    :type enter_editmode: bool | typing.Any | None
    :param location: Location, Location for the newly added object
    :type location: typing.Any | None
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Any | None
    :param layers: Layer
    :type layers: list[bool] | typing.Any | None
    """

    ...

def primitive_nurbs_surface_cylinder_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    radius: typing.Any | None = 1.0,
    view_align: bool | typing.Any | None = False,
    enter_editmode: bool | typing.Any | None = False,
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
    layers: list[bool] | typing.Any | None = (
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
    ),
):
    """Construct a Nurbs surface Cylinder

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param radius: Radius
    :type radius: typing.Any | None
    :param view_align: Align to View, Align the new object to the view
    :type view_align: bool | typing.Any | None
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
    :type enter_editmode: bool | typing.Any | None
    :param location: Location, Location for the newly added object
    :type location: typing.Any | None
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Any | None
    :param layers: Layer
    :type layers: list[bool] | typing.Any | None
    """

    ...

def primitive_nurbs_surface_sphere_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    radius: typing.Any | None = 1.0,
    view_align: bool | typing.Any | None = False,
    enter_editmode: bool | typing.Any | None = False,
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
    layers: list[bool] | typing.Any | None = (
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
    ),
):
    """Construct a Nurbs surface Sphere

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param radius: Radius
    :type radius: typing.Any | None
    :param view_align: Align to View, Align the new object to the view
    :type view_align: bool | typing.Any | None
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
    :type enter_editmode: bool | typing.Any | None
    :param location: Location, Location for the newly added object
    :type location: typing.Any | None
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Any | None
    :param layers: Layer
    :type layers: list[bool] | typing.Any | None
    """

    ...

def primitive_nurbs_surface_surface_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    radius: typing.Any | None = 1.0,
    view_align: bool | typing.Any | None = False,
    enter_editmode: bool | typing.Any | None = False,
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
    layers: list[bool] | typing.Any | None = (
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
    ),
):
    """Construct a Nurbs surface Patch

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param radius: Radius
    :type radius: typing.Any | None
    :param view_align: Align to View, Align the new object to the view
    :type view_align: bool | typing.Any | None
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
    :type enter_editmode: bool | typing.Any | None
    :param location: Location, Location for the newly added object
    :type location: typing.Any | None
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Any | None
    :param layers: Layer
    :type layers: list[bool] | typing.Any | None
    """

    ...

def primitive_nurbs_surface_torus_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    radius: typing.Any | None = 1.0,
    view_align: bool | typing.Any | None = False,
    enter_editmode: bool | typing.Any | None = False,
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
    layers: list[bool] | typing.Any | None = (
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
    ),
):
    """Construct a Nurbs surface Torus

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param radius: Radius
    :type radius: typing.Any | None
    :param view_align: Align to View, Align the new object to the view
    :type view_align: bool | typing.Any | None
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
    :type enter_editmode: bool | typing.Any | None
    :param location: Location, Location for the newly added object
    :type location: typing.Any | None
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Any | None
    :param layers: Layer
    :type layers: list[bool] | typing.Any | None
    """

    ...
