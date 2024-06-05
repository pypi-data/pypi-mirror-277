import typing
import collections.abc
import bpy.types
import bpy_types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class ModifierButtonsPanel:
    bl_context: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class DATA_PT_modifiers(bpy_types.Panel, ModifierButtonsPanel, bpy_types._GenericUI):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def ARMATURE(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def ARRAY(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def BEVEL(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def BOOLEAN(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def BUILD(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def CAST(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def CLOTH(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def COLLISION(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def CORRECTIVE_SMOOTH(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def CURVE(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def DATA_TRANSFER(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def DECIMATE(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def DISPLACE(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def DYNAMIC_PAINT(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def EDGE_SPLIT(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def EXPLODE(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def FLUID_SIMULATION(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def HOOK(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def LAPLACIANDEFORM(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def LAPLACIANSMOOTH(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def LATTICE(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def MASK(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def MESH_CACHE(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def MESH_DEFORM(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def MESH_SEQUENCE_CACHE(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def MIRROR(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def MULTIRES(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def NORMAL_EDIT(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def OCEAN(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def PARTICLE_INSTANCE(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def PARTICLE_SYSTEM(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def REMESH(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def SCREW(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def SHRINKWRAP(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def SIMPLE_DEFORM(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def SKIN(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def SMOKE(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def SMOOTH(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def SOFT_BODY(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def SOLIDIFY(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def SUBSURF(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def SURFACE(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def SURFACE_DEFORM(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def TRIANGULATE(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def UV_PROJECT(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def UV_WARP(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def VERTEX_WEIGHT_EDIT(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def VERTEX_WEIGHT_MIX(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def VERTEX_WEIGHT_PROXIMITY(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def WARP(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def WAVE(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...

    def WIREFRAME(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
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

    def vertex_weight_mask(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """
        ...
