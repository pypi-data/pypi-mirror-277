import typing
import collections.abc
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def bend(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    value: typing.Any | None = 0.0,
    mirror: bool | typing.Any | None = False,
    proportional: str | None = "DISABLED",
    proportional_edit_falloff: str | None = "SMOOTH",
    proportional_size: typing.Any | None = 1.0,
    snap: bool | typing.Any | None = False,
    snap_target: str | None = "CLOSEST",
    snap_point: typing.Any | None = (0.0, 0.0, 0.0),
    snap_align: bool | typing.Any | None = False,
    snap_normal: typing.Any | None = (0.0, 0.0, 0.0),
    gpencil_strokes: bool | typing.Any | None = False,
    release_confirm: bool | typing.Any | None = False,
):
    """Bend selected items between the 3D cursor and the mouse

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Angle
        :type value: typing.Any | None
        :param mirror: Mirror Editing
        :type mirror: bool | typing.Any | None
        :param proportional: Proportional Editing

    DISABLED Disable, Proportional Editing disabled.

    ENABLED Enable, Proportional Editing enabled.

    PROJECTED Projected (2D), Proportional Editing using screen space locations.

    CONNECTED Connected, Proportional Editing using connected geometry only.
        :type proportional: str | None
        :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.

    CONSTANT Constant, Constant falloff.

    RANDOM Random, Random falloff.
        :type proportional_edit_falloff: str | None
        :param proportional_size: Proportional Size
        :type proportional_size: typing.Any | None
        :param snap: Use Snapping Options
        :type snap: bool | typing.Any | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: str | None
        :param snap_point: Point
        :type snap_point: typing.Any | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | typing.Any | None
        :param snap_normal: Normal
        :type snap_normal: typing.Any | None
        :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
        :type gpencil_strokes: bool | typing.Any | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | typing.Any | None
    """

    ...

def create_orientation(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str | typing.Any = "",
    use_view: bool | typing.Any | None = False,
    use: bool | typing.Any | None = False,
    overwrite: bool | typing.Any | None = False,
):
    """Create transformation orientation from selection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the new custom orientation
    :type name: str | typing.Any
    :param use_view: Use View, Use the current view instead of the active object to create the new orientation
    :type use_view: bool | typing.Any | None
    :param use: Use after creation, Select orientation after its creation
    :type use: bool | typing.Any | None
    :param overwrite: Overwrite previous, Overwrite previously created orientation with same name
    :type overwrite: bool | typing.Any | None
    """

    ...

