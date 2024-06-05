import typing
import collections.abc
import bl_operators.wm
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def alembic_export(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    hide_props_region: bool | typing.Any | None = True,
    check_existing: bool | typing.Any | None = True,
    filter_blender: bool | typing.Any | None = False,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = True,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "FILE_SORT_ALPHA",
    start: typing.Any | None = -2147483648,
    end: typing.Any | None = -2147483648,
    xsamples: typing.Any | None = 1,
    gsamples: typing.Any | None = 1,
    sh_open: typing.Any | None = 0.0,
    sh_close: typing.Any | None = 1.0,
    selected: bool | typing.Any | None = False,
    renderable_only: bool | typing.Any | None = True,
    visible_layers_only: bool | typing.Any | None = False,
    flatten: bool | typing.Any | None = False,
    uvs: bool | typing.Any | None = True,
    packuv: bool | typing.Any | None = True,
    normals: bool | typing.Any | None = True,
    vcolors: bool | typing.Any | None = False,
    face_sets: bool | typing.Any | None = False,
    subdiv_schema: bool | typing.Any | None = False,
    apply_subdiv: bool | typing.Any | None = False,
    curves_as_mesh: bool | typing.Any | None = False,
    compression_type: str | None = "OGAWA",
    global_scale: typing.Any | None = 1.0,
    triangulate: bool | typing.Any | None = False,
    quad_method: str | None = "SHORTEST_DIAGONAL",
    ngon_method: str | None = "BEAUTY",
    export_hair: bool | typing.Any | None = True,
    export_particles: bool | typing.Any | None = True,
    as_background_job: bool | typing.Any | None = False,
    init_scene_frame_range: bool | typing.Any | None = False,
):
    """Export current scene in an Alembic archive

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | typing.Any | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param display_type: Display Type

    DEFAULT Default, Automatically determine display type for files.

    LIST_VERTICAL Short List, Display files as short list.

    LIST_HORIZONTAL Long List, Display files as a detailed list.

    THUMBNAIL Thumbnails, Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode

    FILE_SORT_ALPHA Name, Sort the file list alphabetically.

    FILE_SORT_EXTENSION Extension, Sort the file list by extension/type.

    FILE_SORT_TIME Modified Date, Sort files by modification time.

    FILE_SORT_SIZE Size, Sort files by size.
        :type sort_method: str | None
        :param start: Start Frame, Start frame of the export, use the default value to take the start frame of the current scene
        :type start: typing.Any | None
        :param end: End Frame, End frame of the export, use the default value to take the end frame of the current scene
        :type end: typing.Any | None
        :param xsamples: Transform Samples, Number of times per frame transformations are sampled
        :type xsamples: typing.Any | None
        :param gsamples: Geometry Samples, Number of times per frame object data are sampled
        :type gsamples: typing.Any | None
        :param sh_open: Shutter Open, Time at which the shutter is open
        :type sh_open: typing.Any | None
        :param sh_close: Shutter Close, Time at which the shutter is closed
        :type sh_close: typing.Any | None
        :param selected: Selected Objects Only, Export only selected objects
        :type selected: bool | typing.Any | None
        :param renderable_only: Renderable Objects Only, Export only objects marked renderable in the outliner
        :type renderable_only: bool | typing.Any | None
        :param visible_layers_only: Visible Layers Only, Export only objects in visible layers
        :type visible_layers_only: bool | typing.Any | None
        :param flatten: Flatten Hierarchy, Do not preserve objects' parent/children relationship
        :type flatten: bool | typing.Any | None
        :param uvs: UVs, Export UVs
        :type uvs: bool | typing.Any | None
        :param packuv: Pack UV Islands, Export UVs with packed island
        :type packuv: bool | typing.Any | None
        :param normals: Normals, Export normals
        :type normals: bool | typing.Any | None
        :param vcolors: Vertex Colors, Export vertex colors
        :type vcolors: bool | typing.Any | None
        :param face_sets: Face Sets, Export per face shading group assignments
        :type face_sets: bool | typing.Any | None
        :param subdiv_schema: Use Subdivision Schema, Export meshes using Alembic's subdivision schema
        :type subdiv_schema: bool | typing.Any | None
        :param apply_subdiv: Apply Subsurf, Export subdivision surfaces as meshes
        :type apply_subdiv: bool | typing.Any | None
        :param curves_as_mesh: Curves as Mesh, Export curves and NURBS surfaces as meshes
        :type curves_as_mesh: bool | typing.Any | None
        :param compression_type: Compression
        :type compression_type: str | None
        :param global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
        :type global_scale: typing.Any | None
        :param triangulate: Triangulate, Export Polygons (Quads & NGons) as Triangles
        :type triangulate: bool | typing.Any | None
        :param quad_method: Quad Method, Method for splitting the quads into triangles

    BEAUTY Beauty , Split the quads in nice triangles, slower method.

    FIXED Fixed, Split the quads on the first and third vertices.

    FIXED_ALTERNATE Fixed Alternate, Split the quads on the 2nd and 4th vertices.

    SHORTEST_DIAGONAL Shortest Diagonal, Split the quads based on the distance between the vertices.
        :type quad_method: str | None
        :param ngon_method: Polygon Method, Method for splitting the polygons into triangles

    BEAUTY Beauty , Split the quads in nice triangles, slower method.

    FIXED Fixed, Split the quads on the first and third vertices.

    FIXED_ALTERNATE Fixed Alternate, Split the quads on the 2nd and 4th vertices.

    SHORTEST_DIAGONAL Shortest Diagonal, Split the quads based on the distance between the vertices.
        :type ngon_method: str | None
        :param export_hair: Export Hair, Exports hair particle systems as animated curves
        :type export_hair: bool | typing.Any | None
        :param export_particles: Export Particles, Exports non-hair particle systems
        :type export_particles: bool | typing.Any | None
        :param as_background_job: Run as Background Job, Enable this to run the import in the background, disable to block Blender while importing. This option is deprecated; EXECUTE this operator to run in the foreground, and INVOKE it to run as a background job
        :type as_background_job: bool | typing.Any | None
        :type init_scene_frame_range: bool | typing.Any | None
    """

    ...

