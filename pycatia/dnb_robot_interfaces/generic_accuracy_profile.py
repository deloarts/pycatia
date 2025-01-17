#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_robot_interfaces.rob_generic_controller import RobGenericController
from pycatia.system_interfaces.any_object import AnyObject


class GenericAccuracyProfile(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     GenericAccuracyProfile
                | 
                | Interface to manage Generic Accuracy Profile of Robot
                | controller.
                | 
                | Role: This interface provides methods to get/set data related to Accuracy
                | Profile.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.generic_accuracy_profile = com_object

    def get_accuracy_type(self, accuracy: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetAccuracyType(AccuracyType accuracy)
                | 
                |     Get the accuracy type for the profile.
                | 
                |     Parameters:
                | 
                |         accurancy
                |             accurancy type to get, could be ACCURACY_TYPE_DISTANCE /
                |             ACCURACY_TYPE_SPEED 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param int accuracy:
        :return: None
        :rtype: None
        """
        return self.generic_accuracy_profile.GetAccuracyType(accuracy)

    def get_accuracy_value(self, value: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetAccuracyValue(double value)
                | 
                |     Retrieves accuracy value of the profile.
                | 
                |     Parameters:
                | 
                |         value
                |             This parameter contains accuracy value. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param float value:
        :return: None
        :rtype: None
        """
        return self.generic_accuracy_profile.GetAccuracyValue(value)

    def get_controller(self, o_controller: RobGenericController) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetController(RobGenericController oController)
                | 
                |     Retrieves controller owning the profile.
                | 
                |     Parameters:
                | 
                |         oController
                |             This parameter contains pointer to controller. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param RobGenericController o_controller:
        :return: None
        :rtype: None
        """
        return self.generic_accuracy_profile.GetController(o_controller.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_controller'
        # # vba_code = """
        # # Public Function get_controller(generic_accuracy_profile)
        # #     Dim oController (2)
        # #     generic_accuracy_profile.GetController oController
        # #     get_controller = oController
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_fly_by_mode(self, o_mode: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetFlyByMode(boolean oMode)
                | 
                |     Gets On/Off status of Flyby mode.
                | 
                |     Parameters:
                | 
                |         oMode
                |             mode indicating On/Off status. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param bool o_mode:
        :return: None
        :rtype: None
        """
        return self.generic_accuracy_profile.GetFlyByMode(o_mode)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_fly_by_mode'
        # # vba_code = """
        # # Public Function get_fly_by_mode(generic_accuracy_profile)
        # #     Dim oMode (2)
        # #     generic_accuracy_profile.GetFlyByMode oMode
        # #     get_fly_by_mode = oMode
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_name(self, o_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetName(CATBSTR oName)
                | 
                |     Gets name of the Accuracy Profile.
                | 
                |     Parameters:
                | 
                |         oName
                |             Name of the required Accuracy Profile. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param str o_name:
        :return: None
        :rtype: None
        """
        return self.generic_accuracy_profile.GetName(o_name)

    def set_accuracy_type(self, accuracy: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAccuracyType(AccuracyType accuracy)
                | 
                |     Set the accuracy type for the profile.
                | 
                |     Parameters:
                | 
                |         accurancy
                |             accurancy type to set, could be ACCURACY_TYPE_DISTANCE /
                |             ACCURACY_TYPE_SPEED 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param int accuracy:
        :return: None
        :rtype: None
        """
        return self.generic_accuracy_profile.SetAccuracyType(accuracy)

    def set_accuracy_value(self, value: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetAccuracyValue(double value)
                | 
                |     Set accuracy value of the profile.
                | 
                |     Parameters:
                | 
                |         value
                |             This parameter is percentage or absolute value, depending on
                |             accurancy type. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param float value:
        :return: None
        :rtype: None
        """
        return self.generic_accuracy_profile.SetAccuracyValue(value)

    def set_fly_by_mode(self, i_mode: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetFlyByMode(boolean iMode)
                | 
                |     Switch On/Off Flyby mode.
                | 
                |     Parameters:
                | 
                |         iMode
                |             mode indicating On/Off status. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param bool i_mode:
        :return: None
        :rtype: None
        """
        return self.generic_accuracy_profile.SetFlyByMode(i_mode)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_fly_by_mode'
        # # vba_code = """
        # # Public Function set_fly_by_mode(generic_accuracy_profile)
        # #     Dim iMode (2)
        # #     generic_accuracy_profile.SetFlyByMode iMode
        # #     set_fly_by_mode = iMode
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_name(self, i_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetName(CATBSTR iName)
                | 
                |     Set name of the Accuracy Profile.
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the Accuracy Profile to be set. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise

        :param str i_name:
        :return: None
        :rtype: None
        """
        return self.generic_accuracy_profile.SetName(i_name)

    def __repr__(self):
        return f'GenericAccuracyProfile(name="{self.name}")'