def delete_orientation(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Delete transformation orientation

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def edge_bevelweight(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    value: typing.Any | None = 0.0,
    snap: bool | typing.Any | None = False,
    snap_target: str | None = "CLOSEST",
    snap_point: typing.Any | None = (0.0, 0.0, 0.0),
    snap_align: bool | typing.Any | None = False,
    snap_normal: typing.Any | None = (0.0, 0.0, 0.0),
    release_confirm: bool | typing.Any | None = False,
):
    """Change the bevel weight of edges

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Factor
        :type value: typing.Any | None
        :param snap: Use Snapping Options
        :type snap: bool | typing.Any | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: str | None
        :param snap_point: Point
        :type snap_point: typing.Any | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | typing.Any | None
        :param snap_normal: Normal
        :type snap_normal: typing.Any | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | typing.Any | None
    """

    ...

def edge_crease(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    value: typing.Any | None = 0.0,
    snap: bool | typing.Any | None = False,
    snap_target: str | None = "CLOSEST",
    snap_point: typing.Any | None = (0.0, 0.0, 0.0),
    snap_align: bool | typing.Any | None = False,
    snap_normal: typing.Any | None = (0.0, 0.0, 0.0),
    release_confirm: bool | typing.Any | None = False,
):
    """Change the crease of edges

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Factor
        :type value: typing.Any | None
        :param snap: Use Snapping Options
        :type snap: bool | typing.Any | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: str | None
        :param snap_point: Point
        :type snap_point: typing.Any | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | typing.Any | None
        :param snap_normal: Normal
        :type snap_normal: typing.Any | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | typing.Any | None
    """

    ...

def edge_slide(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    value: typing.Any | None = 0.0,
    single_side: bool | typing.Any | None = False,
    use_even: bool | typing.Any | None = False,
    flipped: bool | typing.Any | None = False,
    use_clamp: bool | typing.Any | None = True,
    mirror: bool | typing.Any | None = False,
    snap: bool | typing.Any | None = False,
    snap_target: str | None = "CLOSEST",
    snap_point: typing.Any | None = (0.0, 0.0, 0.0),
    snap_align: bool | typing.Any | None = False,
    snap_normal: typing.Any | None = (0.0, 0.0, 0.0),
    correct_uv: bool | typing.Any | None = False,
    release_confirm: bool | typing.Any | None = False,
):
    """Slide an edge loop along a mesh

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Factor
        :type value: typing.Any | None
        :param single_side: Single Side
        :type single_side: bool | typing.Any | None
        :param use_even: Even, Make the edge loop match the shape of the adjacent edge loop
        :type use_even: bool | typing.Any | None
        :param flipped: Flipped, When Even mode is active, flips between the two adjacent edge loops
        :type flipped: bool | typing.Any | None
        :param use_clamp: Clamp, Clamp within the edge extents
        :type use_clamp: bool | typing.Any | None
        :param mirror: Mirror Editing
        :type mirror: bool | typing.Any | None
        :param snap: Use Snapping Options
        :type snap: bool | typing.Any | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: str | None
        :param snap_point: Point
        :type snap_point: typing.Any | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | typing.Any | None
        :param snap_normal: Normal
        :type snap_normal: typing.Any | None
        :param correct_uv: Correct UVs, Correct UV coordinates when transforming
        :type correct_uv: bool | typing.Any | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | typing.Any | None
    """

    ...

def mirror(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    constraint_axis: list[bool] | typing.Any | None = (False, False, False),
    constraint_orientation: str | None = "GLOBAL",
    proportional: str | None = "DISABLED",
    proportional_edit_falloff: str | None = "SMOOTH",
    proportional_size: typing.Any | None = 1.0,
    gpencil_strokes: bool | typing.Any | None = False,
    release_confirm: bool | typing.Any | None = False,
):
    """Mirror selected items around one or more axes

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint_axis: Constraint Axis
        :type constraint_axis: list[bool] | typing.Any | None
        :param constraint_orientation: Orientation, Transformation orientation
        :type constraint_orientation: str | None
        :param proportional: Proportional Editing

    DISABLED Disable, Proportional Editing disabled.

    ENABLED Enable, Proportional Editing enabled.

    PROJECTED Projected (2D), Proportional Editing using screen space locations.

    CONNECTED Connected, Proportional Editing using connected geometry only.
        :type proportional: str | None
        :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.

    CONSTANT Constant, Constant falloff.

    RANDOM Random, Random falloff.
        :type proportional_edit_falloff: str | None
        :param proportional_size: Proportional Size
        :type proportional_size: typing.Any | None
        :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
        :type gpencil_strokes: bool | typing.Any | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | typing.Any | None
    """

    ...

def push_pull(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    value: typing.Any | None = 0.0,
    mirror: bool | typing.Any | None = False,
    proportional: str | None = "DISABLED",
    proportional_edit_falloff: str | None = "SMOOTH",
    proportional_size: typing.Any | None = 1.0,
    snap: bool | typing.Any | None = False,
    snap_target: str | None = "CLOSEST",
    snap_point: typing.Any | None = (0.0, 0.0, 0.0),
    snap_align: bool | typing.Any | None = False,
    snap_normal: typing.Any | None = (0.0, 0.0, 0.0),
    release_confirm: bool | typing.Any | None = False,
):
    """Push/Pull selected items

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Distance
        :type value: typing.Any | None
        :param mirror: Mirror Editing
        :type mirror: bool | typing.Any | None
        :param proportional: Proportional Editing

    DISABLED Disable, Proportional Editing disabled.

    ENABLED Enable, Proportional Editing enabled.

    PROJECTED Projected (2D), Proportional Editing using screen space locations.

    CONNECTED Connected, Proportional Editing using connected geometry only.
        :type proportional: str | None
        :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.

    CONSTANT Constant, Constant falloff.

    RANDOM Random, Random falloff.
        :type proportional_edit_falloff: str | None
        :param proportional_size: Proportional Size
        :type proportional_size: typing.Any | None
        :param snap: Use Snapping Options
        :type snap: bool | typing.Any | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: str | None
        :param snap_point: Point
        :type snap_point: typing.Any | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | typing.Any | None
        :param snap_normal: Normal
        :type snap_normal: typing.Any | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | typing.Any | None
    """

    ...

def resize(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    value: typing.Any | None = (1.0, 1.0, 1.0),
    constraint_axis: list[bool] | typing.Any | None = (False, False, False),
    constraint_orientation: str | None = "GLOBAL",
    mirror: bool | typing.Any | None = False,
    proportional: str | None = "DISABLED",
    proportional_edit_falloff: str | None = "SMOOTH",
    proportional_size: typing.Any | None = 1.0,
    snap: bool | typing.Any | None = False,
    snap_target: str | None = "CLOSEST",
    snap_point: typing.Any | None = (0.0, 0.0, 0.0),
    snap_align: bool | typing.Any | None = False,
    snap_normal: typing.Any | None = (0.0, 0.0, 0.0),
    gpencil_strokes: bool | typing.Any | None = False,
    texture_space: bool | typing.Any | None = False,
    remove_on_cancel: bool | typing.Any | None = False,
    release_confirm: bool | typing.Any | None = False,
):
    """Scale (resize) selected items

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Vector
        :type value: typing.Any | None
        :param constraint_axis: Constraint Axis
        :type constraint_axis: list[bool] | typing.Any | None
        :param constraint_orientation: Orientation, Transformation orientation
        :type constraint_orientation: str | None
        :param mirror: Mirror Editing
        :type mirror: bool | typing.Any | None
        :param proportional: Proportional Editing

    DISABLED Disable, Proportional Editing disabled.

    ENABLED Enable, Proportional Editing enabled.

    PROJECTED Projected (2D), Proportional Editing using screen space locations.

    CONNECTED Connected, Proportional Editing using connected geometry only.
        :type proportional: str | None
        :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.

    CONSTANT Constant, Constant falloff.

    RANDOM Random, Random falloff.
        :type proportional_edit_falloff: str | None
        :param proportional_size: Proportional Size
        :type proportional_size: typing.Any | None
        :param snap: Use Snapping Options
        :type snap: bool | typing.Any | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: str | None
        :param snap_point: Point
        :type snap_point: typing.Any | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | typing.Any | None
        :param snap_normal: Normal
        :type snap_normal: typing.Any | None
        :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
        :type gpencil_strokes: bool | typing.Any | None
        :param texture_space: Edit Texture Space, Edit Object data texture space
        :type texture_space: bool | typing.Any | None
        :param remove_on_cancel: Remove on Cancel, Remove elements on cancel
        :type remove_on_cancel: bool | typing.Any | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | typing.Any | None
    """

    ...

def rotate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    value: typing.Any | None = 0.0,
    axis: typing.Any | None = (0.0, 0.0, 0.0),
    constraint_axis: list[bool] | typing.Any | None = (False, False, False),
    constraint_orientation: str | None = "GLOBAL",
    mirror: bool | typing.Any | None = False,
    proportional: str | None = "DISABLED",
    proportional_edit_falloff: str | None = "SMOOTH",
    proportional_size: typing.Any | None = 1.0,
    snap: bool | typing.Any | None = False,
    snap_target: str | None = "CLOSEST",
    snap_point: typing.Any | None = (0.0, 0.0, 0.0),
    snap_align: bool | typing.Any | None = False,
    snap_normal: typing.Any | None = (0.0, 0.0, 0.0),
    gpencil_strokes: bool | typing.Any | None = False,
    release_confirm: bool | typing.Any | None = False,
):
    """Rotate selected items

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Angle
        :type value: typing.Any | None
        :param axis: Axis, The axis around which the transformation occurs
        :type axis: typing.Any | None
        :param constraint_axis: Constraint Axis
        :type constraint_axis: list[bool] | typing.Any | None
        :param constraint_orientation: Orientation, Transformation orientation
        :type constraint_orientation: str | None
        :param mirror: Mirror Editing
        :type mirror: bool | typing.Any | None
        :param proportional: Proportional Editing

    DISABLED Disable, Proportional Editing disabled.

    ENABLED Enable, Proportional Editing enabled.

    PROJECTED Projected (2D), Proportional Editing using screen space locations.

    CONNECTED Connected, Proportional Editing using connected geometry only.
        :type proportional: str | None
        :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.

    CONSTANT Constant, Constant falloff.

    RANDOM Random, Random falloff.
        :type proportional_edit_falloff: str | None
        :param proportional_size: Proportional Size
        :type proportional_size: typing.Any | None
        :param snap: Use Snapping Options
        :type snap: bool | typing.Any | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: str | None
        :param snap_point: Point
        :type snap_point: typing.Any | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | typing.Any | None
        :param snap_normal: Normal
        :type snap_normal: typing.Any | None
        :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
        :type gpencil_strokes: bool | typing.Any | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | typing.Any | None
    """

    ...

