import typing
import collections.abc
import bpy.types
import bpy_types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class NodeAddOperator:
    settings: typing.Any
    type: typing.Any
    use_transform: typing.Any

    def create_node(self, context, node_type=None):
        """

        :param context:
        :param node_type:
        """
        ...

    def execute(self, context):
        """

        :param context:
        """
        ...

    def invoke(self, context, event):
        """

        :param context:
        :param event:
        """
        ...

    def poll(self, context):
        """

        :param context:
        """
        ...

    def store_mouse_cursor(self, context, event):
        """

        :param context:
        :param event:
        """
        ...

class NODE_OT_collapse_hide_unused_toggle(bpy_types.Operator):
    """Toggle collapsed nodes and hide unused sockets"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    order: typing.Any

    def as_keywords(self, ignore=()):
        """Return a copy of the properties as a dictionary

        :param ignore:
        """
        ...

    def as_pointer(self) -> int:
        """Returns the memory address which holds a pointer to blenders internal data

        :return: int (memory address).
        :rtype: int
        """
        ...

    def driver_add(self) -> bpy.types.FCurve:
        """Adds driver(s) to the given property

        :return: The driver(s) added.
        :rtype: bpy.types.FCurve
        """
        ...

    def driver_remove(self) -> bool:
        """Remove driver(s) from the given property

        :return: Success of driver removal.
        :rtype: bool
        """
        ...

    def execute(self, context):
        """

        :param context:
        """
        ...

    def get(self):
        """Returns the value of the custom property assigned to key or default
        when not found (matches pythons dictionary function of the same name).

        """
        ...

    def is_property_hidden(self) -> bool:
        """Check if a property is hidden.

        :return: True when the property is hidden.
        :rtype: bool
        """
        ...

    def is_property_readonly(self) -> bool:
        """Check if a property is readonly.

        :return: True when the property is readonly (not writable).
        :rtype: bool
        """
        ...

    def is_property_set(self) -> bool:
        """Check if a property is set, use for testing operator properties.

        :return: True when the property has been set.
        :rtype: bool
        """
        ...

    def items(self):
        """Returns the items of this objects custom properties (matches pythons
        dictionary function of the same name).

                :return: custom property key, value pairs.
        """
        ...

    def keyframe_delete(self) -> bool:
        """Remove a keyframe from this properties fcurve.

        :return: Success of keyframe deleation.
        :rtype: bool
        """
        ...

    def keyframe_insert(self) -> bool:
        """Insert a keyframe on the property given, adding fcurves and animation data when necessary.

        :return: Success of keyframe insertion.
        :rtype: bool
        """
        ...

    def keys(self) -> list[str]:
        """Returns the keys of this objects custom properties (matches pythons
        dictionary function of the same name).

                :return: custom property keys.
                :rtype: list[str]
        """
        ...

    def path_from_id(self) -> str:
        """Returns the data path from the ID to this object (string).

                :return: The path from `bpy.types.bpy_struct.id_data`
        to this struct and property (when given).
                :rtype: str
        """
        ...

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def poll(self, context):
        """

        :param context:
        """
        ...

    def property_unset(self):
        """Unset a property, will use default value afterward."""
        ...

    def type_recast(self):
        """Return a new instance, this is needed because types
        such as textures can be changed at runtime.

                :return: a new instance of this object with the type initialized again.
        """
        ...

    def values(self) -> list:
        """Returns the values of this objects custom properties (matches pythons
        dictionary function of the same name).

                :return: custom property values.
                :rtype: list
        """
        ...

class NODE_OT_tree_path_parent(bpy_types.Operator):
    """Go to parent node tree"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    order: typing.Any

    def as_keywords(self, ignore=()):
        """Return a copy of the properties as a dictionary

        :param ignore:
        """
        ...

    def as_pointer(self) -> int:
        """Returns the memory address which holds a pointer to blenders internal data

        :return: int (memory address).
        :rtype: int
        """
        ...

    def driver_add(self) -> bpy.types.FCurve:
        """Adds driver(s) to the given property

        :return: The driver(s) added.
        :rtype: bpy.types.FCurve
        """
        ...

    def driver_remove(self) -> bool:
        """Remove driver(s) from the given property

        :return: Success of driver removal.
        :rtype: bool
        """
        ...

    def execute(self, context):
        """

        :param context:
        """
        ...

    def get(self):
        """Returns the value of the custom property assigned to key or default
        when not found (matches pythons dictionary function of the same name).

        """
        ...

    def is_property_hidden(self) -> bool:
        """Check if a property is hidden.

        :return: True when the property is hidden.
        :rtype: bool
        """
        ...

    def is_property_readonly(self) -> bool:
        """Check if a property is readonly.

        :return: True when the property is readonly (not writable).
        :rtype: bool
        """
        ...

    def is_property_set(self) -> bool:
        """Check if a property is set, use for testing operator properties.

        :return: True when the property has been set.
        :rtype: bool
        """
        ...

    def items(self):
        """Returns the items of this objects custom properties (matches pythons
        dictionary function of the same name).

                :return: custom property key, value pairs.
        """
        ...

    def keyframe_delete(self) -> bool:
        """Remove a keyframe from this properties fcurve.

        :return: Success of keyframe deleation.
        :rtype: bool
        """
        ...

    def keyframe_insert(self) -> bool:
        """Insert a keyframe on the property given, adding fcurves and animation data when necessary.

        :return: Success of keyframe insertion.
        :rtype: bool
        """
        ...

    def keys(self) -> list[str]:
        """Returns the keys of this objects custom properties (matches pythons
        dictionary function of the same name).

                :return: custom property keys.
                :rtype: list[str]
        """
        ...

    def path_from_id(self) -> str:
        """Returns the data path from the ID to this object (string).

                :return: The path from `bpy.types.bpy_struct.id_data`
        to this struct and property (when given).
                :rtype: str
        """
        ...

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def poll(self, context):
        """

        :param context:
        """
        ...

    def property_unset(self):
        """Unset a property, will use default value afterward."""
        ...

    def type_recast(self):
        """Return a new instance, this is needed because types
        such as textures can be changed at runtime.

                :return: a new instance of this object with the type initialized again.
        """
        ...

    def values(self) -> list:
        """Returns the values of this objects custom properties (matches pythons
        dictionary function of the same name).

                :return: custom property values.
                :rtype: list
        """
        ...

