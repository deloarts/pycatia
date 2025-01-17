#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_app_connectable import SchAppConnectable
from pycatia.cat_sch_platform_interfaces.sch_list_of_bst_rs import SchListOfBSTRs
from pycatia.cat_sch_platform_interfaces.sch_list_of_objects import SchListOfObjects
from pycatia.in_interfaces.document import Document
from pycatia.system_interfaces.any_object import AnyObject


class SchAppMultiImageMaster(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchAppMultiImageMaster
                | 
                | Interface to manage the master object in the Multi-Image-Object
                | concept.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_app_multi_image_master = com_object

    def app_add_image(self, i_image: SchAppConnectable) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppAddImage(SchAppConnectable iImage)
                | 
                |     Add an image for this master object.
                | 
                |     Parameters:
                | 
                |         iImage
                |             Pointer to the image to link this master to. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppMultiImageMaster
                |          Dim objImage As SchAppConnectable
                |           ...
                |          objThisIntf.AppAddImage objImage

        :param SchAppConnectable i_image:
        :return: None
        :rtype: None
        """
        return self.sch_app_multi_image_master.AppAddImage(i_image.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_add_image'
        # # vba_code = """
        # # Public Function app_add_image(sch_app_multi_image_master)
        # #     Dim iImage (2)
        # #     sch_app_multi_image_master.AppAddImage iImage
        # #     app_add_image = iImage
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def app_is_ok_to_create_image(
            self,
            i_image_doc: Document,
            o_b_yes: bool,
            o_nls_file_name: str,
            o_nls_file_key_to_message: str
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppIsOKToCreateImage(Document iImageDoc,
                | boolean oBYes,
                | CATBSTR oNLSFileName,
                | CATBSTR oNLSFileKeyToMessage)
                | 
                |     Check if OK to create an image of this master object.
                | 
                |     Parameters:
                | 
                |         iImageDoc
                |             Pointer to the document the image is in. 
                |         oBYes
                |             TRUE if this object is valid to be the master of a MIO
                |             relationship. 
                |         oNLSFileName
                |             File name for the NLS messages. 
                |         oNLSFileKeyToMessage
                |             Message key to the application specific diagnostics.
                |             
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppMultiImageMaster
                |          Dim objImageDoc As Document
                |          Dim bYes As boolean
                |          Dim strFileName As String
                |          Dim strFileKeyToMsg As String
                |           ...
                |          objThisIntf.AppIsOKToCreateImage
                |          objImageDoc,bYes,strFileName,strFileKeyToMsg

        :param Document i_image_doc:
        :param bool o_b_yes:
        :param str o_nls_file_name:
        :param str o_nls_file_key_to_message:
        :return: None
        :rtype: None
        """
        return self.sch_app_multi_image_master.AppIsOKToCreateImage(
            i_image_doc.com_object,
            o_b_yes,
            o_nls_file_name,
            o_nls_file_key_to_message
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_is_ok_to_create_image'
        # # vba_code = """
        # # Public Function app_is_ok_to_create_image(sch_app_multi_image_master)
        # #     Dim iImageDoc (2)
        # #     sch_app_multi_image_master.AppIsOKToCreateImage iImageDoc
        # #     app_is_ok_to_create_image = iImageDoc
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def app_list_images(self, i_l_filter: SchListOfBSTRs, o_l_images: SchListOfObjects) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AppListImages(SchListOfBSTRs iLFilter,
                | SchListOfObjects oLImages)
                | 
                |     List the images of this master object.
                | 
                |     Parameters:
                | 
                |         iLFilter
                |             A list of image class names for filtering (can be NULL).
                |             
                |         oLUKImages
                |             A list of image pointers (a list of CATIASchAppMultiImage
                |             pointers). 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchAppMultiImageMaster
                |          Dim objLFilter As SchListOfBSTRs
                |          Dim objLImages As SchListOfObjects
                |           ...
                |          objThisIntf.AppListImages objLFilter,objLImages

        :param SchListOfBSTRs i_l_filter:
        :param SchListOfObjects o_l_images:
        :return: None
        :rtype: None
        """
        return self.sch_app_multi_image_master.AppListImages(i_l_filter.com_object, o_l_images.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'app_list_images'
        # # vba_code = """
        # # Public Function app_list_images(sch_app_multi_image_master)
        # #     Dim iLFilter (2)
        # #     sch_app_multi_image_master.AppListImages iLFilter
        # #     app_list_images = iLFilter
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SchAppMultiImageMaster(name="{self.name}")'
