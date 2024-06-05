import typing
import collections.abc
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def addon_disable(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    module: str | typing.Any = "",
):
    """Disable an add-on

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param module: Module, Module name of the add-on to disable
    :type module: str | typing.Any
    """

    ...

def addon_enable(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    module: str | typing.Any = "",
):
    """Enable an add-on

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param module: Module, Module name of the add-on to enable
    :type module: str | typing.Any
    """

    ...

def addon_expand(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    module: str | typing.Any = "",
):
    """Display information and preferences for this add-on

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param module: Module, Module name of the add-on to expand
    :type module: str | typing.Any
    """

    ...

def addon_install(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    overwrite: bool | typing.Any | None = True,
    target: str | None = "DEFAULT",
    filepath: str | typing.Any = "",
    filter_folder: bool | typing.Any | None = True,
    filter_python: bool | typing.Any | None = True,
    filter_glob: str | typing.Any = "*.py;*.zip",
):
    """Install an add-on

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param overwrite: Overwrite, Remove existing add-ons with the same ID
    :type overwrite: bool | typing.Any | None
    :param target: Target Path
    :type target: str | None
    :param filepath: filepath
    :type filepath: str | typing.Any
    :param filter_folder: Filter folders
    :type filter_folder: bool | typing.Any | None
    :param filter_python: Filter python
    :type filter_python: bool | typing.Any | None
    :param filter_glob: filter_glob
    :type filter_glob: str | typing.Any
    """

    ...

def addon_refresh(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Scan add-on directories for new modules

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def addon_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    module: str | typing.Any = "",
):
    """Delete the add-on from the file system

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param module: Module, Module name of the add-on to remove
    :type module: str | typing.Any
    """

    ...

def addon_userpref_show(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    module: str | typing.Any = "",
):
    """Show add-on user preferences

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param module: Module, Module name of the add-on to expand
    :type module: str | typing.Any
    """

    ...

def alembic_export(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    check_existing: bool | typing.Any | None = True,
    filter_blender: bool | typing.Any | None = False,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
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
    compression_type: str | None = "OGAWA",
    global_scale: typing.Any | None = 1.0,
    triangulate: bool | typing.Any | None = False,
    quad_method: str | None = "SHORTEST_DIAGONAL",
    ngon_method: str | None = "BEAUTY",
    export_hair: bool | typing.Any | None = True,
    export_particles: bool | typing.Any | None = True,
    as_background_job: bool | typing.Any | None = True,
    init_scene_frame_range: bool | typing.Any | None = False,
):
    """Export current scene in an Alembic archive

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
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

    LIST_SHORT Short List, Display files as short list.

    LIST_LONG Long List, Display files as a detailed list.

    THUMBNAIL Thumbnails, Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode

    FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.

    FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.

    FILE_SORT_TIME Sort by time, Sort files by modification time.

    FILE_SORT_SIZE Sort by size, Sort files by size.
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
        :param as_background_job: Run as Background Job, Enable this to run the import in the background, disable to block Blender while importing
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
    check_existing: bool | typing.Any | None = True,
    filter_blender: bool | typing.Any | None = False,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = True,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "FILE_SORT_ALPHA",
    scale: typing.Any | None = 1.0,
    set_frame_range: bool | typing.Any | None = True,
    validate_meshes: bool | typing.Any | None = False,
    is_sequence: bool | typing.Any | None = False,
    as_background_job: bool | typing.Any | None = True,
):
    """Load an Alembic archive

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
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

    LIST_SHORT Short List, Display files as short list.

    LIST_LONG Long List, Display files as a detailed list.

    THUMBNAIL Thumbnails, Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode

    FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.

    FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.

    FILE_SORT_TIME Sort by time, Sort files by modification time.

    FILE_SORT_SIZE Sort by size, Sort files by size.
        :type sort_method: str | None
        :param scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
        :type scale: typing.Any | None
        :param set_frame_range: Set Frame Range, If checked, update scene's start and end frame to match those of the Alembic archive
        :type set_frame_range: bool | typing.Any | None
        :param validate_meshes: Validate Meshes, Check imported mesh objects for invalid data (slow)
        :type validate_meshes: bool | typing.Any | None
        :param is_sequence: Is Sequence, Set to true if the cache is split into separate files
        :type is_sequence: bool | typing.Any | None
        :param as_background_job: Run as Background Job, Enable this to run the export in the background, disable to block Blender while exporting
        :type as_background_job: bool | typing.Any | None
    """

    ...

def app_template_install(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    overwrite: bool | typing.Any | None = True,
    filepath: str | typing.Any = "",
    filter_folder: bool | typing.Any | None = True,
    filter_glob: str | typing.Any = "*.zip",
):
    """Install an application-template

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param overwrite: Overwrite, Remove existing template with the same ID
    :type overwrite: bool | typing.Any | None
    :param filepath: filepath
    :type filepath: str | typing.Any
    :param filter_folder: Filter folders
    :type filter_folder: bool | typing.Any | None
    :param filter_glob: filter_glob
    :type filter_glob: str | typing.Any
    """

    ...

def appconfig_activate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
):
    """Undocumented

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: filepath
    :type filepath: str | typing.Any
    """

    ...

def appconfig_default(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Undocumented

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
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
    active_layer: bool | typing.Any | None = True,
    instance_groups: bool | typing.Any | None = False,
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

    LIST_SHORT Short List, Display files as short list.

    LIST_LONG Long List, Display files as a detailed list.

    THUMBNAIL Thumbnails, Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode

    FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.

    FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.

    FILE_SORT_TIME Sort by time, Sort files by modification time.

    FILE_SORT_SIZE Sort by size, Sort files by size.
        :type sort_method: str | None
        :param link: Link, Link the objects or data-blocks rather than appending
        :type link: bool | typing.Any | None
        :param autoselect: Select, Select new objects
        :type autoselect: bool | typing.Any | None
        :param active_layer: Active Layer, Put new objects on the active layer
        :type active_layer: bool | typing.Any | None
        :param instance_groups: Instance Groups, Create Dupli-Group instances for each group
        :type instance_groups: bool | typing.Any | None
        :param set_fake: Fake User, Set Fake User for appended items (except Objects and Groups)
        :type set_fake: bool | typing.Any | None
        :param use_recursive: Localize All, Localize all appended data, including those indirectly linked from other libraries
        :type use_recursive: bool | typing.Any | None
    """

    ...

