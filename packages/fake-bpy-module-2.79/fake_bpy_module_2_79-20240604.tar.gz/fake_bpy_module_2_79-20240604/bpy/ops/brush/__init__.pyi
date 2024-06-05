import typing
import collections.abc
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def active_index_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | typing.Any = "",
    index: typing.Any | None = 0,
):
    """Set active sculpt/paint brush from it's number

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode, Paint mode to set brush for
    :type mode: str | typing.Any
    :param index: Number, Brush number
    :type index: typing.Any | None
    """

    ...

def add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add brush by mode type

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def curve_preset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    shape: str | None = "SMOOTH",
):
    """Set brush shape

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param shape: Mode
    :type shape: str | None
    """

    ...

def reset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Return brush to defaults based on current tool

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def scale_size(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    scalar: typing.Any | None = 1.0,
):
    """Change brush size by a scalar

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param scalar: Scalar, Factor to scale brush size by
    :type scalar: typing.Any | None
    """

    ...

def stencil_control(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "TRANSLATION",
    texmode: str | None = "PRIMARY",
):
    """Control the stencil brush

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Tool
    :type mode: str | None
    :param texmode: Tool
    :type texmode: str | None
    """

    ...

def stencil_fit_image_aspect(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_repeat: bool | typing.Any | None = True,
    use_scale: bool | typing.Any | None = True,
    mask: bool | typing.Any | None = False,
):
    """When using an image texture, adjust the stencil size to fit the image aspect ratio

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_repeat: Use Repeat, Use repeat mapping values
    :type use_repeat: bool | typing.Any | None
    :param use_scale: Use Scale, Use texture scale values
    :type use_scale: bool | typing.Any | None
    :param mask: Modify Mask Stencil, Modify either the primary or mask stencil
    :type mask: bool | typing.Any | None
    """

    ...

def stencil_reset_transform(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mask: bool | typing.Any | None = False,
):
    """Reset the stencil transformation to the default

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mask: Modify Mask Stencil, Modify either the primary or mask stencil
    :type mask: bool | typing.Any | None
    """

    ...

def uv_sculpt_tool_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    tool: str | None = "PINCH",
):
    """Set the UV sculpt tool

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param tool: Tool

    PINCH Pinch, Pinch UVs.

    RELAX Relax, Relax UVs.

    GRAB Grab, Grab UVs.
        :type tool: str | None
    """

    ...