def alembic_import(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    hide_props_region: bool | typing.Any | None = True,
    check_existing: bool | typing.Any | None = True,
    filter_blender: bool | typing.Any | None = False,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = True,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    relative_path: bool | typing.Any | None = True,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "FILE_SORT_ALPHA",
    scale: typing.Any | None = 1.0,
    set_frame_range: bool | typing.Any | None = True,
    validate_meshes: bool | typing.Any | None = False,
    is_sequence: bool | typing.Any | None = False,
    as_background_job: bool | typing.Any | None = False,
):
    """Load an Alembic archive

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | typing.Any | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param relative_path: Relative Path, Select the file relative to the blend file
        :type relative_path: bool | typing.Any | None
        :param display_type: Display Type

    DEFAULT Default, Automatically determine display type for files.

    LIST_VERTICAL Short List, Display files as short list.

    LIST_HORIZONTAL Long List, Display files as a detailed list.

    THUMBNAIL Thumbnails, Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode

    FILE_SORT_ALPHA Name, Sort the file list alphabetically.

    FILE_SORT_EXTENSION Extension, Sort the file list by extension/type.

    FILE_SORT_TIME Modified Date, Sort files by modification time.

    FILE_SORT_SIZE Size, Sort files by size.
        :type sort_method: str | None
        :param scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
        :type scale: typing.Any | None
        :param set_frame_range: Set Frame Range, If checked, update scene's start and end frame to match those of the Alembic archive
        :type set_frame_range: bool | typing.Any | None
        :param validate_meshes: Validate Meshes, Check imported mesh objects for invalid data (slow)
        :type validate_meshes: bool | typing.Any | None
        :param is_sequence: Is Sequence, Set to true if the cache is split into separate files
        :type is_sequence: bool | typing.Any | None
        :param as_background_job: Run as Background Job, Enable this to run the export in the background, disable to block Blender while exporting. This option is deprecated; EXECUTE this operator to run in the foreground, and INVOKE it to run as a background job
        :type as_background_job: bool | typing.Any | None
    """

    ...

def append(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    directory: str | typing.Any = "",
    filename: str | typing.Any = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    filter_blender: bool | typing.Any | None = True,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = True,
    filemode: typing.Any | None = 1,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "FILE_SORT_ALPHA",
    link: bool | typing.Any | None = False,
    autoselect: bool | typing.Any | None = True,
    active_collection: bool | typing.Any | None = True,
    instance_collections: bool | typing.Any | None = False,
    set_fake: bool | typing.Any | None = False,
    use_recursive: bool | typing.Any | None = True,
):
    """Append from a Library .blend file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param directory: Directory, Directory of the file
        :type directory: str | typing.Any
        :param filename: File Name, Name of the file
        :type filename: str | typing.Any
        :param files: Files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param display_type: Display Type

    DEFAULT Default, Automatically determine display type for files.

    LIST_VERTICAL Short List, Display files as short list.

    LIST_HORIZONTAL Long List, Display files as a detailed list.

    THUMBNAIL Thumbnails, Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode

    FILE_SORT_ALPHA Name, Sort the file list alphabetically.

    FILE_SORT_EXTENSION Extension, Sort the file list by extension/type.

    FILE_SORT_TIME Modified Date, Sort files by modification time.

    FILE_SORT_SIZE Size, Sort files by size.
        :type sort_method: str | None
        :param link: Link, Link the objects or data-blocks rather than appending
        :type link: bool | typing.Any | None
        :param autoselect: Select, Select new objects
        :type autoselect: bool | typing.Any | None
        :param active_collection: Active Collection, Put new objects on the active collection
        :type active_collection: bool | typing.Any | None
        :param instance_collections: Instance Collections, Create instances for collections, rather than adding them directly to the scene
        :type instance_collections: bool | typing.Any | None
        :param set_fake: Fake User, Set Fake User for appended items (except Objects and Groups)
        :type set_fake: bool | typing.Any | None
        :param use_recursive: Localize All, Localize all appended data, including those indirectly linked from other libraries
        :type use_recursive: bool | typing.Any | None
    """

    ...

def batch_rename(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_type: str | None = "OBJECT",
    data_source: str | None = "SELECT",
    actions: bpy.types.bpy_prop_collection[bl_operators.wm.BatchRenameAction]
    | None = None,
):
    """Undocumented contribute <https://developer.blender.org/T51061>

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_type: Type, Type of data to rename
    :type data_type: str | None
    :param data_source: Source
    :type data_source: str | None
    :param actions: actions
    :type actions: bpy.types.bpy_prop_collection[bl_operators.wm.BatchRenameAction] | None
    """

    ...

def blend_strings_utf8_validate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Check and fix all strings in current .blend file to be valid UTF-8 Unicode (needed for some old, 2.4x area files)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def call_menu(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str | typing.Any = "",
):
    """Call (draw) a pre-defined menu

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the menu
    :type name: str | typing.Any
    """

    ...

def call_menu_pie(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str | typing.Any = "",
):
    """Call (draw) a pre-defined pie menu

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the pie menu
    :type name: str | typing.Any
    """

    ...

def call_panel(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str | typing.Any = "",
    keep_open: bool | typing.Any | None = True,
):
    """Call (draw) a pre-defined panel

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the menu
    :type name: str | typing.Any
    :param keep_open: Keep Open
    :type keep_open: bool | typing.Any | None
    """

    ...