def blenderplayer_start(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Launch the blender-player with the current blend-file

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

def collada_export(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    check_existing: bool | typing.Any | None = True,
    filter_blender: bool | typing.Any | None = False,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = True,
    filter_alembic: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "FILE_SORT_ALPHA",
    apply_modifiers: bool | typing.Any | None = False,
    export_mesh_type: typing.Any | None = 0,
    export_mesh_type_selection: str | None = "view",
    selected: bool | typing.Any | None = False,
    include_children: bool | typing.Any | None = False,
    include_armatures: bool | typing.Any | None = False,
    include_shapekeys: bool | typing.Any | None = True,
    deform_bones_only: bool | typing.Any | None = False,
    active_uv_only: bool | typing.Any | None = False,
    use_texture_copies: bool | typing.Any | None = True,
    triangulate: bool | typing.Any | None = True,
    use_object_instantiation: bool | typing.Any | None = True,
    use_blender_profile: bool | typing.Any | None = True,
    sort_by_name: bool | typing.Any | None = False,
    export_transformation_type: typing.Any | None = 0,
    export_transformation_type_selection: str | None = "matrix",
    export_texture_type: typing.Any | None = 0,
    export_texture_type_selection: str | None = "mat",
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

    LIST_SHORT Short List, Display files as short list.

    LIST_LONG Long List, Display files as a detailed list.

    THUMBNAIL Thumbnails, Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode

    FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.

    FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.

    FILE_SORT_TIME Sort by time, Sort files by modification time.

    FILE_SORT_SIZE Sort by size, Sort files by size.
        :type sort_method: str | None
        :param apply_modifiers: Apply Modifiers, Apply modifiers to exported mesh (non destructive))
        :type apply_modifiers: bool | typing.Any | None
        :param export_mesh_type: Resolution, Modifier resolution for export
        :type export_mesh_type: typing.Any | None
        :param export_mesh_type_selection: Resolution, Modifier resolution for export

    view View, Apply modifier's view settings.

    render Render, Apply modifier's render settings.
        :type export_mesh_type_selection: str | None
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
        :param export_transformation_type: Transform, Transformation type for translation, scale and rotation
        :type export_transformation_type: typing.Any | None
        :param export_transformation_type_selection: Transform, Transformation type for translation, scale and rotation

    matrix Matrix, Use <matrix> to specify transformations.

    transrotloc TransRotLoc, Use <translate>, <rotate>, <scale> to specify transformations.
        :type export_transformation_type_selection: str | None
        :param export_texture_type: Texture Type, Type for exported Textures (UV or MAT)
        :type export_texture_type: typing.Any | None
        :param export_texture_type_selection: Texture Type, Type for exported Textures (UV or MAT)

    mat Materials, Export Materials.

    uv UV Textures, Export UV Textures (Face textures) as materials.
        :type export_texture_type_selection: str | None
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
    filter_blender: bool | typing.Any | None = False,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
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

    LIST_SHORT Short List, Display files as short list.

    LIST_LONG Long List, Display files as a detailed list.

    THUMBNAIL Thumbnails, Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode

    FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.

    FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.

    FILE_SORT_TIME Sort by time, Sort files by modification time.

    FILE_SORT_SIZE Sort by size, Sort files by size.
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
    """Undocumented

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
    """Undocumented

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
):
    """Toggle a context value

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Context Attributes, RNA context string
    :type data_path: str | typing.Any
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

def copy_prev_settings(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Copy settings from previous version

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
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

def dependency_relations(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Print dependency graph relations to the console

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def doc_view(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    doc_id: str | typing.Any = "",
):
    """Load online reference docs

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

