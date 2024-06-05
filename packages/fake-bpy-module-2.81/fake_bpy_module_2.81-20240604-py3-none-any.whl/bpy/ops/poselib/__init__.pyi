import typing
import collections.abc
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def action_sanitize(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Make action suitable for use as a Pose Library

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def apply_pose(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    pose_index: typing.Any | None = -1,
):
    """Apply specified Pose Library pose to the rig

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param pose_index: Pose, Index of the pose to apply (-2 for no change to pose, -1 for poselib active pose)
    :type pose_index: typing.Any | None
    """

    ...

def browse_interactive(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    pose_index: typing.Any | None = -1,
):
    """Interactively browse poses in 3D-View

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param pose_index: Pose, Index of the pose to apply (-2 for no change to pose, -1 for poselib active pose)
    :type pose_index: typing.Any | None
    """

    ...

def new(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add New Pose Library to active Object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def pose_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    frame: typing.Any | None = 1,
    name: str | typing.Any = "Pose",
):
    """Add the current Pose to the active Pose Library

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param frame: Frame, Frame to store pose on
    :type frame: typing.Any | None
    :param name: Pose Name, Name of newly added Pose
    :type name: str | typing.Any
    """

    ...

def pose_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    pose: str | None = "",
    direction: str | None = "UP",
):
    """Move the pose up or down in the active Pose Library

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param pose: Pose, The pose to move
    :type pose: str | None
    :param direction: Direction, Direction to move the chosen pose towards
    :type direction: str | None
    """

    ...

def pose_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    pose: str | None = "",
):
    """Remove nth pose from the active Pose Library

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param pose: Pose, The pose to remove
    :type pose: str | None
    """

    ...

def pose_rename(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str | typing.Any = "RenamedPose",
    pose: str | None = "",
):
    """Rename specified pose from the active Pose Library

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: New Pose Name, New name for pose
    :type name: str | typing.Any
    :param pose: Pose, The pose to rename
    :type pose: str | None
    """

    ...

def unlink(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove Pose Library from active Object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...
