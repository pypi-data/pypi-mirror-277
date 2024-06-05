import typing
import collections.abc
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def fbx(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    directory: str | typing.Any = "",
    filter_glob: str | typing.Any = "*.fbx",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    ui_tab: str | None = "MAIN",
    use_manual_orientation: bool | typing.Any | None = False,
    global_scale: typing.Any | None = 1.0,
    bake_space_transform: bool | typing.Any | None = False,
    use_custom_normals: bool | typing.Any | None = True,
    use_image_search: bool | typing.Any | None = True,
    use_alpha_decals: bool | typing.Any | None = False,
    decal_offset: typing.Any | None = 0.0,
    use_anim: bool | typing.Any | None = True,
    anim_offset: typing.Any | None = 1.0,
    use_subsurf: bool | typing.Any | None = False,
    use_custom_props: bool | typing.Any | None = True,
    use_custom_props_enum_as_string: bool | typing.Any | None = True,
    ignore_leaf_bones: bool | typing.Any | None = False,
    force_connect_children: bool | typing.Any | None = False,
    automatic_bone_orientation: bool | typing.Any | None = False,
    primary_bone_axis: str | None = "Y",
    secondary_bone_axis: str | None = "X",
    use_prepost_rot: bool | typing.Any | None = True,
    axis_forward: str | None = "-Z",
    axis_up: str | None = "Y",
):
    """Load a FBX file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Filepath used for importing the file
        :type filepath: str | typing.Any
        :param directory: directory
        :type directory: str | typing.Any
        :param filter_glob: filter_glob
        :type filter_glob: str | typing.Any
        :param files: File Path
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
        :param ui_tab: ui_tab, Import options categories

    MAIN Main, Main basic settings.

    ARMATURE Armatures, Armature-related settings.
        :type ui_tab: str | None
        :param use_manual_orientation: Manual Orientation, Specify orientation and scale, instead of using embedded data in FBX file
        :type use_manual_orientation: bool | typing.Any | None
        :param global_scale: Scale
        :type global_scale: typing.Any | None
        :param bake_space_transform: !EXPERIMENTAL! Apply Transform, Bake space transform into object data, avoids getting unwanted rotations to objects when target space is not aligned with Blender's space (WARNING! experimental option, use at own risks, known broken with armatures/animations)
        :type bake_space_transform: bool | typing.Any | None
        :param use_custom_normals: Import Normals, Import custom normals, if available (otherwise Blender will recompute them)
        :type use_custom_normals: bool | typing.Any | None
        :param use_image_search: Image Search, Search subdirs for any associated images (WARNING: may be slow)
        :type use_image_search: bool | typing.Any | None
        :param use_alpha_decals: Alpha Decals, Treat materials with alpha as decals (no shadow casting)
        :type use_alpha_decals: bool | typing.Any | None
        :param decal_offset: Decal Offset, Displace geometry of alpha meshes
        :type decal_offset: typing.Any | None
        :param use_anim: Import Animation, Import FBX animation
        :type use_anim: bool | typing.Any | None
        :param anim_offset: Animation Offset, Offset to apply to animation during import, in frames
        :type anim_offset: typing.Any | None
        :param use_subsurf: Import Subdivision Surface, Import FBX subdivision information as subdivision surface modifiers
        :type use_subsurf: bool | typing.Any | None
        :param use_custom_props: Import User Properties, Import user properties as custom properties
        :type use_custom_props: bool | typing.Any | None
        :param use_custom_props_enum_as_string: Import Enums As Strings, Store enumeration values as strings
        :type use_custom_props_enum_as_string: bool | typing.Any | None
        :param ignore_leaf_bones: Ignore Leaf Bones, Ignore the last bone at the end of each chain (used to mark the length of the previous bone)
        :type ignore_leaf_bones: bool | typing.Any | None
        :param force_connect_children: Force Connect Children, Force connection of children bones to their parent, even if their computed head/tail positions do not match (can be useful with pure-joints-type armatures)
        :type force_connect_children: bool | typing.Any | None
        :param automatic_bone_orientation: Automatic Bone Orientation, Try to align the major bone axis with the bone children
        :type automatic_bone_orientation: bool | typing.Any | None
        :param primary_bone_axis: Primary Bone Axis
        :type primary_bone_axis: str | None
        :param secondary_bone_axis: Secondary Bone Axis
        :type secondary_bone_axis: str | None
        :param use_prepost_rot: Use Pre/Post Rotation, Use pre/post rotation from FBX transform (you may have to disable that in some cases)
        :type use_prepost_rot: bool | typing.Any | None
        :param axis_forward: Forward
        :type axis_forward: str | None
        :param axis_up: Up
        :type axis_up: str | None
    """

    ...