class NodeSetting(bpy_types.PropertyGroup):
    bl_rna: typing.Any
    id_data: typing.Any
    value: typing.Any

    def as_pointer(self) -> int:
        """Returns the memory address which holds a pointer to blenders internal data

        :return: int (memory address).
        :rtype: int
        """
        ...

    def driver_add(self) -> bpy.types.FCurve:
        """Adds driver(s) to the given property

        :return: The driver(s) added.
        :rtype: bpy.types.FCurve
        """
        ...

    def driver_remove(self) -> bool:
        """Remove driver(s) from the given property

        :return: Success of driver removal.
        :rtype: bool
        """
        ...

    def get(self):
        """Returns the value of the custom property assigned to key or default
        when not found (matches pythons dictionary function of the same name).

        """
        ...

    def is_property_hidden(self) -> bool:
        """Check if a property is hidden.

        :return: True when the property is hidden.
        :rtype: bool
        """
        ...

    def is_property_readonly(self) -> bool:
        """Check if a property is readonly.

        :return: True when the property is readonly (not writable).
        :rtype: bool
        """
        ...

    def is_property_set(self) -> bool:
        """Check if a property is set, use for testing operator properties.

        :return: True when the property has been set.
        :rtype: bool
        """
        ...

    def items(self):
        """Returns the items of this objects custom properties (matches pythons
        dictionary function of the same name).

                :return: custom property key, value pairs.
        """
        ...

    def keyframe_delete(self) -> bool:
        """Remove a keyframe from this properties fcurve.

        :return: Success of keyframe deleation.
        :rtype: bool
        """
        ...

    def keyframe_insert(self) -> bool:
        """Insert a keyframe on the property given, adding fcurves and animation data when necessary.

        :return: Success of keyframe insertion.
        :rtype: bool
        """
        ...

    def keys(self) -> list[str]:
        """Returns the keys of this objects custom properties (matches pythons
        dictionary function of the same name).

                :return: custom property keys.
                :rtype: list[str]
        """
        ...

    def path_from_id(self) -> str:
        """Returns the data path from the ID to this object (string).

                :return: The path from `bpy.types.bpy_struct.id_data`
        to this struct and property (when given).
                :rtype: str
        """
        ...

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def property_unset(self):
        """Unset a property, will use default value afterward."""
        ...

    def type_recast(self):
        """Return a new instance, this is needed because types
        such as textures can be changed at runtime.

                :return: a new instance of this object with the type initialized again.
        """
        ...

    def values(self) -> list:
        """Returns the values of this objects custom properties (matches pythons
        dictionary function of the same name).

                :return: custom property values.
                :rtype: list
        """
        ...

