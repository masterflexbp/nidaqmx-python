<%
    from codegen.utilities.attribute_helpers import get_attributes, get_enums_used, transform_attributes
    from codegen.utilities.text_wrappers import wrap
    attributes = get_attributes(data, "Channel")
    attributes =  transform_attributes(attributes, "Channel")
    enums_used = get_enums_used(attributes)
%>\
# Do not edit this file; it was automatically generated.

import ctypes
import numpy

import nidaqmx
from nidaqmx._lib import lib_importer, ctypes_byte_str, c_bool32
from nidaqmx.system.physical_channel import PhysicalChannel
from nidaqmx.errors import (
    check_for_error, is_string_buffer_too_small, is_array_buffer_too_small)
from nidaqmx.utils import flatten_channel_string, unflatten_channel_string
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})


class Channel:
    """
    Represents virtual channel or a list of virtual channels.
    """
    __slots__ = ['_handle', '_name', '__weakref__']

    def __init__(self, task_handle, virtual_or_physical_name, interpreter):
        """
        Args:
            task_handle (TaskHandle): Specifies the handle of the task that
                this channel is associated with.
            virtual_or_physical_name (str): Specifies the flattened virtual or
                physical name of a channel.
            interpreter: Specifies the interpreter instance assigned.
        """
        self._handle = task_handle
        self._name = virtual_or_physical_name
        self._interpreter = interpreter

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise NotImplementedError(
                'Cannot concatenate objects of type {} and {}'
                .format(self.__class__, other.__class__))

        if self._handle != other._handle:
            raise NotImplementedError(
                'Cannot concatenate Channel objects from different tasks.')

        name = flatten_channel_string([self.name, other.name])
        return Channel._factory(self._handle, name)

    def __contains__(self, item):
        channel_names = self.channel_names

        if isinstance(item, str):
            items = unflatten_channel_string(item)
        elif isinstance(item, Channel):
            items = item.channel_names

        return all([item in channel_names for item in items])

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self._handle == other._handle and
                    set(self.channel_names) == set(other.channel_names))
        return False

    def __hash__(self):
        return hash((self._handle.value, frozenset(self.channel_names)))

    def __iadd__(self, other):
        return self.__add__(other)

    def __iter__(self):
        for channel_name in self.channel_names:
            yield Channel._factory(self._handle, channel_name)

    def __len__(self):
        return len(self.channel_names)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __reversed__(self):
        channel_names = self.channel_names
        channel_names.reverse()

        for channel_name in channel_names:
            yield Channel._factory(self._handle, channel_name)

    def __repr__(self):
        return f'Channel(name={self.name})'

    @staticmethod
    def _factory(task_handle, virtual_or_physical_name, interpreter):
        """
        Implements the factory pattern for nidaqmx channels.

        Args:
            task_handle (TaskHandle): Specifies the handle of the task that
                this channel is associated with.
            virtual_or_physical_name (str): Specifies the flattened virtual
                or physical name of a channel.
            interpreter: Specifies the interpreter instance assigned.
        Returns:
            nidaqmx._task_modules.channels.channel.Channel:

            Indicates an object that represents the specified channel.
        """
        chan_type = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetChanType
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            task_handle, virtual_or_physical_name, ctypes.byref(chan_type))
        check_for_error(error_code)

        channel_type = ChannelType(chan_type.value)

        if channel_type == ChannelType.ANALOG_INPUT:
            return nidaqmx._task_modules.channels.AIChannel(
                task_handle, virtual_or_physical_name, interpreter)
        elif channel_type == ChannelType.ANALOG_OUTPUT:
            return nidaqmx._task_modules.channels.AOChannel(
                task_handle, virtual_or_physical_name, interpreter)
        elif channel_type == ChannelType.COUNTER_INPUT:
            return nidaqmx._task_modules.channels.CIChannel(
                task_handle, virtual_or_physical_name, interpreter)
        elif channel_type == ChannelType.COUNTER_OUTPUT:
            return nidaqmx._task_modules.channels.COChannel(
                task_handle, virtual_or_physical_name, interpreter)
        elif channel_type == ChannelType.DIGITAL_INPUT:
            return nidaqmx._task_modules.channels.DIChannel(
                task_handle, virtual_or_physical_name, interpreter)
        elif channel_type == ChannelType.DIGITAL_OUTPUT:
            return nidaqmx._task_modules.channels.DOChannel(
                task_handle, virtual_or_physical_name, interpreter)

    @property
    def name(self):
        """
        str: Specifies the name of the virtual channel this object
            represents.
        """
        if self._name:
            return self._name
        else:
            return self._all_channels_name

    @property
    def channel_names(self):
        """
        List[str]: Specifies the unflattened list of the virtual channels.
        """
        if self._name:
            return unflatten_channel_string(self._name)
        else:
            return unflatten_channel_string(self._all_channels_name)

    @property
    def _all_channels_name(self):
        """
        str: Specifies the flattened names of all the virtual channels in
            the task.
        """
        cfunc = lib_importer.windll.DAQmxGetTaskChannels
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p, ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.value.decode('ascii')

<%namespace name="property_template" file="/property_template.py.mako"/>\
%for attribute in attributes:
${property_template.script_property(attribute)}\
%endfor
\
    def save(self, save_as="", author="", overwrite_existing_channel=False,
             allow_interactive_editing=True, allow_interactive_deletion=True):
        """
        Saves this local or global channel to MAX as a global channel.

        Args:
            save_as (Optional[str]): Is the name to save the task,
                global channel, or custom scale as. If you do not
                specify a value for this input, NI-DAQmx uses the name
                currently assigned to the task, global channel, or
                custom scale.
            author (Optional[str]): Is a name to store with the task,
                global channel, or custom scale.
            overwrite_existing_channel (Optional[bool]): Specifies whether to
                overwrite a global channel of the same name if one is already
                saved in MAX. If this input is False and a global channel of
                the same name is already saved in MAX, this function returns
                an error.
            allow_interactive_editing (Optional[bool]): Specifies whether to
                allow the task, global channel, or custom scale to be edited
                in the DAQ Assistant. If allow_interactive_editing is True,
                the DAQ Assistant must support all task or global channel
                settings.
            allow_interactive_deletion (Optional[bool]): Specifies whether
                to allow the task, global channel, or custom scale to be
                deleted through MAX.
        """
        options = 0
        if overwrite_existing_channel:
            options |= _Save.OVERWRITE.value
        if allow_interactive_editing:
            options |= _Save.ALLOW_INTERACTIVE_EDITING.value
        if allow_interactive_deletion:
            options |= _Save.ALLOW_INTERACTIVE_DELETION.value

        cfunc = lib_importer.windll.DAQmxSaveGlobalChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_uint]

        error_code = cfunc(
            self._handle, self._name, save_as, author, options)
        check_for_error(error_code)
