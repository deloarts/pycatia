#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dmaps_interfaces.activity import Activity
from pycatia.system_interfaces.any_object import AnyObject


class DeviceTask(Activity):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DMAPSInterfaces.Activity
                |                         DeviceTask
                | 
                | Represents the Device Task.
                | 
                | Role: The interface is used manage activities under a Device
                | Task.
                | The following code snippet can be used to obtain the Device Task from a Device
                | Task Factory.
                | 
                |    Dim objDeviceTaskFactory As DeviceTaskFactory
                |    Dim objDevice As Product
                |    ...
                |    Set objDeviceTaskFactory = objDevice.GetTechnologicalObject("DeviceTaskFactory" )
                |    Dim objDeviceTaskList(3) as DeviceTask
                |    Dim objDeviceTask as DeviceTask
                |    objDeviceTaskFactory.GetAllDeviceTasks objDeviceTaskList
                |    objDeviceTask=objDeviceTaskList[0]
                |  
                | 
                | 
                | The Device Task can also be obtained from an activity of the type
                | DeviceTask.
                | 
                |    Dim objActivity as Activity
                |    ...
                |    Dim objDeviceTask as DeviceTask
                |    Set objDeviceTask = objActivity.GetTechnologicalObject("DeviceTask" )
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.device_task = com_object

    def create_delay_activity(
            self,
            isp_father: AnyObject,
            position: int,
            delay_time: float,
            o_delay_acty: Activity
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub CreateDelayActivity(AnyObject ispFather,
                | short position,
                | double delay_time,
                | Activity oDelayActy)
                | 
                |     Creates a Delay Activity inside a Device Task
                | 
                |     Parameters:
                | 
                |         ispFather
                |             The Activity preceeding the new activity. 
                |         position
                |             Whether to insert activity before or after father. 0 tells at the
                |             start and 1 means after 
                |         delay_time
                |             The input delay time value to be set. 
                |         oDelayActy
                |             The created Delay Activity 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The Delay Activity was successfully created.
                |         E_FAIL
                |             The Delay Activity could not be created.
                | 
                |         Example:
                |             The following example creates An Delay Activity under a given
                |             device task
                | 
                |                Dim objDeviceTask as DeviceTask
                |                Dim objPreceedingActy as Activity
                |                ..
                |                Dim objDelayAct as Object
                |                objDeviceTask.CreateDelayActivity
                |                objPreceedingActy,1,objDelayAct

        :param AnyObject isp_father:
        :param int position:
        :param float delay_time:
        :param Activity o_delay_acty:
        :return: None
        :rtype: None
        """
        return self.device_task.CreateDelayActivity(
            isp_father.com_object,
            position,
            delay_time,
            o_delay_acty.com_object
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'create_delay_activity'
        # # vba_code = """
        # # Public Function create_delay_activity(device_task)
        # #     Dim ispFather (2)
        # #     device_task.CreateDelayActivity ispFather
        # #     create_delay_activity = ispFather
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def create_move_home_activity(self, isp_father: AnyObject, position: int, o_move_home_acty: Activity) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub CreateMoveHomeActivity(AnyObject ispFather,
                | short position,
                | Activity oMoveHomeActy)
                | 
                |     Creates a MoveHome Activity inside a Device Task
                | 
                |     Parameters:
                | 
                |         ispFather
                |             The Activity preceeding the new activity. 
                |         position
                |             Whether to insert activity before or after father. 0 tells at the
                |             start and 1 means after 
                |         oMoveHomeActy
                |             The created MoveHome Activity 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The MoveHome Activity was successfully created.
                |         E_FAIL
                |             The MoveHome Activity could not be created.
                | 
                |         Example:
                |             The following example creates An MoveHome Activity under a given
                |             device task
                | 
                |                Dim objDeviceTask as DeviceTask
                |                Dim objPreceedingActy as Activity
                |                ..
                |                Dim objMovHomeAct as Object
                |                objDeviceTask.CreateMoveHomeActivity
                |                objPreceedingActy,1,objMovHomeAct

        :param AnyObject isp_father:
        :param int position:
        :param Activity o_move_home_acty:
        :return: None
        :rtype: None
        """
        return self.device_task.CreateMoveHomeActivity(isp_father.com_object, position, o_move_home_acty.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'create_move_home_activity'
        # # vba_code = """
        # # Public Function create_move_home_activity(device_task)
        # #     Dim ispFather (2)
        # #     device_task.CreateMoveHomeActivity ispFather
        # #     create_move_home_activity = ispFather
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def create_move_joints_activity(self, isp_father: AnyObject, position: int, o_move_joints_acty: Activity) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub CreateMoveJointsActivity(AnyObject ispFather,
                | short position,
                | Activity oMoveJointsActy)
                | 
                |     Creates a MoveJoints Activity inside a Device Task
                | 
                |     Parameters:
                | 
                |         ispFather
                |             The Activity preceeding the new activity. 
                |         position
                |             Whether to insert activity before or after father. 0 tells at the
                |             start and 1 means after 
                |         oMoveJointsActy
                |             The created MoveJoints Activity 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The MoveJoints Activity was successfully created.
                |         E_FAIL
                |             The MoveJoints Activity could not be created.
                | 
                |         Example:
                |             The following example creates An MoveJoints Activity under a given
                |             device task
                | 
                |                Dim objDeviceTask as DeviceTask
                |                Dim objPreceedingActy as Activity
                |                ..
                |                Dim objMovJointsAct as Object
                |                objDeviceTask.CreateMoveJointsActivity
                |                objPreceedingActy,1,objMovJointsAct

        :param AnyObject isp_father:
        :param int position:
        :param Activity o_move_joints_acty:
        :return: None
        :rtype: None
        """
        return self.device_task.CreateMoveJointsActivity(isp_father.com_object, position, o_move_joints_acty.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'create_move_joints_activity'
        # # vba_code = """
        # # Public Function create_move_joints_activity(device_task)
        # #     Dim ispFather (2)
        # #     device_task.CreateMoveJointsActivity ispFather
        # #     create_move_joints_activity = ispFather
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'DeviceTask(name="{self.name}")'