def gltf(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    filter_glob: str | typing.Any = "*.glb;*.gltf",
    loglevel: typing.Any | None = 0,
    import_pack_images: bool | typing.Any | None = True,
    import_shading: str | None = "NORMALS",
):
    """Load a glTF 2.0 file

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: File Path, Filepath used for importing the file
    :type filepath: str | typing.Any
    :param filter_glob: filter_glob
    :type filter_glob: str | typing.Any
    :param loglevel: Log Level, Log Level
    :type loglevel: typing.Any | None
    :param import_pack_images: Pack images, Pack all images into .blend file
    :type import_pack_images: bool | typing.Any | None
    :param import_shading: Shading, How normals are computed during import
    :type import_shading: str | None
    """

    ...

def obj(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    filter_glob: str | typing.Any = "*.obj;*.mtl",
    use_edges: bool | typing.Any | None = True,
    use_smooth_groups: bool | typing.Any | None = True,
    use_split_objects: bool | typing.Any | None = True,
    use_split_groups: bool | typing.Any | None = False,
    use_groups_as_vgroups: bool | typing.Any | None = False,
    use_image_search: bool | typing.Any | None = True,
    split_mode: str | None = "ON",
    global_clight_size: typing.Any | None = 0.0,
    axis_forward: str | None = "-Z",
    axis_up: str | None = "Y",
):
    """Load a Wavefront OBJ File

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Filepath used for importing the file
        :type filepath: str | typing.Any
        :param filter_glob: filter_glob
        :type filter_glob: str | typing.Any
        :param use_edges: Lines, Import lines and faces with 2 verts as edge
        :type use_edges: bool | typing.Any | None
        :param use_smooth_groups: Smooth Groups, Surround smooth groups by sharp edges
        :type use_smooth_groups: bool | typing.Any | None
        :param use_split_objects: Object, Import OBJ Objects into Blender Objects
        :type use_split_objects: bool | typing.Any | None
        :param use_split_groups: Group, Import OBJ Groups into Blender Objects
        :type use_split_groups: bool | typing.Any | None
        :param use_groups_as_vgroups: Poly Groups, Import OBJ groups as vertex groups
        :type use_groups_as_vgroups: bool | typing.Any | None
        :param use_image_search: Image Search, Search subdirs for any associated images (Warning, may be slow)
        :type use_image_search: bool | typing.Any | None
        :param split_mode: Split

    ON Split, Split geometry, omits unused verts.

    OFF Keep Vert Order, Keep vertex order from file.
        :type split_mode: str | None
        :param global_clight_size: Clamp Size, Clamp bounds under this value (zero to disable)
        :type global_clight_size: typing.Any | None
        :param axis_forward: Forward
        :type axis_forward: str | None
        :param axis_up: Up
        :type axis_up: str | None
    """

    ...

def x3d(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    filter_glob: str | typing.Any = "*.x3d;*.wrl",
    axis_forward: str | None = "Z",
    axis_up: str | None = "Y",
):
    """Import an X3D or VRML2 file

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: File Path, Filepath used for importing the file
    :type filepath: str | typing.Any
    :param filter_glob: filter_glob
    :type filter_glob: str | typing.Any
    :param axis_forward: Forward
    :type axis_forward: str | None
    :param axis_up: Up
    :type axis_up: str | None
    """

    ...
