import typing
import collections.abc
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def actuator_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "",
    name: str | typing.Any = "",
    object: str | typing.Any = "",
):
    """Add an actuator to the active object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type, Type of actuator to add
    :type type: str | None
    :param name: Name, Name of the Actuator to add
    :type name: str | typing.Any
    :param object: Object, Name of the Object to add the Actuator to
    :type object: str | typing.Any
    """

    ...

def actuator_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    actuator: str | typing.Any = "",
    object: str | typing.Any = "",
    direction: str | None = "UP",
):
    """Move Actuator

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param actuator: Actuator, Name of the actuator to edit
    :type actuator: str | typing.Any
    :param object: Object, Name of the object the actuator belongs to
    :type object: str | typing.Any
    :param direction: Direction, Move Up or Down
    :type direction: str | None
    """

    ...

def actuator_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    actuator: str | typing.Any = "",
    object: str | typing.Any = "",
):
    """Remove an actuator from the active object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param actuator: Actuator, Name of the actuator to edit
    :type actuator: str | typing.Any
    :param object: Object, Name of the object the actuator belongs to
    :type object: str | typing.Any
    """

    ...

def controller_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "LOGIC_AND",
    name: str | typing.Any = "",
    object: str | typing.Any = "",
):
    """Add a controller to the active object

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type, Type of controller to add

    LOGIC_AND And, Logic And.

    LOGIC_OR Or, Logic Or.

    LOGIC_NAND Nand, Logic Nand.

    LOGIC_NOR Nor, Logic Nor.

    LOGIC_XOR Xor, Logic Xor.

    LOGIC_XNOR Xnor, Logic Xnor.

    EXPRESSION Expression.

    PYTHON Python.
        :type type: str | None
        :param name: Name, Name of the Controller to add
        :type name: str | typing.Any
        :param object: Object, Name of the Object to add the Controller to
        :type object: str | typing.Any
    """

    ...

def controller_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    controller: str | typing.Any = "",
    object: str | typing.Any = "",
    direction: str | None = "UP",
):
    """Move Controller

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param controller: Controller, Name of the controller to edit
    :type controller: str | typing.Any
    :param object: Object, Name of the object the controller belongs to
    :type object: str | typing.Any
    :param direction: Direction, Move Up or Down
    :type direction: str | None
    """

    ...

def controller_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    controller: str | typing.Any = "",
    object: str | typing.Any = "",
):
    """Remove a controller from the active object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param controller: Controller, Name of the controller to edit
    :type controller: str | typing.Any
    :param object: Object, Name of the object the controller belongs to
    :type object: str | typing.Any
    """

    ...

def links_cut(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    cursor: typing.Any | None = 9,
):
    """Remove logic brick connections

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param path: path
    :type path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None
    :param cursor: Cursor
    :type cursor: typing.Any | None
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

def sensor_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "",
    name: str | typing.Any = "",
    object: str | typing.Any = "",
):
    """Add a sensor to the active object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type, Type of sensor to add
    :type type: str | None
    :param name: Name, Name of the Sensor to add
    :type name: str | typing.Any
    :param object: Object, Name of the Object to add the Sensor to
    :type object: str | typing.Any
    """

    ...

def sensor_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    sensor: str | typing.Any = "",
    object: str | typing.Any = "",
    direction: str | None = "UP",
):
    """Move Sensor

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param sensor: Sensor, Name of the sensor to edit
    :type sensor: str | typing.Any
    :param object: Object, Name of the object the sensor belongs to
    :type object: str | typing.Any
    :param direction: Direction, Move Up or Down
    :type direction: str | None
    """

    ...

def sensor_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    sensor: str | typing.Any = "",
    object: str | typing.Any = "",
):
    """Remove a sensor from the active object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param sensor: Sensor, Name of the sensor to edit
    :type sensor: str | typing.Any
    :param object: Object, Name of the object the sensor belongs to
    :type object: str | typing.Any
    """

    ...

def view_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Resize view so you can see all logic bricks

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...
