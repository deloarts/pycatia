#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dmaps_interfaces.activity import Activity


class CallRobotTaskActivity(Activity):
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
                |                         CallRobotTaskActivity
                | 
                | Interface representing a CallRobotTaskActivity.
                | 
                | Role: This interface is used to analyze the CallRobotTask
                | activity
                | The following code snippet can be used to obtain a CallRobotTaskActivity from a
                | selected Activity
                | 
                |    Dim oSelectAct As Activity
                |    Set oSelectAct = CATIA.ActiveDocument.Selection.FindObject("CATIAActivity")
                |    Dim objCallRobotTaskAct As CallRobotTaskActivity
                |    Set objCallRobotTaskAct = oSelectAct.GetTechnologicalObject("CallRobotTaskActivity")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.call_robot_task_activity = com_object

    def get_pointed_task_name(self, o_robot_task_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetPointedTaskName(CATBSTR oRobotTaskName)
                | 
                |     Gets the name of the Pointed RobotTask.
                | 
                |     Parameters:
                | 
                |         oRobotTaskName
                |             The name of the RobotTask being pointed. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The pointed RobotTask name is retrieve
                |             successfully.
                |         E_FAIL
                |             Unable to retrieve the pointed RobotTask name.
                | 
                |         Example:
                |             The following example shows how to retrieve the pointed
                |             RobotTask
                | 
                |                Dim objCallRobotTaskActy as
                |                CallRobotTaskActivity
                |                ...
                |                Dim strTaskName as String
                |                objCallRobotTaskActy.GetPointedTaskName
                |                strTaskName

        :param str o_robot_task_name:
        :return: None
        :rtype: None
        """
        return self.call_robot_task_activity.GetPointedTaskName(o_robot_task_name)

    def get_task(self, o_robot_task: Activity) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetTask(Activity oRobotTask)
                | 
                |     Gets the Pointed RobotTask.
                | 
                |     Parameters:
                | 
                |         oRobotTask
                |             The RobotTask pointed by this Activity. 
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The RobotTask is retrieve successfully.
                |         E_FAIL
                |             Unable to retrieve the RobotTask.
                | 
                |         Example:
                |             The following example shows how to retrieve the pointed
                |             RobotTask
                | 
                |                Dim objCallRobotTaskActy as
                |                CallRobotTaskActivity
                |                ...
                |                Dim objPointedTask as RobotTask
                |                objCallRobotTaskActy.GetTask objPointedTask

        :param Activity o_robot_task:
        :return: None
        :rtype: None
        """
        return self.call_robot_task_activity.GetTask(o_robot_task.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_task'
        # # vba_code = """
        # # Public Function get_task(call_robot_task_activity)
        # #     Dim oRobotTask (2)
        # #     call_robot_task_activity.GetTask oRobotTask
        # #     get_task = oRobotTask
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_task(self, i_target_robot_task: Activity, o_list_of_pointing_tasks: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetTask(Activity iTargetRobotTask,
                | CATSafeArrayVariant oListOfPointingTasks)
                | 
                |     Sets the Pointed RobotTask.
                | 
                |     Parameters:
                | 
                |         iTargetRobotTask
                |             The Desired Pointed Task. 
                |         oListOfPointingTasks
                |             The List of RobotTasks which have the cyclic dependancy.
                |             
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             The RobotTask is set successfully.
                |         E_FAIL
                |             Unable to set the RobotTask (either the RobotTask belongs to a
                |             different robot or existing cyclic dependancy).
                | 
                |         Example:
                |             The following example shows how to set the desired
                |             RobotTask
                | 
                |                Dim objCallRobotTaskActy as
                |                CallRobotTaskActivity
                |                Dim objTask as RobotTask
                |                ...
                |                Dim objCyclicTasks(5) 
                |                objCallRobotTaskActy.SetTask
                |                objTask,objCyclicTasks

        :param Activity i_target_robot_task:
        :param tuple o_list_of_pointing_tasks:
        :return: None
        :rtype: None
        """
        return self.call_robot_task_activity.SetTask(i_target_robot_task.com_object, o_list_of_pointing_tasks)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_task'
        # # vba_code = """
        # # Public Function set_task(call_robot_task_activity)
        # #     Dim iTargetRobotTask (2)
        # #     call_robot_task_activity.SetTask iTargetRobotTask
        # #     set_task = iTargetRobotTask
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'CallRobotTaskActivity(name="{self.name}")'
