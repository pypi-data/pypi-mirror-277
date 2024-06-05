import typing
import collections.abc
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def autocomplete(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Show a list of used text in the open document

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def comment(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Convert selected text to comment

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def convert_whitespace(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "SPACES",
):
    """Convert whitespaces by type

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type, Type of whitespace to convert to
    :type type: str | None
    """

    ...

def copy(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Copy selected text to clipboard

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def cursor_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    x: typing.Any | None = 0,
    y: typing.Any | None = 0,
):
    """Set cursor position

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param x: X
    :type x: typing.Any | None
    :param y: Y
    :type y: typing.Any | None
    """

    ...

def cut(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Cut selected text to clipboard

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def delete(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "NEXT_CHARACTER",
):
    """Delete text by cursor position

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type, Which part of the text to delete
    :type type: str | None
    """

    ...

def duplicate_line(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Duplicate the current line

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def find(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Find specified text

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def find_set_selected(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Find specified text and set as selected

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def indent(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Indent selected text

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def insert(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    text: str | typing.Any = "",
):
    """Insert text at cursor position

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param text: Text, Text to insert at the cursor position
    :type text: str | typing.Any
    """

    ...

def jump(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    line: typing.Any | None = 1,
):
    """Jump cursor to line

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param line: Line, Line number to jump to
    :type line: typing.Any | None
    """

    ...

def line_break(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Insert line break at cursor position

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def line_number(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """The current line number

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def make_internal(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Make active text file internal

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "LINE_BEGIN",
):
    """Move cursor to position type

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type, Where to move cursor to
    :type type: str | None
    """

    ...

def move_lines(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    direction: str | None = "DOWN",
):
    """Move the currently selected line(s) up/down

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction
    :type direction: str | None
    """

    ...

def move_select(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "LINE_BEGIN",
):
    """Move the cursor while selecting

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type, Where to move cursor to, to make a selection
    :type type: str | None
    """

    ...

def new(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Create a new text data block

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def open(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    filter_blender: bool | typing.Any | None = False,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = True,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = True,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 9,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "FILE_SORT_ALPHA",
    internal: bool | typing.Any | None = False,
):
    """Open a new text data block

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param display_type: Display Type

    DEFAULT Default, Automatically determine display type for files.

    LIST_SHORT Short List, Display files as short list.

    LIST_LONG Long List, Display files as a detailed list.

    THUMBNAIL Thumbnails, Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode

    FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.

    FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.

    FILE_SORT_TIME Sort by time, Sort files by modification time.

    FILE_SORT_SIZE Sort by size, Sort files by size.
        :type sort_method: str | None
        :param internal: Make internal, Make text file internal after loading
        :type internal: bool | typing.Any | None
    """

    ...

def overwrite_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Toggle overwrite while typing

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def paste(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    selection: bool | typing.Any | None = False,
):
    """Paste text from clipboard

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param selection: Selection, Paste text selected elsewhere rather than copied (X11 only)
    :type selection: bool | typing.Any | None
    """

    ...

def properties(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Toggle the properties region visibility

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def refresh_pyconstraints(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Refresh all pyconstraints

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def reload(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reload active text data block from its file

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def replace(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Replace text with the specified text

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def replace_set_selected(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Replace text with specified text and set as selected

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def resolve_conflict(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    resolution: str | None = "IGNORE",
):
    """When external text is out of sync, resolve the conflict

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param resolution: Resolution, How to solve conflict due to differences in internal and external text
    :type resolution: str | None
    """

    ...

def run_script(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Run active script

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def save(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Save active text data block

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def save_as(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    check_existing: bool | typing.Any | None = True,
    filter_blender: bool | typing.Any | None = False,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = True,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = True,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 9,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "FILE_SORT_ALPHA",
):
    """Save active text file with options

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param display_type: Display Type

    DEFAULT Default, Automatically determine display type for files.

    LIST_SHORT Short List, Display files as short list.

    LIST_LONG Long List, Display files as a detailed list.

    THUMBNAIL Thumbnails, Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode

    FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.

    FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.

    FILE_SORT_TIME Sort by time, Sort files by modification time.

    FILE_SORT_SIZE Sort by size, Sort files by size.
        :type sort_method: str | None
    """

    ...

def scroll(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    lines: typing.Any | None = 1,
):
    """Undocumented

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param lines: Lines, Number of lines to scroll
    :type lines: typing.Any | None
    """

    ...

def scroll_bar(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    lines: typing.Any | None = 1,
):
    """Undocumented

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param lines: Lines, Number of lines to scroll
    :type lines: typing.Any | None
    """

    ...

def select_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select all text

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def select_line(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select text by line

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def select_word(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select word under cursor

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def selection_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    select: bool | typing.Any | None = False,
):
    """Set cursor selection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param select: Select, Set selection end rather than cursor
    :type select: bool | typing.Any | None
    """

    ...

def start_find(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Start searching text

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def to_3d_object(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    split_lines: bool | typing.Any | None = False,
):
    """Create 3D text object from active text data block

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param split_lines: Split Lines, Create one object per line in the text
    :type split_lines: bool | typing.Any | None
    """

    ...

def uncomment(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Convert selected comment to text

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def unindent(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Unindent selected text

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def unlink(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Unlink active text data block

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...