def collada_export(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    hide_props_region: bool | typing.Any | None = True,
    check_existing: bool | typing.Any | None = True,
    filter_blender: bool | typing.Any | None = False,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = True,
    filter_alembic: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "FILE_SORT_ALPHA",
    prop_bc_export_ui_section: str | None = "main",
    apply_modifiers: bool | typing.Any | None = False,
    export_mesh_type: typing.Any | None = 0,
    export_mesh_type_selection: str | None = "view",
    export_global_forward_selection: str | None = "Y",
    export_global_up_selection: str | None = "Z",
    apply_global_orientation: bool | typing.Any | None = False,
    selected: bool | typing.Any | None = False,
    include_children: bool | typing.Any | None = False,
    include_armatures: bool | typing.Any | None = False,
    include_shapekeys: bool | typing.Any | None = False,
    deform_bones_only: bool | typing.Any | None = False,
    include_animations: bool | typing.Any | None = True,
    include_all_actions: bool | typing.Any | None = True,
    export_animation_type_selection: str | None = "sample",
    sampling_rate: typing.Any | None = 1,
    keep_smooth_curves: bool | typing.Any | None = False,
    keep_keyframes: bool | typing.Any | None = False,
    keep_flat_curves: bool | typing.Any | None = False,
    active_uv_only: bool | typing.Any | None = False,
    use_texture_copies: bool | typing.Any | None = True,
    triangulate: bool | typing.Any | None = True,
    use_object_instantiation: bool | typing.Any | None = True,
    use_blender_profile: bool | typing.Any | None = True,
    sort_by_name: bool | typing.Any | None = False,
    export_object_transformation_type: typing.Any | None = 0,
    export_object_transformation_type_selection: str | None = "matrix",
    export_animation_transformation_type: typing.Any | None = 0,
    export_animation_transformation_type_selection: str | None = "matrix",
    open_sim: bool | typing.Any | None = False,
    limit_precision: bool | typing.Any | None = False,
    keep_bind_info: bool | typing.Any | None = False,
):
    """Save a Collada file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | typing.Any | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param display_type: Display Type

    DEFAULT Default, Automatically determine display type for files.

    LIST_VERTICAL Short List, Display files as short list.

    LIST_HORIZONTAL Long List, Display files as a detailed list.

    THUMBNAIL Thumbnails, Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode

    FILE_SORT_ALPHA Name, Sort the file list alphabetically.

    FILE_SORT_EXTENSION Extension, Sort the file list by extension/type.

    FILE_SORT_TIME Modified Date, Sort files by modification time.

    FILE_SORT_SIZE Size, Sort files by size.
        :type sort_method: str | None
        :param prop_bc_export_ui_section: Export Section, Only for User Interface organization

    main Main, Data Export Section.

    geometry Geom, Geometry Export Section.

    armature Arm, Armature Export Section.

    animation Anim, Animation Export Section.

    collada Extra, Collada Export Section.
        :type prop_bc_export_ui_section: str | None
        :param apply_modifiers: Apply Modifiers, Apply modifiers to exported mesh (non destructive))
        :type apply_modifiers: bool | typing.Any | None
        :param export_mesh_type: Resolution, Modifier resolution for export
        :type export_mesh_type: typing.Any | None
        :param export_mesh_type_selection: Resolution, Modifier resolution for export

    view View, Apply modifier's view settings.

    render Render, Apply modifier's render settings.
        :type export_mesh_type_selection: str | None
        :param export_global_forward_selection: Global Forward Axis, Global Forward axis for export

    X X Forward, Global Forward is positive X Axis.

    Y Y Forward, Global Forward is positive Y Axis.

    Z Z Forward, Global Forward is positive Z Axis.

    -X -X Forward, Global Forward is negative X Axis.

    -Y -Y Forward, Global Forward is negative Y Axis.

    -Z -Z Forward, Global Forward is negative Z Axis.
        :type export_global_forward_selection: str | None
        :param export_global_up_selection: Global Up Axis, Global Up axis for export

    X X Up, Global UP is positive X Axis.

    Y Y Up, Global UP is positive Y Axis.

    Z Z Up, Global UP is positive Z Axis.

    -X -X Up, Global UP is negative X Axis.

    -Y -Y Up, Global UP is negative Y Axis.

    -Z -Z Up, Global UP is negative Z Axis.
        :type export_global_up_selection: str | None
        :param apply_global_orientation: Apply Global Orientation, Rotate all root objects to match the global orientation settings otherwise set the global orientation per Collada asset
        :type apply_global_orientation: bool | typing.Any | None
        :param selected: Selection Only, Export only selected elements
        :type selected: bool | typing.Any | None
        :param include_children: Include Children, Export all children of selected objects (even if not selected)
        :type include_children: bool | typing.Any | None
        :param include_armatures: Include Armatures, Export related armatures (even if not selected)
        :type include_armatures: bool | typing.Any | None
        :param include_shapekeys: Include Shape Keys, Export all Shape Keys from Mesh Objects
        :type include_shapekeys: bool | typing.Any | None
        :param deform_bones_only: Deform Bones only, Only export deforming bones with armatures
        :type deform_bones_only: bool | typing.Any | None
        :param include_animations: Include Animations, Export animations if available (exporting animations will enforce the decomposition of node transforms into  <translation> <rotation> and <scale> components)
        :type include_animations: bool | typing.Any | None
        :param include_all_actions: Include all Actions, Export also unassigned actions (this allows you to export entire animation libraries for your character(s))
        :type include_all_actions: bool | typing.Any | None
        :param export_animation_type_selection: Key Type, Type for exported animations (use sample keys or Curve keys)

    sample Samples, Export Sampled points guided by sampling rate.

    keys Curves, Export Curves (note: guided by curve keys).
        :type export_animation_type_selection: str | None
        :param sampling_rate: Sampling Rate, The distance between 2 keyframes (1 to key every frame)
        :type sampling_rate: typing.Any | None
        :param keep_smooth_curves: Keep Smooth curves, Export also the curve handles (if available) (this does only work when the inverse parent matrix is the unity matrix, otherwise you may end up with odd results)
        :type keep_smooth_curves: bool | typing.Any | None
        :param keep_keyframes: Keep Keyframes, Use existing keyframes as additional sample points (this helps when you want to keep manual tweaks)
        :type keep_keyframes: bool | typing.Any | None
        :param keep_flat_curves: All keyed curves, Export also curves which have only one key or are totally flat
        :type keep_flat_curves: bool | typing.Any | None
        :param active_uv_only: Only Selected UV Map, Export only the selected UV Map
        :type active_uv_only: bool | typing.Any | None
        :param use_texture_copies: Copy, Copy textures to same folder where the .dae file is exported
        :type use_texture_copies: bool | typing.Any | None
        :param triangulate: Triangulate, Export Polygons (Quads & NGons) as Triangles
        :type triangulate: bool | typing.Any | None
        :param use_object_instantiation: Use Object Instances, Instantiate multiple Objects from same Data
        :type use_object_instantiation: bool | typing.Any | None
        :param use_blender_profile: Use Blender Profile, Export additional Blender specific information (for material, shaders, bones, etc.)
        :type use_blender_profile: bool | typing.Any | None
        :param sort_by_name: Sort by Object name, Sort exported data by Object name
        :type sort_by_name: bool | typing.Any | None
        :param export_object_transformation_type: Transform, Object Transformation type for translation, scale and rotation
        :type export_object_transformation_type: typing.Any | None
        :param export_object_transformation_type_selection: Transform, Object Transformation type for translation, scale and rotation

    matrix Matrix, Use <matrix> representation for exported transformations.

    decomposed Decomposed, Use <rotate>, <translate> and <scale> representation for exported transformations.
        :type export_object_transformation_type_selection: str | None
        :param export_animation_transformation_type: Transform, Transformation type for translation, scale and rotation. Note: The Animation transformation type in the Anim Tab is always equal to the Object transformation type in the Geom tab
        :type export_animation_transformation_type: typing.Any | None
        :param export_animation_transformation_type_selection: Transform, Transformation type for translation, scale and rotation. Note: The Animation transformation type in the Anim Tab is always equal to the Object transformation type in the Geom tab

    matrix Matrix, Use <matrix> representation for exported transformations.

    decomposed Decomposed, Use <rotate>, <translate> and <scale> representation for exported transformations.
        :type export_animation_transformation_type_selection: str | None
        :param open_sim: Export to SL/OpenSim, Compatibility mode for SL, OpenSim and other compatible online worlds
        :type open_sim: bool | typing.Any | None
        :param limit_precision: Limit Precision, Reduce the precision of the exported data to 6 digits
        :type limit_precision: bool | typing.Any | None
        :param keep_bind_info: Keep Bind Info, Store Bindpose information in custom bone properties for later use during Collada export
        :type keep_bind_info: bool | typing.Any | None
    """

    ...