def select_orientation(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    orientation: str | None = "GLOBAL",
):
    """Select transformation orientation

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param orientation: Orientation, Transformation orientation
    :type orientation: str | None
    """

    ...

def seq_slide(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    value: typing.Any | None = (0.0, 0.0),
    snap: bool | typing.Any | None = False,
    snap_target: str | None = "CLOSEST",
    snap_point: typing.Any | None = (0.0, 0.0, 0.0),
    snap_align: bool | typing.Any | None = False,
    snap_normal: typing.Any | None = (0.0, 0.0, 0.0),
    release_confirm: bool | typing.Any | None = False,
):
    """Slide a sequence strip in time

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Vector
        :type value: typing.Any | None
        :param snap: Use Snapping Options
        :type snap: bool | typing.Any | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: str | None
        :param snap_point: Point
        :type snap_point: typing.Any | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | typing.Any | None
        :param snap_normal: Normal
        :type snap_normal: typing.Any | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | typing.Any | None
    """

    ...

def shear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    value: typing.Any | None = 0.0,
    mirror: bool | typing.Any | None = False,
    proportional: str | None = "DISABLED",
    proportional_edit_falloff: str | None = "SMOOTH",
    proportional_size: typing.Any | None = 1.0,
    snap: bool | typing.Any | None = False,
    snap_target: str | None = "CLOSEST",
    snap_point: typing.Any | None = (0.0, 0.0, 0.0),
    snap_align: bool | typing.Any | None = False,
    snap_normal: typing.Any | None = (0.0, 0.0, 0.0),
    gpencil_strokes: bool | typing.Any | None = False,
    release_confirm: bool | typing.Any | None = False,
):
    """Shear selected items along the horizontal screen axis

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Offset
        :type value: typing.Any | None
        :param mirror: Mirror Editing
        :type mirror: bool | typing.Any | None
        :param proportional: Proportional Editing

    DISABLED Disable, Proportional Editing disabled.

    ENABLED Enable, Proportional Editing enabled.

    PROJECTED Projected (2D), Proportional Editing using screen space locations.

    CONNECTED Connected, Proportional Editing using connected geometry only.
        :type proportional: str | None
        :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.

    CONSTANT Constant, Constant falloff.

    RANDOM Random, Random falloff.
        :type proportional_edit_falloff: str | None
        :param proportional_size: Proportional Size
        :type proportional_size: typing.Any | None
        :param snap: Use Snapping Options
        :type snap: bool | typing.Any | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: str | None
        :param snap_point: Point
        :type snap_point: typing.Any | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | typing.Any | None
        :param snap_normal: Normal
        :type snap_normal: typing.Any | None
        :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
        :type gpencil_strokes: bool | typing.Any | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | typing.Any | None
    """

    ...

