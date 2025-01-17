#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.system_interfaces.any_object import AnyObject


class SchAppReplace(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchAppReplace
                | 
                | Manage a schematic component.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_app_replace = com_object

    def app_ok_to_replace(self, i_sch_object_to_be_replaced_by_this: AnyObject, o_b_yes: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppOKToReplace(AnyObject iSchObjectToBeReplacedByThis,
                | boolean oBYes)
                | 
                |     Query whether it is OK to replace an existing object (component, route...)
                |     with this object.
                | 
                |     Parameters:
                | 
                |         iSchObjectToBeReplacedByThis
                |             Pointer to the existing object to be replaced by this object.
                |             
                |         oBYes
                |             If TRUE, then it is OK to replace the object. 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchAppReplace
                |          Dim objArg1 As AnyObject
                |          Dim bVar2 As boolean
                |           ...
                |          objThisIntf.AppOKToReplaceobjArg1,bVar2

        :param AnyObject i_sch_object_to_be_replaced_by_this:
        :param bool o_b_yes:
        :return: None
        :rtype: None
        """
        return self.sch_app_replace.AppOKToReplace(i_sch_object_to_be_replaced_by_this.com_object, o_b_yes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_ok_to_replace'
        # # vba_code = """
        # # Public Function app_ok_to_replace(sch_app_replace)
        # #     Dim iSchObjectToBeReplacedByThis (2)
        # #     sch_app_replace.AppOKToReplace iSchObjectToBeReplacedByThis
        # #     app_ok_to_replace = iSchObjectToBeReplacedByThis
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def app_post_replace_process(self, i_sch_object_to_be_replaced_by_this: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppPostReplaceProcess(AnyObject
                | iSchObjectToBeReplacedByThis)
                | 
                |     Post process after replacing an object.
                | 
                |     Parameters:
                | 
                |         iNewObject
                |             The new Application object 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppReplace
                |          Dim objArg1 As AnyObject
                |           ...
                |          objThisIntf.AppPostReplaceProcessobjArg1

        :param AnyObject i_sch_object_to_be_replaced_by_this:
        :return: None
        :rtype: None
        """
        return self.sch_app_replace.AppPostReplaceProcess(i_sch_object_to_be_replaced_by_this.com_object)

    def __repr__(self):
        return f'SchAppReplace(name="{self.name}")'
