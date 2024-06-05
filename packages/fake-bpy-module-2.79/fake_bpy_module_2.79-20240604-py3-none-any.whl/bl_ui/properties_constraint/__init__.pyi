import typing
import collections.abc
import bpy.types
import bpy_types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class ConstraintButtonsPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

    def ACTION(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def CAMERA_SOLVER(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def CHILD_OF(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def CLAMP_TO(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def COPY_LOCATION(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def COPY_ROTATION(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def COPY_SCALE(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def COPY_TRANSFORMS(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def DAMPED_TRACK(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def FLOOR(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def FOLLOW_PATH(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def FOLLOW_TRACK(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def IK(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def IK_COPY_POSE(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def IK_DISTANCE(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def LIMIT_DISTANCE(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def LIMIT_LOCATION(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def LIMIT_ROTATION(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def LIMIT_SCALE(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def LOCKED_TRACK(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def MAINTAIN_VOLUME(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def OBJECT_SOLVER(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def PIVOT(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def RIGID_BODY_JOINT(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def SCRIPT(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def SHRINKWRAP(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def SPLINE_IK(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def STRETCH_TO(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def TRACK_TO(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def TRANSFORM(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def TRANSFORM_CACHE(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def draw_constraint(self, context, con):
        """

        :param context:
        :param con:
        """
        ...

    def ik_template(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def space_template(self, layout, con, target=True, owner=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
        """
        ...

class BONE_PT_constraints(
    bpy_types.Panel, ConstraintButtonsPanel, bpy_types._GenericUI
):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def ACTION(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def CAMERA_SOLVER(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def CHILD_OF(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def CLAMP_TO(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def COPY_LOCATION(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def COPY_ROTATION(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def COPY_SCALE(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def COPY_TRANSFORMS(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def DAMPED_TRACK(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def FLOOR(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def FOLLOW_PATH(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def FOLLOW_TRACK(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def IK(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def IK_COPY_POSE(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def IK_DISTANCE(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def LIMIT_DISTANCE(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def LIMIT_LOCATION(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def LIMIT_ROTATION(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def LIMIT_SCALE(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def LOCKED_TRACK(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def MAINTAIN_VOLUME(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def OBJECT_SOLVER(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def PIVOT(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def RIGID_BODY_JOINT(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def SCRIPT(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def SHRINKWRAP(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def SPLINE_IK(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def STRETCH_TO(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def TRACK_TO(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def TRANSFORM(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def TRANSFORM_CACHE(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def append(self, draw_func):
        """Append a draw function to this menu,
        takes the same arguments as the menus draw function

                :param draw_func:
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

    def draw_constraint(self, context, con):
        """

        :param context:
        :param con:
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

    def ik_template(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def is_extended(self): ...
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

    def prepend(self, draw_func):
        """Prepend a draw function to this menu, takes the same arguments as
        the menus draw function

                :param draw_func:
        """
        ...

    def property_unset(self):
        """Unset a property, will use default value afterward."""
        ...

    def remove(self, draw_func):
        """Remove a draw function that has been added to this menu

        :param draw_func:
        """
        ...

    def space_template(self, layout, con, target=True, owner=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_constraints(
    bpy_types.Panel, ConstraintButtonsPanel, bpy_types._GenericUI
):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def ACTION(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def CAMERA_SOLVER(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def CHILD_OF(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def CLAMP_TO(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def COPY_LOCATION(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def COPY_ROTATION(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def COPY_SCALE(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def COPY_TRANSFORMS(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def DAMPED_TRACK(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def FLOOR(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def FOLLOW_PATH(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def FOLLOW_TRACK(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def IK(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def IK_COPY_POSE(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def IK_DISTANCE(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def LIMIT_DISTANCE(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def LIMIT_LOCATION(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def LIMIT_ROTATION(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def LIMIT_SCALE(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def LOCKED_TRACK(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def MAINTAIN_VOLUME(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def OBJECT_SOLVER(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def PIVOT(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def RIGID_BODY_JOINT(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def SCRIPT(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def SHRINKWRAP(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def SPLINE_IK(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def STRETCH_TO(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def TRACK_TO(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def TRANSFORM(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def TRANSFORM_CACHE(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """
        ...

    def append(self, draw_func):
        """Append a draw function to this menu,
        takes the same arguments as the menus draw function

                :param draw_func:
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

    def draw_constraint(self, context, con):
        """

        :param context:
        :param con:
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

    def ik_template(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def is_extended(self): ...
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

    def prepend(self, draw_func):
        """Prepend a draw function to this menu, takes the same arguments as
        the menus draw function

                :param draw_func:
        """
        ...

    def property_unset(self):
        """Unset a property, will use default value afterward."""
        ...

    def remove(self, draw_func):
        """Remove a draw function that has been added to this menu

        :param draw_func:
        """
        ...

    def space_template(self, layout, con, target=True, owner=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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