def shrink_fatten(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    value: typing.Any | None = 0.0,
    use_even_offset: bool | typing.Any | None = True,
    mirror: bool | typing.Any | None = False,
    proportional: str | None = "DISABLED",
    proportional_edit_falloff: str | None = "SMOOTH",
    proportional_size: typing.Any | None = 1.0,
    snap: bool | typing.Any | None = False,
    snap_target: str | None = "CLOSEST",
    snap_point: typing.Any | None = (0.0, 0.0, 0.0),
    snap_align: bool | typing.Any | None = False,
    snap_normal: typing.Any | None = (0.0, 0.0, 0.0),
    release_confirm: bool | typing.Any | None = False,
):
    """Shrink/fatten selected vertices along normals

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Offset
        :type value: typing.Any | None
        :param use_even_offset: Offset Even, Scale the offset to give more even thickness
        :type use_even_offset: bool | typing.Any | None
        :param mirror: Mirror Editing
        :type mirror: bool | typing.Any | None
        :param proportional: Proportional Editing

    DISABLED Disable, Proportional Editing disabled.

    ENABLED Enable, Proportional Editing enabled.

    PROJECTED Projected (2D), Proportional Editing using screen space locations.

    CONNECTED Connected, Proportional Editing using connected geometry only.
        :type proportional: str | None
        :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.

    CONSTANT Constant, Constant falloff.

    RANDOM Random, Random falloff.
        :type proportional_edit_falloff: str | None
        :param proportional_size: Proportional Size
        :type proportional_size: typing.Any | None
        :param snap: Use Snapping Options
        :type snap: bool | typing.Any | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: str | None
        :param snap_point: Point
        :type snap_point: typing.Any | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | typing.Any | None
        :param snap_normal: Normal
        :type snap_normal: typing.Any | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | typing.Any | None
    """

    ...