def interaction_preset_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str | typing.Any = "",
    remove_active: bool | typing.Any | None = False,
):
    """Add or remove an Application Interaction Preset

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str | typing.Any
    :param remove_active: remove_active
    :type remove_active: bool | typing.Any | None
    """

    ...

def interface_theme_preset_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str | typing.Any = "",
    remove_active: bool | typing.Any | None = False,
):
    """Add or remove a theme preset

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str | typing.Any
    :param remove_active: remove_active
    :type remove_active: bool | typing.Any | None
    """

    ...

def keyconfig_activate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
):
    """Undocumented

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: filepath
    :type filepath: str | typing.Any
    """

    ...

def keyconfig_export(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "keymap.py",
    filter_folder: bool | typing.Any | None = True,
    filter_text: bool | typing.Any | None = True,
    filter_python: bool | typing.Any | None = True,
):
    """Export key configuration to a python script

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: filepath
    :type filepath: str | typing.Any
    :param filter_folder: Filter folders
    :type filter_folder: bool | typing.Any | None
    :param filter_text: Filter text
    :type filter_text: bool | typing.Any | None
    :param filter_python: Filter python
    :type filter_python: bool | typing.Any | None
    """

    ...

def keyconfig_import(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "keymap.py",
    filter_folder: bool | typing.Any | None = True,
    filter_text: bool | typing.Any | None = True,
    filter_python: bool | typing.Any | None = True,
    keep_original: bool | typing.Any | None = True,
):
    """Import key configuration from a python script

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: filepath
    :type filepath: str | typing.Any
    :param filter_folder: Filter folders
    :type filter_folder: bool | typing.Any | None
    :param filter_text: Filter text
    :type filter_text: bool | typing.Any | None
    :param filter_python: Filter python
    :type filter_python: bool | typing.Any | None
    :param keep_original: Keep original, Keep original file after copying to configuration folder
    :type keep_original: bool | typing.Any | None
    """

    ...

def keyconfig_preset_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str | typing.Any = "",
    remove_active: bool | typing.Any | None = False,
):
    """Add or remove a Key-config Preset

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str | typing.Any
    :param remove_active: remove_active
    :type remove_active: bool | typing.Any | None
    """

    ...

def keyconfig_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove key config

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def keyconfig_test(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Test key-config for conflicts

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def keyitem_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add key map item

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def keyitem_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    item_id: typing.Any | None = 0,
):
    """Remove key map item

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param item_id: Item Identifier, Identifier of the item to remove
    :type item_id: typing.Any | None
    """

    ...

def keyitem_restore(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    item_id: typing.Any | None = 0,
):
    """Restore key map item

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param item_id: Item Identifier, Identifier of the item to remove
    :type item_id: typing.Any | None
    """

    ...

