import typing
import collections.abc
import nodeitems_utils

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class SortedNodeCategory(nodeitems_utils.NodeCategory):
    def poll(self, context):
        """

        :param context:
        """
        ...

class CompositorNodeCategory(SortedNodeCategory, nodeitems_utils.NodeCategory):
    def poll(self, context):
        """

        :param context:
        """
        ...

class ShaderNewNodeCategory(SortedNodeCategory, nodeitems_utils.NodeCategory):
    def poll(self, context):
        """

        :param context:
        """
        ...

class ShaderOldNodeCategory(SortedNodeCategory, nodeitems_utils.NodeCategory):
    def poll(self, context):
        """

        :param context:
        """
        ...

class TextureNodeCategory(SortedNodeCategory, nodeitems_utils.NodeCategory):
    def poll(self, context):
        """

        :param context:
        """
        ...

def group_input_output_item_poll(context): ...
def group_tools_draw(layout, context): ...
def line_style_shader_nodes_poll(context): ...
def node_group_items(context): ...
def object_shader_nodes_poll(context): ...
def register(): ...
def unregister(): ...
def world_shader_nodes_poll(context): ...
