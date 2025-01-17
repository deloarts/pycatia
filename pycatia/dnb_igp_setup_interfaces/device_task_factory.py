#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_igp_setup_interfaces.device_task import DeviceTask
from pycatia.system_interfaces.any_object import AnyObject


class DeviceTaskFactory(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DeviceTaskFactory
                | 
                | Represents the Task Creation Factory for Devices.
                | 
                | Role: Device Task Factory is the object used to create Device
                | tasks.
                | The following code snippet can be used to obtain the Device Task Factory from
                | the Device product.
                | 
                |    Dim objDeviceTaskFactory As DeviceTaskFactory
                |    Dim objDevice As Product
                |    ...
                |    Set objDeviceTaskFactory = objDevice.GetTechnologicalObject("DeviceTaskFactory" )
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.device_task_factory = com_object

    def create_device_task(self, i_name: str, o_device_task: DeviceTask) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub CreateDeviceTask(CATBSTR iName,
                | DeviceTask oDeviceTask)
                | 
                |     Creates a Device Task
                | 
                |     Parameters:
                | 
                |         iName
                |             The Device Task Name. 
                |         oDeviceTask
                |             The Created Device Task. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The Device Task was successfully created.
                |         E_FAIL
                |             The Device Task creation failed.
                | 
                |         Example:
                |             The following example creates a Device task for a
                |             Device.
                | 
                |                Dim objDeviceTaskFactory As DeviceTaskFactory
                |                Dim objDeviceTask as DeviceTask
                |                ..
                |                objDeviceTaskFactory.CreateDeviceTask
                |                "New_DeviceTask_1",objDeviceTask

        :param str i_name:
        :param DeviceTask o_device_task:
        :return: None
        :rtype: None
        """
        return self.device_task_factory.CreateDeviceTask(i_name, o_device_task.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'create_device_task'
        # # vba_code = """
        # # Public Function create_device_task(device_task_factory)
        # #     Dim iName (2)
        # #     device_task_factory.CreateDeviceTask iName
        # #     create_device_task = iName
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def delete_device_task(self, i_device_task: DeviceTask) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub DeleteDeviceTask(DeviceTask iDeviceTask)
                | 
                |     Removes the required Device Task.
                | 
                |     Parameters:
                | 
                |         iDeviceTask
                |             The Device Task to be Removed. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The Device Task could be successfully deleted.
                |         E_FAIL
                |             The deletion of Device Task failed.
                | 
                |         Example:
                |             The following example deletes a device task.
                | 
                |                Dim objDeviceTaskFactory As DeviceTaskFactory
                |                Dim objDeviceTask as DeviceTask
                |                ..
                |                objRobotTaskFactory.DeleteDeviceTask
                |                objDeviceTask

        :param DeviceTask i_device_task:
        :return: None
        :rtype: None
        """
        return self.device_task_factory.DeleteDeviceTask(i_device_task.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'delete_device_task'
        # # vba_code = """
        # # Public Function delete_device_task(device_task_factory)
        # #     Dim iDeviceTask (2)
        # #     device_task_factory.DeleteDeviceTask iDeviceTask
        # #     delete_device_task = iDeviceTask
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_all_device_tasks(self, o_robot_task_list: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetAllDeviceTasks(CATSafeArrayVariant oRobotTaskList)
                | 
                |     Retrieves the list of Device tasks.
                | 
                |     Parameters:
                | 
                |         oDeviceTaskList
                |             The Device Task List. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The Device Task List could be successfully
                |             queried.
                |         E_FAIL
                |             The Device Task List could not be retrieved.
                | 
                |         Example:
                |             The following example Retrieves the list of Device Tasks for the
                |             Device.
                | 
                |                Dim objDeviceTaskFactory As DeviceTaskFactory
                |                Dim objDeviceTask(3) as DeviceTask
                |                ..
                |                objDeviceTaskFactory.GetAllDeviceTasks
                |                objDeviceTask

        :param tuple o_robot_task_list:
        :return: None
        :rtype: None
        """
        return self.device_task_factory.GetAllDeviceTasks(o_robot_task_list)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_all_device_tasks'
        # # vba_code = """
        # # Public Function get_all_device_tasks(device_task_factory)
        # #     Dim oRobotTaskList (2)
        # #     device_task_factory.GetAllDeviceTasks oRobotTaskList
        # #     get_all_device_tasks = oRobotTaskList
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'DeviceTaskFactory(name="{self.name}")'
