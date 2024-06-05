import typing
import collections.abc
import bpy_types

from . import properties_animviz
from . import properties_constraint
from . import properties_data_armature
from . import properties_data_bone
from . import properties_data_camera
from . import properties_data_curve
from . import properties_data_empty
from . import properties_data_lamp
from . import properties_data_lattice
from . import properties_data_mesh
from . import properties_data_metaball
from . import properties_data_modifier
from . import properties_data_speaker
from . import properties_freestyle
from . import properties_game
from . import properties_grease_pencil_common
from . import properties_mask_common
from . import properties_material
from . import properties_object
from . import properties_paint_common
from . import properties_particle
from . import properties_physics_cloth
from . import properties_physics_common
from . import properties_physics_dynamicpaint
from . import properties_physics_field
from . import properties_physics_fluid
from . import properties_physics_rigidbody
from . import properties_physics_rigidbody_constraint
from . import properties_physics_smoke
from . import properties_physics_softbody
from . import properties_render
from . import properties_render_layer
from . import properties_scene
from . import properties_texture
from . import properties_world
from . import space_clip
from . import space_console
from . import space_dopesheet
from . import space_filebrowser
from . import space_graph
from . import space_image
from . import space_info
from . import space_logic
from . import space_nla
from . import space_node
from . import space_outliner
from . import space_properties
from . import space_sequencer
from . import space_text
from . import space_time
from . import space_userpref
from . import space_view3d
from . import space_view3d_toolbar

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class UI_UL_list(bpy_types.UIList, bpy_types._GenericUI):
    bl_rna: typing.Any
    id_data: typing.Any

    def append(self, draw_func):
        """

        :param draw_func:
        """
        ...

    def as_pointer(self): ...
    def driver_add(self): ...
    def driver_remove(self): ...
    def filter_items_by_name(
        self, pattern, bitflag, items, propname="name", flags=None, reverse=False
    ):
        """

        :param pattern:
        :param bitflag:
        :param items:
        :param propname:
        :param flags:
        :param reverse:
        """
        ...

    def get(self): ...
    def is_property_hidden(self): ...
    def is_property_readonly(self): ...
    def is_property_set(self): ...
    def items(self): ...
    def keyframe_delete(self): ...
    def keyframe_insert(self): ...
    def keys(self): ...
    def path_from_id(self): ...
    def path_resolve(self): ...
    def prepend(self, draw_func):
        """

        :param draw_func:
        """
        ...

    def property_unset(self): ...
    def remove(self, draw_func):
        """

        :param draw_func:
        """
        ...

    def sort_items_by_name(self, items, propname="name"):
        """

        :param items:
        :param propname:
        """
        ...

    def sort_items_helper(self, sort_data, key, reverse=False):
        """

        :param sort_data:
        :param key:
        :param reverse:
        """
        ...

    def type_recast(self): ...
    def values(self): ...

def register(): ...
def unregister(): ...