def collada_import(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    hide_props_region: bool | typing.Any | None = True,
    filter_blender: bool | typing.Any | None = False,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = True,
    filter_alembic: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "FILE_SORT_ALPHA",
    import_units: bool | typing.Any | None = False,
    fix_orientation: bool | typing.Any | None = False,
    find_chains: bool | typing.Any | None = False,
    auto_connect: bool | typing.Any | None = False,
    min_chain_length: typing.Any | None = 0,
    keep_bind_info: bool | typing.Any | None = False,
):
    """Load a Collada file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param display_type: Display Type

    DEFAULT Default, Automatically determine display type for files.

    LIST_VERTICAL Short List, Display files as short list.

    LIST_HORIZONTAL Long List, Display files as a detailed list.

    THUMBNAIL Thumbnails, Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode

    FILE_SORT_ALPHA Name, Sort the file list alphabetically.

    FILE_SORT_EXTENSION Extension, Sort the file list by extension/type.

    FILE_SORT_TIME Modified Date, Sort files by modification time.

    FILE_SORT_SIZE Size, Sort files by size.
        :type sort_method: str | None
        :param import_units: Import Units, If disabled match import to Blender's current Unit settings, otherwise use the settings from the Imported scene
        :type import_units: bool | typing.Any | None
        :param fix_orientation: Fix Leaf Bones, Fix Orientation of Leaf Bones (Collada does only support Joints)
        :type fix_orientation: bool | typing.Any | None
        :param find_chains: Find Bone Chains, Find best matching Bone Chains and ensure bones in chain are connected
        :type find_chains: bool | typing.Any | None
        :param auto_connect: Auto Connect, Set use_connect for parent bones which have exactly one child bone
        :type auto_connect: bool | typing.Any | None
        :param min_chain_length: Minimum Chain Length, When searching Bone Chains disregard chains of length below this value
        :type min_chain_length: typing.Any | None
        :param keep_bind_info: Keep Bind Info, Store Bindpose information in custom bone properties for later use during Collada export
        :type keep_bind_info: bool | typing.Any | None
    """

    ...

def context_collection_boolean_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path_iter: str | typing.Any = "",
    data_path_item: str | typing.Any = "",
    type: str | None = "TOGGLE",
):
    """Set boolean values for a collection of items

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path_iter: data_path_iter, The data path relative to the context, must point to an iterable
    :type data_path_iter: str | typing.Any
    :param data_path_item: data_path_item, The data path from each iterable to the value (int or float)
    :type data_path_item: str | typing.Any
    :param type: Type
    :type type: str | None
    """

    ...

def context_cycle_array(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    reverse: bool | typing.Any | None = False,
):
    """Set a context array value (useful for cycling the active mesh edit mode)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, RNA context string
    :type data_path: str | typing.Any
    :param reverse: Reverse, Cycle backwards
    :type reverse: bool | typing.Any | None
    """

    ...

def context_cycle_enum(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    reverse: bool | typing.Any | None = False,
    wrap: bool | typing.Any | None = False,
):
    """Toggle a context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, RNA context string
    :type data_path: str | typing.Any
    :param reverse: Reverse, Cycle backwards
    :type reverse: bool | typing.Any | None
    :param wrap: Wrap, Wrap back to the first/last values
    :type wrap: bool | typing.Any | None
    """

    ...

def context_cycle_int(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    reverse: bool | typing.Any | None = False,
    wrap: bool | typing.Any | None = False,
):
    """Set a context value (useful for cycling active material, vertex keys, groups, etc.)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, RNA context string
    :type data_path: str | typing.Any
    :param reverse: Reverse, Cycle backwards
    :type reverse: bool | typing.Any | None
    :param wrap: Wrap, Wrap back to the first/last values
    :type wrap: bool | typing.Any | None
    """

    ...

def context_menu_enum(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
):
    """Undocumented contribute <https://developer.blender.org/T51061>

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, RNA context string
    :type data_path: str | typing.Any
    """

    ...

def context_modal_mouse(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path_iter: str | typing.Any = "",
    data_path_item: str | typing.Any = "",
    header_text: str | typing.Any = "",
    input_scale: typing.Any | None = 0.01,
    invert: bool | typing.Any | None = False,
    initial_x: typing.Any | None = 0,
):
    """Adjust arbitrary values with mouse input

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path_iter: data_path_iter, The data path relative to the context, must point to an iterable
    :type data_path_iter: str | typing.Any
    :param data_path_item: data_path_item, The data path from each iterable to the value (int or float)
    :type data_path_item: str | typing.Any
    :param header_text: Header Text, Text to display in header during scale
    :type header_text: str | typing.Any
    :param input_scale: input_scale, Scale the mouse movement by this value before applying the delta
    :type input_scale: typing.Any | None
    :param invert: invert, Invert the mouse input
    :type invert: bool | typing.Any | None
    :param initial_x: initial_x
    :type initial_x: typing.Any | None
    """

    ...

def context_pie_enum(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
):
    """Undocumented contribute <https://developer.blender.org/T51061>

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, RNA context string
    :type data_path: str | typing.Any
    """

    ...

def context_scale_float(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    value: typing.Any | None = 1.0,
):
    """Scale a float context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, RNA context string
    :type data_path: str | typing.Any
    :param value: Value, Assign value
    :type value: typing.Any | None
    """

    ...

def context_scale_int(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    value: typing.Any | None = 1.0,
    always_step: bool | typing.Any | None = True,
):
    """Scale an int context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, RNA context string
    :type data_path: str | typing.Any
    :param value: Value, Assign value
    :type value: typing.Any | None
    :param always_step: Always Step, Always adjust the value by a minimum of 1 when 'value' is not 1.0
    :type always_step: bool | typing.Any | None
    """

    ...

def context_set_boolean(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    value: bool | typing.Any | None = True,
):
    """Set a context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, RNA context string
    :type data_path: str | typing.Any
    :param value: Value, Assignment value
    :type value: bool | typing.Any | None
    """

    ...

def context_set_enum(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    value: str | typing.Any = "",
):
    """Set a context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, RNA context string
    :type data_path: str | typing.Any
    :param value: Value, Assignment value (as a string)
    :type value: str | typing.Any
    """

    ...

def context_set_float(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    value: typing.Any | None = 0.0,
    relative: bool | typing.Any | None = False,
):
    """Set a context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, RNA context string
    :type data_path: str | typing.Any
    :param value: Value, Assignment value
    :type value: typing.Any | None
    :param relative: Relative, Apply relative to the current value (delta)
    :type relative: bool | typing.Any | None
    """

    ...

def context_set_id(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    value: str | typing.Any = "",
):
    """Set a context value to an ID data-block

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, RNA context string
    :type data_path: str | typing.Any
    :param value: Value, Assign value
    :type value: str | typing.Any
    """

    ...

def context_set_int(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    value: typing.Any | None = 0,
    relative: bool | typing.Any | None = False,
):
    """Set a context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, RNA context string
    :type data_path: str | typing.Any
    :param value: Value, Assign value
    :type value: typing.Any | None
    :param relative: Relative, Apply relative to the current value (delta)
    :type relative: bool | typing.Any | None
    """

    ...

