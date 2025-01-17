#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_app_connector import SchAppConnector
from pycatia.system_interfaces.any_object import AnyObject


class SchCntrDocLink(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchCntrDocLink
                | 
                | Manage the on-off sheet connector.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_cntr_doc_link = com_object

    def get_link(self, o_sch_connector: SchAppConnector, o_document_name: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetLink(SchAppConnector oSchConnector,
                | CATBSTR oDocumentName)
                | 
                |     Get the linked connector and its document name.
                | 
                |     Parameters:
                | 
                |         oSchConnector
                |             The connector that is linked to this connector. 
                |         oDocumentName
                |             Name of document containing the linked connector. 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchCntrDocLink
                |          Dim objArg1 As SchAppConnector
                |          Dim strVar2 As String
                |           ...
                |          objThisIntf.GetLinkobjArg1,strVar2

        :param SchAppConnector o_sch_connector:
        :param str o_document_name:
        :return: None
        :rtype: None
        """
        return self.sch_cntr_doc_link.GetLink(o_sch_connector.com_object, o_document_name)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_link'
        # # vba_code = """
        # # Public Function get_link(sch_cntr_doc_link)
        # #     Dim oSchConnector (2)
        # #     sch_cntr_doc_link.GetLink oSchConnector
        # #     get_link = oSchConnector
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def link(self, i_sch_connector: SchAppConnector) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Link(SchAppConnector iSchConnector)
                | 
                |     Create an external link to another connector.
                | 
                |     Parameters:
                | 
                |         iSchConnector
                |             The connector to link to. 
                | 
                |     Example:
                |
                |          Dim objThisIntf As SchCntrDocLink
                |          Dim objArg1 As SchAppConnector
                |           ...
                |          objThisIntf.LinkobjArg1

        :param SchAppConnector i_sch_connector:
        :return: None
        :rtype: None
        """
        return self.sch_cntr_doc_link.Link(i_sch_connector.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'link'
        # # vba_code = """
        # # Public Function link(sch_cntr_doc_link)
        # #     Dim iSchConnector (2)
        # #     sch_cntr_doc_link.Link iSchConnector
        # #     link = iSchConnector
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def un_link(self) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub UnLink()
                | 
                |     Remove external link to another connector.
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchCntrDocLink
                |           ...
                |          objThisIntf.UnLink

        :return: None
        :rtype: None
        """
        return self.sch_cntr_doc_link.UnLink()

    def __repr__(self):
        return f'SchCntrDocLink(name="{self.name}")'
