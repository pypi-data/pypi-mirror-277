import typing
import collections.abc
import bpy.types
import bpy_types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class ClearAllRestrictRender(bpy_types.Operator):
    """Reveal all render objects by setting the hide render flag"""

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

class DupliOffsetFromCursor(bpy_types.Operator):
    """Set offset used for DupliGroup based on cursor position"""

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

class IsolateTypeRender(bpy_types.Operator):
    """Hide unselected render objects of same type as active by setting the hide render flag"""

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

class JoinUVs(bpy_types.Operator):
    """Transfer UV Maps from active to selected objects (needs matching geometry)"""

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

class LodByName(bpy_types.Operator):
    """Add levels of detail to this object based on object names"""

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

class LodClearAll(bpy_types.Operator):
    """Remove all levels of detail from this object"""

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

class LodGenerate(bpy_types.Operator):
    """Generate levels of detail using the decimate modifier"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    count: typing.Any
    id_data: typing.Any
    order: typing.Any
    package: typing.Any
    target: typing.Any

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

class MakeDupliFace(bpy_types.Operator):
    """Convert objects into dupli-face instanced"""

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

class SelectCamera(bpy_types.Operator):
    """Select the active camera"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    extend: typing.Any
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

class SelectHierarchy(bpy_types.Operator):
    """Select object relative to the active object's position in the hierarchy"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    direction: typing.Any
    extend: typing.Any
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

class SelectPattern(bpy_types.Operator):
    """Select objects matching a naming pattern"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    case_sensitive: typing.Any
    extend: typing.Any
    id_data: typing.Any
    order: typing.Any
    pattern: typing.Any

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

    def draw(self, context):
        """

        :param context:
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

class ShapeTransfer(bpy_types.Operator):
    """Copy another selected objects active shape to this one by applying the relative offsets"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    mode: typing.Any
    order: typing.Any
    use_clamp: typing.Any

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

class SubdivisionSet(bpy_types.Operator):
    """Sets a Subdivision Surface Level (1-5)"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    level: typing.Any
    order: typing.Any
    relative: typing.Any

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

class TransformsToDeltas(bpy_types.Operator):
    """Convert normal object transforms to delta transforms, any existing delta transforms will be included as well"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    mode: typing.Any
    order: typing.Any
    reset_values: typing.Any

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

    def transfer_location(self, obj):
        """

        :param obj:
        """
        ...

    def transfer_rotation(self, obj):
        """

        :param obj:
        """
        ...

    def transfer_scale(self, obj):
        """

        :param obj:
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

class TransformsToDeltasAnim(bpy_types.Operator):
    """Convert object animation for normal transforms to delta transforms"""

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
