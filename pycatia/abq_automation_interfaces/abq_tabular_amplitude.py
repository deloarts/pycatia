#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.abq_automation_interfaces.abq_property import ABQProperty


class ABQTabularAmplitude(ABQProperty):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ABQAutomationItf.ABQProperty
                |                         ABQTabularAmplitude
                | 
                | Represents a tabular amplitude (ABQTabularAmplitude) object.
                | Role: Access an Abaqus tabular amplitude or determine its
                | properties.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.abq_tabular_amplitude = com_object

    @property
    def time_amplitude_table_size(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TimeAmplitudeTableSize() As long (Read Only)
                | 
                |     Returns the size of the time/amplitude table.
                | 
                |     Returns:
                |         The size of the time/amplitude table.

        :return: int
        :rtype: int
        """

        return self.abq_tabular_amplitude.TimeAmplitudeTableSize

    @property
    def time_span(self) -> int:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property TimeSpan() As TimeSpan_Type
                | 
                |     Sets or returns the timespan in tabular amplitude.
                | 
                |     Returns:
                |         The timespan
                | 
                |         Legal values:
                | 
                |         STEP_TIME
                |         TOTAL_TIME

        :return: int
        :rtype: int
        """

        return self.abq_tabular_amplitude.TimeSpan

    @time_span.setter
    def time_span(self, value: int):
        """
        :param int value:
        """

        self.abq_tabular_amplitude.TimeSpan = value

    def add_time_amplitude_table(self, i_time: tuple, i_amplitude: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddTimeAmplitudeTable(CATSafeArrayVariant iTime,
                | CATSafeArrayVariant iAmplitude)
                | 
                |     Adds a list of time and amplitude for the specified time span STEP_TIME or
                |     TOTAL_TIME The number of values in both of the parameters must match. If either
                |     list contains extra values, the extra values are
                |     discarded.
                | 
                |     Parameters:
                | 
                |         iTime
                |             The list of times.
                |         iAmplitude
                |             The list of amplitudes.

        :param tuple i_time:
        :param tuple i_amplitude:
        :return: None
        :rtype: None
        """
        return self.abq_tabular_amplitude.AddTimeAmplitudeTable(i_time, i_amplitude)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_time_amplitude_table'
        # # vba_code = """
        # # Public Function add_time_amplitude_table(abq_tabular_amplitude)
        # #     Dim iTime (2)
        # #     abq_tabular_amplitude.AddTimeAmplitudeTable iTime
        # #     add_time_amplitude_table = iTime
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_time_amplitude_table(self, o_time: tuple, o_amplitude: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetTimeAmplitudeTable(CATSafeArrayVariant oTime,
                | CATSafeArrayVariant oAmplitude)
                | 
                |     Returns a list of time and amplitude for the specified timespan (STEP_TIME
                |     or TOTAL_TIME).
                | 
                |     Parameters:
                | 
                |         oTime
                |             The list of times.
                |         oTemperature
                |             The list of amplitudes.

        :param tuple o_time:
        :param tuple o_amplitude:
        :return: None
        :rtype: None
        """
        return self.abq_tabular_amplitude.GetTimeAmplitudeTable(o_time, o_amplitude)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_time_amplitude_table'
        # # vba_code = """
        # # Public Function get_time_amplitude_table(abq_tabular_amplitude)
        # #     Dim oTime (2)
        # #     abq_tabular_amplitude.GetTimeAmplitudeTable oTime
        # #     get_time_amplitude_table = oTime
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ABQTabularAmplitude(name="{self.name}")'