def context_set_string(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    value: str | typing.Any = "",
):
    """Set a context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, RNA context string
    :type data_path: str | typing.Any
    :param value: Value, Assign value
    :type value: str | typing.Any
    """

    ...

def context_set_value(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    value: str | typing.Any = "",
):
    """Set a context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, RNA context string
    :type data_path: str | typing.Any
    :param value: Value, Assignment value (as a string)
    :type value: str | typing.Any
    """

    ...

def context_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    module: str | typing.Any = "",
):
    """Toggle a context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, RNA context string
    :type data_path: str | typing.Any
    :param module: Module, Optionally override the context with a module
    :type module: str | typing.Any
    """

    ...

def context_toggle_enum(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    value_1: str | typing.Any = "",
    value_2: str | typing.Any = "",
):
    """Toggle a context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, RNA context string
    :type data_path: str | typing.Any
    :param value_1: Value, Toggle enum
    :type value_1: str | typing.Any
    :param value_2: Value, Toggle enum
    :type value_2: str | typing.Any
    """

    ...

def debug_menu(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    debug_value: typing.Any | None = 0,
):
    """Open a popup to set the debug level

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param debug_value: Debug Value
    :type debug_value: typing.Any | None
    """

    ...

def doc_view(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    doc_id: str | typing.Any = "",
):
    """Open online reference docs in a web browser

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param doc_id: Doc ID
    :type doc_id: str | typing.Any
    """

    ...

def doc_view_manual(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    doc_id: str | typing.Any = "",
):
    """Load online manual

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param doc_id: Doc ID
    :type doc_id: str | typing.Any
    """

    ...

def doc_view_manual_ui_context(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """View a context based online manual in a web browser

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def drop_blend_file(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
):
    """Undocumented contribute <https://developer.blender.org/T51061>

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: filepath
    :type filepath: str | typing.Any
    """

    ...

def interface_theme_preset_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str | typing.Any = "",
    remove_name: bool | typing.Any | None = False,
    remove_active: bool | typing.Any | None = False,
):
    """Add or remove a theme preset

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str | typing.Any
    :param remove_name: remove_name
    :type remove_name: bool | typing.Any | None
    :param remove_active: remove_active
    :type remove_active: bool | typing.Any | None
    """

    ...

def keyconfig_preset_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str | typing.Any = "",
    remove_name: bool | typing.Any | None = False,
    remove_active: bool | typing.Any | None = False,
):
    """Add or remove a Key-config Preset

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str | typing.Any
    :param remove_name: remove_name
    :type remove_name: bool | typing.Any | None
    :param remove_active: remove_active
    :type remove_active: bool | typing.Any | None
    """

    ...

def lib_reload(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    library: str | typing.Any = "",
    filepath: str | typing.Any = "",
    directory: str | typing.Any = "",
    filename: str | typing.Any = "",
    hide_props_region: bool | typing.Any | None = True,
    filter_blender: bool | typing.Any | None = True,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    relative_path: bool | typing.Any | None = True,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "FILE_SORT_ALPHA",
):
    """Reload the given library

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param library: Library, Library to reload
        :type library: str | typing.Any
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param directory: Directory, Directory of the file
        :type directory: str | typing.Any
        :param filename: File Name, Name of the file
        :type filename: str | typing.Any
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param relative_path: Relative Path, Select the file relative to the blend file
        :type relative_path: bool | typing.Any | None
        :param display_type: Display Type

    DEFAULT Default, Automatically determine display type for files.

    LIST_VERTICAL Short List, Display files as short list.

    LIST_HORIZONTAL Long List, Display files as a detailed list.

    THUMBNAIL Thumbnails, Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode

    FILE_SORT_ALPHA Name, Sort the file list alphabetically.

    FILE_SORT_EXTENSION Extension, Sort the file list by extension/type.

    FILE_SORT_TIME Modified Date, Sort files by modification time.

    FILE_SORT_SIZE Size, Sort files by size.
        :type sort_method: str | None
    """

    ...

def lib_relocate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    library: str | typing.Any = "",
    filepath: str | typing.Any = "",
    directory: str | typing.Any = "",
    filename: str | typing.Any = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    hide_props_region: bool | typing.Any | None = True,
    filter_blender: bool | typing.Any | None = True,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    relative_path: bool | typing.Any | None = True,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "FILE_SORT_ALPHA",
):
    """Relocate the given library to one or several others

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param library: Library, Library to relocate
        :type library: str | typing.Any
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param directory: Directory, Directory of the file
        :type directory: str | typing.Any
        :param filename: File Name, Name of the file
        :type filename: str | typing.Any
        :param files: Files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param relative_path: Relative Path, Select the file relative to the blend file
        :type relative_path: bool | typing.Any | None
        :param display_type: Display Type

    DEFAULT Default, Automatically determine display type for files.

    LIST_VERTICAL Short List, Display files as short list.

    LIST_HORIZONTAL Long List, Display files as a detailed list.

    THUMBNAIL Thumbnails, Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode

    FILE_SORT_ALPHA Name, Sort the file list alphabetically.

    FILE_SORT_EXTENSION Extension, Sort the file list by extension/type.

    FILE_SORT_TIME Modified Date, Sort files by modification time.

    FILE_SORT_SIZE Size, Sort files by size.
        :type sort_method: str | None
    """

    ...

def link(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    directory: str | typing.Any = "",
    filename: str | typing.Any = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    filter_blender: bool | typing.Any | None = True,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = True,
    filemode: typing.Any | None = 1,
    relative_path: bool | typing.Any | None = True,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "FILE_SORT_ALPHA",
    link: bool | typing.Any | None = True,
    autoselect: bool | typing.Any | None = True,
    active_collection: bool | typing.Any | None = True,
    instance_collections: bool | typing.Any | None = True,
):
    """Link from a Library .blend file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param directory: Directory, Directory of the file
        :type directory: str | typing.Any
        :param filename: File Name, Name of the file
        :type filename: str | typing.Any
        :param files: Files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param relative_path: Relative Path, Select the file relative to the blend file
        :type relative_path: bool | typing.Any | None
        :param display_type: Display Type

    DEFAULT Default, Automatically determine display type for files.

    LIST_VERTICAL Short List, Display files as short list.

    LIST_HORIZONTAL Long List, Display files as a detailed list.

    THUMBNAIL Thumbnails, Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode

    FILE_SORT_ALPHA Name, Sort the file list alphabetically.

    FILE_SORT_EXTENSION Extension, Sort the file list by extension/type.

    FILE_SORT_TIME Modified Date, Sort files by modification time.

    FILE_SORT_SIZE Size, Sort files by size.
        :type sort_method: str | None
        :param link: Link, Link the objects or data-blocks rather than appending
        :type link: bool | typing.Any | None
        :param autoselect: Select, Select new objects
        :type autoselect: bool | typing.Any | None
        :param active_collection: Active Collection, Put new objects on the active collection
        :type active_collection: bool | typing.Any | None
        :param instance_collections: Instance Collections, Create instances for collections, rather than adding them directly to the scene
        :type instance_collections: bool | typing.Any | None
    """

    ...

def memory_statistics(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Print memory statistics to the console

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def open_mainfile(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    hide_props_region: bool | typing.Any | None = True,
    filter_blender: bool | typing.Any | None = True,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "FILE_SORT_ALPHA",
    load_ui: bool | typing.Any | None = True,
    use_scripts: bool | typing.Any | None = True,
    display_file_selector: bool | typing.Any | None = True,
    state: typing.Any | None = 0,
):
    """Open a Blender file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param display_type: Display Type

    DEFAULT Default, Automatically determine display type for files.

    LIST_VERTICAL Short List, Display files as short list.

    LIST_HORIZONTAL Long List, Display files as a detailed list.

    THUMBNAIL Thumbnails, Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode

    FILE_SORT_ALPHA Name, Sort the file list alphabetically.

    FILE_SORT_EXTENSION Extension, Sort the file list by extension/type.

    FILE_SORT_TIME Modified Date, Sort files by modification time.

    FILE_SORT_SIZE Size, Sort files by size.
        :type sort_method: str | None
        :param load_ui: Load UI, Load user interface setup in the .blend file
        :type load_ui: bool | typing.Any | None
        :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
        :type use_scripts: bool | typing.Any | None
        :param display_file_selector: Display File Selector
        :type display_file_selector: bool | typing.Any | None
        :param state: State
        :type state: typing.Any | None
    """

    ...

def operator_cheat_sheet(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """List all the Operators in a text-block, useful for scripting

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def operator_defaults(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Set the active operator to its default values

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def operator_pie_enum(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    prop_string: str | typing.Any = "",
):
    """Undocumented contribute <https://developer.blender.org/T51061>

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Operator, Operator name (in python as string)
    :type data_path: str | typing.Any
    :param prop_string: Property, Property name (as a string)
    :type prop_string: str | typing.Any
    """

    ...

def operator_preset_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str | typing.Any = "",
    remove_name: bool | typing.Any | None = False,
    remove_active: bool | typing.Any | None = False,
    operator: str | typing.Any = "",
):
    """Add or remove an Operator Preset

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str | typing.Any
    :param remove_name: remove_name
    :type remove_name: bool | typing.Any | None
    :param remove_active: remove_active
    :type remove_active: bool | typing.Any | None
    :param operator: Operator
    :type operator: str | typing.Any
    """

    ...

def owner_disable(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    owner_id: str | typing.Any = "",
):
    """Enable workspace owner ID

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param owner_id: UI Tag
    :type owner_id: str | typing.Any
    """

    ...

def owner_enable(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    owner_id: str | typing.Any = "",
):
    """Enable workspace owner ID

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param owner_id: UI Tag
    :type owner_id: str | typing.Any
    """

    ...

def path_open(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
):
    """Open a path in a file browser

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: filepath
    :type filepath: str | typing.Any
    """

    ...

def previews_batch_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    directory: str | typing.Any = "",
    filter_blender: bool | typing.Any | None = True,
    filter_folder: bool | typing.Any | None = True,
    use_scenes: bool | typing.Any | None = True,
    use_collections: bool | typing.Any | None = True,
    use_objects: bool | typing.Any | None = True,
    use_intern_data: bool | typing.Any | None = True,
    use_trusted: bool | typing.Any | None = False,
    use_backups: bool | typing.Any | None = True,
):
    """Clear selected .blend file's previews

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param files: files
    :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
    :param directory: directory
    :type directory: str | typing.Any
    :param filter_blender: filter_blender
    :type filter_blender: bool | typing.Any | None
    :param filter_folder: filter_folder
    :type filter_folder: bool | typing.Any | None
    :param use_scenes: Scenes, Clear scenes' previews
    :type use_scenes: bool | typing.Any | None
    :param use_collections: Collections, Clear collections' previews
    :type use_collections: bool | typing.Any | None
    :param use_objects: Objects, Clear objects' previews
    :type use_objects: bool | typing.Any | None
    :param use_intern_data: Mat/Tex/..., Clear 'internal' previews (materials, textures, images, etc.)
    :type use_intern_data: bool | typing.Any | None
    :param use_trusted: Trusted Blend Files, Enable python evaluation for selected files
    :type use_trusted: bool | typing.Any | None
    :param use_backups: Save Backups, Keep a backup (.blend1) version of the files when saving with cleared previews
    :type use_backups: bool | typing.Any | None
    """

    ...