class NODE_OT_add_and_link_node(NodeAddOperator, bpy_types.Operator):
    """Add a node to the active tree and link to an existing socket"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    link_socket_index: typing.Any
    order: typing.Any
    settings: typing.Any
    type: typing.Any
    use_transform: typing.Any

    def as_keywords(self, ignore=()):
        """Return a copy of the properties as a dictionary

        :param ignore:
        """
        ...

    def as_pointer(self) -> int:
        """Returns the memory address which holds a pointer to blenders internal data

        :return: int (memory address).
        :rtype: int
        """
        ...

    def create_node(self, context, node_type=None):
        """

        :param context:
        :param node_type:
        """
        ...

    def driver_add(self) -> bpy.types.FCurve:
        """Adds driver(s) to the given property

        :return: The driver(s) added.
        :rtype: bpy.types.FCurve
        """
        ...

    def driver_remove(self) -> bool:
        """Remove driver(s) from the given property

        :return: Success of driver removal.
        :rtype: bool
        """
        ...

    def execute(self, context):
        """

        :param context:
        """
        ...

    def get(self):
        """Returns the value of the custom property assigned to key or default
        when not found (matches pythons dictionary function of the same name).

        """
        ...

    def invoke(self, context, event):
        """

        :param context:
        :param event:
        """
        ...

    def is_property_hidden(self) -> bool:
        """Check if a property is hidden.

        :return: True when the property is hidden.
        :rtype: bool
        """
        ...

    def is_property_readonly(self) -> bool:
        """Check if a property is readonly.

        :return: True when the property is readonly (not writable).
        :rtype: bool
        """
        ...

    def is_property_set(self) -> bool:
        """Check if a property is set, use for testing operator properties.

        :return: True when the property has been set.
        :rtype: bool
        """
        ...

    def items(self):
        """Returns the items of this objects custom properties (matches pythons
        dictionary function of the same name).

                :return: custom property key, value pairs.
        """
        ...

    def keyframe_delete(self) -> bool:
        """Remove a keyframe from this properties fcurve.

        :return: Success of keyframe deleation.
        :rtype: bool
        """
        ...

    def keyframe_insert(self) -> bool:
        """Insert a keyframe on the property given, adding fcurves and animation data when necessary.

        :return: Success of keyframe insertion.
        :rtype: bool
        """
        ...

    def keys(self) -> list[str]:
        """Returns the keys of this objects custom properties (matches pythons
        dictionary function of the same name).

                :return: custom property keys.
                :rtype: list[str]
        """
        ...

    def path_from_id(self) -> str:
        """Returns the data path from the ID to this object (string).

                :return: The path from `bpy.types.bpy_struct.id_data`
        to this struct and property (when given).
                :rtype: str
        """
        ...

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def poll(self, context):
        """

        :param context:
        """
        ...

    def property_unset(self):
        """Unset a property, will use default value afterward."""
        ...

    def store_mouse_cursor(self, context, event):
        """

        :param context:
        :param event:
        """
        ...

    def type_recast(self):
        """Return a new instance, this is needed because types
        such as textures can be changed at runtime.

                :return: a new instance of this object with the type initialized again.
        """
        ...

    def values(self) -> list:
        """Returns the values of this objects custom properties (matches pythons
        dictionary function of the same name).

                :return: custom property values.
                :rtype: list
        """
        ...

class NODE_OT_add_node(NodeAddOperator, bpy_types.Operator):
    """Add a node to the active tree"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    order: typing.Any
    settings: typing.Any
    type: typing.Any
    use_transform: typing.Any

    def as_keywords(self, ignore=()):
        """Return a copy of the properties as a dictionary

        :param ignore:
        """
        ...

    def as_pointer(self) -> int:
        """Returns the memory address which holds a pointer to blenders internal data

        :return: int (memory address).
        :rtype: int
        """
        ...

    def create_node(self, context, node_type=None):
        """

        :param context:
        :param node_type:
        """
        ...

    def driver_add(self) -> bpy.types.FCurve:
        """Adds driver(s) to the given property

        :return: The driver(s) added.
        :rtype: bpy.types.FCurve
        """
        ...

    def driver_remove(self) -> bool:
        """Remove driver(s) from the given property

        :return: Success of driver removal.
        :rtype: bool
        """
        ...

    def execute(self, context):
        """

        :param context:
        """
        ...

    def get(self):
        """Returns the value of the custom property assigned to key or default
        when not found (matches pythons dictionary function of the same name).

        """
        ...

    def invoke(self, context, event):
        """

        :param context:
        :param event:
        """
        ...

    def is_property_hidden(self) -> bool:
        """Check if a property is hidden.

        :return: True when the property is hidden.
        :rtype: bool
        """
        ...

    def is_property_readonly(self) -> bool:
        """Check if a property is readonly.

        :return: True when the property is readonly (not writable).
        :rtype: bool
        """
        ...

    def is_property_set(self) -> bool:
        """Check if a property is set, use for testing operator properties.

        :return: True when the property has been set.
        :rtype: bool
        """
        ...

    def items(self):
        """Returns the items of this objects custom properties (matches pythons
        dictionary function of the same name).

                :return: custom property key, value pairs.
        """
        ...

    def keyframe_delete(self) -> bool:
        """Remove a keyframe from this properties fcurve.

        :return: Success of keyframe deleation.
        :rtype: bool
        """
        ...

    def keyframe_insert(self) -> bool:
        """Insert a keyframe on the property given, adding fcurves and animation data when necessary.

        :return: Success of keyframe insertion.
        :rtype: bool
        """
        ...

    def keys(self) -> list[str]:
        """Returns the keys of this objects custom properties (matches pythons
        dictionary function of the same name).

                :return: custom property keys.
                :rtype: list[str]
        """
        ...

    def path_from_id(self) -> str:
        """Returns the data path from the ID to this object (string).

                :return: The path from `bpy.types.bpy_struct.id_data`
        to this struct and property (when given).
                :rtype: str
        """
        ...

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def poll(self, context):
        """

        :param context:
        """
        ...

    def property_unset(self):
        """Unset a property, will use default value afterward."""
        ...

    def store_mouse_cursor(self, context, event):
        """

        :param context:
        :param event:
        """
        ...

    def type_recast(self):
        """Return a new instance, this is needed because types
        such as textures can be changed at runtime.

                :return: a new instance of this object with the type initialized again.
        """
        ...

    def values(self) -> list:
        """Returns the values of this objects custom properties (matches pythons
        dictionary function of the same name).

                :return: custom property values.
                :rtype: list
        """
        ...

