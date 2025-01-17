#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_app_connectable import SchAppConnectable
from pycatia.cat_sch_platform_interfaces.sch_list_of_objects import SchListOfObjects
from pycatia.system_interfaces.any_object import AnyObject


class SchAppZone(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchAppZone
                | 
                | Manage a schematic zone.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_app_zone = com_object

    def app_add_zone_member(self, i_app_cntbl_to_add: SchAppConnectable) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppAddZoneMember(SchAppConnectable iAppCntblToAdd)
                | 
                |     Add an application connectable object to the zone as
                |     member.
                | 
                |     Parameters:
                | 
                |         iAppCntblToAdd
                |             The application connectable object to be added to the zone.
                |
                |     Example:
                |
                |          Dim objThisIntf As SchAppZone
                |          Dim objArg1 As SchAppConnectable
                |           ...
                |          objThisIntf.AppAddZoneMemberobjArg1

        :param SchAppConnectable i_app_cntbl_to_add:
        :return: None
        :rtype: None
        """
        return self.sch_app_zone.AppAddZoneMember(i_app_cntbl_to_add.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_add_zone_member'
        # # vba_code = """
        # # Public Function app_add_zone_member(sch_app_zone)
        # #     Dim iAppCntblToAdd (2)
        # #     sch_app_zone.AppAddZoneMember iAppCntblToAdd
        # #     app_add_zone_member = iAppCntblToAdd
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def app_list_zone_members(self) -> SchListOfObjects:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func AppListZoneMembers() As SchListOfObjects
                | 
                |     List all members of an application zone.
                | 
                |     Parameters:
                | 
                |         oLAppCntbl
                |             A list of zone members (application connectables).
                |             
                |     Example:
                |
                |          Dim objThisIntf As SchAppZone
                |          Dim objArg1 As SchListOfObjects
                |           ...
                |          Set objArg1 = objThisIntf.AppListZoneMembers

        :return: SchListOfObjects
        :rtype: SchListOfObjects
        """
        return SchListOfObjects(self.sch_app_zone.AppListZoneMembers())

    def app_remove_zone_member(self, i_app_cntbl_to_remove: SchAppConnectable) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppRemoveZoneMember(SchAppConnectable
                | iAppCntblToRemove)
                | 
                |     Remove an application connectable object to the zone as
                |     member.
                | 
                |     Parameters:
                | 
                |         iAppCntblToRemove
                |             The application connectable object to be removed to the zone.
                |
                |     Example:
                |
                |          Dim objThisIntf As SchAppZone
                |          Dim objArg1 As SchAppConnectable
                |           ...
                |          objThisIntf.AppRemoveZoneMemberobjArg1

        :param SchAppConnectable i_app_cntbl_to_remove:
        :return: None
        :rtype: None
        """
        return self.sch_app_zone.AppRemoveZoneMember(i_app_cntbl_to_remove.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_remove_zone_member'
        # # vba_code = """
        # # Public Function app_remove_zone_member(sch_app_zone)
        # #     Dim iAppCntblToRemove (2)
        # #     sch_app_zone.AppRemoveZoneMember iAppCntblToRemove
        # #     app_remove_zone_member = iAppCntblToRemove
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SchAppZone(name="{self.name}")'