def previews_batch_generate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    directory: str | typing.Any = "",
    filter_blender: bool | typing.Any | None = True,
    filter_folder: bool | typing.Any | None = True,
    use_scenes: bool | typing.Any | None = True,
    use_collections: bool | typing.Any | None = True,
    use_objects: bool | typing.Any | None = True,
    use_intern_data: bool | typing.Any | None = True,
    use_trusted: bool | typing.Any | None = False,
    use_backups: bool | typing.Any | None = True,
):
    """Generate selected .blend file's previews

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param files: files
    :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
    :param directory: directory
    :type directory: str | typing.Any
    :param filter_blender: filter_blender
    :type filter_blender: bool | typing.Any | None
    :param filter_folder: filter_folder
    :type filter_folder: bool | typing.Any | None
    :param use_scenes: Scenes, Generate scenes' previews
    :type use_scenes: bool | typing.Any | None
    :param use_collections: Collections, Generate collections' previews
    :type use_collections: bool | typing.Any | None
    :param use_objects: Objects, Generate objects' previews
    :type use_objects: bool | typing.Any | None
    :param use_intern_data: Mat/Tex/..., Generate 'internal' previews (materials, textures, images, etc.)
    :type use_intern_data: bool | typing.Any | None
    :param use_trusted: Trusted Blend Files, Enable python evaluation for selected files
    :type use_trusted: bool | typing.Any | None
    :param use_backups: Save Backups, Keep a backup (.blend1) version of the files when saving with generated previews
    :type use_backups: bool | typing.Any | None
    """

    ...

def previews_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    id_type: set[str] | None = {
        "ALL",
        "GEOMETRY",
        "GROUP",
        "IMAGE",
        "LIGHT",
        "MATERIAL",
        "OBJECT",
        "SCENE",
        "SHADING",
        "TEXTURE",
        "WORLD",
    },
):
    """Clear data-block previews (only for some types like objects, materials, textures, etc.)

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param id_type: Data-Block Type, Which data-block previews to clear

    ALL All Types.

    GEOMETRY All Geometry Types, Clear previews for scenes, collections and objects.

    SHADING All Shading Types, Clear previews for materiasl, lights, worlds, textures and images.

    SCENE Scenes.

    GROUP Groups.

    OBJECT Objects.

    MATERIAL Materials.

    LIGHT Lights.

    WORLD Worlds.

    TEXTURE Textures.

    IMAGE Images.
        :type id_type: set[str] | None
    """

    ...