class NODE_OT_add_search(NodeAddOperator, bpy_types.Operator):
    """Add a node to the active tree"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_property: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    node_item: typing.Any
    order: typing.Any
    settings: typing.Any
    type: typing.Any
    use_transform: typing.Any

    def as_keywords(self, ignore=()):
        """Return a copy of the properties as a dictionary

        :param ignore:
        """
        ...

    def as_pointer(self) -> int:
        """Returns the memory address which holds a pointer to blenders internal data

        :return: int (memory address).
        :rtype: int
        """
        ...

    def create_node(self, context, node_type=None):
        """

        :param context:
        :param node_type:
        """
        ...

    def driver_add(self) -> bpy.types.FCurve:
        """Adds driver(s) to the given property

        :return: The driver(s) added.
        :rtype: bpy.types.FCurve
        """
        ...

    def driver_remove(self) -> bool:
        """Remove driver(s) from the given property

        :return: Success of driver removal.
        :rtype: bool
        """
        ...

    def execute(self, context):
        """

        :param context:
        """
        ...

    def find_node_item(self, context):
        """

        :param context:
        """
        ...

    def get(self):
        """Returns the value of the custom property assigned to key or default
        when not found (matches pythons dictionary function of the same name).

        """
        ...

    def invoke(self, context, event):
        """

        :param context:
        :param event:
        """
        ...

    def is_property_hidden(self) -> bool:
        """Check if a property is hidden.

        :return: True when the property is hidden.
        :rtype: bool
        """
        ...

    def is_property_readonly(self) -> bool:
        """Check if a property is readonly.

        :return: True when the property is readonly (not writable).
        :rtype: bool
        """
        ...

    def is_property_set(self) -> bool:
        """Check if a property is set, use for testing operator properties.

        :return: True when the property has been set.
        :rtype: bool
        """
        ...

    def items(self):
        """Returns the items of this objects custom properties (matches pythons
        dictionary function of the same name).

                :return: custom property key, value pairs.
        """
        ...

    def keyframe_delete(self) -> bool:
        """Remove a keyframe from this properties fcurve.

        :return: Success of keyframe deleation.
        :rtype: bool
        """
        ...

    def keyframe_insert(self) -> bool:
        """Insert a keyframe on the property given, adding fcurves and animation data when necessary.

        :return: Success of keyframe insertion.
        :rtype: bool
        """
        ...

    def keys(self) -> list[str]:
        """Returns the keys of this objects custom properties (matches pythons
        dictionary function of the same name).

                :return: custom property keys.
                :rtype: list[str]
        """
        ...

    def node_enum_items(self, context):
        """

        :param context:
        """
        ...

    def path_from_id(self) -> str:
        """Returns the data path from the ID to this object (string).

                :return: The path from `bpy.types.bpy_struct.id_data`
        to this struct and property (when given).
                :rtype: str
        """
        ...

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def poll(self, context):
        """

        :param context:
        """
        ...

    def property_unset(self):
        """Unset a property, will use default value afterward."""
        ...

    def store_mouse_cursor(self, context, event):
        """

        :param context:
        :param event:
        """
        ...

    def type_recast(self):
        """Return a new instance, this is needed because types
        such as textures can be changed at runtime.

                :return: a new instance of this object with the type initialized again.
        """
        ...

    def values(self) -> list:
        """Returns the values of this objects custom properties (matches pythons
        dictionary function of the same name).

                :return: custom property values.
                :rtype: list
        """
        ...
