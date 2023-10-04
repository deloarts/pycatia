#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_app_connectable import SchAppConnectable
from pycatia.cat_sch_platform_interfaces.sch_app_connector import SchAppConnector
from pycatia.cat_sch_platform_interfaces.sch_list_of_bst_rs import SchListOfBSTRs
from pycatia.cat_sch_platform_interfaces.sch_list_of_objects import SchListOfObjects
from pycatia.system_interfaces.any_object import AnyObject


class SchGRR(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchGRR
                | 
                | Manage the graphical representation of a schematic object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_grr = com_object

    def get_grr_name(self, o_grr_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetGRRName(CATBSTR oGRRName)
                | 
                |     Get current name of the GRR.
                | 
                |     Parameters:
                | 
                |         oGRRName
                |             The name of this GRR. A component can be associated with more than
                |             one GRRs. Each GRR is identified by a specific name. Valid names are specified
                |             by the application when building the component. Every component should have a
                |             GRR named "Primary". The GRR by this name is used in the catalog.
                |
                |     Example:
                |
                |          Dim objThisIntf As SchGRR
                |          Dim strVar1 As String
                |           ...
                |          objThisIntf.GetGRRNamestrVar1

        :param str o_grr_name:
        :return: None
        :rtype: None
        """
        return self.sch_grr.GetGRRName(o_grr_name)

    def get_sch_cntr_owners(self, o_cntr_owner: SchAppConnector, o_grr_owner: 'SchGRR') -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetSchCntrOwners(SchAppConnector oCntrOwner,
                | SchGRR oGRROwner)
                | 
                |     Get the schematic objects that own this connector graphic
                |     representation.
                | 
                |     Parameters:
                | 
                |         oCntrOwner.
                |             A schematic connector that owns this connector graphic
                |             representation. 
                |         oGRROwner
                |             A component or route graphic representation that owns this
                |             connector graphic representation. 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchGRR
                |          Dim objArg1 As SchAppConnector
                |          Dim objArg2 As SchGRR
                |           ...
                |          objThisIntf.GetSchCntrOwnersobjArg1,objArg2

        :param SchAppConnector o_cntr_owner:
        :param SchGRR o_grr_owner:
        :return: None
        :rtype: None
        """
        return self.sch_grr.GetSchCntrOwners(o_cntr_owner.com_object, o_grr_owner.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_sch_cntr_owners'
        # # vba_code = """
        # # Public Function get_sch_cntr_owners(sch_grr)
        # #     Dim oCntrOwner (2)
        # #     sch_grr.GetSchCntrOwners oCntrOwner
        # #     get_sch_cntr_owners = oCntrOwner
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_sch_obj_owner(self) -> SchAppConnectable:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetSchObjOwner() As SchAppConnectable
                | 
                |     Get the schematic object that owns this graphic
                |     representation.
                | 
                |     Parameters:
                | 
                |         oGRROwner
                |             A schematic object that owns this graphic representation.
                |
                |     Example:
                |
                |          Dim objThisIntf As SchGRR
                |          Dim objArg1 As SchAppConnectable
                |           ...
                |          Set objArg1 = objThisIntf.GetSchObjOwner

        :return: SchAppConnectable
        :rtype: SchAppConnectable
        """
        return SchAppConnectable(self.sch_grr.GetSchObjOwner())

    def list_connected_gr_rs(
            self,
            i_grr_owner: SchAppConnectable,
            i_l_cntble_class_filter: SchListOfBSTRs,
            o_l_cntble_gr_rs: SchListOfObjects,
            o_l_cntbles: SchListOfObjects,
            o_l_cntrs_on_this_obj: SchListOfObjects,
            o_l_cntrs_on_connected: SchListOfObjects
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub ListConnectedGRRs(SchAppConnectable iGRROwner,
                | SchListOfBSTRs iLCntbleClassFilter,
                | SchListOfObjects oLCntbleGRRs,
                | SchListOfObjects oLCntbles,
                | SchListOfObjects oLCntrsOnThisObj,
                | SchListOfObjects oLCntrsOnConnected)
                | 
                |     Get a list of graphical objects that connects to this graphic
                |     representation.
                | 
                |     Parameters:
                | 
                |         iGRROwner
                |             A CATISchAppConnectable that owns this graphic representation. In
                |             the case of GRRCntr (this object), iGRROwner is the owner of the owner of this
                |             graphic. 
                |         oLCntrClassFilter
                |             A list of all the class types for filtering the output application
                |             objects list. 
                |         oLCntbleGRRs
                |             A list of GRRs connected to this GRR. (members are CATISchGRR
                |             interface pointers). 
                |         oLCntbles
                |             A list of application objects connected to this object. (members
                |             are CATISchAppConnectable interface pointers). 
                |         oLCntrsOnThisObj
                |             A list of connectors on this object through which the connection is
                |             made. (members are CATISchAppConnector interface pointers).
                |             
                |         oLCntrsOnConnected
                |             A list of connectors on the connected objects through which the
                |             connection is made. (members are CATISchAppConnector interface pointers).
                |             Members in this list corresponds to those in oLCntrsOnThisObj in making the
                |             corresponding connections. 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchGRR
                |          Dim objArg1 As SchAppConnectable
                |          Dim objArg2 As SchListOfBSTRs
                |          Dim objArg3 As SchListOfObjects
                |          Dim objArg4 As SchListOfObjects
                |          Dim objArg5 As SchListOfObjects
                |          Dim objArg6 As SchListOfObjects
                |           ...
                |          objThisIntf.ListConnectedGRRsobjArg1,objArg2,objArg3,objArg4,objArg5,objArg6

        :param SchAppConnectable i_grr_owner:
        :param SchListOfBSTRs i_l_cntble_class_filter:
        :param SchListOfObjects o_l_cntble_gr_rs:
        :param SchListOfObjects o_l_cntbles:
        :param SchListOfObjects o_l_cntrs_on_this_obj:
        :param SchListOfObjects o_l_cntrs_on_connected:
        :return: None
        :rtype: None
        """
        return self.sch_grr.ListConnectedGRRs(
            i_grr_owner.com_object,
            i_l_cntble_class_filter.com_object,
            o_l_cntble_gr_rs.com_object,
            o_l_cntbles.com_object,
            o_l_cntrs_on_this_obj.com_object,
            o_l_cntrs_on_connected.com_object
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'list_connected_gr_rs'
        # # vba_code = """
        # # Public Function list_connected_gr_rs(sch_grr)
        # #     Dim iGRROwner (2)
        # #     sch_grr.ListConnectedGRRs iGRROwner
        # #     list_connected_gr_rs = iGRROwner
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_grr_name(self, i_grr_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetGRRName(CATBSTR iGRRName)
                | 
                |     Set current name of the GRR.
                | 
                |     Parameters:
                | 
                |         iGRRName
                |             The name of this GRR to be set. 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchGRR
                |          Dim strVar1 As String
                |           ...
                |          objThisIntf.SetGRRNamestrVar1

        :param str i_grr_name:
        :return: None
        :rtype: None
        """
        return self.sch_grr.SetGRRName(i_grr_name)

    def __repr__(self):
        return f'SchGRR(name="{self.name}")'