def previews_ensure(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Ensure data-block previews are available and up-to-date (to be saved in .blend file, only for some types like materials, textures, etc.)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def properties_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
):
    """Undocumented contribute <https://developer.blender.org/T51061>

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Property Edit, Property data_path edit
    :type data_path: str | typing.Any
    """

    ...

def properties_context_change(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    context: str | typing.Any = "",
):
    """Jump to a different tab inside the properties editor

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param context: Context
    :type context: str | typing.Any
    """

    ...

def properties_edit(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    property: str | typing.Any = "",
    value: str | typing.Any = "",
    default: str | typing.Any = "",
    min: typing.Any | None = -10000,
    max: typing.Any | None = 10000.0,
    use_soft_limits: bool | typing.Any | None = False,
    is_overridable_library: bool | typing.Any | None = False,
    soft_min: typing.Any | None = -10000,
    soft_max: typing.Any | None = 10000.0,
    description: str | typing.Any = "",
    subtype: str | None = "",
):
    """Undocumented contribute <https://developer.blender.org/T51061>

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Property Edit, Property data_path edit
    :type data_path: str | typing.Any
    :param property: Property Name, Property name edit
    :type property: str | typing.Any
    :param value: Property Value, Property value edit
    :type value: str | typing.Any
    :param default: Default Value, Default value of the property. Important for NLA mixing
    :type default: str | typing.Any
    :param min: Min
    :type min: typing.Any | None
    :param max: Max
    :type max: typing.Any | None
    :param use_soft_limits: Use Soft Limits
    :type use_soft_limits: bool | typing.Any | None
    :param is_overridable_library: Is Library Overridable
    :type is_overridable_library: bool | typing.Any | None
    :param soft_min: Min
    :type soft_min: typing.Any | None
    :param soft_max: Max
    :type soft_max: typing.Any | None
    :param description: Tooltip
    :type description: str | typing.Any
    :param subtype: Subtype
    :type subtype: str | None
    """

    ...

def properties_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path: str | typing.Any = "",
    property: str | typing.Any = "",
):
    """Internal use (edit a property data_path)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Property Edit, Property data_path edit
    :type data_path: str | typing.Any
    :param property: Property Name, Property name edit
    :type property: str | typing.Any
    """

    ...

