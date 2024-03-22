# Do not edit this file; it was automatically generated.

from nidaqmx.constants import (
    DeassertCondition, DigitalWidthUnits, ExportAction, Level, Polarity,
    Signal)


class ExportSignals:
    """
    Represents the exported signal configurations for a DAQmx task.
    """
    def __init__(self, task_handle, interpreter):
        self._handle = task_handle
        self._interpreter = interpreter

    @property
    def adv_cmplt_event_delay(self):
        """
        float: Specifies the output signal delay in periods of the
            sample clock.
        """

        val = self._interpreter.get_exported_signal_attribute_double(self._handle, 0x1757)
        return val

    @adv_cmplt_event_delay.setter
    def adv_cmplt_event_delay(self, val):
        self._interpreter.set_exported_signal_attribute_double(self._handle, 0x1757, val)

    @adv_cmplt_event_delay.deleter
    def adv_cmplt_event_delay(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x1757)

    @property
    def adv_cmplt_event_output_term(self):
        """
        str: Specifies the terminal to which to route the Advance
            Complete Event.
        """

        val = self._interpreter.get_exported_signal_attribute_string(self._handle, 0x1651)
        return val

    @adv_cmplt_event_output_term.setter
    def adv_cmplt_event_output_term(self, val):
        self._interpreter.set_exported_signal_attribute_string(self._handle, 0x1651, val)

    @adv_cmplt_event_output_term.deleter
    def adv_cmplt_event_output_term(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x1651)

    @property
    def adv_cmplt_event_pulse_polarity(self):
        """
        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            the exported Advance Complete Event.
        """

        val = self._interpreter.get_exported_signal_attribute_int32(self._handle, 0x1652)
        return Polarity(val)

    @adv_cmplt_event_pulse_polarity.setter
    def adv_cmplt_event_pulse_polarity(self, val):
        val = val.value
        self._interpreter.set_exported_signal_attribute_int32(self._handle, 0x1652, val)

    @adv_cmplt_event_pulse_polarity.deleter
    def adv_cmplt_event_pulse_polarity(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x1652)

    @property
    def adv_cmplt_event_pulse_width(self):
        """
        float: Specifies the width of the exported Advance Complete
            Event pulse.
        """

        val = self._interpreter.get_exported_signal_attribute_double(self._handle, 0x1654)
        return val

    @adv_cmplt_event_pulse_width.setter
    def adv_cmplt_event_pulse_width(self, val):
        self._interpreter.set_exported_signal_attribute_double(self._handle, 0x1654, val)

    @adv_cmplt_event_pulse_width.deleter
    def adv_cmplt_event_pulse_width(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x1654)

    @property
    def adv_trig_output_term(self):
        """
        str: Specifies the terminal to which to route the Advance
            Trigger.
        """

        val = self._interpreter.get_exported_signal_attribute_string(self._handle, 0x1645)
        return val

    @adv_trig_output_term.setter
    def adv_trig_output_term(self, val):
        self._interpreter.set_exported_signal_attribute_string(self._handle, 0x1645, val)

    @adv_trig_output_term.deleter
    def adv_trig_output_term(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x1645)

    @property
    def adv_trig_pulse_polarity(self):
        """
        :class:`nidaqmx.constants.Polarity`: Indicates the polarity of
            the exported Advance Trigger.
        """

        val = self._interpreter.get_exported_signal_attribute_int32(self._handle, 0x1646)
        return Polarity(val)

    @property
    def adv_trig_pulse_width(self):
        """
        float: Specifies the width of an exported Advance Trigger pulse.
            Specify this value in the units you specify with
            **adv_trig_pulse_width_units**.
        """

        val = self._interpreter.get_exported_signal_attribute_double(self._handle, 0x1648)
        return val

    @adv_trig_pulse_width.setter
    def adv_trig_pulse_width(self, val):
        self._interpreter.set_exported_signal_attribute_double(self._handle, 0x1648, val)

    @adv_trig_pulse_width.deleter
    def adv_trig_pulse_width(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x1648)

    @property
    def adv_trig_pulse_width_units(self):
        """
        :class:`nidaqmx.constants.DigitalWidthUnits`: Specifies the
            units of **adv_trig_pulse_width**.
        """

        val = self._interpreter.get_exported_signal_attribute_int32(self._handle, 0x1647)
        return DigitalWidthUnits(val)

    @adv_trig_pulse_width_units.setter
    def adv_trig_pulse_width_units(self, val):
        val = val.value
        self._interpreter.set_exported_signal_attribute_int32(self._handle, 0x1647, val)

    @adv_trig_pulse_width_units.deleter
    def adv_trig_pulse_width_units(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x1647)

    @property
    def ai_conv_clk_output_term(self):
        """
        str: Specifies the terminal to which to route the AI Convert
            Clock.
        """

        val = self._interpreter.get_exported_signal_attribute_string(self._handle, 0x1687)
        return val

    @ai_conv_clk_output_term.setter
    def ai_conv_clk_output_term(self, val):
        self._interpreter.set_exported_signal_attribute_string(self._handle, 0x1687, val)

    @ai_conv_clk_output_term.deleter
    def ai_conv_clk_output_term(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x1687)

    @property
    def ai_conv_clk_pulse_polarity(self):
        """
        :class:`nidaqmx.constants.Polarity`: Indicates the polarity of
            the exported AI Convert Clock. The polarity is fixed and
            independent of the active edge of the source of the AI
            Convert Clock.
        """

        val = self._interpreter.get_exported_signal_attribute_int32(self._handle, 0x1688)
        return Polarity(val)

    @property
    def ai_hold_cmplt_event_output_term(self):
        """
        str: Specifies the terminal to which to route the AI Hold
            Complete Event.
        """

        val = self._interpreter.get_exported_signal_attribute_string(self._handle, 0x18ed)
        return val

    @ai_hold_cmplt_event_output_term.setter
    def ai_hold_cmplt_event_output_term(self, val):
        self._interpreter.set_exported_signal_attribute_string(self._handle, 0x18ed, val)

    @ai_hold_cmplt_event_output_term.deleter
    def ai_hold_cmplt_event_output_term(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x18ed)

    @property
    def ai_hold_cmplt_event_pulse_polarity(self):
        """
        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            an exported AI Hold Complete Event pulse.
        """

        val = self._interpreter.get_exported_signal_attribute_int32(self._handle, 0x18ee)
        return Polarity(val)

    @ai_hold_cmplt_event_pulse_polarity.setter
    def ai_hold_cmplt_event_pulse_polarity(self, val):
        val = val.value
        self._interpreter.set_exported_signal_attribute_int32(self._handle, 0x18ee, val)

    @ai_hold_cmplt_event_pulse_polarity.deleter
    def ai_hold_cmplt_event_pulse_polarity(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x18ee)

    @property
    def change_detect_event_output_term(self):
        """
        str: Specifies the terminal to which to route the Change
            Detection Event.
        """

        val = self._interpreter.get_exported_signal_attribute_string(self._handle, 0x2197)
        return val

    @change_detect_event_output_term.setter
    def change_detect_event_output_term(self, val):
        self._interpreter.set_exported_signal_attribute_string(self._handle, 0x2197, val)

    @change_detect_event_output_term.deleter
    def change_detect_event_output_term(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x2197)

    @property
    def change_detect_event_pulse_polarity(self):
        """
        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            an exported Change Detection Event pulse.
        """

        val = self._interpreter.get_exported_signal_attribute_int32(self._handle, 0x2303)
        return Polarity(val)

    @change_detect_event_pulse_polarity.setter
    def change_detect_event_pulse_polarity(self, val):
        val = val.value
        self._interpreter.set_exported_signal_attribute_int32(self._handle, 0x2303, val)

    @change_detect_event_pulse_polarity.deleter
    def change_detect_event_pulse_polarity(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x2303)

    @property
    def ctr_out_event_output_behavior(self):
        """
        :class:`nidaqmx.constants.ExportAction`: Specifies whether the
            exported Counter Output Event pulses or changes from one
            state to the other when the counter reaches terminal count.
        """

        val = self._interpreter.get_exported_signal_attribute_int32(self._handle, 0x174f)
        return ExportAction(val)

    @ctr_out_event_output_behavior.setter
    def ctr_out_event_output_behavior(self, val):
        val = val.value
        self._interpreter.set_exported_signal_attribute_int32(self._handle, 0x174f, val)

    @ctr_out_event_output_behavior.deleter
    def ctr_out_event_output_behavior(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x174f)

    @property
    def ctr_out_event_output_term(self):
        """
        str: Specifies the terminal to which to route the Counter Output
            Event.
        """

        val = self._interpreter.get_exported_signal_attribute_string(self._handle, 0x1717)
        return val

    @ctr_out_event_output_term.setter
    def ctr_out_event_output_term(self, val):
        self._interpreter.set_exported_signal_attribute_string(self._handle, 0x1717, val)

    @ctr_out_event_output_term.deleter
    def ctr_out_event_output_term(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x1717)

    @property
    def ctr_out_event_pulse_polarity(self):
        """
        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            the pulses at the output terminal of the counter when
            **ctr_out_event_output_behavior** is
            **ExportActions2.PULSE**. NI-DAQmx ignores this property if
            **ctr_out_event_output_behavior** is
            **ExportActions2.TOGGLE**.
        """

        val = self._interpreter.get_exported_signal_attribute_int32(self._handle, 0x1718)
        return Polarity(val)

    @ctr_out_event_pulse_polarity.setter
    def ctr_out_event_pulse_polarity(self, val):
        val = val.value
        self._interpreter.set_exported_signal_attribute_int32(self._handle, 0x1718, val)

    @ctr_out_event_pulse_polarity.deleter
    def ctr_out_event_pulse_polarity(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x1718)

    @property
    def ctr_out_event_toggle_idle_state(self):
        """
        :class:`nidaqmx.constants.Level`: Specifies the initial state of
            the output terminal of the counter when
            **ctr_out_event_output_behavior** is
            **ExportActions2.TOGGLE**. The terminal enters this state
            when NI-DAQmx commits the task.
        """

        val = self._interpreter.get_exported_signal_attribute_int32(self._handle, 0x186a)
        return Level(val)

    @ctr_out_event_toggle_idle_state.setter
    def ctr_out_event_toggle_idle_state(self, val):
        val = val.value
        self._interpreter.set_exported_signal_attribute_int32(self._handle, 0x186a, val)

    @ctr_out_event_toggle_idle_state.deleter
    def ctr_out_event_toggle_idle_state(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x186a)

    @property
    def data_active_event_lvl_active_lvl(self):
        """
        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            the exported Data Active Event.
        """

        val = self._interpreter.get_exported_signal_attribute_int32(self._handle, 0x1634)
        return Polarity(val)

    @data_active_event_lvl_active_lvl.setter
    def data_active_event_lvl_active_lvl(self, val):
        val = val.value
        self._interpreter.set_exported_signal_attribute_int32(self._handle, 0x1634, val)

    @data_active_event_lvl_active_lvl.deleter
    def data_active_event_lvl_active_lvl(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x1634)

    @property
    def data_active_event_output_term(self):
        """
        str: Specifies the terminal to which to export the Data Active
            Event.
        """

        val = self._interpreter.get_exported_signal_attribute_string(self._handle, 0x1633)
        return val

    @data_active_event_output_term.setter
    def data_active_event_output_term(self, val):
        self._interpreter.set_exported_signal_attribute_string(self._handle, 0x1633, val)

    @data_active_event_output_term.deleter
    def data_active_event_output_term(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x1633)

    @property
    def divided_samp_clk_timebase_output_term(self):
        """
        str: Specifies the terminal to which to route the Divided Sample
            Clock Timebase.
        """

        val = self._interpreter.get_exported_signal_attribute_string(self._handle, 0x21a1)
        return val

    @divided_samp_clk_timebase_output_term.setter
    def divided_samp_clk_timebase_output_term(self, val):
        self._interpreter.set_exported_signal_attribute_string(self._handle, 0x21a1, val)

    @divided_samp_clk_timebase_output_term.deleter
    def divided_samp_clk_timebase_output_term(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x21a1)

    @property
    def exported_10_mhz_ref_clk_output_term(self):
        """
        str: Specifies the terminal to which to route the 10MHz Clock.
        """

        val = self._interpreter.get_exported_signal_attribute_string(self._handle, 0x226e)
        return val

    @exported_10_mhz_ref_clk_output_term.setter
    def exported_10_mhz_ref_clk_output_term(self, val):
        self._interpreter.set_exported_signal_attribute_string(self._handle, 0x226e, val)

    @exported_10_mhz_ref_clk_output_term.deleter
    def exported_10_mhz_ref_clk_output_term(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x226e)

    @property
    def exported_20_mhz_timebase_output_term(self):
        """
        str: Specifies the terminal to which to route the 20MHz
            Timebase.
        """

        val = self._interpreter.get_exported_signal_attribute_string(self._handle, 0x1657)
        return val

    @exported_20_mhz_timebase_output_term.setter
    def exported_20_mhz_timebase_output_term(self, val):
        self._interpreter.set_exported_signal_attribute_string(self._handle, 0x1657, val)

    @exported_20_mhz_timebase_output_term.deleter
    def exported_20_mhz_timebase_output_term(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x1657)

    @property
    def hshk_event_delay(self):
        """
        float: Specifies the number of seconds to delay after the
            Handshake Trigger deasserts before asserting the Handshake
            Event.
        """

        val = self._interpreter.get_exported_signal_attribute_double(self._handle, 0x22bc)
        return val

    @hshk_event_delay.setter
    def hshk_event_delay(self, val):
        self._interpreter.set_exported_signal_attribute_double(self._handle, 0x22bc, val)

    @hshk_event_delay.deleter
    def hshk_event_delay(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x22bc)

    @property
    def hshk_event_interlocked_assert_on_start(self):
        """
        bool: Specifies to assert the Handshake Event when the task
            starts if **hshk_event_output_behavior** is
            **ExportActions5.INTERLOCKED**.
        """

        val = self._interpreter.get_exported_signal_attribute_bool(self._handle, 0x22be)
        return val

    @hshk_event_interlocked_assert_on_start.setter
    def hshk_event_interlocked_assert_on_start(self, val):
        self._interpreter.set_exported_signal_attribute_bool(self._handle, 0x22be, val)

    @hshk_event_interlocked_assert_on_start.deleter
    def hshk_event_interlocked_assert_on_start(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x22be)

    @property
    def hshk_event_interlocked_asserted_lvl(self):
        """
        :class:`nidaqmx.constants.Level`: Specifies the asserted level
            of the exported Handshake Event if
            **hshk_event_output_behavior** is
            **ExportActions5.INTERLOCKED**.
        """

        val = self._interpreter.get_exported_signal_attribute_int32(self._handle, 0x22bd)
        return Level(val)

    @hshk_event_interlocked_asserted_lvl.setter
    def hshk_event_interlocked_asserted_lvl(self, val):
        val = val.value
        self._interpreter.set_exported_signal_attribute_int32(self._handle, 0x22bd, val)

    @hshk_event_interlocked_asserted_lvl.deleter
    def hshk_event_interlocked_asserted_lvl(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x22bd)

    @property
    def hshk_event_interlocked_deassert_delay(self):
        """
        float: Specifies in seconds the amount of time to wait after the
            Handshake Trigger asserts before deasserting the Handshake
            Event if **hshk_event_output_behavior** is
            **ExportActions5.INTERLOCKED**.
        """

        val = self._interpreter.get_exported_signal_attribute_double(self._handle, 0x22bf)
        return val

    @hshk_event_interlocked_deassert_delay.setter
    def hshk_event_interlocked_deassert_delay(self, val):
        self._interpreter.set_exported_signal_attribute_double(self._handle, 0x22bf, val)

    @hshk_event_interlocked_deassert_delay.deleter
    def hshk_event_interlocked_deassert_delay(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x22bf)

    @property
    def hshk_event_output_behavior(self):
        """
        :class:`nidaqmx.constants.ExportAction`: Specifies the output
            behavior of the Handshake Event.
        """

        val = self._interpreter.get_exported_signal_attribute_int32(self._handle, 0x22bb)
        return ExportAction(val)

    @hshk_event_output_behavior.setter
    def hshk_event_output_behavior(self, val):
        val = val.value
        self._interpreter.set_exported_signal_attribute_int32(self._handle, 0x22bb, val)

    @hshk_event_output_behavior.deleter
    def hshk_event_output_behavior(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x22bb)

    @property
    def hshk_event_output_term(self):
        """
        str: Specifies the terminal to which to route the Handshake
            Event.
        """

        val = self._interpreter.get_exported_signal_attribute_string(self._handle, 0x22ba)
        return val

    @hshk_event_output_term.setter
    def hshk_event_output_term(self, val):
        self._interpreter.set_exported_signal_attribute_string(self._handle, 0x22ba, val)

    @hshk_event_output_term.deleter
    def hshk_event_output_term(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x22ba)

    @property
    def hshk_event_pulse_polarity(self):
        """
        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            the exported Handshake Event if
            **hshk_event_output_behavior** is **ExportActions5.PULSE**.
        """

        val = self._interpreter.get_exported_signal_attribute_int32(self._handle, 0x22c0)
        return Polarity(val)

    @hshk_event_pulse_polarity.setter
    def hshk_event_pulse_polarity(self, val):
        val = val.value
        self._interpreter.set_exported_signal_attribute_int32(self._handle, 0x22c0, val)

    @hshk_event_pulse_polarity.deleter
    def hshk_event_pulse_polarity(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x22c0)

    @property
    def hshk_event_pulse_width(self):
        """
        float: Specifies in seconds the pulse width of the exported
            Handshake Event if **hshk_event_output_behavior** is
            **ExportActions5.PULSE**.
        """

        val = self._interpreter.get_exported_signal_attribute_double(self._handle, 0x22c1)
        return val

    @hshk_event_pulse_width.setter
    def hshk_event_pulse_width(self, val):
        self._interpreter.set_exported_signal_attribute_double(self._handle, 0x22c1, val)

    @hshk_event_pulse_width.deleter
    def hshk_event_pulse_width(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x22c1)

    @property
    def pause_trig_lvl_active_lvl(self):
        """
        :class:`nidaqmx.constants.Polarity`: Specifies the active level
            of the exported Pause Trigger.
        """

        val = self._interpreter.get_exported_signal_attribute_int32(self._handle, 0x1616)
        return Polarity(val)

    @pause_trig_lvl_active_lvl.setter
    def pause_trig_lvl_active_lvl(self, val):
        val = val.value
        self._interpreter.set_exported_signal_attribute_int32(self._handle, 0x1616, val)

    @pause_trig_lvl_active_lvl.deleter
    def pause_trig_lvl_active_lvl(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x1616)

    @property
    def pause_trig_output_term(self):
        """
        str: Specifies the terminal to which to route the Pause Trigger.
        """

        val = self._interpreter.get_exported_signal_attribute_string(self._handle, 0x1615)
        return val

    @pause_trig_output_term.setter
    def pause_trig_output_term(self, val):
        self._interpreter.set_exported_signal_attribute_string(self._handle, 0x1615, val)

    @pause_trig_output_term.deleter
    def pause_trig_output_term(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x1615)

    @property
    def rdy_for_start_event_lvl_active_lvl(self):
        """
        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            the exported Ready for Start Event.
        """

        val = self._interpreter.get_exported_signal_attribute_int32(self._handle, 0x1751)
        return Polarity(val)

    @rdy_for_start_event_lvl_active_lvl.setter
    def rdy_for_start_event_lvl_active_lvl(self, val):
        val = val.value
        self._interpreter.set_exported_signal_attribute_int32(self._handle, 0x1751, val)

    @rdy_for_start_event_lvl_active_lvl.deleter
    def rdy_for_start_event_lvl_active_lvl(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x1751)

    @property
    def rdy_for_start_event_output_term(self):
        """
        str: Specifies the terminal to which to route the Ready for
            Start Event.
        """

        val = self._interpreter.get_exported_signal_attribute_string(self._handle, 0x1609)
        return val

    @rdy_for_start_event_output_term.setter
    def rdy_for_start_event_output_term(self, val):
        self._interpreter.set_exported_signal_attribute_string(self._handle, 0x1609, val)

    @rdy_for_start_event_output_term.deleter
    def rdy_for_start_event_output_term(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x1609)

    @property
    def rdy_for_xfer_event_deassert_cond(self):
        """
        :class:`nidaqmx.constants.DeassertCondition`: Specifies when the
            ready for transfer event deasserts.
        """

        val = self._interpreter.get_exported_signal_attribute_int32(self._handle, 0x2963)
        return DeassertCondition(val)

    @rdy_for_xfer_event_deassert_cond.setter
    def rdy_for_xfer_event_deassert_cond(self, val):
        val = val.value
        self._interpreter.set_exported_signal_attribute_int32(self._handle, 0x2963, val)

    @rdy_for_xfer_event_deassert_cond.deleter
    def rdy_for_xfer_event_deassert_cond(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x2963)

    @property
    def rdy_for_xfer_event_deassert_cond_custom_threshold(self):
        """
        int: Specifies in samples the threshold below which the Ready
            for Transfer Event deasserts. This threshold is an amount of
            space available in the onboard memory of the device.
            **rdy_for_xfer_event_deassert_cond** must be
            **DeassertCondition.ONBOARD_MEMORY_CUSTOM_THRESHOLD** to use
            a custom threshold.
        """

        val = self._interpreter.get_exported_signal_attribute_uint32(self._handle, 0x2964)
        return val

    @rdy_for_xfer_event_deassert_cond_custom_threshold.setter
    def rdy_for_xfer_event_deassert_cond_custom_threshold(self, val):
        self._interpreter.set_exported_signal_attribute_uint32(self._handle, 0x2964, val)

    @rdy_for_xfer_event_deassert_cond_custom_threshold.deleter
    def rdy_for_xfer_event_deassert_cond_custom_threshold(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x2964)

    @property
    def rdy_for_xfer_event_lvl_active_lvl(self):
        """
        :class:`nidaqmx.constants.Polarity`: Specifies the active level
            of the exported Ready for Transfer Event.
        """

        val = self._interpreter.get_exported_signal_attribute_int32(self._handle, 0x22b6)
        return Polarity(val)

    @rdy_for_xfer_event_lvl_active_lvl.setter
    def rdy_for_xfer_event_lvl_active_lvl(self, val):
        val = val.value
        self._interpreter.set_exported_signal_attribute_int32(self._handle, 0x22b6, val)

    @rdy_for_xfer_event_lvl_active_lvl.deleter
    def rdy_for_xfer_event_lvl_active_lvl(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x22b6)

    @property
    def rdy_for_xfer_event_output_term(self):
        """
        str: Specifies the terminal to which to route the Ready for
            Transfer Event.
        """

        val = self._interpreter.get_exported_signal_attribute_string(self._handle, 0x22b5)
        return val

    @rdy_for_xfer_event_output_term.setter
    def rdy_for_xfer_event_output_term(self, val):
        self._interpreter.set_exported_signal_attribute_string(self._handle, 0x22b5, val)

    @rdy_for_xfer_event_output_term.deleter
    def rdy_for_xfer_event_output_term(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x22b5)

    @property
    def ref_trig_output_term(self):
        """
        str: Specifies the terminal to which to route the Reference
            Trigger.
        """

        val = self._interpreter.get_exported_signal_attribute_string(self._handle, 0x590)
        return val

    @ref_trig_output_term.setter
    def ref_trig_output_term(self, val):
        self._interpreter.set_exported_signal_attribute_string(self._handle, 0x590, val)

    @ref_trig_output_term.deleter
    def ref_trig_output_term(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x590)

    @property
    def ref_trig_pulse_polarity(self):
        """
        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            the exported Reference Trigger.
        """

        val = self._interpreter.get_exported_signal_attribute_int32(self._handle, 0x591)
        return Polarity(val)

    @ref_trig_pulse_polarity.setter
    def ref_trig_pulse_polarity(self, val):
        val = val.value
        self._interpreter.set_exported_signal_attribute_int32(self._handle, 0x591, val)

    @ref_trig_pulse_polarity.deleter
    def ref_trig_pulse_polarity(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x591)

    @property
    def samp_clk_delay_offset(self):
        """
        float: Specifies in seconds the amount of time to offset the
            exported Sample clock.  Refer to timing diagrams for
            generation applications in the device documentation for more
            information about this value.
        """

        val = self._interpreter.get_exported_signal_attribute_double(self._handle, 0x21c4)
        return val

    @samp_clk_delay_offset.setter
    def samp_clk_delay_offset(self, val):
        self._interpreter.set_exported_signal_attribute_double(self._handle, 0x21c4, val)

    @samp_clk_delay_offset.deleter
    def samp_clk_delay_offset(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x21c4)

    @property
    def samp_clk_output_behavior(self):
        """
        :class:`nidaqmx.constants.ExportAction`: Specifies whether the
            exported Sample Clock issues a pulse at the beginning of a
            sample or changes to a high state for the duration of the
            sample.
        """

        val = self._interpreter.get_exported_signal_attribute_int32(self._handle, 0x186b)
        return ExportAction(val)

    @samp_clk_output_behavior.setter
    def samp_clk_output_behavior(self, val):
        val = val.value
        self._interpreter.set_exported_signal_attribute_int32(self._handle, 0x186b, val)

    @samp_clk_output_behavior.deleter
    def samp_clk_output_behavior(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x186b)

    @property
    def samp_clk_output_term(self):
        """
        str: Specifies the terminal to which to route the Sample Clock.
        """

        val = self._interpreter.get_exported_signal_attribute_string(self._handle, 0x1663)
        return val

    @samp_clk_output_term.setter
    def samp_clk_output_term(self, val):
        self._interpreter.set_exported_signal_attribute_string(self._handle, 0x1663, val)

    @samp_clk_output_term.deleter
    def samp_clk_output_term(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x1663)

    @property
    def samp_clk_pulse_polarity(self):
        """
        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            the exported Sample Clock if **samp_clk_output_behavior** is
            **ExportActions3.PULSE**.
        """

        val = self._interpreter.get_exported_signal_attribute_int32(self._handle, 0x1664)
        return Polarity(val)

    @samp_clk_pulse_polarity.setter
    def samp_clk_pulse_polarity(self, val):
        val = val.value
        self._interpreter.set_exported_signal_attribute_int32(self._handle, 0x1664, val)

    @samp_clk_pulse_polarity.deleter
    def samp_clk_pulse_polarity(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x1664)

    @property
    def samp_clk_timebase_output_term(self):
        """
        str: Specifies the terminal to which to route the Sample Clock
            Timebase.
        """

        val = self._interpreter.get_exported_signal_attribute_string(self._handle, 0x18f9)
        return val

    @samp_clk_timebase_output_term.setter
    def samp_clk_timebase_output_term(self, val):
        self._interpreter.set_exported_signal_attribute_string(self._handle, 0x18f9, val)

    @samp_clk_timebase_output_term.deleter
    def samp_clk_timebase_output_term(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x18f9)

    @property
    def start_trig_output_term(self):
        """
        str: Specifies the terminal to which to route the Start Trigger.
        """

        val = self._interpreter.get_exported_signal_attribute_string(self._handle, 0x584)
        return val

    @start_trig_output_term.setter
    def start_trig_output_term(self, val):
        self._interpreter.set_exported_signal_attribute_string(self._handle, 0x584, val)

    @start_trig_output_term.deleter
    def start_trig_output_term(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x584)

    @property
    def start_trig_pulse_polarity(self):
        """
        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            the exported Start Trigger.
        """

        val = self._interpreter.get_exported_signal_attribute_int32(self._handle, 0x585)
        return Polarity(val)

    @start_trig_pulse_polarity.setter
    def start_trig_pulse_polarity(self, val):
        val = val.value
        self._interpreter.set_exported_signal_attribute_int32(self._handle, 0x585, val)

    @start_trig_pulse_polarity.deleter
    def start_trig_pulse_polarity(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x585)

    @property
    def sync_pulse_event_output_term(self):
        """
        str: Specifies the terminal to which to route the
            Synchronization Pulse Event.
        """

        val = self._interpreter.get_exported_signal_attribute_string(self._handle, 0x223c)
        return val

    @sync_pulse_event_output_term.setter
    def sync_pulse_event_output_term(self, val):
        self._interpreter.set_exported_signal_attribute_string(self._handle, 0x223c, val)

    @sync_pulse_event_output_term.deleter
    def sync_pulse_event_output_term(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x223c)

    @property
    def watchdog_expired_event_output_term(self):
        """
        str: Specifies the terminal  to which to route the Watchdog
            Timer Expired Event.
        """

        val = self._interpreter.get_exported_signal_attribute_string(self._handle, 0x21aa)
        return val

    @watchdog_expired_event_output_term.setter
    def watchdog_expired_event_output_term(self, val):
        self._interpreter.set_exported_signal_attribute_string(self._handle, 0x21aa, val)

    @watchdog_expired_event_output_term.deleter
    def watchdog_expired_event_output_term(self):
        self._interpreter.reset_exported_signal_attribute(self._handle, 0x21aa)

    def export_signal(self, signal_id, output_terminal):
        """
        Routes a control signal to the terminal you specify. The output
        terminal can reside on the device that generates the control
        signal or on a different device. You can use this function to
        share clocks and triggers among multiple tasks and devices. The
        routes this function creates are task-based routes.

        Args:
            signal_id (nidaqmx.constants.Signal): Is the name of the
                trigger, clock, or event to export.
            output_terminal (str): Is the destination of the exported
                signal. A DAQmx terminal constant lists all terminals on
                installed devices. You can also specify a string
                containing a comma-delimited list of terminal names.
        """

        self._interpreter.export_signal(
            self._handle, signal_id.value, output_terminal)