def keymap_restore(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    all: bool | typing.Any | None = False,
):
    """Restore key map(s)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param all: All Keymaps, Restore all keymaps to default
    :type all: bool | typing.Any | None
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
    filter_blender: bool | typing.Any | None = True,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
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

    LIST_SHORT Short List, Display files as short list.

    LIST_LONG Long List, Display files as a detailed list.

    THUMBNAIL Thumbnails, Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode

    FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.

    FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.

    FILE_SORT_TIME Sort by time, Sort files by modification time.

    FILE_SORT_SIZE Sort by size, Sort files by size.
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
    filter_blender: bool | typing.Any | None = True,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
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

    LIST_SHORT Short List, Display files as short list.

    LIST_LONG Long List, Display files as a detailed list.

    THUMBNAIL Thumbnails, Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode

    FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.

    FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.

    FILE_SORT_TIME Sort by time, Sort files by modification time.

    FILE_SORT_SIZE Sort by size, Sort files by size.
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
    active_layer: bool | typing.Any | None = True,
    instance_groups: bool | typing.Any | None = True,
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

    LIST_SHORT Short List, Display files as short list.

    LIST_LONG Long List, Display files as a detailed list.

    THUMBNAIL Thumbnails, Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode

    FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.

    FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.

    FILE_SORT_TIME Sort by time, Sort files by modification time.

    FILE_SORT_SIZE Sort by size, Sort files by size.
        :type sort_method: str | None
        :param link: Link, Link the objects or data-blocks rather than appending
        :type link: bool | typing.Any | None
        :param autoselect: Select, Select new objects
        :type autoselect: bool | typing.Any | None
        :param active_layer: Active Layer, Put new objects on the active layer
        :type active_layer: bool | typing.Any | None
        :param instance_groups: Instance Groups, Create Dupli-Group instances for each group
        :type instance_groups: bool | typing.Any | None
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
    filter_blender: bool | typing.Any | None = True,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
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
):
    """Open a Blender file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
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

    LIST_SHORT Short List, Display files as short list.

    LIST_LONG Long List, Display files as a detailed list.

    THUMBNAIL Thumbnails, Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode

    FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.

    FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.

    FILE_SORT_TIME Sort by time, Sort files by modification time.

    FILE_SORT_SIZE Sort by size, Sort files by size.
        :type sort_method: str | None
        :param load_ui: Load UI, Load user interface setup in the .blend file
        :type load_ui: bool | typing.Any | None
        :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
        :type use_scripts: bool | typing.Any | None
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
    """Undocumented

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
    remove_active: bool | typing.Any | None = False,
    operator: str | typing.Any = "",
):
    """Add or remove an Operator Preset

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str | typing.Any
    :param remove_active: remove_active
    :type remove_active: bool | typing.Any | None
    :param operator: Operator
    :type operator: str | typing.Any
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
    use_groups: bool | typing.Any | None = True,
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
    :param use_groups: Groups, Clear groups' previews
    :type use_groups: bool | typing.Any | None
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
    use_groups: bool | typing.Any | None = True,
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
    :param use_groups: Groups, Generate groups' previews
    :type use_groups: bool | typing.Any | None
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
        "GROUP",
        "IMAGE",
        "LAMP",
        "MATERIAL",
        "OBJECT",
        "SCENE",
        "TEXTURE",
        "WORLD",
    },
):
    """Clear data-block previews (only for some types like objects, materials, textures, etc.)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param id_type: Data-Block Type, Which data-block previews to clear
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
    """Undocumented

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
    min: typing.Any | None = -10000,
    max: typing.Any | None = 10000.0,
    use_soft_limits: bool | typing.Any | None = False,
    soft_min: typing.Any | None = -10000,
    soft_max: typing.Any | None = 10000.0,
    description: str | typing.Any = "",
):
    """Undocumented

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param data_path: Property Edit, Property data_path edit
    :type data_path: str | typing.Any
    :param property: Property Name, Property name edit
    :type property: str | typing.Any
    :param value: Property Value, Property value edit
    :type value: str | typing.Any
    :param min: Min
    :type min: typing.Any | None
    :param max: Max
    :type max: typing.Any | None
    :param use_soft_limits: Use Soft Limits
    :type use_soft_limits: bool | typing.Any | None
    :param soft_min: Min
    :type soft_min: typing.Any | None
    :param soft_max: Max
    :type soft_max: typing.Any | None
    :param description: Tooltip
    :type description: str | typing.Any
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
    """Load default file and user preferences

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :type app_template: str | typing.Any
    :param use_empty: Empty
    :type use_empty: bool | typing.Any | None
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
    use_empty: bool | typing.Any | None = False,
    use_splash: bool | typing.Any | None = False,
    app_template: str | typing.Any = "Template",
):
    """Open the default file (doesn't save the current file)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: File Path, Path to an alternative start-up file
    :type filepath: str | typing.Any
    :param load_ui: Load UI, Load user interface setup from the .blend file
    :type load_ui: bool | typing.Any | None
    :param use_empty: Empty
    :type use_empty: bool | typing.Any | None
    :param use_splash: Splash
    :type use_splash: bool | typing.Any | None
    :type app_template: str | typing.Any
    """

    ...