def quit_blender(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Quit Blender

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def radial_control(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    data_path_primary: str | typing.Any = "",
    data_path_secondary: str | typing.Any = "",
    use_secondary: str | typing.Any = "",
    rotation_path: str | typing.Any = "",
    color_path: str | typing.Any = "",
    fill_color_path: str | typing.Any = "",
    fill_color_override_path: str | typing.Any = "",
    fill_color_override_test_path: str | typing.Any = "",
    zoom_path: str | typing.Any = "",
    image_id: str | typing.Any = "",
    secondary_tex: bool | typing.Any | None = False,
):
    """Set some size property (like e.g. brush size) with mouse wheel

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path_primary: Primary Data Path, Primary path of property to be set by the radial control
    :type data_path_primary: str | typing.Any
    :param data_path_secondary: Secondary Data Path, Secondary path of property to be set by the radial control
    :type data_path_secondary: str | typing.Any
    :param use_secondary: Use Secondary, Path of property to select between the primary and secondary data paths
    :type use_secondary: str | typing.Any
    :param rotation_path: Rotation Path, Path of property used to rotate the texture display
    :type rotation_path: str | typing.Any
    :param color_path: Color Path, Path of property used to set the color of the control
    :type color_path: str | typing.Any
    :param fill_color_path: Fill Color Path, Path of property used to set the fill color of the control
    :type fill_color_path: str | typing.Any
    :param fill_color_override_path: Fill Color Override Path
    :type fill_color_override_path: str | typing.Any
    :param fill_color_override_test_path: Fill Color Override Test
    :type fill_color_override_test_path: str | typing.Any
    :param zoom_path: Zoom Path, Path of property used to set the zoom level for the control
    :type zoom_path: str | typing.Any
    :param image_id: Image ID, Path of ID that is used to generate an image for the control
    :type image_id: str | typing.Any
    :param secondary_tex: Secondary Texture, Tweak brush secondary/mask texture
    :type secondary_tex: bool | typing.Any | None
    """

    ...

def read_factory_settings(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    app_template: str | typing.Any = "Template",
    use_empty: bool | typing.Any | None = False,
):
    """Load factory default startup file and preferences. To make changes permanent, use "Save Startup File" and "Save Preferences"

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :type app_template: str | typing.Any
    :param use_empty: Empty
    :type use_empty: bool | typing.Any | None
    """

    ...

def read_factory_userpref(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Load factory default preferences. To make changes to preferences permanent, use "Save Preferences"

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def read_history(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reloads history and bookmarks

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def read_homefile(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    load_ui: bool | typing.Any | None = True,
    use_splash: bool | typing.Any | None = False,
    app_template: str | typing.Any = "Template",
    use_empty: bool | typing.Any | None = False,
):
    """Open the default file (doesn't save the current file)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: File Path, Path to an alternative start-up file
    :type filepath: str | typing.Any
    :param load_ui: Load UI, Load user interface setup from the .blend file
    :type load_ui: bool | typing.Any | None
    :param use_splash: Splash
    :type use_splash: bool | typing.Any | None
    :type app_template: str | typing.Any
    :param use_empty: Empty
    :type use_empty: bool | typing.Any | None
    """

    ...

def read_userpref(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Load last saved preferences

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def recover_auto_save(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    hide_props_region: bool | typing.Any | None = True,
    filter_blender: bool | typing.Any | None = True,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = False,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    display_type: str | None = "LIST_VERTICAL",
    sort_method: str | None = "FILE_SORT_TIME",
):
    """Open an automatically saved file to recover it

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param display_type: Display Type

    DEFAULT Default, Automatically determine display type for files.

    LIST_VERTICAL Short List, Display files as short list.

    LIST_HORIZONTAL Long List, Display files as a detailed list.

    THUMBNAIL Thumbnails, Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode

    FILE_SORT_ALPHA Name, Sort the file list alphabetically.

    FILE_SORT_EXTENSION Extension, Sort the file list by extension/type.

    FILE_SORT_TIME Modified Date, Sort files by modification time.

    FILE_SORT_SIZE Size, Sort files by size.
        :type sort_method: str | None
    """

    ...

def recover_last_session(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Open the last closed file ("quit.blend")

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def redraw_timer(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "DRAW",
    iterations: typing.Any | None = 10,
    time_limit: typing.Any | None = 0.0,
):
    """Simple redraw timer to test the speed of updating the interface

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    DRAW Draw Region, Draw Region.

    DRAW_SWAP Draw Region + Swap, Draw Region and Swap.

    DRAW_WIN Draw Window, Draw Window.

    DRAW_WIN_SWAP Draw Window + Swap, Draw Window and Swap.

    ANIM_STEP Anim Step, Animation Steps.

    ANIM_PLAY Anim Play, Animation Playback.

    UNDO Undo/Redo, Undo/Redo.
        :type type: str | None
        :param iterations: Iterations, Number of times to redraw
        :type iterations: typing.Any | None
        :param time_limit: Time Limit, Seconds to run the test for (override iterations)
        :type time_limit: typing.Any | None
    """

    ...

def revert_mainfile(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_scripts: bool | typing.Any | None = True,
):
    """Reload the saved file

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
    :type use_scripts: bool | typing.Any | None
    """

    ...

def save_as_mainfile(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    hide_props_region: bool | typing.Any | None = True,
    check_existing: bool | typing.Any | None = True,
    filter_blender: bool | typing.Any | None = True,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "FILE_SORT_ALPHA",
    compress: bool | typing.Any | None = False,
    relative_remap: bool | typing.Any | None = True,
    copy: bool | typing.Any | None = False,
):
    """Save the current file in the desired location

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | typing.Any | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param display_type: Display Type

    DEFAULT Default, Automatically determine display type for files.

    LIST_VERTICAL Short List, Display files as short list.

    LIST_HORIZONTAL Long List, Display files as a detailed list.

    THUMBNAIL Thumbnails, Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode

    FILE_SORT_ALPHA Name, Sort the file list alphabetically.

    FILE_SORT_EXTENSION Extension, Sort the file list by extension/type.

    FILE_SORT_TIME Modified Date, Sort files by modification time.

    FILE_SORT_SIZE Size, Sort files by size.
        :type sort_method: str | None
        :param compress: Compress, Write compressed .blend file
        :type compress: bool | typing.Any | None
        :param relative_remap: Remap Relative, Make paths relative when saving to a different directory
        :type relative_remap: bool | typing.Any | None
        :param copy: Save Copy, Save a copy of the actual working state but does not make saved file active
        :type copy: bool | typing.Any | None
    """

    ...

def save_homefile(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Make the current file the default .blend file

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def save_mainfile(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    hide_props_region: bool | typing.Any | None = True,
    check_existing: bool | typing.Any | None = True,
    filter_blender: bool | typing.Any | None = True,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "FILE_SORT_ALPHA",
    compress: bool | typing.Any | None = False,
    relative_remap: bool | typing.Any | None = False,
    exit: bool | typing.Any | None = False,
):
    """Save the current Blender file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | typing.Any | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param display_type: Display Type

    DEFAULT Default, Automatically determine display type for files.

    LIST_VERTICAL Short List, Display files as short list.

    LIST_HORIZONTAL Long List, Display files as a detailed list.

    THUMBNAIL Thumbnails, Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode

    FILE_SORT_ALPHA Name, Sort the file list alphabetically.

    FILE_SORT_EXTENSION Extension, Sort the file list by extension/type.

    FILE_SORT_TIME Modified Date, Sort files by modification time.

    FILE_SORT_SIZE Size, Sort files by size.
        :type sort_method: str | None
        :param compress: Compress, Write compressed .blend file
        :type compress: bool | typing.Any | None
        :param relative_remap: Remap Relative, Make paths relative when saving to a different directory
        :type relative_remap: bool | typing.Any | None
        :param exit: Exit, Exit Blender after saving
        :type exit: bool | typing.Any | None
    """

    ...

def save_userpref(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Make the current preferences default

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def search_menu(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Pop-up a search menu over all available operators in current context

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def set_stereo_3d(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    display_mode: str | None = "ANAGLYPH",
    anaglyph_type: str | None = "RED_CYAN",
    interlace_type: str | None = "ROW_INTERLEAVED",
    use_interlace_swap: bool | typing.Any | None = False,
    use_sidebyside_crosseyed: bool | typing.Any | None = False,
):
    """Toggle 3D stereo support for current window (or change the display mode)

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param display_mode: Display Mode

    ANAGLYPH Anaglyph, Render views for left and right eyes as two differently filtered colors in a single image (anaglyph glasses are required).

    INTERLACE Interlace, Render views for left and right eyes interlaced in a single image (3D-ready monitor is required).

    TIMESEQUENTIAL Time Sequential, Render alternate eyes (also known as page flip, quad buffer support in the graphic card is required).

    SIDEBYSIDE Side-by-Side, Render views for left and right eyes side-by-side.

    TOPBOTTOM Top-Bottom, Render views for left and right eyes one above another.
        :type display_mode: str | None
        :param anaglyph_type: Anaglyph Type
        :type anaglyph_type: str | None
        :param interlace_type: Interlace Type
        :type interlace_type: str | None
        :param use_interlace_swap: Swap Left/Right, Swap left and right stereo channels
        :type use_interlace_swap: bool | typing.Any | None
        :param use_sidebyside_crosseyed: Cross-Eyed, Right eye should see left image and vice-versa
        :type use_sidebyside_crosseyed: bool | typing.Any | None
    """

    ...

def splash(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Open the splash screen with release info

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def sysinfo(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
):
    """Generate system information, saved into a text file

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: filepath
    :type filepath: str | typing.Any
    """

    ...

def tool_set_by_id(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str | typing.Any = "",
    cycle: bool | typing.Any | None = False,
    space_type: str | None = "EMPTY",
):
    """Set the tool by name (for keymaps)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Identifier, Identifier of the tool
    :type name: str | typing.Any
    :param cycle: Cycle, Cycle through tools in this group
    :type cycle: bool | typing.Any | None
    :param space_type: Type
    :type space_type: str | None
    """

    ...

def tool_set_by_index(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    index: typing.Any | None = 0,
    cycle: bool | typing.Any | None = False,
    expand: bool | typing.Any | None = True,
    space_type: str | None = "EMPTY",
):
    """Set the tool by index (for keymaps)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param index: Index in toolbar
    :type index: typing.Any | None
    :param cycle: Cycle, Cycle through tools in this group
    :type cycle: bool | typing.Any | None
    :param expand: expand, Include tool sub-groups
    :type expand: bool | typing.Any | None
    :param space_type: Type
    :type space_type: str | None
    """

    ...

def toolbar(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Undocumented contribute <https://developer.blender.org/T51061>

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def url_open(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    url: str | typing.Any = "",
):
    """Open a website in the web-browser

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param url: URL, URL to open
    :type url: str | typing.Any
    """

    ...

def url_open_preset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "",
    id: str | typing.Any = "",
):
    """Open a preset website in the web-browser

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Site
    :type type: str | None
    :param id: Identifier, Optional identifier
    :type id: str | typing.Any
    """

    ...

def userpref_autoexec_path_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add path to exclude from autoexecution

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def userpref_autoexec_path_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    index: typing.Any | None = 0,
):
    """Remove path to exclude from autoexecution

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param index: Index
    :type index: typing.Any | None
    """

    ...

def window_close(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Close the current window

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def window_fullscreen_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Toggle the current window fullscreen

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def window_new(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Create a new window

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def window_new_main(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Create a new main window with its own workspace and scene selection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...
