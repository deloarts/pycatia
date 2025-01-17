#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.eno_cd5_interfaces.cd5_id import CD5ID
from pycatia.system_interfaces.any_object import AnyObject


class CD5Structure(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CD5Structure
                | 
                | Represents the structure of an ENOVIA V6 object.
                | Role: It represents the structure of an ENOVIA V6 root object on which it is
                | possible to include some sub components. Its final purpose is to perform a
                | Partial Open on it, showing only the root and the sub components that were
                | previously included. It is managed by CD5Engine.
                | 
                | See also:
                |     CD5ID, CD5Engine
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.cd5_structure = com_object

    def get_root(self) -> CD5ID:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetRoot() As CD5ID
                | 
                |     Returns the root ENOVIA V6 Identifier of the CD5Structure.
                | 
                |     Returns:
                |         The CD5ID. 
                |     Example:
                | 
                |           The following example creates a Structure from "RootProduct" and gets
                |           its root identifier.
                |
                |          Dim oCD5Engine As CD5Engine
                |          Set oCD5Engine = CATIA.GetItem("CD5Engine")
                |          Dim iRootCD5ID, oDummyCD5ID As CD5ID
                |          Set iRootCD5ID = oCD5Engine.GetIDFromTNR("CATProduct For Team", "RootProduct", "---")
                |          Dim oCD5Structure As CD5Structure
                |          Set oCD5Structure = oCD5Engine.GetStructure(iRootCD5ID)
                |          Set oDummyCD5ID = oCD5Structure.GetRoot()

        :return: CD5ID
        :rtype: CD5ID
        """
        return CD5ID(self.cd5_structure.GetRoot())

    def include(self, i_id: CD5ID) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Include(CD5ID iID)
                | 
                |     Includes an sub component (identified by its ENOVIA V6 Identifier) for a
                |     future Partial Open operation.
                | 
                |     Parameters:
                | 
                |         iID
                |             The ENOIACD5ID of the sub component to include. 
                | 
                |     Example:
                | 
                |           The following example creates a Structure from "RootProduct" and
                |           includes the object "IncludedPart".
                |
                |          Dim oCD5Engine As CD5Engine
                |          Set oCD5Engine = CATIA.GetItem("CD5Engine")
                |          Dim iRootCD5ID, iIncludedCD5ID As CD5ID
                |          Set iRootCD5ID = oCD5Engine.GetIDFromTNR("CATProduct For Team", "RootProduct", "---")
                |          Set iIncludedCD5ID = oCD5Engine.GetIDFromTNR("CATProduct For Team", "IncludedPart", "---")
                |          Dim oCD5Structure As CD5Structure
                |          Set oCD5Structure = oCD5Engine.GetStructure(iRootCD5ID)
                |          oCD5Structure.Include(iIncludedCD5ID)

        :param CD5ID i_id:
        :return: None
        :rtype: None
        """
        return self.cd5_structure.Include(i_id.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'include'
        # # vba_code = """
        # # Public Function include(cd5_structure)
        # #     Dim iID (2)
        # #     cd5_structure.Include iID
        # #     include = iID
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'CD5Structure(name="{self.name}")'