def skin_resize(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    value: typing.Any | None = (1.0, 1.0, 1.0),
    constraint_axis: list[bool] | typing.Any | None = (False, False, False),
    constraint_orientation: str | None = "GLOBAL",
    mirror: bool | typing.Any | None = False,
    proportional: str | None = "DISABLED",
    proportional_edit_falloff: str | None = "SMOOTH",
    proportional_size: typing.Any | None = 1.0,
    snap: bool | typing.Any | None = False,
    snap_target: str | None = "CLOSEST",
    snap_point: typing.Any | None = (0.0, 0.0, 0.0),
    snap_align: bool | typing.Any | None = False,
    snap_normal: typing.Any | None = (0.0, 0.0, 0.0),
    release_confirm: bool | typing.Any | None = False,
):
    """Scale selected vertices' skin radii

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Vector
        :type value: typing.Any | None
        :param constraint_axis: Constraint Axis
        :type constraint_axis: list[bool] | typing.Any | None
        :param constraint_orientation: Orientation, Transformation orientation
        :type constraint_orientation: str | None
        :param mirror: Mirror Editing
        :type mirror: bool | typing.Any | None
        :param proportional: Proportional Editing

    DISABLED Disable, Proportional Editing disabled.

    ENABLED Enable, Proportional Editing enabled.

    PROJECTED Projected (2D), Proportional Editing using screen space locations.

    CONNECTED Connected, Proportional Editing using connected geometry only.
        :type proportional: str | None
        :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.

    CONSTANT Constant, Constant falloff.

    RANDOM Random, Random falloff.
        :type proportional_edit_falloff: str | None
        :param proportional_size: Proportional Size
        :type proportional_size: typing.Any | None
        :param snap: Use Snapping Options
        :type snap: bool | typing.Any | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: str | None
        :param snap_point: Point
        :type snap_point: typing.Any | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | typing.Any | None
        :param snap_normal: Normal
        :type snap_normal: typing.Any | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | typing.Any | None
    """

    ...

