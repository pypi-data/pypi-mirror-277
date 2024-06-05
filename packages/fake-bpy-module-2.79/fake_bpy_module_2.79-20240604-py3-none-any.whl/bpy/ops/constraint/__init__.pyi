import typing
import collections.abc
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def childof_clear_inverse(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    constraint: str | typing.Any = "",
    owner: str | None = "OBJECT",
):
    """Clear inverse correction for ChildOf constraint

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str | typing.Any
        :param owner: Owner, The owner of this constraint

    OBJECT Object, Edit a constraint on the active object.

    BONE Bone, Edit a constraint on the active bone.
        :type owner: str | None
    """

    ...

def childof_set_inverse(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    constraint: str | typing.Any = "",
    owner: str | None = "OBJECT",
):
    """Set inverse correction for ChildOf constraint

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str | typing.Any
        :param owner: Owner, The owner of this constraint

    OBJECT Object, Edit a constraint on the active object.

    BONE Bone, Edit a constraint on the active bone.
        :type owner: str | None
    """

    ...

def delete(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove constraint from constraint stack

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def followpath_path_animate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    constraint: str | typing.Any = "",
    owner: str | None = "OBJECT",
    frame_start: typing.Any | None = 1,
    length: typing.Any | None = 100,
):
    """Add default animation for path used by constraint if it isn't animated already

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str | typing.Any
        :param owner: Owner, The owner of this constraint

    OBJECT Object, Edit a constraint on the active object.

    BONE Bone, Edit a constraint on the active bone.
        :type owner: str | None
        :param frame_start: Start Frame, First frame of path animation
        :type frame_start: typing.Any | None
        :param length: Length, Number of frames that path animation should take
        :type length: typing.Any | None
    """

    ...

def limitdistance_reset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    constraint: str | typing.Any = "",
    owner: str | None = "OBJECT",
):
    """Reset limiting distance for Limit Distance Constraint

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str | typing.Any
        :param owner: Owner, The owner of this constraint

    OBJECT Object, Edit a constraint on the active object.

    BONE Bone, Edit a constraint on the active bone.
        :type owner: str | None
    """

    ...

def move_down(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    constraint: str | typing.Any = "",
    owner: str | None = "OBJECT",
):
    """Move constraint down in constraint stack

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str | typing.Any
        :param owner: Owner, The owner of this constraint

    OBJECT Object, Edit a constraint on the active object.

    BONE Bone, Edit a constraint on the active bone.
        :type owner: str | None
    """

    ...

def move_up(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    constraint: str | typing.Any = "",
    owner: str | None = "OBJECT",
):
    """Move constraint up in constraint stack

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str | typing.Any
        :param owner: Owner, The owner of this constraint

    OBJECT Object, Edit a constraint on the active object.

    BONE Bone, Edit a constraint on the active bone.
        :type owner: str | None
    """

    ...

def objectsolver_clear_inverse(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    constraint: str | typing.Any = "",
    owner: str | None = "OBJECT",
):
    """Clear inverse correction for ObjectSolver constraint

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str | typing.Any
        :param owner: Owner, The owner of this constraint

    OBJECT Object, Edit a constraint on the active object.

    BONE Bone, Edit a constraint on the active bone.
        :type owner: str | None
    """

    ...

def objectsolver_set_inverse(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    constraint: str | typing.Any = "",
    owner: str | None = "OBJECT",
):
    """Set inverse correction for ObjectSolver constraint

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str | typing.Any
        :param owner: Owner, The owner of this constraint

    OBJECT Object, Edit a constraint on the active object.

    BONE Bone, Edit a constraint on the active bone.
        :type owner: str | None
    """

    ...

def stretchto_reset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    constraint: str | typing.Any = "",
    owner: str | None = "OBJECT",
):
    """Reset original length of bone for Stretch To Constraint

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str | typing.Any
        :param owner: Owner, The owner of this constraint

    OBJECT Object, Edit a constraint on the active object.

    BONE Bone, Edit a constraint on the active bone.
        :type owner: str | None
    """

    ...
