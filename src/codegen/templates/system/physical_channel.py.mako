<%
    from codegen.utilities.text_wrappers import wrap
    from codegen.utilities.function_helpers import get_functions,  get_enums_used as function_enums
    from codegen.utilities.attribute_helpers import get_attributes,  get_enums_used as attribute_enums, transform_attributes
    from codegen.utilities.helpers import get_enums_to_import
    attributes = get_attributes(data, "PhysicalChannel")
    attributes = transform_attributes(attributes, "PhysicalChannel")
    functions = get_functions(data,"PhysicalChannel")
    attr_enums = attribute_enums(attributes)
    func_enums = function_enums(functions)
    enums_used = get_enums_to_import(attr_enums, func_enums)
%>\
# Do not edit this file; it was automatically generated.

import ctypes
import numpy
import deprecation

from nidaqmx._lib import (
    lib_importer, wrapped_ndpointer, enum_bitfield_to_list, ctypes_byte_str,
    c_bool32)
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small, is_array_buffer_too_small)
from nidaqmx.utils import unflatten_channel_string
%if enums_used:
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})
%endif

__all__ = ['PhysicalChannel']


class PhysicalChannel:
    """
    Represents a DAQmx physical channel.
    """
    __slots__ = ['_name', '__weakref__']

    def __init__(self, name):
        """
        Args:
            name (str): Specifies the name of the physical channel.
        """
        self._name = name

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._name == other._name
        return False

    def __hash__(self):
        return hash(self._name)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return f'PhysicalChannel(name={self._name})'

    @property
    def name(self):
        """
        str: Specifies the name of this physical channel.
        """
        return self._name

<%namespace name="property_template" file="/property_template.py.mako"/>\
%for attribute in attributes:
${property_template.script_property(attribute)}\
%endfor
\
<%namespace name="deprecated_template" file="/property_deprecated_template.py.mako"/>\
${deprecated_template.script_deprecated_property(attributes)}\
<%namespace name="function_template" file="/function_template.py.mako"/>\
%for function_object in functions:
${function_template.script_function(function_object)}
%endfor