def tilt(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    value: typing.Any | None = 0.0,
    mirror: bool | typing.Any | None = False,
    proportional: str | None = "DISABLED",
    proportional_edit_falloff: str | None = "SMOOTH",
    proportional_size: typing.Any | None = 1.0,
    snap: bool | typing.Any | None = False,
    snap_target: str | None = "CLOSEST",
    snap_point: typing.Any | None = (0.0, 0.0, 0.0),
    snap_align: bool | typing.Any | None = False,
    snap_normal: typing.Any | None = (0.0, 0.0, 0.0),
    release_confirm: bool | typing.Any | None = False,
):
    """Tilt selected control vertices of 3D curve

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Angle
        :type value: typing.Any | None
        :param mirror: Mirror Editing
        :type mirror: bool | typing.Any | None
        :param proportional: Proportional Editing

    DISABLED Disable, Proportional Editing disabled.

    ENABLED Enable, Proportional Editing enabled.

    PROJECTED Projected (2D), Proportional Editing using screen space locations.

    CONNECTED Connected, Proportional Editing using connected geometry only.
        :type proportional: str | None
        :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.

    CONSTANT Constant, Constant falloff.

    RANDOM Random, Random falloff.
        :type proportional_edit_falloff: str | None
        :param proportional_size: Proportional Size
        :type proportional_size: typing.Any | None
        :param snap: Use Snapping Options
        :type snap: bool | typing.Any | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: str | None
        :param snap_point: Point
        :type snap_point: typing.Any | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | typing.Any | None
        :param snap_normal: Normal
        :type snap_normal: typing.Any | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | typing.Any | None
    """

    ...

def tosphere(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    value: typing.Any | None = 0.0,
    mirror: bool | typing.Any | None = False,
    proportional: str | None = "DISABLED",
    proportional_edit_falloff: str | None = "SMOOTH",
    proportional_size: typing.Any | None = 1.0,
    snap: bool | typing.Any | None = False,
    snap_target: str | None = "CLOSEST",
    snap_point: typing.Any | None = (0.0, 0.0, 0.0),
    snap_align: bool | typing.Any | None = False,
    snap_normal: typing.Any | None = (0.0, 0.0, 0.0),
    gpencil_strokes: bool | typing.Any | None = False,
    release_confirm: bool | typing.Any | None = False,
):
    """Move selected vertices outward in a spherical shape around mesh center

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Factor
        :type value: typing.Any | None
        :param mirror: Mirror Editing
        :type mirror: bool | typing.Any | None
        :param proportional: Proportional Editing

    DISABLED Disable, Proportional Editing disabled.

    ENABLED Enable, Proportional Editing enabled.

    PROJECTED Projected (2D), Proportional Editing using screen space locations.

    CONNECTED Connected, Proportional Editing using connected geometry only.
        :type proportional: str | None
        :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.

    CONSTANT Constant, Constant falloff.

    RANDOM Random, Random falloff.
        :type proportional_edit_falloff: str | None
        :param proportional_size: Proportional Size
        :type proportional_size: typing.Any | None
        :param snap: Use Snapping Options
        :type snap: bool | typing.Any | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: str | None
        :param snap_point: Point
        :type snap_point: typing.Any | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | typing.Any | None
        :param snap_normal: Normal
        :type snap_normal: typing.Any | None
        :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
        :type gpencil_strokes: bool | typing.Any | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | typing.Any | None
    """

    ...

def trackball(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    value: typing.Any | None = (0.0, 0.0),
    mirror: bool | typing.Any | None = False,
    proportional: str | None = "DISABLED",
    proportional_edit_falloff: str | None = "SMOOTH",
    proportional_size: typing.Any | None = 1.0,
    snap: bool | typing.Any | None = False,
    snap_target: str | None = "CLOSEST",
    snap_point: typing.Any | None = (0.0, 0.0, 0.0),
    snap_align: bool | typing.Any | None = False,
    snap_normal: typing.Any | None = (0.0, 0.0, 0.0),
    gpencil_strokes: bool | typing.Any | None = False,
    release_confirm: bool | typing.Any | None = False,
):
    """Trackball style rotation of selected items

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Angle
        :type value: typing.Any | None
        :param mirror: Mirror Editing
        :type mirror: bool | typing.Any | None
        :param proportional: Proportional Editing

    DISABLED Disable, Proportional Editing disabled.

    ENABLED Enable, Proportional Editing enabled.

    PROJECTED Projected (2D), Proportional Editing using screen space locations.

    CONNECTED Connected, Proportional Editing using connected geometry only.
        :type proportional: str | None
        :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.

    CONSTANT Constant, Constant falloff.

    RANDOM Random, Random falloff.
        :type proportional_edit_falloff: str | None
        :param proportional_size: Proportional Size
        :type proportional_size: typing.Any | None
        :param snap: Use Snapping Options
        :type snap: bool | typing.Any | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: str | None
        :param snap_point: Point
        :type snap_point: typing.Any | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | typing.Any | None
        :param snap_normal: Normal
        :type snap_normal: typing.Any | None
        :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
        :type gpencil_strokes: bool | typing.Any | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | typing.Any | None
    """

    ...

