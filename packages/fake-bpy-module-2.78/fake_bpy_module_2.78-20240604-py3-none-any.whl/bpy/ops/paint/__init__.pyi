import typing
import collections.abc
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def add_simple_uvs(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add cube map uvs on mesh

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def add_texture_paint_slot(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "DIFFUSE_COLOR",
    name: str | typing.Any = "Untitled",
    width: typing.Any | None = 1024,
    height: typing.Any | None = 1024,
    color: typing.Any | None = (0.0, 0.0, 0.0, 1.0),
    alpha: bool | typing.Any | None = True,
    generated_type: str | None = "BLANK",
    float: bool | typing.Any | None = False,
):
    """Add a texture paint slot

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type, Merge method to use
        :type type: str | None
        :param name: Name, Image datablock name
        :type name: str | typing.Any
        :param width: Width, Image width
        :type width: typing.Any | None
        :param height: Height, Image height
        :type height: typing.Any | None
        :param color: Color, Default fill color
        :type color: typing.Any | None
        :param alpha: Alpha, Create an image with an alpha channel
        :type alpha: bool | typing.Any | None
        :param generated_type: Generated Type, Fill the image with a grid for UV map testing

    BLANK Blank, Generate a blank image.

    UV_GRID UV Grid, Generated grid to test UV mappings.

    COLOR_GRID Color Grid, Generated improved UV grid to test UV mappings.
        :type generated_type: str | None
        :param float: 32 bit Float, Create image with 32 bit floating point bit depth
        :type float: bool | typing.Any | None
    """

    ...

def brush_colors_flip(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Toggle foreground and background brush colors

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def brush_select(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    paint_mode: str | None = "ACTIVE",
    sculpt_tool: str | None = "BLOB",
    vertex_paint_tool: str | None = "MIX",
    weight_paint_tool: str | None = "MIX",
    texture_paint_tool: str | None = "DRAW",
    toggle: bool | typing.Any | None = False,
    create_missing: bool | typing.Any | None = False,
):
    """Select a paint mode's brush by tool type

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param paint_mode: Paint Mode

    ACTIVE Current, Set brush for active paint mode.

    SCULPT Sculpt.

    VERTEX_PAINT Vertex Paint.

    WEIGHT_PAINT Weight Paint.

    TEXTURE_PAINT Texture Paint.
        :type paint_mode: str | None
        :param sculpt_tool: Sculpt Tool
        :type sculpt_tool: str | None
        :param vertex_paint_tool: Vertex Paint Tool

    MIX Mix, Use mix blending mode while painting.

    ADD Add, Use add blending mode while painting.

    SUB Subtract, Use subtract blending mode while painting.

    MUL Multiply, Use multiply blending mode while painting.

    BLUR Blur, Blur the color with surrounding values.

    LIGHTEN Lighten, Use lighten blending mode while painting.

    DARKEN Darken, Use darken blending mode while painting.
        :type vertex_paint_tool: str | None
        :param weight_paint_tool: Weight Paint Tool

    MIX Mix, Use mix blending mode while painting.

    ADD Add, Use add blending mode while painting.

    SUB Subtract, Use subtract blending mode while painting.

    MUL Multiply, Use multiply blending mode while painting.

    BLUR Blur, Blur the color with surrounding values.

    LIGHTEN Lighten, Use lighten blending mode while painting.

    DARKEN Darken, Use darken blending mode while painting.
        :type weight_paint_tool: str | None
        :param texture_paint_tool: Texture Paint Tool
        :type texture_paint_tool: str | None
        :param toggle: Toggle, Toggle between two brushes rather than cycling
        :type toggle: bool | typing.Any | None
        :param create_missing: Create Missing, If the requested brush type does not exist, create a new brush
        :type create_missing: bool | typing.Any | None
    """

    ...

def delete_texture_paint_slot(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Delete selected texture paint slot

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def face_select_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    action: str | None = "TOGGLE",
):
    """Change selection for all faces

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Action, Selection action to execute

    TOGGLE Toggle, Toggle selection for all elements.

    SELECT Select, Select all elements.

    DESELECT Deselect, Deselect all elements.

    INVERT Invert, Invert selection of all elements.
        :type action: str | None
    """

    ...

def face_select_hide(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    unselected: bool | typing.Any | None = False,
):
    """Hide selected faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Hide unselected rather than selected objects
    :type unselected: bool | typing.Any | None
    """

    ...

def face_select_linked(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select linked faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def face_select_linked_pick(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    deselect: bool | typing.Any | None = False,
):
    """Select linked faces under the cursor

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param deselect: Deselect, Deselect rather than select items
    :type deselect: bool | typing.Any | None
    """

    ...

def face_select_reveal(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    unselected: bool | typing.Any | None = False,
):
    """Reveal hidden faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Hide unselected rather than selected objects
    :type unselected: bool | typing.Any | None
    """

    ...

def grab_clone(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    delta: typing.Any | None = (0.0, 0.0),
):
    """Move the clone source image

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param delta: Delta, Delta offset of clone image in 0.0..1.0 coordinates
    :type delta: typing.Any | None
    """

    ...

def hide_show(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    action: str | None = "HIDE",
    area: str | None = "INSIDE",
    xmin: typing.Any | None = 0,
    xmax: typing.Any | None = 0,
    ymin: typing.Any | None = 0,
    ymax: typing.Any | None = 0,
):
    """Hide/show some vertices

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Action, Whether to hide or show vertices

    HIDE Hide, Hide vertices.

    SHOW Show, Show vertices.
        :type action: str | None
        :param area: Area, Which vertices to hide or show

    OUTSIDE Outside, Hide or show vertices outside the selection.

    INSIDE Inside, Hide or show vertices inside the selection.

    ALL All, Hide or show all vertices.

    MASKED Masked, Hide or show vertices that are masked (minimum mask value of 0.5).
        :type area: str | None
        :param xmin: X Min
        :type xmin: typing.Any | None
        :param xmax: X Max
        :type xmax: typing.Any | None
        :param ymin: Y Min
        :type ymin: typing.Any | None
        :param ymax: Y Max
        :type ymax: typing.Any | None
    """

    ...

def image_from_view(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
):
    """Make an image from the current 3D view for re-projection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: File Path, Name of the file
    :type filepath: str | typing.Any
    """

    ...

def image_paint(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    mode: str | None = "NORMAL",
):
    """Paint a stroke into the image

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param stroke: Stroke
        :type stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement] | None
        :param mode: Stroke Mode, Action taken when a paint stroke is made

    NORMAL Normal, Apply brush normally.

    INVERT Invert, Invert action of brush for duration of stroke.

    SMOOTH Smooth, Switch brush to smooth mode for duration of stroke.
        :type mode: str | None
    """

    ...

def mask_flood_fill(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "VALUE",
    value: typing.Any | None = 0.0,
):
    """Fill the whole mask with a given value, or invert its values

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode

    VALUE Value, Set mask to the level specified by the 'value' property.

    VALUE_INVERSE Value Inverted, Set mask to the level specified by the inverted 'value' property.

    INVERT Invert, Invert the mask.
        :type mode: str | None
        :param value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
        :type value: typing.Any | None
    """

    ...

def mask_lasso_gesture(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    mode: str | None = "VALUE",
    value: typing.Any | None = 1.0,
):
    """Add mask within the lasso as you move the brush

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param path: path
        :type path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None
        :param mode: Mode

    VALUE Value, Set mask to the level specified by the 'value' property.

    VALUE_INVERSE Value Inverted, Set mask to the level specified by the inverted 'value' property.

    INVERT Invert, Invert the mask.
        :type mode: str | None
        :param value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
        :type value: typing.Any | None
    """

    ...

def project_image(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    image: str | None = "",
):
    """Project an edited render from the active camera back onto the object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param image: Image
    :type image: str | None
    """

    ...

def sample_color(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    location: typing.Any | None = (0, 0),
    merged: bool | typing.Any | None = False,
    palette: bool | typing.Any | None = False,
):
    """Use the mouse to sample a color in the image

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param location: Location
    :type location: typing.Any | None
    :param merged: Sample Merged, Sample the output display color
    :type merged: bool | typing.Any | None
    :param palette: Add to Palette
    :type palette: bool | typing.Any | None
    """

    ...

def texture_paint_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Toggle texture paint mode in 3D view

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vert_select_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    action: str | None = "TOGGLE",
):
    """Change selection for all vertices

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Action, Selection action to execute

    TOGGLE Toggle, Toggle selection for all elements.

    SELECT Select, Select all elements.

    DESELECT Deselect, Deselect all elements.

    INVERT Invert, Invert selection of all elements.
        :type action: str | None
    """

    ...

def vert_select_ungrouped(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    extend: bool | typing.Any | None = False,
):
    """Select vertices without a group

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend the selection
    :type extend: bool | typing.Any | None
    """

    ...

def vertex_color_brightness_contrast(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    brightness: typing.Any | None = 0.0,
    contrast: typing.Any | None = 0.0,
):
    """Adjust vertex color brightness/contrast

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param brightness: Brightness
    :type brightness: typing.Any | None
    :param contrast: Contrast
    :type contrast: typing.Any | None
    """

    ...

def vertex_color_dirt(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    blur_strength: typing.Any | None = 1.0,
    blur_iterations: typing.Any | None = 1,
    clean_angle: typing.Any | None = 3.14159,
    dirt_angle: typing.Any | None = 0.0,
    dirt_only: bool | typing.Any | None = False,
):
    """Undocumented

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param blur_strength: Blur Strength, Blur strength per iteration
    :type blur_strength: typing.Any | None
    :param blur_iterations: Blur Iterations, Number of times to blur the colors (higher blurs more)
    :type blur_iterations: typing.Any | None
    :param clean_angle: Highlight Angle, Less than 90 limits the angle used in the tonal range
    :type clean_angle: typing.Any | None
    :param dirt_angle: Dirt Angle, Less than 90 limits the angle used in the tonal range
    :type dirt_angle: typing.Any | None
    :param dirt_only: Dirt Only, Don't calculate cleans for convex areas
    :type dirt_only: bool | typing.Any | None
    """

    ...

def vertex_color_hsv(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    h: typing.Any | None = 0.5,
    s: typing.Any | None = 1.0,
    v: typing.Any | None = 1.0,
):
    """Adjust vertex color HSV values

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param h: Hue
    :type h: typing.Any | None
    :param s: Saturation
    :type s: typing.Any | None
    :param v: Value
    :type v: typing.Any | None
    """

    ...

def vertex_color_invert(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Invert RGB values

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vertex_color_levels(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    offset: typing.Any | None = 0.0,
    gain: typing.Any | None = 1.0,
):
    """Adjust levels of vertex colors

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param offset: Offset, Value to add to colors
    :type offset: typing.Any | None
    :param gain: Gain, Value to multiply colors by
    :type gain: typing.Any | None
    """

    ...

def vertex_color_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Fill the active vertex color layer with the current paint color

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vertex_color_smooth(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Smooth colors across vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vertex_paint(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    mode: str | None = "NORMAL",
):
    """Paint a stroke in the active vertex color layer

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param stroke: Stroke
        :type stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement] | None
        :param mode: Stroke Mode, Action taken when a paint stroke is made

    NORMAL Normal, Apply brush normally.

    INVERT Invert, Invert action of brush for duration of stroke.

    SMOOTH Smooth, Switch brush to smooth mode for duration of stroke.
        :type mode: str | None
    """

    ...

def vertex_paint_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Toggle the vertex paint mode in 3D view

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def weight_from_bones(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "AUTOMATIC",
):
    """Set the weights of the groups matching the attached armature's selected bones, using the distance between the vertices and the bones

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type, Method to use for assigning weights

    AUTOMATIC Automatic, Automatic weights from bones.

    ENVELOPES From Envelopes, Weights from envelopes with user defined radius.
        :type type: str | None
    """

    ...

def weight_gradient(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "LINEAR",
    xstart: typing.Any | None = 0,
    xend: typing.Any | None = 0,
    ystart: typing.Any | None = 0,
    yend: typing.Any | None = 0,
    cursor: typing.Any | None = 1002,
):
    """Draw a line to apply a weight gradient to selected vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    :param xstart: X Start
    :type xstart: typing.Any | None
    :param xend: X End
    :type xend: typing.Any | None
    :param ystart: Y Start
    :type ystart: typing.Any | None
    :param yend: Y End
    :type yend: typing.Any | None
    :param cursor: Cursor, Mouse cursor style to use during the modal operator
    :type cursor: typing.Any | None
    """

    ...

def weight_paint(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    mode: str | None = "NORMAL",
):
    """Paint a stroke in the current vertex group's weights

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param stroke: Stroke
        :type stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement] | None
        :param mode: Stroke Mode, Action taken when a paint stroke is made

    NORMAL Normal, Apply brush normally.

    INVERT Invert, Invert action of brush for duration of stroke.

    SMOOTH Smooth, Switch brush to smooth mode for duration of stroke.
        :type mode: str | None
    """

    ...

def weight_paint_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Toggle weight paint mode in 3D view

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def weight_sample(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Use the mouse to sample a weight in the 3D view

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def weight_sample_group(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    group: str | None = "DEFAULT",
):
    """Select one of the vertex groups available under current mouse position

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param group: Keying Set, The Keying Set to use
    :type group: str | None
    """

    ...

def weight_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Fill the active vertex group with the current paint weight

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...
