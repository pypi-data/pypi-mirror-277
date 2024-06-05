import typing
import collections.abc

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class NodeCategory:
    def poll(self, context):
        """

        :param context:
        """
        ...

class NodeItem:
    label: typing.Any

    def draw(self, layout, context):
        """

        :param layout:
        :param context:
        """
        ...

class NodeItemCustom: ...

def draw_node_categories_menu(context): ...
def node_categories_iter(context): ...
def node_items_iter(context): ...
def register_node_categories(identifier, cat_list): ...
def unregister_node_cat_types(cats): ...
def unregister_node_categories(identifier=None): ...