def transform(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "TRANSLATION",
    value: typing.Any | None = (0.0, 0.0, 0.0, 0.0),
    axis: typing.Any | None = (0.0, 0.0, 0.0),
    constraint_axis: list[bool] | typing.Any | None = (False, False, False),
    constraint_orientation: str | None = "GLOBAL",
    mirror: bool | typing.Any | None = False,
    proportional: str | None = "DISABLED",
    proportional_edit_falloff: str | None = "SMOOTH",
    proportional_size: typing.Any | None = 1.0,
    snap: bool | typing.Any | None = False,
    snap_target: str | None = "CLOSEST",
    snap_point: typing.Any | None = (0.0, 0.0, 0.0),
    snap_align: bool | typing.Any | None = False,
    snap_normal: typing.Any | None = (0.0, 0.0, 0.0),
    gpencil_strokes: bool | typing.Any | None = False,
    release_confirm: bool | typing.Any | None = False,
):
    """Transform selected items by mode type

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode
        :type mode: str | None
        :param value: Values
        :type value: typing.Any | None
        :param axis: Axis, The axis around which the transformation occurs
        :type axis: typing.Any | None
        :param constraint_axis: Constraint Axis
        :type constraint_axis: list[bool] | typing.Any | None
        :param constraint_orientation: Orientation, Transformation orientation
        :type constraint_orientation: str | None
        :param mirror: Mirror Editing
        :type mirror: bool | typing.Any | None
        :param proportional: Proportional Editing

    DISABLED Disable, Proportional Editing disabled.

    ENABLED Enable, Proportional Editing enabled.

    PROJECTED Projected (2D), Proportional Editing using screen space locations.

    CONNECTED Connected, Proportional Editing using connected geometry only.
        :type proportional: str | None
        :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.

    CONSTANT Constant, Constant falloff.

    RANDOM Random, Random falloff.
        :type proportional_edit_falloff: str | None
        :param proportional_size: Proportional Size
        :type proportional_size: typing.Any | None
        :param snap: Use Snapping Options
        :type snap: bool | typing.Any | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: str | None
        :param snap_point: Point
        :type snap_point: typing.Any | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | typing.Any | None
        :param snap_normal: Normal
        :type snap_normal: typing.Any | None
        :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
        :type gpencil_strokes: bool | typing.Any | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | typing.Any | None
    """

    ...

def translate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    value: typing.Any | None = (0.0, 0.0, 0.0),
    constraint_axis: list[bool] | typing.Any | None = (False, False, False),
    constraint_orientation: str | None = "GLOBAL",
    mirror: bool | typing.Any | None = False,
    proportional: str | None = "DISABLED",
    proportional_edit_falloff: str | None = "SMOOTH",
    proportional_size: typing.Any | None = 1.0,
    snap: bool | typing.Any | None = False,
    snap_target: str | None = "CLOSEST",
    snap_point: typing.Any | None = (0.0, 0.0, 0.0),
    snap_align: bool | typing.Any | None = False,
    snap_normal: typing.Any | None = (0.0, 0.0, 0.0),
    gpencil_strokes: bool | typing.Any | None = False,
    texture_space: bool | typing.Any | None = False,
    remove_on_cancel: bool | typing.Any | None = False,
    release_confirm: bool | typing.Any | None = False,
):
    """Translate (move) selected items

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Vector
        :type value: typing.Any | None
        :param constraint_axis: Constraint Axis
        :type constraint_axis: list[bool] | typing.Any | None
        :param constraint_orientation: Orientation, Transformation orientation
        :type constraint_orientation: str | None
        :param mirror: Mirror Editing
        :type mirror: bool | typing.Any | None
        :param proportional: Proportional Editing

    DISABLED Disable, Proportional Editing disabled.

    ENABLED Enable, Proportional Editing enabled.

    PROJECTED Projected (2D), Proportional Editing using screen space locations.

    CONNECTED Connected, Proportional Editing using connected geometry only.
        :type proportional: str | None
        :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.

    CONSTANT Constant, Constant falloff.

    RANDOM Random, Random falloff.
        :type proportional_edit_falloff: str | None
        :param proportional_size: Proportional Size
        :type proportional_size: typing.Any | None
        :param snap: Use Snapping Options
        :type snap: bool | typing.Any | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: str | None
        :param snap_point: Point
        :type snap_point: typing.Any | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | typing.Any | None
        :param snap_normal: Normal
        :type snap_normal: typing.Any | None
        :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
        :type gpencil_strokes: bool | typing.Any | None
        :param texture_space: Edit Texture Space, Edit Object data texture space
        :type texture_space: bool | typing.Any | None
        :param remove_on_cancel: Remove on Cancel, Remove elements on cancel
        :type remove_on_cancel: bool | typing.Any | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | typing.Any | None
    """

    ...