def recover_auto_save(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    filter_blender: bool | typing.Any | None = True,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = False,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = False,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 8,
    display_type: str | None = "LIST_LONG",
    sort_method: str | None = "FILE_SORT_TIME",
):
    """Open an automatically saved file to recover it

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
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

    LIST_SHORT Short List, Display files as short list.

    LIST_LONG Long List, Display files as a detailed list.

    THUMBNAIL Thumbnails, Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode

    FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.

    FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.

    FILE_SORT_TIME Sort by time, Sort files by modification time.

    FILE_SORT_SIZE Sort by size, Sort files by size.
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
    check_existing: bool | typing.Any | None = True,
    filter_blender: bool | typing.Any | None = True,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
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
    use_mesh_compat: bool | typing.Any | None = False,
):
    """Save the current file in the desired location

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
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

    LIST_SHORT Short List, Display files as short list.

    LIST_LONG Long List, Display files as a detailed list.

    THUMBNAIL Thumbnails, Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode

    FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.

    FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.

    FILE_SORT_TIME Sort by time, Sort files by modification time.

    FILE_SORT_SIZE Sort by size, Sort files by size.
        :type sort_method: str | None
        :param compress: Compress, Write compressed .blend file
        :type compress: bool | typing.Any | None
        :param relative_remap: Remap Relative, Remap relative paths when saving in a different directory
        :type relative_remap: bool | typing.Any | None
        :param copy: Save Copy, Save a copy of the actual working state but does not make saved file active
        :type copy: bool | typing.Any | None
        :param use_mesh_compat: Legacy Mesh Format, Save using legacy mesh format (no ngons) - WARNING: only saves tris and quads, other ngons will be lost (no implicit triangulation)
        :type use_mesh_compat: bool | typing.Any | None
    """

    ...

def save_homefile(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Make the current file the default .blend file, includes preferences

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
    check_existing: bool | typing.Any | None = True,
    filter_blender: bool | typing.Any | None = True,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
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
):
    """Save the current Blender file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
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

    LIST_SHORT Short List, Display files as short list.

    LIST_LONG Long List, Display files as a detailed list.

    THUMBNAIL Thumbnails, Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode

    FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.

    FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.

    FILE_SORT_TIME Sort by time, Sort files by modification time.

    FILE_SORT_SIZE Sort by size, Sort files by size.
        :type sort_method: str | None
        :param compress: Compress, Write compressed .blend file
        :type compress: bool | typing.Any | None
        :param relative_remap: Remap Relative, Remap relative paths when saving in a different directory
        :type relative_remap: bool | typing.Any | None
    """

    ...

def save_userpref(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Save user preferences separately, overrides startup file preferences

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

def theme_install(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    overwrite: bool | typing.Any | None = True,
    filepath: str | typing.Any = "",
    filter_folder: bool | typing.Any | None = True,
    filter_glob: str | typing.Any = "*.xml",
):
    """Load and apply a Blender XML theme file

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param overwrite: Overwrite, Remove existing theme file if exists
    :type overwrite: bool | typing.Any | None
    :param filepath: filepath
    :type filepath: str | typing.Any
    :param filter_folder: Filter folders
    :type filter_folder: bool | typing.Any | None
    :param filter_glob: filter_glob
    :type filter_glob: str | typing.Any
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
    """Close the current Blender window

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def window_duplicate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Duplicate the current Blender window

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
