import typing
import collections.abc
import bpy_types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class ToolActivePanelHelper:
    bl_label: typing.Any

    def draw(self, context):
        """

        :param context:
        """
        ...

class ToolDef:
    cursor: typing.Any
    data_block: typing.Any
    description: typing.Any
    draw_cursor: typing.Any
    draw_settings: typing.Any
    icon: typing.Any
    idname: typing.Any
    keymap: typing.Any
    label: typing.Any
    operator: typing.Any
    widget: typing.Any

    def count(self, value):
        """

        :param value:
        """
        ...

    def from_dict(self, kw_args):
        """

        :param kw_args:
        """
        ...

    def from_fn(self, fn):
        """

        :param fn:
        """
        ...

    def index(self, value, start=0, stop=9223372036854775807):
        """

        :param value:
        :param start:
        :param stop:
        """
        ...

class ToolSelectPanelHelper:
    def draw(self, context):
        """

        :param context:
        """
        ...

    def draw_active_tool_header(
        self, context, layout, show_tool_name=False, tool_key=None
    ):
        """

        :param context:
        :param layout:
        :param show_tool_name:
        :param tool_key:
        """
        ...

    def draw_cls(self, layout, context, detect_layout=True, scale_y=1.75):
        """

        :param layout:
        :param context:
        :param detect_layout:
        :param scale_y:
        """
        ...

    def keymap_ui_hierarchy(self, context_mode):
        """

        :param context_mode:
        """
        ...

    def register(self): ...
    def tool_active_from_context(self, context):
        """

        :param context:
        """
        ...

class WM_MT_toolsystem_submenu(bpy_types.Menu, bpy_types._GenericUI):
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def append(self, draw_func):
        """

        :param draw_func:
        """
        ...

    def as_pointer(self): ...
    def bl_rna_get_subclass(self): ...
    def bl_rna_get_subclass_py(self): ...
    def draw(self, context):
        """

        :param context:
        """
        ...

    def draw_collapsible(self, context, layout):
        """

        :param context:
        :param layout:
        """
        ...

    def draw_preset(self, _context):
        """

        :param _context:
        """
        ...

    def driver_add(self): ...
    def driver_remove(self): ...
    def get(self): ...
    def is_extended(self): ...
    def is_property_hidden(self): ...
    def is_property_overridable_library(self): ...
    def is_property_readonly(self): ...
    def is_property_set(self): ...
    def items(self): ...
    def keyframe_delete(self): ...
    def keyframe_insert(self): ...
    def keys(self): ...
    def path_from_id(self): ...
    def path_menu(
        self,
        searchpaths,
        operator,
        props_default=None,
        prop_filepath="filepath",
        filter_ext=None,
        filter_path=None,
        display_name=None,
        add_operator=None,
    ):
        """

        :param searchpaths:
        :param operator:
        :param props_default:
        :param prop_filepath:
        :param filter_ext:
        :param filter_path:
        :param display_name:
        :param add_operator:
        """
        ...

    def path_resolve(self): ...
    def pop(self): ...
    def prepend(self, draw_func):
        """

        :param draw_func:
        """
        ...

    def property_overridable_library_set(self): ...
    def property_unset(self): ...
    def remove(self, draw_func):
        """

        :param draw_func:
        """
        ...

    def type_recast(self): ...
    def values(self): ...

def activate_by_id(context, space_type, text): ...
def activate_by_id_or_cycle(context, space_type, idname, offset=1): ...
def description_from_id(context, space_type, idname, use_operator=True): ...
def item_from_flat_index(context, space_type, index): ...
def item_from_id(context, space_type, idname): ...
def item_from_index(context, space_type, index): ...
def keymap_from_id(context, space_type, idname): ...