def vert_slide(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    value: typing.Any | None = 0.0,
    use_even: bool | typing.Any | None = False,
    flipped: bool | typing.Any | None = False,
    use_clamp: bool | typing.Any | None = True,
    mirror: bool | typing.Any | None = False,
    snap: bool | typing.Any | None = False,
    snap_target: str | None = "CLOSEST",
    snap_point: typing.Any | None = (0.0, 0.0, 0.0),
    snap_align: bool | typing.Any | None = False,
    snap_normal: typing.Any | None = (0.0, 0.0, 0.0),
    correct_uv: bool | typing.Any | None = False,
    release_confirm: bool | typing.Any | None = False,
):
    """Slide a vertex along a mesh

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Factor
        :type value: typing.Any | None
        :param use_even: Even, Make the edge loop match the shape of the adjacent edge loop
        :type use_even: bool | typing.Any | None
        :param flipped: Flipped, When Even mode is active, flips between the two adjacent edge loops
        :type flipped: bool | typing.Any | None
        :param use_clamp: Clamp, Clamp within the edge extents
        :type use_clamp: bool | typing.Any | None
        :param mirror: Mirror Editing
        :type mirror: bool | typing.Any | None
        :param snap: Use Snapping Options
        :type snap: bool | typing.Any | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: str | None
        :param snap_point: Point
        :type snap_point: typing.Any | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | typing.Any | None
        :param snap_normal: Normal
        :type snap_normal: typing.Any | None
        :param correct_uv: Correct UVs, Correct UV coordinates when transforming
        :type correct_uv: bool | typing.Any | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | typing.Any | None
    """

    ...

def vertex_random(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    offset: typing.Any | None = 0.1,
    uniform: typing.Any | None = 0.0,
    normal: typing.Any | None = 0.0,
    seed: typing.Any | None = 0,
):
    """Randomize vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param offset: Amount, Distance to offset
    :type offset: typing.Any | None
    :param uniform: Uniform, Increase for uniform offset distance
    :type uniform: typing.Any | None
    :param normal: normal, Align offset direction to normals
    :type normal: typing.Any | None
    :param seed: Random Seed, Seed for the random number generator
    :type seed: typing.Any | None
    """

    ...

def vertex_warp(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    warp_angle: typing.Any | None = 6.28319,
    offset_angle: typing.Any | None = 0.0,
    min: typing.Any | None = -1,
    max: typing.Any | None = 1.0,
    viewmat: typing.Any | None = (
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
    ),
    center: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Warp vertices around the cursor

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param warp_angle: Warp Angle, Amount to warp about the cursor
    :type warp_angle: typing.Any | None
    :param offset_angle: Offset Angle, Angle to use as the basis for warping
    :type offset_angle: typing.Any | None
    :param min: Min
    :type min: typing.Any | None
    :param max: Max
    :type max: typing.Any | None
    :param viewmat: Matrix
    :type viewmat: typing.Any | None
    :param center: Center
    :type center: typing.Any | None
    """

    ...
